#!/usr/bin/env python3
"""find_ambiguous_wikilinks.py

Find wiki-links like [[Advancement]] that could resolve to multiple places.

This matters because your current rulebook_viewer.py resolves [[Title]] by *first heading title match*.
If the title exists in many files, your link may silently point to the wrong section.

The script:
- Loads tag-registry.yml (if present) and builds a map: link_text -> destinations.
- Falls back to heading-title matching when the registry is missing.
- Scans all <content-root>/**/*.md wiki-links.
- Reports wiki-links where link_text maps to 2+ destinations.
- Ignores flagged links like [[UNCLEAR: ...]] / [[TODO: ...]] / [[NOTE: ...]].

Usage
  python tools/find_ambiguous_wikilinks.py --repo .
  python tools/find_ambiguous_wikilinks.py --repo . --top 50
  python tools/find_ambiguous_wikilinks.py --repo . --content-root draft
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*(?:\{#[A-Za-z0-9][A-Za-z0-9\-_]*\})?\s*$")
FLAG_PREFIXES = ("UNCLEAR:", "TODO:", "NOTE:")
DEFAULT_CONTENT_ROOT = "draft"
LEGACY_CONTENT_ROOT = "build"
VALID_CONTENT_ROOTS = (DEFAULT_CONTENT_ROOT, LEGACY_CONTENT_ROOT)


def rel(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except Exception:
        return str(p).replace("\\", "/")


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


def build_known_targets_from_markdown(content_dir: Path, repo: Path) -> Dict[str, List[str]]:
    known: Dict[str, List[str]] = defaultdict(list)
    for p in content_dir.rglob("*.md"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        file_rel = rel(p, repo)
        for line_no, line in enumerate(txt.splitlines(), start=1):
            m = HEADING_RE.match(line.rstrip())
            if not m:
                continue
            title = m.group(2).strip()
            if title:
                known[title].append(f"{file_rel}:{line_no}")
    return known


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".", help="Repo root")
    ap.add_argument(
        "--content-root",
        default=DEFAULT_CONTENT_ROOT,
        help="Content folder to scan (default: draft; falls back to build if missing)",
    )
    ap.add_argument("--top", type=int, default=200, help="Max ambiguous link instances to print")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    content_dir = _resolve_content_root(repo, args.content_root)
    reg_path = repo / "tag-registry.yml"

    if not content_dir.exists():
        print(f"ERROR: missing {rel(content_dir, repo)}")
        return 2

    known: Dict[str, List[str]] = defaultdict(list)
    if reg_path.exists():
        try:
            reg = yaml.safe_load(reg_path.read_text(encoding="utf-8", errors="replace")) or {}
            for target, destinations in build_known_targets(reg).items():
                known[target].extend(destinations)
        except Exception as e:
            print(f"WARN: failed to parse {rel(reg_path, repo)} ({e}); using markdown headings only.")
    else:
        print(f"WARN: missing {rel(reg_path, repo)}; using markdown headings only.")

    for target, destinations in build_known_targets_from_markdown(content_dir, repo).items():
        known[target].extend(destinations)

    # De-duplicate destination lists to keep counts stable.
    for target, destinations in list(known.items()):
        deduped = list(dict.fromkeys(destinations))
        known[target] = deduped

    ambiguous_hits: List[Tuple[str, str, int, int]] = []
    # (target, file, line, num_destinations)

    for p in content_dir.rglob("*.md"):
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
