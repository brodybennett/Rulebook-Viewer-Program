#!/usr/bin/env python3
"""merge_tag_delta.py

Merge TAG DELTA YAML outputs into tag-registry.yml (anchors only), with deduping.

Default is DRY RUN: prints what would change and exits.
Use --write to apply changes.

Supported TAG DELTA shape (your prompt spec):
  new_anchors:
    - id: <anchor-id>
      title: <Title>
      file: <path>
      suggested_aliases: [ ... ]

Read-only unless --write.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def _read_yaml(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {}


def _dedupe_aliases(title: str, aliases: List[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    title_norm = (title or "").strip()
    for a in aliases or []:
        a = str(a).strip()
        if not a:
            continue
        if a == title_norm:
            continue
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def _dump_yaml(data: dict) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


def _unified_diff(a: str, b: str, fromfile: str, tofile: str) -> str:
    return "".join(difflib.unified_diff(
        a.splitlines(keepends=True),
        b.splitlines(keepends=True),
        fromfile=fromfile,
        tofile=tofile,
    ))


def merge(reg: dict, delta: dict) -> Tuple[dict, List[str]]:
    """Return (new_registry, change_log)."""
    new_reg = copy.deepcopy(reg)
    anchors = new_reg.setdefault("anchors", {})
    if not isinstance(anchors, dict):
        anchors = {}
        new_reg["anchors"] = anchors

    change_log: List[str] = []

    new_anchors = delta.get("new_anchors") or []
    if not isinstance(new_anchors, list):
        return new_reg, ["WARN: delta has no list 'new_anchors'."]

    for entry in new_anchors:
        if not isinstance(entry, dict):
            continue
        aid = str(entry.get("id") or "").strip()
        title = str(entry.get("title") or "").strip()
        file_ = str(entry.get("file") or "").strip()
        aliases = entry.get("suggested_aliases") or []
        aliases = [str(a) for a in aliases if str(a).strip()]

        if not aid or not title:
            change_log.append(f"SKIP: missing id/title in entry: {entry}")
            continue

        existing = anchors.get(aid)
        if existing and isinstance(existing, dict):
            # merge aliases
            old_aliases = existing.get("aliases") or []
            merged = _dedupe_aliases(title, [*old_aliases, *aliases])
            if merged != old_aliases:
                existing["aliases"] = merged
                change_log.append(f"MERGE: updated aliases for {aid}")
            # fill file/title if missing
            if not existing.get("title"):
                existing["title"] = title
                change_log.append(f"MERGE: set title for {aid}")
            if file_ and not existing.get("file"):
                existing["file"] = file_
                change_log.append(f"MERGE: set file for {aid}")
            continue

        anchors[aid] = {
            "title": title,
            "file": file_ or None,
            "aliases": _dedupe_aliases(title, aliases),
            "status": "exists" if file_ else "unknown",
        }
        change_log.append(f"ADD: {aid} -> {title}")

    # normalize alias dedupe across entire registry (cheap cleanup)
    for aid, meta in anchors.items():
        if not isinstance(meta, dict):
            continue
        title = str(meta.get("title") or "").strip()
        meta["aliases"] = _dedupe_aliases(title, meta.get("aliases") or [])

    return new_reg, change_log


def main() -> int:
    ap = argparse.ArgumentParser(description="Merge TAG DELTA YAML into tag-registry.yml (anchors only).")
    ap.add_argument("--repo", type=str, default=".")
    ap.add_argument("--delta", type=str, required=True, help="TAG DELTA YAML file")
    ap.add_argument("--write", action="store_true", help="Actually write changes to tag-registry.yml")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    reg_path = repo / "tag-registry.yml"
    delta_path = (repo / args.delta).resolve() if not Path(args.delta).is_absolute() else Path(args.delta)

    if not reg_path.exists():
        print(f"ERROR: tag-registry.yml not found at {reg_path}", file=sys.stderr)
        return 2
    if not delta_path.exists():
        print(f"ERROR: delta not found at {delta_path}", file=sys.stderr)
        return 2

    reg = _read_yaml(reg_path)
    delta = _read_yaml(delta_path)

    before = _dump_yaml(reg)
    new_reg, log = merge(reg, delta)
    after = _dump_yaml(new_reg)

    if log:
        print("Change log:")
        for l in log[:200]:
            print(" -", l)
        if len(log) > 200:
            print(f" ... +{len(log)-200} more")
        print()

    if before == after:
        print("No changes.")
        return 0

    diff = _unified_diff(before, after, "tag-registry.yml (before)", "tag-registry.yml (after)")
    print(diff)

    if args.write:
        reg_path.write_text(after, encoding="utf-8")
        print("\nWROTE: tag-registry.yml updated.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
