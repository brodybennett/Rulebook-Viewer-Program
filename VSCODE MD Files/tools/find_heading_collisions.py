#!/usr/bin/env python3
"""find_heading_collisions.py

Scan your repo for repeated heading titles (with anchors), which makes title-based wikilinks ambiguous.

Outputs:
- a human-readable report (default)
- optional JSON via --json

Example
  python tools/find_heading_collisions.py --repo . --min-count 2

Read-only.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*\{#([A-Za-z0-9][A-Za-z0-9\-_]*)\}\s*$")


def iter_md(repo: Path) -> List[Path]:
    build = repo / "build"
    root = build if build.exists() else repo
    return sorted(root.rglob("*.md"))


def rel(p: Path, repo: Path) -> str:
    try:
        return p.relative_to(repo).as_posix()
    except Exception:
        return p.as_posix()


def main() -> int:
    ap = argparse.ArgumentParser(description="Find repeated heading titles that cause ambiguous [[Title]] links.")
    ap.add_argument("--repo", type=str, default=".")
    ap.add_argument("--min-count", type=int, default=2)
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()

    hits: Dict[str, List[Tuple[str, int, int, str]]] = defaultdict(list)
    for md in iter_md(repo):
        text = md.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), start=1):
            m = HEADING_RE.match(line.strip())
            if not m:
                continue
            lvl = len(m.group(1))
            title = m.group(2).strip()
            aid = m.group(3)
            hits[title].append((rel(md, repo), i, lvl, aid))

    collisions = {k: v for k, v in hits.items() if len(v) >= args.min_count}

    if args.json:
        out = {
            "repo": str(repo),
            "min_count": args.min_count,
            "collisions": {
                title: [
                    {"file": f, "line": line, "level": lvl, "anchor": aid}
                    for (f, line, lvl, aid) in entries
                ]
                for title, entries in sorted(collisions.items(), key=lambda x: (-len(x[1]), x[0].lower()))
            },
        }
        Path(args.json).write_text(json.dumps(out, indent=2), encoding="utf-8")

    # human report
    ordered = sorted(collisions.items(), key=lambda x: (-len(x[1]), x[0].lower()))
    if not ordered:
        print("No heading collisions found.")
        return 0

    print(f"Heading collisions (count >= {args.min_count}): {len(ordered)} titles\n")
    for title, entries in ordered:
        print(f"- {title}  (x{len(entries)})")
        for f, line, lvl, aid in entries[:20]:
            print(f"    - {f}:{line}  (h{lvl})  {{#{aid}}}")
        if len(entries) > 20:
            print(f"    ... +{len(entries)-20} more")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
