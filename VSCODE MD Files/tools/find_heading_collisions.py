#!/usr/bin/env python3
"""find_heading_collisions.py

Scan your repo for repeated heading titles (anchors optional), which makes title-based wikilinks ambiguous.

Outputs:
- a human-readable report (default)
- optional JSON via --json

Example
  python tools/find_heading_collisions.py --repo . --min-count 2
  python tools/find_heading_collisions.py --repo . --content-root draft

Read-only.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

HEADING_RE = re.compile(r"^(?P<h>#{1,6})\s+(?P<title>.+?)(?:\s*\{#(?P<id>[A-Za-z0-9][A-Za-z0-9\-_]*)\})?\s*$")
DEFAULT_CONTENT_ROOT = "draft"
LEGACY_CONTENT_ROOT = "build"
VALID_CONTENT_ROOTS = (DEFAULT_CONTENT_ROOT, LEGACY_CONTENT_ROOT)


def _resolve_content_root(repo: Path, content_root: str) -> Path:
    preferred = (content_root or DEFAULT_CONTENT_ROOT).strip()
    candidates: List[str] = []
    if preferred:
        candidates.append(preferred)
    for root_name in VALID_CONTENT_ROOTS:
        if root_name not in candidates:
            candidates.append(root_name)
    for root_name in candidates:
        candidate = repo / root_name
        if candidate.exists() and candidate.is_dir():
            return candidate
    return repo / preferred


def iter_md(repo: Path, content_root: str) -> List[Path]:
    root = _resolve_content_root(repo, content_root)
    return sorted(root.rglob("*.md"))


def rel(p: Path, repo: Path) -> str:
    try:
        return p.relative_to(repo).as_posix()
    except Exception:
        return p.as_posix()


def _slugify_anchor(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or "section"


def _unique_anchor(base: str, used: set, counts: Dict[str, int]) -> str:
    n = counts.get(base, 0)
    while True:
        candidate = base if n == 0 else f"{base}-{n+1}"
        if candidate not in used:
            break
        n += 1
    counts[base] = n + 1
    used.add(candidate)
    return candidate


def main() -> int:
    ap = argparse.ArgumentParser(description="Find repeated heading titles that cause ambiguous [[Title]] links.")
    ap.add_argument("--repo", type=str, default=".")
    ap.add_argument(
        "--content-root",
        type=str,
        default=DEFAULT_CONTENT_ROOT,
        help="Content folder to scan (default: draft; falls back to build if missing)",
    )
    ap.add_argument("--min-count", type=int, default=2)
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()

    hits: Dict[str, List[Tuple[str, int, int, str]]] = defaultdict(list)
    for md in iter_md(repo, args.content_root):
        text = md.read_text(encoding="utf-8", errors="replace")
        used: set = set()
        counts: Dict[str, int] = {}
        for i, line in enumerate(text.splitlines(), start=1):
            m = HEADING_RE.match(line.rstrip())
            if not m:
                continue
            lvl = len(m.group("h"))
            title = m.group("title").strip()
            aid = m.group("id")
            if aid:
                anchor = aid
                used.add(anchor)
            else:
                anchor = _unique_anchor(_slugify_anchor(title), used, counts)
            hits[title].append((rel(md, repo), i, lvl, anchor))

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
