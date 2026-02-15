#!/usr/bin/env python3
"""prompt_bundle.py

Generate a *small* prompt bundle (glossary + relevant registry slice) for a given raw section or .md file.

Why:
- Avoid pasting the full tag-registry.yml into your editing prompt.
- Keep only anchors that are likely relevant: current file anchors + any wikilinks referenced.

Outputs YAML to stdout by default.

Examples
  # For a raw chunk text file
  python tools/prompt_bundle.py --repo . --raw chunk.txt > prompt_bundle.yml

  # For an existing markdown file (includes anchors in that file)
  python tools/prompt_bundle.py --repo . --md draft/sequences/apprentice/seq-02.md > prompt_bundle.yml

  # Pipe raw text from clipboard
  pbpaste | python tools/prompt_bundle.py --repo . --stdin > prompt_bundle.yml

Notes
- This script is read-only.
- If `tag-registry.yml` is missing, it emits a glossary-only bundle.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml

WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
HEADING_ANCHOR_RE = re.compile(r"^#{1,6}\s+.+?\s*\{#([A-Za-z0-9][A-Za-z0-9\-_]*)\}\s*$", re.MULTILINE)


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def _parse_front_matter(text: str) -> Tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    # naive but good enough for this repo
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    fm_raw = parts[0].split("\n", 1)[1] if "\n" in parts[0] else ""
    try:
        fm = yaml.safe_load(fm_raw) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, parts[1]


def _extract_wikilink_targets(text: str) -> List[str]:
    targets: List[str] = []
    for m in WIKILINK_RE.finditer(text):
        inner = m.group(1).strip()
        if '|' in inner:
            target = inner.split('|', 1)[0].strip()
        else:
            target = inner
        targets.append(target)
    return targets


def _normalize_target(t: str) -> str:
    return t.strip()


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(_read_text(path)) or {}


def _index_anchors(reg: dict) -> Tuple[Dict[str, dict], Dict[str, str]]:
    """Return (anchors_by_id, lookup_by_title_or_alias_lower -> anchor_id)."""
    anchors_by_id: Dict[str, dict] = reg.get("anchors", {}) or {}
    lookup: Dict[str, str] = {}
    for aid, meta in anchors_by_id.items():
        if not isinstance(meta, dict):
            continue
        title = str(meta.get("title") or "").strip()
        if title:
            lookup[title.lower()] = aid
        for a in meta.get("aliases") or []:
            a = str(a).strip()
            if a:
                lookup.setdefault(a.lower(), aid)
    return anchors_by_id, lookup


def _slice_anchors(
    *,
    anchors_by_id: Dict[str, dict],
    lookup: Dict[str, str],
    targets: List[str],
    extra_anchor_ids: Set[str],
) -> Tuple[Dict[str, dict], List[str], List[str]]:
    """Returns (slice, found_ids, missing_targets)."""
    found_ids: Set[str] = set(extra_anchor_ids)
    missing: List[str] = []

    for raw_t in targets:
        t = _normalize_target(raw_t)
        if not t:
            continue
        # Ignore explicit missing refs (they're already flagged in text)
        if t.startswith("MISSING REF:"):
            continue
        # Support explicit id form: [[id:anchor-id]] or [[#anchor-id]]
        if t.startswith("id:"):
            aid = t[3:].strip()
            if aid in anchors_by_id:
                found_ids.add(aid)
            else:
                missing.append(t)
            continue
        if t.startswith("#"):
            aid = t[1:].strip()
            if aid in anchors_by_id:
                found_ids.add(aid)
            else:
                missing.append(t)
            continue

        aid = lookup.get(t.lower())
        if aid and aid in anchors_by_id:
            found_ids.add(aid)
        else:
            missing.append(t)

    # registry slice
    sliced: Dict[str, dict] = {}
    for aid in sorted(found_ids):
        meta = anchors_by_id.get(aid)
        if isinstance(meta, dict):
            # copy minimal fields
            sliced[aid] = {
                "title": meta.get("title"),
                "file": meta.get("file"),
                "aliases": meta.get("aliases") or [],
                "status": meta.get("status"),
            }

    return sliced, sorted(found_ids), missing


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a compact glossary+registry slice for prompting.")
    ap.add_argument("--repo", type=str, default=".", help="Repo root (contains tag-registry.yml)")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--raw", type=str, help="Path to raw chunk text")
    src.add_argument("--md", type=str, help="Path to an existing markdown file")
    src.add_argument("--stdin", action="store_true", help="Read raw chunk text from stdin")
    ap.add_argument("--include-glossary", action="store_true", default=True, help="Include glossary.yml")
    ap.add_argument("--no-glossary", dest="include_glossary", action="store_false")
    ap.add_argument("--max-aliases", type=int, default=6, help="Cap aliases per anchor in output (keeps bundles short)")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    reg_path = repo / "tag-registry.yml"
    gl_path = repo / "glossary.yml"

    reg_missing = False
    reg: dict = {}
    if not reg_path.exists():
        print(f"WARN: tag-registry.yml not found at: {reg_path}; emitting glossary-only bundle.", file=sys.stderr)
        reg_missing = True
    else:
        try:
            reg = _load_yaml(reg_path)
        except Exception as e:
            print(f"WARN: failed to parse tag-registry.yml ({e}); emitting glossary-only bundle.", file=sys.stderr)
            reg_missing = True
            reg = {}
    anchors_by_id, lookup = _index_anchors(reg)

    if args.stdin:
        text = sys.stdin.read()
    elif args.raw:
        text = _read_text((repo / args.raw).resolve() if not Path(args.raw).is_absolute() else Path(args.raw))
    else:
        md_path = (repo / args.md).resolve() if not Path(args.md).is_absolute() else Path(args.md)
        raw = _read_text(md_path)
        _fm, body = _parse_front_matter(raw)
        text = body

    targets = _extract_wikilink_targets(text)

    # If md file path is provided, include anchors that appear in that file.
    extra_ids: Set[str] = set()
    if args.md:
        md_path = (repo / args.md).resolve() if not Path(args.md).is_absolute() else Path(args.md)
        raw = _read_text(md_path)
        for aid in HEADING_ANCHOR_RE.findall(raw):
            extra_ids.add(aid)

    if reg_missing:
        sliced: Dict[str, dict] = {}
        found_ids = sorted(extra_ids)
        missing = []
    else:
        sliced, found_ids, missing = _slice_anchors(
            anchors_by_id=anchors_by_id,
            lookup=lookup,
            targets=targets,
            extra_anchor_ids=extra_ids,
        )

    # trim aliases
    for aid, meta in sliced.items():
        aliases = [str(a) for a in (meta.get("aliases") or []) if str(a).strip()]
        # de-dupe while preserving order
        seen = set()
        deduped = []
        for a in aliases:
            if a not in seen:
                seen.add(a)
                deduped.append(a)
        meta["aliases"] = deduped[: max(0, args.max_aliases)]

    out: dict = {}
    if args.include_glossary and gl_path.exists():
        out["glossary"] = _load_yaml(gl_path)

    out["tag_registry_slice"] = {
        "registry_present": not reg_missing,
        "anchors": sliced,
        "stats": {
            "anchors_in_slice": len(sliced),
            "wikilinks_found": len(targets),
        },
        "resolved_anchor_ids": found_ids,
        "missing_targets": missing,
    }

    yaml.safe_dump(out, sys.stdout, sort_keys=False, allow_unicode=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
