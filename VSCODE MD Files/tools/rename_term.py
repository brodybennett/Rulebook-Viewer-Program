#!/usr/bin/env python3
"""
rename_term.py

Repo-wide safe term rename with dry-run by default.

Examples:
  python tools/rename_term.py --repo . --from "Spirituality Points" --to "Spirituality"
  python tools/rename_term.py --repo . --from "Spirituality Points" --to "Spirituality" --write
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


DEFAULT_EXTENSIONS = (
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".py",
    ".json",
    ".css",
    ".js",
    ".html",
    ".toml",
    ".ini",
    ".cfg",
    ".ps1",
)

DEFAULT_EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
}

GENERATED_DIRS = {
    "dist",
    "reports",
}


@dataclass(frozen=True)
class FileChange:
    path: Path
    replacements: int


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def iter_files(
    repo: Path,
    *,
    include_exts: set[str],
    include_generated: bool,
    include_paths: List[Path],
) -> Iterable[Path]:
    if include_paths:
        for root in include_paths:
            if not root.exists():
                continue
            if root.is_file():
                if root.suffix.lower() in include_exts:
                    yield root
                continue
            for path in sorted(root.rglob("*")):
                if not path.is_file():
                    continue
                if path.suffix.lower() not in include_exts:
                    continue
                parts = {part.lower() for part in path.parts}
                if parts & DEFAULT_EXCLUDE_DIRS:
                    continue
                if not include_generated and parts & GENERATED_DIRS:
                    continue
                yield path
        return

    for path in sorted(repo.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in include_exts:
            continue
        parts = {part.lower() for part in path.parts}
        if parts & DEFAULT_EXCLUDE_DIRS:
            continue
        if not include_generated and parts & GENERATED_DIRS:
            continue
        yield path


def replace_text(
    text: str,
    *,
    old: str,
    new: str,
    ignore_case: bool,
    word_boundary: bool,
) -> tuple[str, int]:
    flags = re.IGNORECASE if ignore_case else 0
    escaped = re.escape(old)
    if word_boundary:
        pattern = re.compile(rf"(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])", flags)
        updated, count = pattern.subn(new, text)
        return updated, count
    if ignore_case:
        pattern = re.compile(escaped, flags)
        updated, count = pattern.subn(new, text)
        return updated, count
    count = text.count(old)
    if count == 0:
        return text, 0
    return text.replace(old, new), count


def main() -> int:
    parser = argparse.ArgumentParser(description="Repo-wide safe term rename (dry-run by default).")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory).")
    parser.add_argument("--from", dest="from_text", required=True, help="Literal text to replace.")
    parser.add_argument("--to", dest="to_text", required=True, help="Replacement text.")
    parser.add_argument(
        "--path",
        action="append",
        default=[],
        help="Optional path(s) under repo to limit the rename scope. Repeatable.",
    )
    parser.add_argument(
        "--ext",
        action="append",
        default=[],
        help="Optional extension filter(s), e.g. --ext .md --ext .yml. Defaults to common text/code files.",
    )
    parser.add_argument("--ignore-case", action="store_true", help="Match text case-insensitively.")
    parser.add_argument("--word-boundary", action="store_true", help="Match only whole-token boundaries.")
    parser.add_argument("--include-generated", action="store_true", help="Include dist/ and reports/ directories.")
    parser.add_argument("--write", action="store_true", help="Apply edits in-place. Without this flag, run is preview-only.")
    args = parser.parse_args()

    old = args.from_text
    new = args.to_text
    if old == "":
        print("ERROR: --from cannot be empty.")
        return 2
    if old == new:
        print("No-op: --from and --to are identical.")
        return 0

    repo = Path(args.repo).resolve()
    include_exts = {e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.ext} if args.ext else set(DEFAULT_EXTENSIONS)
    include_paths = [resolve_under_repo(repo, raw) for raw in args.path]

    changes: List[FileChange] = []
    total_replacements = 0
    files_scanned = 0

    for path in iter_files(
        repo,
        include_exts=include_exts,
        include_generated=args.include_generated,
        include_paths=include_paths,
    ):
        files_scanned += 1
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated, count = replace_text(
            original,
            old=old,
            new=new,
            ignore_case=args.ignore_case,
            word_boundary=args.word_boundary,
        )
        if count <= 0:
            continue
        rel = path.relative_to(repo)
        changes.append(FileChange(path=rel, replacements=count))
        total_replacements += count
        if args.write:
            path.write_text(updated, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: scanned {files_scanned} file(s).")
    print(f"matches: {total_replacements} across {len(changes)} file(s).")
    if not changes:
        return 0

    print("")
    for change in changes[:300]:
        print(f"- {change.path.as_posix()} ({change.replacements})")
    if len(changes) > 300:
        print(f"- ... +{len(changes) - 300} more file(s)")

    if not args.write:
        print("")
        print("Preview only. Re-run with --write to apply changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

