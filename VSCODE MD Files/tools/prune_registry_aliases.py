#!/usr/bin/env python3
"""prune_registry_aliases.py

Small cleanup pass for tag-registry.yml anchors:
- removes duplicate aliases
- removes aliases identical to title
- optional: drop overly-generic aliases ("Abilities", "Ritual", "Materials", etc.)

Default is DRY RUN. Use --write to apply.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import re
from pathlib import Path
from typing import List, Tuple

import yaml

GENERIC_DEFAULT = [
    "abilities",
    "ability",
    "ritual",
    "materials",
    "advancement",
    "attribute gain",
]


def _dump(data: dict) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


def _diff(a: str, b: str) -> str:
    return "".join(difflib.unified_diff(
        a.splitlines(keepends=True),
        b.splitlines(keepends=True),
        fromfile="tag-registry.yml (before)",
        tofile="tag-registry.yml (after)",
    ))


def _dedupe(title: str, aliases: List[str], generic: List[str]) -> List[str]:
    title = (title or "").strip()
    out = []
    seen = set()
    for a in aliases or []:
        a = str(a).strip()
        if not a:
            continue
        if a == title:
            continue
        if a.lower() in generic:
            continue
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Prune tag-registry.yml aliases.")
    ap.add_argument("--repo", type=str, default=".")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--keep-generic", action="store_true", help="Do not remove generic aliases")
    ap.add_argument("--generic", type=str, default="", help="Regex (case-insensitive) for generic aliases to remove")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    reg_path = repo / "tag-registry.yml"

    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8", errors="replace")) or {}
    before = _dump(reg)

    new_reg = copy.deepcopy(reg)
    anchors = new_reg.get("anchors") or {}

    generic_list = [] if args.keep_generic else GENERIC_DEFAULT
    generic_set = set([g.lower() for g in generic_list])
    generic_re = re.compile(args.generic, re.I) if args.generic else None

    changed = 0
    for aid, meta in anchors.items():
        if not isinstance(meta, dict):
            continue
        title = str(meta.get("title") or "")
        aliases = meta.get("aliases") or []

        # apply regex-based generic removal
        if generic_re:
            aliases = [a for a in aliases if not generic_re.search(str(a))]

        pruned = _dedupe(title, aliases, list(generic_set))
        if pruned != meta.get("aliases"):
            meta["aliases"] = pruned
            changed += 1

    after = _dump(new_reg)
    if before == after:
        print("No changes.")
        return 0

    print(f"Would update {changed} anchors.\n")
    print(_diff(before, after))
    if args.write:
        reg_path.write_text(after, encoding="utf-8")
        print("\nWROTE: tag-registry.yml updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
