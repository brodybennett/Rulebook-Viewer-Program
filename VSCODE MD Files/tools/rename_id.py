#!/usr/bin/env python3
"""
rename_id.py

Safely rename ability IDs in markdown `yaml ability` blocks.
Dry-run by default.

Examples:
  python tools/rename_id.py --repo . --from fool-seq-09-old-id --to fool-seq-09-new-id
  python tools/rename_id.py --repo . --from fool-seq-09-old-id --to fool-seq-09-new-id --write
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    raise SystemExit(2)


DEFAULT_CONTENT_ROOT = "draft"
DEFAULT_SCHEMA_PATH = "meta/ability_schema.yml"
FENCE_START_RE = re.compile(r"^\s*```(?:yaml|yml)\s+ability\s*$", re.IGNORECASE)
FENCE_END_RE = re.compile(r"^\s*```\s*$")
ID_LINE_RE = re.compile(r"^(?P<prefix>\s*id\s*:\s*)(?P<quote>['\"]?)(?P<value>[^\"'#\n]+?)(?P=quote)(?P<suffix>\s*(?:#.*)?)\s*$")


@dataclass(frozen=True)
class FileChange:
    path: Path
    yaml_id_replacements: int
    wikilink_replacements: int
    plain_replacements: int

    @property
    def total(self) -> int:
        return self.yaml_id_replacements + self.wikilink_replacements + self.plain_replacements


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def load_id_pattern(schema_path: Path) -> re.Pattern[str] | None:
    if not schema_path.exists():
        return None
    payload = yaml.safe_load(schema_path.read_text(encoding="utf-8", errors="replace")) or {}
    ability_schema = payload.get("ability_schema") if isinstance(payload, dict) else None
    if not isinstance(ability_schema, dict):
        return None
    raw = str(ability_schema.get("id_pattern") or "").strip()
    if not raw:
        return None
    return re.compile(raw)


def replace_yaml_ability_ids(text: str, old_id: str, new_id: str) -> Tuple[str, int]:
    lines = text.splitlines(keepends=True)
    in_fence = False
    replacements = 0
    out: List[str] = []

    for line in lines:
        raw = line.rstrip("\r\n")
        newline = line[len(raw) :]

        if FENCE_START_RE.match(raw):
            in_fence = True
            out.append(line)
            continue
        if in_fence and FENCE_END_RE.match(raw):
            in_fence = False
            out.append(line)
            continue

        if in_fence:
            m = ID_LINE_RE.match(raw)
            if m:
                current = m.group("value").strip()
                if current == old_id:
                    replaced = f"{m.group('prefix')}{m.group('quote')}{new_id}{m.group('quote')}{m.group('suffix')}{newline}"
                    out.append(replaced)
                    replacements += 1
                    continue

        out.append(line)

    return "".join(out), replacements


def replace_wikilink_ids(text: str, old_id: str, new_id: str) -> Tuple[str, int]:
    pattern = re.compile(rf"(\[\[id:){re.escape(old_id)}(?=[|\]])")
    updated, count = pattern.subn(rf"\1{new_id}", text)
    return updated, count


def replace_plain_ids(text: str, old_id: str, new_id: str) -> Tuple[str, int]:
    pattern = re.compile(rf"(?<![A-Za-z0-9_-]){re.escape(old_id)}(?![A-Za-z0-9_-])")
    updated, count = pattern.subn(new_id, text)
    return updated, count


def iter_markdown_files(root: Path) -> List[Path]:
    if not root.exists() or not root.is_dir():
        return []
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Rename ability IDs in YAML ability blocks (dry-run by default).")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory).")
    parser.add_argument("--content-root", default=DEFAULT_CONTENT_ROOT, help=f"Markdown root under repo (default: {DEFAULT_CONTENT_ROOT}).")
    parser.add_argument("--schema", default=DEFAULT_SCHEMA_PATH, help=f"Ability schema path for ID validation (default: {DEFAULT_SCHEMA_PATH}).")
    parser.add_argument("--from", dest="from_id", required=True, help="Existing ability ID.")
    parser.add_argument("--to", dest="to_id", required=True, help="New ability ID.")
    parser.add_argument("--replace-plain", action="store_true", help="Also replace plain ID token occurrences (not only YAML and [[id:...]] refs).")
    parser.add_argument("--write", action="store_true", help="Apply edits. Without this flag, run is preview-only.")
    args = parser.parse_args()

    old_id = args.from_id.strip().lower()
    new_id = args.to_id.strip().lower()
    if not old_id or not new_id:
        print("ERROR: --from/--to IDs must be non-empty.")
        return 2
    if old_id == new_id:
        print("No-op: --from and --to are identical.")
        return 0

    repo = Path(args.repo).resolve()
    content_root = resolve_under_repo(repo, args.content_root)
    schema_path = resolve_under_repo(repo, args.schema)

    id_pattern = load_id_pattern(schema_path)
    if id_pattern is not None and not id_pattern.fullmatch(new_id):
        print(f"ERROR: --to `{new_id}` does not match schema id_pattern `{id_pattern.pattern}`.")
        return 2

    files = iter_markdown_files(content_root)
    if not files:
        print(f"No markdown files found under: {content_root}")
        return 0

    changes: List[FileChange] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        updated, yaml_count = replace_yaml_ability_ids(text, old_id, new_id)
        updated, wikilink_count = replace_wikilink_ids(updated, old_id, new_id)
        plain_count = 0
        if args.replace_plain:
            updated, plain_count = replace_plain_ids(updated, old_id, new_id)

        if yaml_count + wikilink_count + plain_count <= 0:
            continue

        rel = path.relative_to(repo)
        changes.append(
            FileChange(
                path=rel,
                yaml_id_replacements=yaml_count,
                wikilink_replacements=wikilink_count,
                plain_replacements=plain_count,
            )
        )
        if args.write:
            path.write_text(updated, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    total = sum(c.total for c in changes)
    print(f"{mode}: scanned {len(files)} file(s) under {content_root}.")
    print(f"matches: {total} across {len(changes)} file(s).")
    if not changes:
        return 0

    print("")
    for change in changes[:300]:
        print(
            f"- {change.path.as_posix()} "
            f"(yaml_id={change.yaml_id_replacements}, wikilink={change.wikilink_replacements}, plain={change.plain_replacements})"
        )
    if len(changes) > 300:
        print(f"- ... +{len(changes) - 300} more file(s)")

    if not args.write:
        print("")
        print("Preview only. Re-run with --write to apply changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

