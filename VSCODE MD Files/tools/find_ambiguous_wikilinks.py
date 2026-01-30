#!/usr/bin/env python3
"""find_ambiguous_wikilinks.py

Find wiki-links like [[Advancement]] that could resolve to multiple places.

This matters because your current rulebook_viewer.py resolves [[Title]] by *first heading title match*.
If the title exists in many files, your link may silently point to the wrong section.

The script:
- Loads tag-registry.yml and builds a map: link_text -> list of destinations.
- Scans all build/**/*.md wiki-links.
- Reports wiki-links where link_text maps to 2+ destinations.
- Ignores flagged links like [[UNCLEAR: ...]] / [[TODO: ...]] / [[NOTE: ...]].

Usage
  python tools/find_ambiguous_wikilinks.py --repo .
  python tools/find_ambiguous_wikilinks.py --repo . --top 50
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
FLAG_PREFIXES = ("UNCLEAR:", "TODO:", "NOTE:")


def rel(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except Exception:
        return str(p).replace("\\", "/")


def parse_wikilinks(text: str) -> List[Tuple[str, int]]:
    out: List[Tuple[str, int]] = []
    for i, line in enumerate(text.splitlines(), start=1):
        for m in WIKILINK_RE.finditer(line):
            inner = m.group(1).strip()
            if "|" in inner:
                target, _display = inner.split("|", 1)
                target = target.strip()
            else:
                target = inner
            out.append((target, i))
    return out


def build_known_targets(reg: dict) -> Dict[str, List[str]]:
    known: Dict[str, List[str]] = defaultdict(list)

    # file titles
    for entry in (reg.get("files") or []):
        title = (entry.get("title") or "").strip()
        path = (entry.get("path") or "").strip()
        if title and path:
            known[title].append(path)

    # anchors + aliases
    anchors = reg.get("anchors") or {}
    if isinstance(anchors, dict):
        for aid, meta in anchors.items():
            if not isinstance(meta, dict):
                continue
            file = (meta.get("file") or "").strip() or "(anchor)"
            title = (meta.get("title") or "").strip()
            if title:
                known[title].append(f"{file}#{aid}")
            for al in (meta.get("aliases") or []) or []:
                al = str(al).strip()
                if al:
                    known[al].append(f"{file}#{aid}")
    return known


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".", help="Repo root (contains tag-registry.yml)")
    ap.add_argument("--top", type=int, default=200, help="Max ambiguous link instances to print")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    build_dir = repo / "build"
    reg_path = repo / "tag-registry.yml"

    if not reg_path.exists():
        print(f"ERROR: missing {rel(reg_path, repo)}")
        return 2

    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8", errors="replace")) or {}
    known = build_known_targets(reg)

    if not build_dir.exists():
        print(f"ERROR: missing {rel(build_dir, repo)}")
        return 2

    ambiguous_hits: List[Tuple[str, str, int, int]] = []
    # (target, file, line, num_destinations)

    for p in build_dir.rglob("*.md"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        r = rel(p, repo)
        for target, line in parse_wikilinks(txt):
            if any(target.startswith(prefix) for prefix in FLAG_PREFIXES):
                continue
            # id-based links are already unambiguous
            if target.startswith("id:") or target.startswith("#"):
                continue
            dests = known.get(target)
            if dests and len(dests) >= 2:
                ambiguous_hits.append((target, r, line, len(dests)))

    if not ambiguous_hits:
        print("No ambiguous wiki-links found (nice).")
        return 0

    ambiguous_hits.sort(key=lambda x: (-x[3], x[0].lower(), x[1], x[2]))

    print(f"Ambiguous wiki-link instances: {len(ambiguous_hits)}")
    print(f"(showing up to {args.top})\n")

    shown = 0
    for target, file, line, n in ambiguous_hits:
        print(f"- [[{target}]]  ({n} destinations)  at {file}:{line}")
        shown += 1
        if shown >= args.top:
            break

    print("\nTip: switch these to id-based links, e.g. [[id:<anchor-id>|Display Text]]")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
