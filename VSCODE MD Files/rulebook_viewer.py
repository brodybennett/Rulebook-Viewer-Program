#!/usr/bin/env python3
"""
Rulebook Viewer (MVP) - single-file, read-only local web app

Features
- Reads Markdown files (optionally via tag-registry.yml order)
- Renders Markdown (tables, task lists, formatting) with Mistune
- Supports "{#anchor}" heading anchors and auto-generated heading anchors
- Supports wiki-links: [[Exact Section Title]] and [[Target|Display]]
- Sidebar navigation + search
- Read-only: never modifies your markdown files

python "VSCODE MD Files/rulebook_viewer.py" --source "VSCODE MD Files" --content-root draft


Usage examples
  python rulebook_viewer.py
  python rulebook_viewer.py --source /path/to/repo
  python rulebook_viewer.py --source "/path/to/VSCODE MD Files.zip"
  python rulebook_viewer.py --source /path/to/repo --content-root draft
  python rulebook_viewer.py --port 7860 --no-browser
"""

from __future__ import annotations

import argparse
import dataclasses
import html
import json
import os
import re
import sys
import tempfile
import textwrap
import urllib.parse
import webbrowser
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from flask import Flask, abort, redirect, render_template_string, request, url_for, Response
except ImportError:
    print("[error] Missing dependency: flask\n\nInstall with: pip install flask", file=sys.stderr)
    raise SystemExit(2)

try:
    import yaml
except ImportError:
    print("[error] Missing dependency: pyyaml\n\nInstall with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

try:
    import mistune
    from mistune.plugins import table, task_lists, formatting, footnotes, url
except ImportError:
    print("[error] Missing dependency: mistune\n\nInstall with: pip install mistune", file=sys.stderr)
    raise SystemExit(2)

# ----------------------------
# Data model
# ----------------------------

DEFAULT_CONTENT_ROOT = "draft"
LEGACY_CONTENT_ROOT = "build"
VALID_CONTENT_ROOTS = (DEFAULT_CONTENT_ROOT, LEGACY_CONTENT_ROOT)

@dataclasses.dataclass(frozen=True)
class Doc:
    doc_id: str
    title: str
    relpath: str  # posix-style path relative to repo root, e.g. "draft/core-rules/checks.md"
    abspath: Optional[str]  # None if missing/planned
    tags: List[str]
    status: str  # exists/planned/unknown


@dataclasses.dataclass
class Index:
    repo_root: Path
    content_root: str  # preferred content root name ("draft" or "build")
    content_prefix: str  # actual prefix used in relpaths, includes trailing "/" when present
    docs_by_id: Dict[str, Doc]
    order: List[str]  # doc_ids in nav order
    path_to_id: Dict[str, str]  # relpath -> doc_id
    # Heading text -> (doc_id, anchor_id)
    heading_index: Dict[str, Tuple[str, str]]
    # (doc_id) -> list of (level, heading_text, anchor_id)
    toc_by_doc: Dict[str, List[Tuple[int, str, str]]]
    anchor_to_doc: Dict[str, str] # anchor_id -> doc_id


# ----------------------------
# Markdown processing
# ----------------------------

HEADING_LINE_RE = re.compile(
    r'^(?P<h>#{1,6})\s+(?P<title>.+?)(?:\s*\{#(?P<id>[A-Za-z0-9\-_]+)\})?\s*$'
)

WIKILINK_RE = re.compile(r'\[\[(.+?)\]\]')  # [[Target]] or [[Target|Display]]
UNCLEAR_RE = re.compile(r'\[\[UNCLEAR:\s*(.+?)\]\]')
ABILITY_FENCE_START_RE = re.compile(r'^\s*```(?:ya?ml)\s+ability\s*$', re.IGNORECASE)
FENCE_END_RE = re.compile(r'^\s*```\s*$')

ABILITY_DICE_FIELDS = (
    ("check_roll", "Check"),
    ("damage_roll", "Damage"),
    ("heal_roll", "Heal"),
    ("effect_roll", "Effect"),
    ("notes", "Notes"),
)

def _strip_front_matter(md_text: str) -> Tuple[Dict, str]:
    """
    Returns (front_matter_dict, body_markdown).
    If no front matter, returns ({}, md_text).
    """
    # Some files may start with a UTF-8 BOM; strip it so front matter and first
    # heading parsing works consistently.
    if md_text.startswith("\ufeff"):
        md_text = md_text[1:]

    # find second '---' on its own line (supports Windows CRLF)
    # Allow harmless leading blank lines before front matter.
    m = re.match(
        r'\A(?:[ \t]*\r?\n)*---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)',
        md_text,
        flags=re.DOTALL,
    )
    if m:
        fm_raw = m.group(1)
        try:
            fm = yaml.safe_load(fm_raw) or {}
        except Exception:
            fm = {}
        body = md_text[m.end():]
        return fm, body
    return {}, md_text


def _slugify_anchor(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
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


def _process_headings(body: str, inject: bool) -> Tuple[List[Tuple[int, str, str]], Optional[str]]:
    toc: List[Tuple[int, str, str]] = []
    out_lines: List[str] = []
    used: set = set()
    counts: Dict[str, int] = {}

    for line in body.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        newline = line[len(content):]
        m = HEADING_LINE_RE.match(content)
        if not m:
            if inject:
                out_lines.append(line)
            continue

        hashes = m.group('h')
        raw_title = m.group('title') or ""
        explicit_id = m.group('id')
        title = raw_title.strip()

        if explicit_id:
            anchor = explicit_id.strip()
            used.add(anchor)
        else:
            base = _slugify_anchor(title)
            anchor = _unique_anchor(base, used, counts)

        toc.append((len(hashes), title, anchor))

        if inject:
            clean_title = raw_title.rstrip()
            heading_line = f"{hashes} {clean_title}".rstrip() + newline
            line_break = newline if newline else "\n"
            anchor_line = f"<a id=\"{html.escape(anchor, quote=True)}\"></a>{line_break}"
            out_lines.append(anchor_line)
            out_lines.append(heading_line)

    return toc, "".join(out_lines) if inject else None


def _inject_heading_anchors(body: str) -> str:
    _toc, updated = _process_headings(body, inject=True)
    return updated if updated is not None else body


def _wikilink_html(inner: str) -> str:
    if inner.lower().startswith("link later:"):
        payload = inner[len("LINK LATER:"):].strip()
        parts = [p.strip() for p in payload.split("|") if p.strip()]

        target = parts[0] if parts else ""
        meta = {}
        for part in parts[1:]:
            if "=" in part:
                k, v = part.split("=", 1)
                meta[k.strip().lower()] = v.strip()
            else:
                meta.setdefault("hint", part)

        if not target:
            return html.escape(f"[[{inner}]]")

        type_ = meta.get("type", "").strip()
        hint = meta.get("hint", "").strip()

        title_bits = ["Link later"]
        if type_:
            title_bits.append(f"type={type_}")
        if hint:
            title_bits.append(f"hint={hint}")
        title_attr = " | ".join(title_bits)

        href = "/search?q=" + urllib.parse.quote(target, safe="")
        return (
            f'<a class="linklater" href="{href}" '
            f'title="{html.escape(title_attr, quote=True)}">{html.escape(target)}</a>'
        )

    if "|" in inner:
        target, display = inner.split("|", 1)
        target = target.strip()
        display = display.strip()
    else:
        target, display = inner, inner
    href = "/w/" + urllib.parse.quote(target, safe="")
    return f'<a class="wikilink" href="{href}">{html.escape(display)}</a>'


def _replace_unclear(text: str) -> str:
    def repl_unclear(m: re.Match) -> str:
        msg = m.group(1).strip()
        safe = html.escape(msg)
        return f'<span class="unclear">UNCLEAR: {safe}</span>'

    return UNCLEAR_RE.sub(repl_unclear, text)


def _replace_wikilinks(text: str) -> str:
    def repl_wikilink(m: re.Match) -> str:
        inner = m.group(1).strip()
        return _wikilink_html(inner)

    return WIKILINK_RE.sub(repl_wikilink, text)


def _escape_and_linkify_wikilinks(text: str) -> str:
    if not text:
        return ""
    out: List[str] = []
    last = 0
    for m in WIKILINK_RE.finditer(text):
        out.append(html.escape(text[last:m.start()]))
        out.append(_wikilink_html(m.group(1).strip()))
        last = m.end()
    out.append(html.escape(text[last:]))
    return "".join(out)


def _render_markdown_snippet(text: str) -> str:
    if not text:
        return ""
    snippet = _replace_unclear(text)
    snippet = _replace_wikilinks(snippet)
    return MD(snippet)


def _format_scalar(value, *, linkify: bool = False) -> str:
    if value is None or value == "":
        return '<span class="ability-muted">none</span>'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if linkify:
        return _escape_and_linkify_wikilinks(text)
    return html.escape(text)


def _format_map(value, *, linkify: bool = False) -> str:
    if not isinstance(value, dict) or not value:
        return '<span class="ability-muted">none</span>'
    parts: List[str] = []
    for k, v in value.items():
        key = html.escape(str(k))
        if isinstance(v, dict):
            val = _format_map(v, linkify=linkify)
        elif isinstance(v, list):
            val = _format_list(v, linkify=linkify)
        else:
            val = _format_scalar(v, linkify=linkify)
        parts.append(f'<div class="ability-kv"><span class="ability-k">{key}</span>: <span class="ability-v">{val}</span></div>')
    return "".join(parts)


def _format_list(value, *, linkify: bool = False) -> str:
    if not isinstance(value, list) or not value:
        return '<span class="ability-muted">none</span>'
    items = []
    for entry in value:
        if isinstance(entry, dict):
            when = _format_scalar(entry.get("when"), linkify=linkify)
            changes = entry.get("changes")
            if isinstance(changes, dict):
                changes_html = _format_map(changes, linkify=linkify)
            else:
                changes_html = _format_scalar(changes, linkify=linkify)
            item = (
                f'<div><span class="ability-k">when</span>: {when}</div>'
                f'<div><span class="ability-k">changes</span>: {changes_html}</div>'
            )
            items.append(f"<li>{item}</li>")
        else:
            items.append(f"<li>{_format_scalar(entry, linkify=linkify)}</li>")
    return '<ul class="ability-list">' + "".join(items) + "</ul>"


def _render_dice_table(dice: dict) -> str:
    if not isinstance(dice, dict) or not dice:
        return '<span class="ability-muted">none</span>'
    rows = []
    for key, label in ABILITY_DICE_FIELDS:
        val = dice.get(key)
        if val is None or val == "":
            val_html = '<span class="ability-muted">none</span>'
        else:
            if key == "notes":
                val_html = _escape_and_linkify_wikilinks(str(val))
            else:
                val_html = html.escape(str(val))
        rows.append(f"<tr><th>{label}</th><td>{val_html}</td></tr>")
    return '<table class="ability-dice">' + "".join(rows) + "</table>"


def _ability_html_from_data(data: dict, raw_yaml: str) -> str:
    name = data.get("name") or data.get("id") or "Ability"
    ability_id = data.get("id") or ""
    pathway = data.get("pathway")
    sequence = data.get("sequence")
    status = data.get("status")
    type_ = data.get("type")
    action = data.get("action")
    cost = data.get("cost")
    roll = data.get("roll")
    opposed_by = data.get("opposed_by")
    range_ = data.get("range")
    target = data.get("target")
    duration = data.get("duration")
    tags = data.get("tags")
    scaling = data.get("scaling")
    dice = data.get("dice") or {}
    text = data.get("text")

    badges = []
    if pathway:
        badges.append(f'<span class="ability-badge">Pathway: {html.escape(str(pathway))}</span>')
    if sequence is not None:
        badges.append(f'<span class="ability-badge">Sequence {html.escape(str(sequence))}</span>')
    if status:
        badges.append(f'<span class="ability-badge">{html.escape(str(status))}</span>')
    badge_html = "".join(badges)

    tags_html = ""
    if isinstance(tags, list) and tags:
        tags_html = "".join(f'<span class="ability-tag">{html.escape(str(t))}</span>' for t in tags)
    else:
        tags_html = '<span class="ability-muted">none</span>'

    rows = [
        ("Type", _format_scalar(type_)),
        ("Action", _format_scalar(action)),
        ("Cost", _format_map(cost, linkify=True)),
        ("Roll", _format_scalar(roll)),
        ("Opposed By", _format_scalar(opposed_by)),
        ("Range", _format_scalar(range_, linkify=True)),
        ("Target", _format_scalar(target, linkify=True)),
        ("Duration", _format_scalar(duration, linkify=True)),
    ]
    row_html = "".join(f"<tr><th>{label}</th><td>{val}</td></tr>" for label, val in rows)

    scaling_html = _format_list(scaling, linkify=True)
    dice_html = _render_dice_table(dice)
    text_html = _render_markdown_snippet(str(text)) if isinstance(text, str) and text.strip() else ""

    raw_yaml = raw_yaml.rstrip("\n")
    raw_yaml_html = html.escape(raw_yaml)

    return (
        '<div class="ability-card">'
        f'<div class="ability-head">'
        f'<div><div class="ability-name">{html.escape(str(name))}</div>'
        f'<div class="ability-id">{html.escape(str(ability_id))}</div></div>'
        f'<div class="ability-badges">{badge_html}</div>'
        '</div>'
        f'<table class="ability-table">{row_html}</table>'
        f'<div class="ability-section"><div class="ability-section-title">Tags</div><div class="ability-tags">{tags_html}</div></div>'
        f'<div class="ability-section"><div class="ability-section-title">Dice</div>{dice_html}</div>'
        f'<div class="ability-section"><div class="ability-section-title">Scaling</div>{scaling_html}</div>'
        f'<div class="ability-section"><div class="ability-section-title">Text</div><div class="ability-text">{text_html}</div></div>'
        f'<details class="ability-raw"><summary>Raw YAML</summary><pre><code>{raw_yaml_html}</code></pre></details>'
        '</div>'
    )


def _render_ability_yaml_block(yaml_text: str) -> str:
    try:
        data = yaml.safe_load(yaml_text) or {}
    except Exception:
        data = None
    if not isinstance(data, dict) or not data:
        safe = html.escape(yaml_text.rstrip("\n"))
        return f"<pre><code>{safe}</code></pre>"
    return _ability_html_from_data(data, yaml_text)


def _render_ability_blocks(body: str) -> str:
    lines = body.splitlines(keepends=True)
    out: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if ABILITY_FENCE_START_RE.match(line):
            i += 1
            yaml_lines: List[str] = []
            while i < len(lines) and not FENCE_END_RE.match(lines[i]):
                yaml_lines.append(lines[i])
                i += 1
            if i < len(lines) and FENCE_END_RE.match(lines[i]):
                i += 1
            yaml_text = "".join(yaml_lines)
            out.append(_render_ability_yaml_block(yaml_text))
            out.append("\n")
            continue
        out.append(line)
        i += 1
    return "".join(out)


def _preprocess_markdown(body: str) -> str:
    """
    Minimal transformations to preserve intended formatting + enable anchors.
    - Converts heading anchors and auto-anchors: "## Title" => "<a id='title'></a>\n## Title"
    - Styles [[UNCLEAR: ...]] with a span (still readable as text)
    - Converts wiki-links [[Target]] / [[Target|Text]] to HTML links (resolved server-side)
    """
    body = _inject_heading_anchors(body)
    body = _render_ability_blocks(body)
    body = _replace_unclear(body)
    body = _replace_wikilinks(body)
    return body


def _make_markdown_renderer() -> mistune.Markdown:
    """
    Mistune renderer configured for "rulebook-style" markdown:
    - tables
    - task lists
    - formatting extensions
    - footnotes
    - urls
    Raw HTML is allowed (we inject anchors + wikilinks).
    """
    renderer = mistune.HTMLRenderer(escape=False)
    md = mistune.create_markdown(
        renderer=renderer,
        plugins=[
            table.table,
            task_lists.task_lists,
            formatting.strikethrough,
            formatting.subscript,
            formatting.superscript,
            formatting.mark,
            formatting.insert,
            footnotes.footnotes,
            url.url,
        ],
    )
    return md


MD = _make_markdown_renderer()


def _extract_headings_for_toc(body: str) -> List[Tuple[int, str, str]]:
    """
    Extract headings (explicit {#id} or auto-generated).
    Returns list of (level, heading_text, anchor_id).
    """
    toc, _ = _process_headings(body, inject=False)
    return toc


# ----------------------------
# Display helpers
# ----------------------------

CHAPTER_PREFIX_RE = re.compile(r'^\s*chapter\s+\d+\s*[:\-]\s*', re.IGNORECASE)

SPECIAL_LABELS = {
    "front-matter": "Front Matters",
    "lore-reference": "Lore Reference",
    "core-rules": "Core Rules",
    "advanced-systems": "Advanced Systems",
    "sequences": "Sequences",
    "supplementary": "Supplementary",
}

def _clean_label(seg: str) -> str:
    # Strip leading numeric prefixes from folder/file segments for a cleaner nav label.
    seg = re.sub(r"^\d+[-_ ]+", "", seg)
    seg = seg.strip()
    if not seg:
        return seg
    if seg in SPECIAL_LABELS:
        return SPECIAL_LABELS[seg]
    label = seg.replace("_", " ").replace("-", " ").strip()
    return label.title() if label else seg

def _display_title(raw_title: str) -> str:
    title = CHAPTER_PREFIX_RE.sub("", raw_title).strip()
    title = re.sub(r"\s+", " ", title)
    if title.lower() == "index":
        return ""
    return title or raw_title.strip()

def _display_title_for_doc(doc: Doc) -> str:
    title = _display_title(doc.title)
    if title:
        return title
    rel = doc.relpath.replace("\\", "/")
    if _is_index_relpath(rel):
        parent = Path(rel).parent.name
        if parent:
            return _clean_label(parent)
    stem = Path(rel).stem
    if stem.lower() == "index":
        parent = Path(rel).parent.name
        if parent:
            return _clean_label(parent)
        return "Overview"
    fallback = stem.replace("_", " ").replace("-", " ").strip().title()
    return fallback or doc.title

def _is_index_relpath(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    return rel.endswith("/index.md")


# ----------------------------
# Index building
# ----------------------------

def _safe_relpath(p: Path) -> str:
    return p.as_posix().lstrip('/')

def _find_repo_root(start: Path) -> Path:
    """
    Find a directory containing tag-registry.yml, searching up to 3 parents.
    If not found, return start.
    """
    cur = start.resolve()
    for _ in range(4):
        if (cur / "tag-registry.yml").exists():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return start.resolve()

def _load_registry(repo_root: Path) -> Optional[dict]:
    reg_path = repo_root / "tag-registry.yml"
    if not reg_path.exists():
        return None
    try:
        data = yaml.safe_load(reg_path.read_text(encoding="utf-8", errors="replace"))
        if isinstance(data, dict) and isinstance(data.get("files"), list):
            return data
    except Exception:
        return None
    return None

def _slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s or "doc"

HIDDEN_SEGMENTS = {
    "_templates",
    ".git",
    ".github",
    ".vscode",
    "__pycache__",
    "node_modules",
}

def _is_hidden_relpath(rel: str) -> bool:
    """
    Return True when any path segment is an editor/cache folder or starts with _ / .
    These files are ignored for nav/search so templates and tooling docs stay out of the UI.
    """
    parts = rel.replace("\\", "/").split("/")
    for part in parts:
        if not part:
            continue
        low = part.lower()
        if part.startswith(("_", ".")) or low in HIDDEN_SEGMENTS:
            return True
    return False

def _discover_content_root(repo_root: Path, content_root: str) -> Path:
    """
    Prefer the requested content root, then fall back between draft/build, else repo_root.
    """
    preferred = (content_root or DEFAULT_CONTENT_ROOT).strip()
    candidates: List[str] = []
    if preferred:
        candidates.append(preferred)
    for root_name in VALID_CONTENT_ROOTS:
        if root_name not in candidates:
            candidates.append(root_name)
    for root_name in candidates:
        candidate = repo_root / root_name
        if candidate.exists() and candidate.is_dir():
            return candidate
    return repo_root

def build_index(source_root: Path, content_root: str = DEFAULT_CONTENT_ROOT) -> Index:
    repo_root = _find_repo_root(source_root)
    registry = _load_registry(repo_root)
    content_root = (content_root or DEFAULT_CONTENT_ROOT).strip()
    content_dir = _discover_content_root(repo_root, content_root)
    content_prefix = ""
    if content_dir != repo_root:
        try:
            content_prefix = _safe_relpath(content_dir.relative_to(repo_root))
        except Exception:
            content_prefix = ""
        if content_prefix and not content_prefix.endswith("/"):
            content_prefix += "/"

    docs_by_id: Dict[str, Doc] = {}
    order: List[str] = []
    path_to_id: Dict[str, str] = {}

    anchor_to_doc: Dict[str, str] = {}


    heading_index: Dict[str, Tuple[str, str]] = {}
    toc_by_doc: Dict[str, List[Tuple[int, str, str]]] = {}

    # 1) Load docs from registry (preferred order)
    if registry:
        for entry in registry.get("files", []):
            try:
                rel = str(entry.get("path", "")).strip()
                if not rel:
                    continue
                rel_posix = rel.replace("\\", "/")
                if content_prefix and not rel_posix.startswith(content_prefix):
                    continue
                if _is_hidden_relpath(rel_posix):
                    continue
                doc_id = str(entry.get("id") or "").strip() or _slugify(rel_posix)
                title = str(entry.get("title") or Path(rel_posix).stem).strip()
                tags = entry.get("tags") or []
                if not isinstance(tags, list):
                    tags = []
                status = str(entry.get("status") or "unknown").strip()

                abs_path = (repo_root / rel_posix).resolve()
                abspath_str = str(abs_path) if abs_path.exists() else None

                # If file exists, prefer front matter for title/id/tags when present
                if abspath_str:
                    raw = abs_path.read_text(encoding="utf-8", errors="replace")
                    fm, _body = _strip_front_matter(raw)
                    title = str(fm.get("title") or title).strip()
                    doc_id = str(fm.get("id") or doc_id).strip()
                    fm_tags = fm.get("tags")
                    if isinstance(fm_tags, list) and fm_tags:
                        tags = [str(t) for t in fm_tags]
                    status = "exists"

                    # Headings for toc/index
                    toc_by_doc[doc_id] = _extract_headings_for_toc(_body)
                    for lvl, htxt, aid in toc_by_doc[doc_id]:
                        # exact heading text mapping
                        if htxt not in heading_index:
                            heading_index[htxt] = (doc_id, aid)

                doc = Doc(
                    doc_id=doc_id,
                    title=title,
                    relpath=rel_posix,
                    abspath=abspath_str,
                    tags=[str(t) for t in tags],
                    status=status,
                )
                docs_by_id[doc_id] = doc
                path_to_id[rel_posix] = doc_id
                order.append(doc_id)
            except Exception:
                continue

    # 2) Add any markdown files not in registry (discovered)
    for p in sorted(content_dir.rglob("*.md")):
        try:
            rel = _safe_relpath(p.relative_to(repo_root))
        except Exception:
            continue
        if _is_hidden_relpath(rel):
            continue

        if rel in path_to_id:
            continue

        raw = p.read_text(encoding="utf-8", errors="replace")
        fm, _body = _strip_front_matter(raw)
        doc_id = str(fm.get("id") or _slugify(rel)).strip()
        title = str(fm.get("title") or _first_heading_title(raw) or p.stem).strip()
        tags = fm.get("tags") if isinstance(fm.get("tags"), list) else []
        toc_by_doc[doc_id] = _extract_headings_for_toc(_body)
        for lvl, htxt, aid in toc_by_doc[doc_id]:
            if htxt not in heading_index:
                heading_index[htxt] = (doc_id, aid)

        doc = Doc(
            doc_id=doc_id,
            title=title,
            relpath=rel,
            abspath=str(p.resolve()),
            tags=[str(t) for t in tags],
            status="exists",
        )
        docs_by_id[doc_id] = doc
        path_to_id[rel] = doc_id
        order.append(doc_id)

    # 3) Deduplicate order while preserving first occurrence
    seen = set()
    deduped = []
    for d in order:
        if d in docs_by_id and d not in seen:
            deduped.append(d)
            seen.add(d)
    order = deduped

    # 4) Map registry anchors (id -> file) to doc_ids (used by [[id:...]] linking).
    if registry:
        reg_anchors = registry.get("anchors") or {}
        if isinstance(reg_anchors, dict):
            for aid, meta in reg_anchors.items():
                if not isinstance(meta, dict):
                    continue
                f = str(meta.get("file") or "").replace("\\", "/").strip()
                if not f:
                    continue
                did = path_to_id.get(f)
                if did:
                    anchor_to_doc[aid] = did

    # 5) Fallback: map heading anchors to docs when registry is absent/incomplete.
    for did, toc in toc_by_doc.items():
        for _, _, aid in toc:
            anchor_to_doc.setdefault(aid, did)

    # 6) Case-insensitive heading lookup fallback
    # (Only add if it doesn't shadow an exact match.)
    for htxt, (did, aid) in list(heading_index.items()):
        low = htxt.lower()
        if low not in heading_index:
            heading_index[low] = (did, aid)

    order = _apply_custom_order(order, docs_by_id, content_prefix)

    return Index(
        repo_root=repo_root,
        content_root=content_root,
        content_prefix=content_prefix,
        docs_by_id=docs_by_id,
        order=order,
        path_to_id=path_to_id,
        heading_index=heading_index,
        toc_by_doc=toc_by_doc,
        anchor_to_doc=anchor_to_doc,
    )


def _first_heading_title(raw: str) -> Optional[str]:
    """
    Best-effort: return first Markdown ATX heading text.
    """
    for line in raw.splitlines():
        m = re.match(r'^\s*#{1,6}\s+(.+?)\s*$', line)
        if m:
            txt = m.group(1)
            txt = re.sub(r'\s*\{#.*?\}\s*$', '', txt).strip()
            if txt:
                return txt
    return None


# ----------------------------
# HTML UI (single template)
# ----------------------------

BASE_TEMPLATE = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{{ page_title }}</title>
  <link rel="stylesheet" href="{{ url_for('viewer_css') }}?v={{ css_version }}" />
  <script defer src="{{ url_for('viewer_js') }}?v={{ js_version }}"></script>
</head>
<body>
  <div class="app" id="app">
    <aside class="sidebar" id="sidebar" aria-label="Rulebook navigation">
      <div class="brand">
        <div class="sigil" aria-hidden="true">⟡</div>
        <div class="brand-text">
          <div class="title">Lord of Mysteries • TTRPG</div>
          <div class="sub">Rulebook Viewer (draft)</div>
        </div>
      </div>

      <div class="nav-wrap">
        <div class="nav-header">
          <div class="nav-title">Contents</div>
          <button class="iconbtn" type="button" data-action="collapse-all" title="Collapse all">▾</button>
        </div>
        <nav class="nav" id="nav">
          {{ nav_html|safe }}
        </nav>
      </div>
    </aside>

    <section class="content">
      <header class="topbar">
        <button class="iconbtn" type="button" data-action="toggle-sidebar" aria-label="Toggle sidebar">☰</button>
        <form class="search" action="{{ url_for('search') }}" method="get" role="search">
          <input type="search" name="q" value="{{ query|default('') }}" placeholder="Search the rulebook…" />
          <button class="btn" type="submit">Search</button>
          <a class="btn btn-ghost" href="{{ url_for('reload_index') }}">Reload</a>
        </form>
      </header>

      <div class="content-body">
        <main class="main" id="main">
          {% if is_search %}
            <h1 class="page-title">Search</h1>
            <div class="meta">Query: <code>{{ query }}</code> • Results: {{ results|length }}</div>
            <div class="search-results">
              {% for r in results %}
                <div class="result">
                  <div class="rtitle"><a href="{{ r.href }}">{{ r.title }}</a></div>
                  <div class="rsnip">{{ r.snippet }}</div>
                  <div class="meta">{{ r.relpath }}</div>
                </div>
              {% endfor %}
            </div>
          {% else %}
            <div class="md">
              {{ content_html|safe }}
            </div>

            <div class="meta">
              <div>File: <code>{{ relpath }}</code></div>
              {% if tags and tags|length > 0 %}
                <div>Tags: {{ tags|join(', ') }}</div>
              {% endif %}
              <div>Status: {{ status }}</div>
            </div>

            <div class="footer-nav">
              {% if prev_doc %}
                <a href="{{ prev_doc.href }}"><span class="label">Previous</span>{{ prev_doc.title }}</a>
              {% else %}
                <span></span>
              {% endif %}
              {% if next_doc %}
                <a href="{{ next_doc.href }}"><span class="label">Next</span>{{ next_doc.title }}</a>
              {% else %}
                <span></span>
              {% endif %}
            </div>
          {% endif %}
        </main>

        <aside class="toc" aria-label="On this page">
          <h3>On this page</h3>
          {% if page_toc and page_toc|length > 0 %}
            {% for h in page_toc %}
              <a class="lvl{{ h.level }}" href="{{ h.href }}">{{ h.text }}</a>
            {% endfor %}
          {% else %}
            <div class="meta">No anchored headings found.</div>
          {% endif %}
        </aside>
      </div>
    </section>
  </div>
</body>
</html>
"""

CUSTOM_CSS_FILENAME = "viewer_theme.css"
CUSTOM_JS_FILENAME = "viewer_theme.js"

DEFAULT_THEME_CSS = r"""
/* Lord of Mysteries–inspired theme (dark brass / parchment) */
/* You can override by creating `viewer_theme.css` next to tag-registry.yml. */

:root{
  --bg: #070606;
  --panel: #0f0b0a;
  --panel2: #120e0c;
  --paper: #0f0d0c;
  --paper2: rgba(255,255,255,0.03);
  --ink: #efe7dc;
  --muted: rgba(239,231,220,0.70);
  --border: rgba(201,162,75,0.22);
  --border2: rgba(255,255,255,0.08);
  --accent: #c9a24b;
  --accent2: #7a1c1c;
  --link: #e3c77d;
  --codebg: rgba(201,162,75,0.08);
  --quote: rgba(201,162,75,0.28);
  --shadow: 0 18px 40px rgba(0,0,0,0.45);
  --radius: 14px;
}

html, body{ height:100%; }
body{
  margin:0;
  background:
    radial-gradient(1200px 800px at 20% 10%, rgba(122,28,28,0.14), transparent 55%),
    radial-gradient(900px 700px at 80% 20%, rgba(201,162,75,0.12), transparent 60%),
    radial-gradient(900px 700px at 30% 90%, rgba(201,162,75,0.08), transparent 60%),
    linear-gradient(180deg, #060404, #070606 45%, #060404);
  color: var(--ink);
  font-family: ui-serif, Georgia, "Times New Roman", Times, serif;
}

a{ color: var(--link); text-decoration: none; }
a:hover{ text-decoration: underline; }

.app{
  display:flex;
  height:100%;
  overflow:hidden;
}

.sidebar{
  width: 340px;
  min-width: 270px;
  max-width: 460px;
  background:
    linear-gradient(180deg, rgba(201,162,75,0.10), transparent 30%),
    repeating-linear-gradient(135deg, rgba(255,255,255,0.02) 0 8px, rgba(0,0,0,0.00) 8px 16px),
    var(--panel);
  border-right: 1px solid var(--border);
  box-shadow: inset -1px 0 0 var(--border2);
  overflow:auto;
}

.content{
  flex:1;
  display:flex;
  flex-direction:column;
  overflow:hidden;
}

.topbar{
  display:flex;
  gap: 10px;
  align-items:center;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  background:
    linear-gradient(180deg, rgba(201,162,75,0.10), rgba(0,0,0,0)),
    rgba(15,11,10,0.75);
  backdrop-filter: blur(8px);
}

.content-body{
  flex:1;
  display:flex;
  overflow:hidden;
}

.main{
  flex:1;
  overflow:auto;
  padding: 24px 28px 88px 28px;
}

.toc{
  width: 300px;
  border-left: 1px solid var(--border);
  background:
    linear-gradient(180deg, rgba(201,162,75,0.08), rgba(0,0,0,0)),
    var(--panel);
  overflow:auto;
  padding: 16px;
  display:none;
}
@media (min-width: 1200px){
  .toc{ display:block; }
}

@media (max-width: 980px){
  .sidebar{
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    transform: translateX(-102%);
    transition: transform 180ms ease;
    z-index: 30;
  }
  body.sidebar-open .sidebar{ transform: translateX(0); }
  body.sidebar-open::before{
    content:"";
    position: fixed;
    inset:0;
    background: rgba(0,0,0,0.55);
    z-index: 25;
  }
}

.search{
  display:flex;
  gap: 10px;
  align-items:center;
  flex:1;
}

input[type="search"]{
  width:100%;
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: rgba(255,255,255,0.03);
  color: var(--ink);
  outline: none;
}
input[type="search"]::placeholder{ color: var(--muted); }

.btn{
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: rgba(255,255,255,0.03);
  color: var(--ink);
  cursor: pointer;
  text-decoration:none;
  font-size: 14px;
  white-space: nowrap;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
}
.btn:hover{ background: rgba(255,255,255,0.06); }
.btn-ghost{ border-color: rgba(255,255,255,0.10); }

.iconbtn{
  width: 38px;
  height: 38px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: rgba(255,255,255,0.03);
  color: var(--ink);
  cursor: pointer;
  font-size: 16px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.iconbtn:hover{ background: rgba(255,255,255,0.06); }

.brand{
  display:flex;
  gap: 12px;
  align-items:center;
  padding: 16px 14px 14px 14px;
  border-bottom: 1px solid var(--border);
}
.sigil{
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background:
    radial-gradient(circle at 30% 30%, rgba(255,255,255,0.10), transparent 55%),
    linear-gradient(180deg, rgba(201,162,75,0.22), rgba(0,0,0,0)),
    rgba(255,255,255,0.03);
  border: 1px solid rgba(201,162,75,0.28);
  box-shadow: 0 8px 18px rgba(0,0,0,0.25);
  display:flex;
  align-items:center;
  justify-content:center;
  color: var(--accent);
  font-size: 16px;
}
.brand .title{
  font-family: ui-serif, Georgia, "Times New Roman", Times, serif;
  font-weight: 800;
  letter-spacing: 0.02em;
  font-size: 14px;
}
.brand .sub{
  margin-top: 4px;
  font-size: 12px;
  color: var(--muted);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}

.nav-wrap{ padding: 10px 10px 40px 10px; }
.nav-header{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap: 8px;
  padding: 8px 8px 6px 8px;
}
.nav-title{
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}

.nav{ font-size: 14px; line-height: 1.25; }

details.nav-dir{ margin: 6px 0; }
summary{
  cursor:pointer;
  user-select:none;
  list-style: none;
  padding: 7px 10px;
  padding-left: calc(10px + var(--indent, 0px));
  border-radius: 12px;
  color: var(--muted);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
summary:hover{ background: rgba(255,255,255,0.04); color: var(--ink); }

summary::-webkit-details-marker{ display:none; }
summary::before{
  content:"▸";
  display:inline-block;
  width: 18px;
  margin-right: 6px;
  color: rgba(201,162,75,0.75);
  transform: translateY(-0.5px);
  transition: transform 120ms ease;
}
details[open] > summary::before{ transform: rotate(90deg) translateY(-0.5px); }

.nav .nav-num{
  display:inline-block;
  min-width: 2.4em;
  text-align:right;
  margin-right: 8px;
  color: rgba(201,162,75,0.86);
  font-variant-numeric: tabular-nums;
  font-weight: 700;
}
.nav .nav-label{
  color: var(--ink);
  opacity: 0.92;
}
.nav .nav-dir-link{
  color: inherit;
  text-decoration: none;
}
.nav .nav-dir-link:hover{ text-decoration: underline; }

.nav a.item{
  display:block;
  padding: 7px 10px;
  padding-left: calc(28px + var(--indent, 0px));
  border-radius: 12px;
  margin: 4px 0;
  color: var(--ink);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.nav a.item:hover{ background: rgba(255,255,255,0.04); }
.nav a.item.active{
  background: rgba(201,162,75,0.12);
  border: 1px solid rgba(201,162,75,0.25);
  box-shadow: 0 0 0 1px rgba(0,0,0,0.15) inset;
}

.md{
  max-width: 980px;
  margin: 0 auto;
  background:
    radial-gradient(900px 600px at 20% 0%, rgba(201,162,75,0.06), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,0.03), rgba(0,0,0,0)),
    rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  box-shadow: var(--shadow);
  padding: 22px 22px 26px 22px;
}

.md h1,.md h2,.md h3,.md h4,.md h5,.md h6{
  margin-top: 1.1em;
  margin-bottom: 0.5em;
  scroll-margin-top: 84px;
  color: var(--ink);
}
.md h1{ font-size: 34px; letter-spacing: 0.01em; }
.md h2{ font-size: 26px; color: rgba(239,231,220,0.96); }
.md h3{ font-size: 20px; color: rgba(239,231,220,0.92); }
.md p{ line-height: 1.7; }
.md a.wikilink{ color: var(--link); border-bottom: 1px dotted rgba(201,162,75,0.5); }
.md a.wikilink:hover{ border-bottom-style: solid; text-decoration:none; }

.md code{
  background: var(--codebg);
  padding: 2px 6px;
  border-radius: 8px;
  border: 1px solid rgba(201,162,75,0.18);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.95em;
}
.md pre code{
  display:block;
  padding: 12px 14px;
  overflow:auto;
  border-radius: 14px;
  border: 1px solid rgba(201,162,75,0.22);
}

.md blockquote{
  margin: 14px 0;
  padding: 10px 14px;
  border-left: 4px solid var(--quote);
  background: rgba(0,0,0,0.18);
  border-radius: 12px;
}

.md table{
  width:100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 0.96em;
}
.md th,.md td{
  border: 1px solid rgba(201,162,75,0.22);
  padding: 8px 10px;
  vertical-align: top;
}
.md th{ background: rgba(201,162,75,0.08); text-align:left; }

.md hr{ border:none; border-top: 1px solid rgba(201,162,75,0.20); margin: 18px 0; }
.md ul,.md ol{ padding-left: 1.3em; }
.md li{ margin: 4px 0; }

.meta{
  max-width: 980px;
  margin: 12px auto 0 auto;
  color: var(--muted);
  font-size: 12px;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.meta code{ font-size: 12px; }

.footer-nav{
  max-width: 980px;
  margin: 26px auto 0 auto;
  display:flex;
  gap: 10px;
  padding-top: 18px;
  border-top: 1px solid rgba(201,162,75,0.18);
}
.footer-nav a{
  flex:1;
  padding: 12px 12px;
  border: 1px solid rgba(201,162,75,0.22);
  border-radius: 14px;
  background: rgba(255,255,255,0.02);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.footer-nav a:hover{ background: rgba(255,255,255,0.05); text-decoration:none; }
.footer-nav .label{
  display:block;
  font-size: 12px;
  color: var(--muted);
  margin-bottom: 6px;
}

.toc h3{
  margin: 6px 0 10px 0;
  font-size: 12px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.toc a{
  display:block;
  padding: 7px 8px;
  border-radius: 12px;
  color: var(--ink);
  font-size: 13px;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.toc a:hover{ background: rgba(255,255,255,0.04); text-decoration:none; }
.toc .lvl2{ margin-left: 10px; }
.toc .lvl3{ margin-left: 20px; }
.toc .lvl4{ margin-left: 30px; }
.toc .lvl5{ margin-left: 40px; }
.toc .lvl6{ margin-left: 50px; }

.unclear{
  display:inline-block;
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid rgba(201,162,75,0.32);
  background: rgba(122,28,28,0.18);
  color: rgba(255,220,140,0.95);
  font-weight: 800;
  font-size: 0.92em;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.linklater{
  display:inline-block;
  padding: 1px 6px;
  border-radius: 999px;
  border: 1px dashed rgba(201,162,75,0.30);
  background: rgba(255,255,255,0.03);
  color: var(--link);
  white-space: nowrap;
}
.linklater:hover{
  background: rgba(255,255,255,0.06);
  text-decoration:none;
}

.ability-card{
  margin: 16px 0;
  padding: 14px 16px;
  border: 1px solid rgba(201,162,75,0.22);
  border-radius: 14px;
  background: rgba(255,255,255,0.02);
  box-shadow: 0 10px 24px rgba(0,0,0,0.35);
}
.ability-head{
  display:flex;
  align-items:flex-start;
  justify-content:space-between;
  gap: 10px;
  flex-wrap: wrap;
}
.ability-name{
  font-size: 20px;
  font-weight: 800;
  letter-spacing: 0.01em;
}
.ability-id{
  margin-top: 4px;
  font-size: 12px;
  color: var(--muted);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
.ability-badges{
  display:flex;
  gap: 6px;
  flex-wrap: wrap;
}
.ability-badge{
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid rgba(201,162,75,0.25);
  background: rgba(255,255,255,0.03);
  color: var(--muted);
  font-size: 12px;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.ability-table{
  width:100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 0.95em;
}
.ability-table th,.ability-table td{
  border: 1px solid rgba(201,162,75,0.20);
  padding: 6px 8px;
  vertical-align: top;
}
.ability-table th{
  width: 140px;
  text-align:left;
  color: var(--muted);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  background: rgba(201,162,75,0.06);
}
.ability-tags{
  display:flex;
  gap: 6px;
  flex-wrap: wrap;
}
.ability-tag{
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid rgba(201,162,75,0.30);
  background: rgba(201,162,75,0.08);
  font-size: 12px;
}
.ability-muted{
  color: var(--muted);
  font-size: 12px;
}
.ability-section{
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid rgba(201,162,75,0.16);
}
.ability-section-title{
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.ability-dice{
  width:100%;
  border-collapse: collapse;
}
.ability-dice th,.ability-dice td{
  border: 1px solid rgba(201,162,75,0.20);
  padding: 6px 8px;
  vertical-align: top;
}
.ability-dice th{
  width: 120px;
  text-align:left;
  color: var(--muted);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  background: rgba(201,162,75,0.06);
}
.ability-list{
  margin: 0;
  padding-left: 1.2em;
}
.ability-k{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
.ability-text p{ margin: 6px 0; }
.ability-raw{
  margin-top: 10px;
}
.ability-raw summary{
  cursor: pointer;
  color: var(--muted);
  font-size: 12px;
}
.ability-raw pre{
  margin-top: 8px;
}

.search-results{
  display:flex;
  flex-direction:column;
  gap: 10px;
  margin-top: 14px;
}
.result{
  border: 1px solid rgba(201,162,75,0.22);
  border-radius: 14px;
  background: rgba(255,255,255,0.02);
  padding: 12px 12px;
}
.result .rtitle{ font-weight: 800; margin-bottom: 6px; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
.result .rsnip{
  color: var(--muted);
  font-size: 13px;
  line-height: 1.6;
  white-space: pre-wrap;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
"""

DEFAULT_VIEWER_JS = r"""
(function(){
  function safeJsonParse(s, fallback){ try{ return JSON.parse(s); }catch(e){ return fallback; } }
  const body = document.body;

  const toggleBtn = document.querySelector('[data-action="toggle-sidebar"]');
  if(toggleBtn){
    toggleBtn.addEventListener('click', function(){ body.classList.toggle('sidebar-open'); });
  }

  document.addEventListener('click', function(e){
    if(!body.classList.contains('sidebar-open')) return;
    const sidebar = document.getElementById('sidebar');
    if(!sidebar) return;
    const inside = sidebar.contains(e.target);
    const isToggle = e.target && e.target.closest && e.target.closest('[data-action="toggle-sidebar"]');
    if(!inside && !isToggle){ body.classList.remove('sidebar-open'); }
  });

  const STORAGE_KEY = 'rv_nav_open';
  const nav = document.getElementById('nav');
  if(nav){
    const details = Array.from(nav.querySelectorAll('details.nav-dir[data-path]'));
    const openSet = new Set(safeJsonParse(localStorage.getItem(STORAGE_KEY), []));
    details.forEach(d => {
      const p = d.getAttribute('data-path') || '';
      if(p && openSet.has(p)) d.open = true;
      d.addEventListener('toggle', () => {
        const path = d.getAttribute('data-path') || '';
        if(!path) return;
        if(d.open) openSet.add(path); else openSet.delete(path);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(openSet)));
      });
    });

    const collapseAll = document.querySelector('[data-action="collapse-all"]');
    if(collapseAll){
      collapseAll.addEventListener('click', () => {
        details.forEach(d => d.open = false);
        localStorage.setItem(STORAGE_KEY, '[]');
      });
    }
  }

  document.addEventListener('keydown', function(e){
    const tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : '';
    const inInput = tag === 'input' || tag === 'textarea' || (e.target && e.target.isContentEditable);

    if((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')){
      e.preventDefault();
      const s = document.querySelector('input[type="search"]');
      if(s) s.focus();
      return;
    }
    if(inInput) return;

    if(e.key === '['){
      const prev = document.querySelector('.footer-nav a:first-child');
      if(prev && prev.getAttribute('href')) window.location.href = prev.getAttribute('href');
    }
    if(e.key === ']'){
      const links = document.querySelectorAll('.footer-nav a');
      const next = links.length > 1 ? links[1] : null;
      if(next && next.getAttribute('href')) window.location.href = next.getAttribute('href');
    }
    if(e.key === 'Escape'){ body.classList.remove('sidebar-open'); }
  });
})();
"""

TOP_LEVEL_ORDER = [
    "front-matter",
    "lore-reference",
    "core-rules",
    "advanced-systems",
    "sequences",
    "supplementary",
]

SECTION_ITEM_ORDER = {
    "front-matter": [
        "preface.md",
        "worldview.md",
    ],
    "lore-reference": [
        "historical-timeline-differences.md",
        "names-and-honorific-titles.md",
        "extra-rank-suppression.md",
    ],
    "core-rules": [
        "checks.md",
        "attributes.md",
        "skills-professions.md",
        "becoming-a-beyonder/",
        "combat/",
        "not-a-beyonder-optional.md",
        "beyonder-items.md",
        "ritual-magic.md",
    ],
    "advanced-systems": [
        "mythical-creature-form.md",
        "special-regions.md",
        "beyonder-creatures/",
        ("gm-guide.md", "bombard-and-killing-beyonders-module.md"),
        "special-potions-talismans-items.md",
        "changing-sequences.md",
    ],
}

SEQUENCE_FILE_RE = re.compile(r"^seq-(\d+)\.md$", re.IGNORECASE)

def _apply_custom_order(base_order: List[str], docs_by_id: Dict[str, Doc], content_prefix: str) -> List[str]:
    order_pos = {doc_id: idx for idx, doc_id in enumerate(base_order)}

    def strip_prefix(rel: str) -> str:
        rel = rel.replace("\\", "/")
        if content_prefix and rel.startswith(content_prefix):
            return rel[len(content_prefix):]
        return rel

    def section_rank(section: str) -> int:
        if section in TOP_LEVEL_ORDER:
            return TOP_LEVEL_ORDER.index(section)
        return len(TOP_LEVEL_ORDER) + 1

    def match_item(order_items, tail: str) -> Optional[int]:
        for i, item in enumerate(order_items):
            options = item if isinstance(item, (list, tuple, set)) else (item,)
            for opt in options:
                if opt.endswith("/"):
                    if tail.startswith(opt):
                        return i
                else:
                    if tail == opt:
                        return i
        return None

    filtered = []
    for doc_id in base_order:
        doc = docs_by_id.get(doc_id)
        if not doc:
            continue
        rel = strip_prefix(doc.relpath)
        if not rel:
            continue
        if rel == "front-matter/table-of-contents.md":
            continue
        if rel == "index.md":
            continue
        filtered.append(doc_id)

    def sort_key(doc_id: str):
        doc = docs_by_id[doc_id]
        rel = strip_prefix(doc.relpath)
        parts = rel.split("/")
        section = parts[0] if len(parts) > 1 else ""
        s_rank = section_rank(section)
        original = order_pos.get(doc_id, 10**9)

        if section == "sequences":
            if len(parts) >= 3:
                pathway = parts[1]
                filename = parts[-1]
            elif len(parts) == 2:
                pathway = ""
                filename = parts[1]
            else:
                pathway = ""
                filename = parts[0]
            seq_rank = 999
            m = SEQUENCE_FILE_RE.match(filename)
            if m:
                seq_rank = -int(m.group(1))
            index_bias = -1 if filename.lower() == "index.md" else 0
            return (s_rank, pathway, seq_rank, index_bias, filename, original)

        tail = "/".join(parts[1:]) if section else rel
        item_rank = 999
        if section in SECTION_ITEM_ORDER:
            matched = match_item(SECTION_ITEM_ORDER[section], tail)
            if matched is not None:
                item_rank = matched
        index_bias = -1 if Path(tail).name.lower() == "index.md" else 0
        return (s_rank, item_rank, index_bias, tail, original)

    return sorted(filtered, key=sort_key)

def _build_nav_html(index: Index, active_doc_id: Optional[str]) -> str:
    """
    Build a collapsible tree based on relpaths.

    Improvements:
    - Mixed ordering: folders and files appear in the same sequence as `index.order`
      (so "07-*.md" can appear before "08-*/" if the registry says so).
    - Visible hierarchy: indentation makes expansions obvious.
    - Folder labels are prettified (numeric prefixes become a small badge + title-cased label).
    """
    # If everything is under a single content root, hide it in the sidebar.
    strip_prefix = index.content_prefix or ""

    dir_title_map: Dict[str, str] = {}
    dir_index_doc: Dict[str, str] = {}
    for doc in index.docs_by_id.values():
        rel = doc.relpath.replace("\\", "/")
        if strip_prefix and rel.startswith(strip_prefix):
            rel = rel[len(strip_prefix):]
        if _is_index_relpath(rel) and "/" in rel:
            dir_path = rel.rsplit("/", 1)[0]
            dir_index_doc[dir_path] = doc.doc_id
            title = _display_title_for_doc(doc)
            dir_title_map[dir_path] = title or _clean_label(dir_path.split("/")[-1])

    # Tree node: {"__items__": [("dir", name), ("file", doc_id), ...], "__dirs__": {name: node}}
    tree = {"__items__": [], "__dirs__": {}}

    def ensure_dir(parent: dict, name: str) -> dict:
        dirs = parent["__dirs__"]
        if name not in dirs:
            dirs[name] = {"__items__": [], "__dirs__": {}}
            parent["__items__"].append(("dir", name))
        return dirs[name]

    for doc_id in index.order:
        doc = index.docs_by_id.get(doc_id)
        if not doc:
            continue
        rel = doc.relpath.replace("\\", "/")
        if strip_prefix and rel.startswith(strip_prefix):
            rel = rel[len(strip_prefix):]
        if _is_index_relpath(rel) and "/" in rel:
            # Use index.md as the folder label/link instead of a duplicate file entry.
            continue
        parts = [p for p in rel.split("/") if p]
        if not parts:
            continue

        node = tree
        for part in parts[:-1]:
            node = ensure_dir(node, part)
        node["__items__"].append(("file", doc_id))

    active_rel = None
    if active_doc_id and active_doc_id in index.docs_by_id:
        active_rel = index.docs_by_id[active_doc_id].relpath.replace("\\", "/")
        if strip_prefix and active_rel.startswith(strip_prefix):
            active_rel = active_rel[len(strip_prefix):]

    def render_node(node: dict, depth: int, path_prefix: str) -> str:
        out: List[str] = []
        indent_px = depth * 14

        for kind, value in node.get("__items__", []):
            if kind == "dir":
                name = value
                child = node["__dirs__"][name]
                path = (path_prefix + name).strip("/")
                open_attr = ""
                if active_rel and (active_rel == path or active_rel.startswith(path + "/")):
                    open_attr = " open"

                label = dir_title_map.get(path)
                if not label or label.strip().lower() == "index":
                    label = _clean_label(name)
                out.append(f'<details class="nav-dir"{open_attr} data-path="{html.escape(path, quote=True)}">')
                link_doc_id = dir_index_doc.get(path)
                if link_doc_id:
                    href = url_for("doc", doc_id=link_doc_id)
                    out.append(
                        f'<summary style="--indent:{indent_px}px">'
                        f'<a class="nav-dir-link" href="{href}"><span class="nav-label">{html.escape(label)}</span></a>'
                        f'</summary>'
                    )
                else:
                    out.append(f'<summary style="--indent:{indent_px}px"><span class="nav-label">{html.escape(label)}</span></summary>')
                out.append(render_node(child, depth + 1, path_prefix + name + "/"))
                out.append("</details>")
            else:
                did = value
                d = index.docs_by_id[did]
                href = url_for("doc", doc_id=did)
                cls = "item" + (" active" if did == active_doc_id else "")
                out.append(f'<a class="{cls}" style="--indent:{indent_px}px" href="{href}">{html.escape(_display_title_for_doc(d))}</a>')

        return "\n".join(out)

    return render_node(tree, depth=0, path_prefix="")


def _neighbor_docs(index: Index, doc_id: str) -> Tuple[Optional[Dict], Optional[Dict]]:
    try:
        i = index.order.index(doc_id)
    except ValueError:
        return None, None
    prev_id = index.order[i-1] if i > 0 else None
    next_id = index.order[i+1] if i < len(index.order)-1 else None
    prev_doc = None
    next_doc = None
    if prev_id and prev_id in index.docs_by_id:
        d = index.docs_by_id[prev_id]
        prev_doc = {"href": url_for('doc', doc_id=prev_id), "title": _display_title_for_doc(d)}
    if next_id and next_id in index.docs_by_id:
        d = index.docs_by_id[next_id]
        next_doc = {"href": url_for('doc', doc_id=next_id), "title": _display_title_for_doc(d)}
    return prev_doc, next_doc

def _render_doc_html(index: Index, doc: Doc) -> str:
    if not doc.abspath:
        # planned/missing
        missing = f"**Missing file**\n\nThis entry is listed in `tag-registry.yml` but the file does not exist:\n\n- `{doc.relpath}`\n"
        body = _preprocess_markdown(missing)
        return MD(body)

    raw = Path(doc.abspath).read_text(encoding="utf-8", errors="replace")
    fm, body = _strip_front_matter(raw)
    body = _preprocess_markdown(body)
    return MD(body)

def _page_toc(index: Index, doc_id: str) -> List[Dict]:
    toc = index.toc_by_doc.get(doc_id) or []
    out = []
    for level, text_, anchor in toc:
        out.append({
            "level": level,
            "text": text_,
            "href": url_for('doc', doc_id=doc_id) + "#" + urllib.parse.quote(anchor),
        })
    return out

# ----------------------------
# App
# ----------------------------

app = Flask(__name__)
GLOBAL_INDEX: Optional[Index] = None

def _asset_version(index: Index, filename: str) -> int:
    p = index.repo_root / filename
    if p.exists():
        try:
            return int(p.stat().st_mtime)
        except Exception:
            return 1
    return 1

@app.route("/assets/viewer.css")
def viewer_css():
    if GLOBAL_INDEX:
        p = GLOBAL_INDEX.repo_root / CUSTOM_CSS_FILENAME
        if p.exists():
            return Response(p.read_text(encoding="utf-8", errors="replace"), mimetype="text/css")
    return Response(DEFAULT_THEME_CSS, mimetype="text/css")

@app.route("/assets/viewer.js")
def viewer_js():
    custom_js = ""
    if GLOBAL_INDEX:
        p = GLOBAL_INDEX.repo_root / CUSTOM_JS_FILENAME
        if p.exists():
            custom_js = p.read_text(encoding="utf-8", errors="replace")
    if custom_js:
        # Keep default viewer behavior, then apply optional custom script.
        return Response(DEFAULT_VIEWER_JS + "\n\n" + custom_js, mimetype="text/javascript")
    return Response(DEFAULT_VIEWER_JS, mimetype="text/javascript")

@app.route("/assets/compendium.json")
def compendium_json():
    if not GLOBAL_INDEX:
        abort(500)
    p = GLOBAL_INDEX.repo_root / "dist" / "compendium.json"
    if not p.exists():
        abort(404)
    try:
        payload = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        abort(500)
    return Response(json.dumps(payload), mimetype="application/json")


def _default_doc_id(index: Index) -> str:
    # Prefer table of contents, then index.md, else first in order.
    if "table-of-contents" in index.order:
        return "table-of-contents"
    # try any doc whose relpath matches the content root index.md
    for did in index.order:
        d = index.docs_by_id.get(did)
        if not d:
            continue
        rel = d.relpath.replace("\\", "/")
        if index.content_prefix:
            if rel == f"{index.content_prefix}index.md":
                return did
        else:
            if rel == "index.md":
                return did
    return index.order[0] if index.order else next(iter(index.docs_by_id.keys()))

@app.route("/")
def home():
    if not GLOBAL_INDEX:
        abort(500)
    did = _default_doc_id(GLOBAL_INDEX)
    return redirect(url_for("doc", doc_id=did))

@app.route("/doc/<doc_id>")
def doc(doc_id: str):
    if not GLOBAL_INDEX:
        abort(500)
    index = GLOBAL_INDEX
    if doc_id not in index.docs_by_id:
        abort(404)

    d = index.docs_by_id[doc_id]
    content_html = _render_doc_html(index, d)
    nav_html = _build_nav_html(index, active_doc_id=doc_id)
    prev_doc, next_doc = _neighbor_docs(index, doc_id)

    return render_template_string(
        BASE_TEMPLATE,
        css_version=_asset_version(index, CUSTOM_CSS_FILENAME),
        js_version=_asset_version(index, CUSTOM_JS_FILENAME),
        page_title=f"{d.title} — Rulebook Viewer",
        nav_html=nav_html,
        content_html=content_html,
        relpath=d.relpath,
        tags=d.tags,
        status=d.status,
        prev_doc=prev_doc,
        next_doc=next_doc,
        is_search=False,
        query="",
        results=[],
        page_toc=_page_toc(index, doc_id),
    )

@app.route("/w/<target>")
def wikilink(target: str):
    """
    Resolve [[Exact Section Title]] by:
    1) exact heading match -> doc + #anchor
    2) case-insensitive heading match
    3) exact doc title match -> doc
    4) fallback to search
    """
    if not GLOBAL_INDEX:
        abort(500)
    index = GLOBAL_INDEX
    t = urllib.parse.unquote(target)

    if t.startswith("id:") or t.startswith("#"):
        aid = t[3:].strip() if t.startswith("id:") else t[1:].strip()
        did = index.anchor_to_doc.get(aid)
        if did:
            return redirect(url_for("doc", doc_id=did) + "#" + urllib.parse.quote(aid))


    # 1-2) Heading match
    if t in index.heading_index:
        did, aid = index.heading_index[t]
        return redirect(url_for("doc", doc_id=did) + "#" + urllib.parse.quote(aid))
    low = t.lower()
    if low in index.heading_index:
        did, aid = index.heading_index[low]
        return redirect(url_for("doc", doc_id=did) + "#" + urllib.parse.quote(aid))

    # 3) Doc title match
    for did in index.order:
        d = index.docs_by_id.get(did)
        if d and d.title == t:
            return redirect(url_for("doc", doc_id=did))
        if d and d.title.lower() == low:
            return redirect(url_for("doc", doc_id=did))

    # 4) fallback to search
    return redirect(url_for("search", q=t))

@app.route("/search")
def search():
    if not GLOBAL_INDEX:
        abort(500)
    index = GLOBAL_INDEX
    q = (request.args.get("q") or "").strip()
    nav_html = _build_nav_html(index, active_doc_id=None)

    results = []
    if q:
        qlow = q.lower()
        for did in index.order:
            d = index.docs_by_id.get(did)
            if not d:
                continue
            if not d.abspath:
                hay = ""
            else:
                hay = Path(d.abspath).read_text(encoding="utf-8", errors="replace")
            if qlow in hay.lower():
                snippet = _make_snippet(hay, q, radius=220)
                results.append({
                    "href": url_for("doc", doc_id=did) + _best_anchor_for_query(index, did, hay, q),
                    "title": d.title,
                    "relpath": d.relpath,
                    "snippet": snippet,
                })
                if len(results) >= 60:
                    break

    return render_template_string(
        BASE_TEMPLATE,
        css_version=_asset_version(index, CUSTOM_CSS_FILENAME),
        js_version=_asset_version(index, CUSTOM_JS_FILENAME),
        page_title="Search — Rulebook Viewer",
        nav_html=nav_html,
        content_html="",
        relpath="",
        tags=[],
        status="",
        prev_doc=None,
        next_doc=None,
        is_search=True,
        query=q,
        results=results,
        page_toc=[],
    )

@app.route("/reload")
def reload_index():
    """
    Re-scan files on disk and rebuild the index.
    """
    global GLOBAL_INDEX
    if not GLOBAL_INDEX:
        abort(500)
    source_root = GLOBAL_INDEX.repo_root
    GLOBAL_INDEX = build_index(source_root, content_root=GLOBAL_INDEX.content_root)
    return redirect(url_for("home"))

def _make_snippet(text: str, q: str, radius: int = 180) -> str:
    if not text:
        return ""
    qlow = q.lower()
    low = text.lower()
    i = low.find(qlow)
    if i == -1:
        return textwrap.shorten(text.replace("\r", "").replace("\n", " "), width=2*radius, placeholder="…")
    start = max(0, i - radius)
    end = min(len(text), i + len(q) + radius)
    snip = text[start:end].replace("\r", "")
    snip = re.sub(r'\n{3,}', '\n\n', snip)
    # lightly mark matches
    snip = re.sub(re.escape(q), lambda m: f"[{m.group(0)}]", snip, flags=re.IGNORECASE)
    if start > 0:
        snip = "…" + snip
    if end < len(text):
        snip = snip + "…"
    return snip.strip()

def _best_anchor_for_query(index: Index, doc_id: str, raw: str, q: str) -> str:
    """
    Best-effort: if a heading contains the query, link to that heading's anchor.
    """
    qlow = q.lower()
    toc = index.toc_by_doc.get(doc_id) or []
    for _, htxt, aid in toc:
        if qlow in htxt.lower():
            return "#" + urllib.parse.quote(aid)
    return ""

# ----------------------------
# Source handling (dir or zip)
# ----------------------------

def _prepare_source(source: Path) -> Tuple[Path, Optional[str]]:
    """
    Returns (source_root_dir, temp_dir_used_or_none).
    If source is a zip, extracts to a temp directory and returns extracted root.
    """
    if source.is_file() and source.suffix.lower() == ".zip":
        tmp = tempfile.mkdtemp(prefix="rulebook_viewer_")
        with zipfile.ZipFile(source, "r") as z:
            z.extractall(tmp)
        # Prefer a single top-level folder inside the zip
        root = Path(tmp)
        children = [p for p in root.iterdir() if p.is_dir()]
        if len(children) == 1:
            return children[0], tmp
        return root, tmp
    return source, None

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only rulebook markdown viewer (single-file).")
    parser.add_argument("--source", type=str, default=".", help="Repo directory or a .zip containing the markdown files.")
    parser.add_argument(
        "--content-root",
        type=str,
        default=DEFAULT_CONTENT_ROOT,
        choices=list(VALID_CONTENT_ROOTS),
        help="Content folder to read from (default: draft; falls back to build if missing).",
    )
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to bind (default: 127.0.0.1).")
    parser.add_argument("--port", type=int, default=7860, help="Port to use (default: 7860).")
    parser.add_argument("--no-browser", action="store_true", help="Do not open a browser tab automatically.")
    args = parser.parse_args(argv)

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        print(f"[error] source not found: {source}", file=sys.stderr)
        return 2

    source_root, tmpdir = _prepare_source(source)

    global GLOBAL_INDEX
    GLOBAL_INDEX = build_index(source_root, content_root=args.content_root)

    if not GLOBAL_INDEX.order and not GLOBAL_INDEX.docs_by_id:
        print("[error] no markdown files found.", file=sys.stderr)
        return 3

    url = f"http://{args.host}:{args.port}/"
    if not args.no_browser:
        try:
            webbrowser.open(url, new=1)
        except Exception:
            pass

    # Flask dev server is fine for local MVP.
    # Use threaded to keep UI responsive.
    try:
        app.run(host=args.host, port=args.port, debug=False, threaded=True)
    finally:
        # If we extracted from zip, we leave temp dir on disk so links keep working.
        # It's in your system temp folder; safe to delete after you stop the server.
        if tmpdir:
            print(f"[info] extracted zip to: {tmpdir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

