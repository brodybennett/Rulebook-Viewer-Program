#!/usr/bin/env python3
"""
backfill_enum_ids.py

Conservatively backfill `conditions` and `damage_types` in fenced `yaml ability`
blocks where IDs can be inferred with high confidence from existing text.

Dry-run by default.

Examples:
  python tools/backfill_enum_ids.py --repo .
  python tools/backfill_enum_ids.py --repo . --write
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    raise SystemExit(2)


DEFAULT_CONTENT_ROOT = "draft"
FENCE_START_RE = re.compile(r"^\s*```(?:yaml|yml)\s+ability\s*$", re.IGNORECASE)
FENCE_END_RE = re.compile(r"^\s*```\s*$")

# Conservative condition matching: avoid broad terms that over-trigger.
CONDITION_PATTERNS: Sequence[Tuple[str, re.Pattern[str]]] = (
    ("off_balance", re.compile(r"\boff[- ]balance\b", re.IGNORECASE)),
    ("helpless", re.compile(r"\bhelpless\b", re.IGNORECASE)),
    ("silenced", re.compile(r"\bsilenced\b", re.IGNORECASE)),
    ("restrained", re.compile(r"\brestrained\b", re.IGNORECASE)),
    ("caught_off_guard", re.compile(r"\bcaught(?:[- ]off[- ]guard| off guard)\b", re.IGNORECASE)),
    ("dazed", re.compile(r"\bdazed\b", re.IGNORECASE)),
    ("blinded", re.compile(r"\bblinded\b", re.IGNORECASE)),
    ("deafened", re.compile(r"\bdeafened\b", re.IGNORECASE)),
    ("invisible", re.compile(r"\binvisib(?:le|ility)\b", re.IGNORECASE)),
    ("fear", re.compile(r"\bfear(?:ed|ful)?\b", re.IGNORECASE)),
    ("rage_taunted", re.compile(r"\b(?:rage|taunted?)\b", re.IGNORECASE)),
    ("constitution_advantage_disadvantage", re.compile(r"\bconstitution.*(?:advantage|disadvantage)\b", re.IGNORECASE)),
    ("bloodbath", re.compile(r"\bbloodbath\b", re.IGNORECASE)),
    ("bleeding", re.compile(r"\bbleeding\b", re.IGNORECASE)),
    ("dying", re.compile(r"\bdying\b", re.IGNORECASE)),
    ("dead", re.compile(r"\bdead\b", re.IGNORECASE)),
)

# Damage types require nearby damage/harm/loss signal for confidence.
DAMAGE_PATTERNS: Sequence[Tuple[str, re.Pattern[str]]] = (
    ("physical", re.compile(r"\bphysical\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("fire", re.compile(r"\b(?:fire|flame|burn)\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("lightning", re.compile(r"\b(?:lightning|electric)\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("poison", re.compile(r"\bpoison\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("cold", re.compile(r"\b(?:cold|frost|ice)\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("holy", re.compile(r"\b(?:holy|sacred)\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("psychic", re.compile(r"\bpsychic\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("mental", re.compile(r"\bmental\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
    ("sanity", re.compile(r"\bsanity(?:\s*/\s*rationality)?\b.{0,20}\b(?:loss|damage|harm)\b", re.IGNORECASE)),
    ("rationality", re.compile(r"\brationality\b.{0,20}\b(?:loss|damage|harm)\b", re.IGNORECASE)),
    ("curse", re.compile(r"\bcurse(?:d)?\b.{0,20}\b(?:damage|harm)\b", re.IGNORECASE)),
)


@dataclass(frozen=True)
class BlockChange:
    line: int
    ability_id: str
    conditions: List[str]
    damage_types: List[str]


@dataclass(frozen=True)
class FileChange:
    path: Path
    block_changes: List[BlockChange]

    @property
    def block_count(self) -> int:
        return len(self.block_changes)


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def iter_markdown_files(scan_root: Path) -> List[Path]:
    if not scan_root.exists() or not scan_root.is_dir():
        return []
    return sorted(p for p in scan_root.rglob("*.md") if p.is_file())


def extract_signal_text(payload: Dict[str, object]) -> str:
    parts: List[str] = []
    for key in ("name", "text"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            parts.append(value)
    dice = payload.get("dice")
    if isinstance(dice, dict):
        notes = dice.get("notes")
        if isinstance(notes, str) and notes.strip():
            parts.append(notes)
    return "\n".join(parts)


def infer_enum_ids(payload: Dict[str, object]) -> Tuple[List[str], List[str]]:
    signal = extract_signal_text(payload)
    if not signal:
        return [], []

    conditions: List[str] = []
    damage_types: List[str] = []

    for enum_id, pattern in CONDITION_PATTERNS:
        if pattern.search(signal):
            conditions.append(enum_id)
    for enum_id, pattern in DAMAGE_PATTERNS:
        if pattern.search(signal):
            damage_types.append(enum_id)

    return conditions, damage_types


def insertion_index(block_lines: Sequence[str]) -> int:
    for idx, line in enumerate(block_lines):
        stripped = line.lstrip()
        if stripped.startswith("tags:") or stripped.startswith("text:"):
            return idx
    return len(block_lines)


def build_insert_lines(
    *,
    newline: str,
    conditions: List[str],
    damage_types: List[str],
) -> List[str]:
    out: List[str] = []
    if conditions:
        out.append(f"conditions:{newline}")
        for cond in conditions:
            out.append(f"- {cond}{newline}")
    if damage_types:
        out.append(f"damage_types:{newline}")
        for dmg in damage_types:
            out.append(f"- {dmg}{newline}")
    return out


def process_file(path: Path, repo: Path, *, write: bool) -> FileChange | None:
    original = path.read_text(encoding="utf-8", errors="replace")
    newline = "\r\n" if "\r\n" in original else "\n"
    lines = original.splitlines(keepends=True)
    changed_blocks: List[BlockChange] = []

    i = 0
    while i < len(lines):
        if not FENCE_START_RE.match(lines[i].rstrip("\r\n")):
            i += 1
            continue

        start_idx = i
        j = i + 1
        while j < len(lines) and not FENCE_END_RE.match(lines[j].rstrip("\r\n")):
            j += 1
        if j >= len(lines):
            break

        block_lines = lines[start_idx + 1 : j]
        block_text = "".join(block_lines)
        try:
            payload = yaml.safe_load(block_text)
        except Exception:
            i = j + 1
            continue
        if not isinstance(payload, dict):
            i = j + 1
            continue

        existing_conditions = payload.get("conditions")
        existing_damage_types = payload.get("damage_types")

        inferred_conditions, inferred_damage_types = infer_enum_ids(payload)
        add_conditions = inferred_conditions if not existing_conditions else []
        add_damage_types = inferred_damage_types if not existing_damage_types else []

        if add_conditions or add_damage_types:
            insert_at = insertion_index(block_lines)
            to_insert = build_insert_lines(
                newline=newline,
                conditions=add_conditions,
                damage_types=add_damage_types,
            )
            if to_insert:
                block_lines = list(block_lines[:insert_at]) + to_insert + list(block_lines[insert_at:])
                lines[start_idx + 1 : j] = block_lines
                # fence index shifts by inserted amount
                j = j + len(to_insert)
                changed_blocks.append(
                    BlockChange(
                        line=start_idx + 1,
                        ability_id=str(payload.get("id") or ""),
                        conditions=add_conditions,
                        damage_types=add_damage_types,
                    )
                )

        i = j + 1

    if not changed_blocks:
        return None

    if write:
        path.write_text("".join(lines), encoding="utf-8")

    return FileChange(path=path.relative_to(repo), block_changes=changed_blocks)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Backfill conditions/damage_types IDs in yaml ability blocks (dry-run by default)."
    )
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory).")
    parser.add_argument(
        "--content-root",
        default=DEFAULT_CONTENT_ROOT,
        help=f"Markdown root under repo (default: {DEFAULT_CONTENT_ROOT}).",
    )
    parser.add_argument("--write", action="store_true", help="Apply edits in-place. Without this flag, run is preview-only.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    scan_root = resolve_under_repo(repo, args.content_root)
    files = iter_markdown_files(scan_root)

    file_changes: List[FileChange] = []
    for path in files:
        change = process_file(path, repo, write=args.write)
        if change is not None:
            file_changes.append(change)

    changed_blocks = sum(fc.block_count for fc in file_changes)
    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: scanned {len(files)} markdown files.")
    print(f"updated blocks: {changed_blocks} across {len(file_changes)} files.")

    for fc in file_changes[:200]:
        print(f"- {fc.path.as_posix()} ({fc.block_count} block(s))")
    if len(file_changes) > 200:
        print(f"- ... +{len(file_changes) - 200} more file(s)")

    if not args.write:
        print("Preview only. Re-run with --write to apply.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

