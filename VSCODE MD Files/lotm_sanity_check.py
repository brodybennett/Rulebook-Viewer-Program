#!/usr/bin/env python3
"""
lotm_sanity_check.py
Read-only sanity checker + optional clickthrough UI for this Markdown rulebook repo.

CLI mode (default):
- prints issues (ERROR/WARN/INFO) and exits with code 0/1

UI mode:
- python lotm_sanity_check.py --serve
- opens http://127.0.0.1:<port>/ with a clickable report (files, lines, anchors)

No files are modified unless you pass --json to write a report.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import os
import re
import socketserver
import sys
import urllib.parse
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

try:
    import yaml  # PyYAML
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise

HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*\{#([A-Za-z0-9][A-Za-z0-9\-_]*)\}\s*$')
WIKILINK_RE = re.compile(r'\[\[([^\]]+?)\]\]')
FENCE_RE = re.compile(r'^\s*```')

FLAG_PREFIXES = ("UNCLEAR:", "TODO:", "NOTE:")

@dataclass
class Issue:
    level: str  # "ERROR" | "WARN" | "INFO"
    msg: str
    file: Optional[str] = None
    line: Optional[int] = None

    def to_dict(self) -> dict:
        return {"level": self.level, "msg": self.msg, "file": self.file, "line": self.line}

def rel(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except Exception:
        return str(p).replace("\\", "/")

def safe_resolve_under_root(root: Path, user_path: str) -> Optional[Path]:
    try:
        p = (root / user_path).resolve()
        root_res = root.resolve()
        # Ensure p is within root
        if str(p).startswith(str(root_res) + os.sep) or p == root_res:
            return p
        return None
    except Exception:
        return None

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""

def parse_front_matter(text: str) -> Tuple[Optional[dict], str]:
    lines = text.splitlines()
    if not lines:
        return None, text
    if lines[0].strip() != "---":
        return None, text
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            raw = "\n".join(lines[1:idx])
            body = "\n".join(lines[idx + 1 :])
            try:
                data = yaml.safe_load(raw) or {}
            except Exception as e:
                data = {"__parse_error__": str(e)}
            return data, body
    return {"__parse_error__": "missing closing ---"}, text

def strip_front_matter_and_code(text: str) -> str:
    _, body = parse_front_matter(text)
    lines = body.splitlines()
    out: List[str] = []
    in_code = False
    for line in lines:
        if FENCE_RE.match(line):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    return "\n".join(out)

def iter_md_files(build_dir: Path) -> Iterable[Path]:
    if not build_dir.exists():
        return []
    return build_dir.rglob("*.md")

def get_headings(text: str) -> List[Tuple[int, str, str, int]]:
    heads: List[Tuple[int, str, str, int]] = []
    for i, line in enumerate(text.splitlines(), start=1):
        m = HEADING_RE.match(line.strip())
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            hid = m.group(3)
            heads.append((level, title, hid, i))
    return heads

def get_wikilinks(text: str) -> List[Tuple[str, int]]:
    links: List[Tuple[str, int]] = []
    for i, line in enumerate(text.splitlines(), start=1):
        for m in WIKILINK_RE.finditer(line):
            links.append((m.group(1).strip(), i))
    return links

def best_path_suggestion(missing_path: str, root: Path, build_dir: Path) -> Optional[str]:
    candidates = [rel(p, root) for p in iter_md_files(build_dir)]
    if not candidates:
        return None
    match = difflib.get_close_matches(missing_path, candidates, n=1, cutoff=0.55)
    return match[0] if match else None

def compute_report(
    *,
    root: Path,
    build_dir: Path,
    registry_path: Path,
    glossary_path: Path,
    placeholder_level: str,
) -> dict:
    issues: List[Issue] = []
    data: dict = {
        "root": str(root),
        "build_dir": rel(build_dir, root),
        "registry": rel(registry_path, root),
        "glossary": rel(glossary_path, root),
        "issues": [],
        "counts": {"ERROR": 0, "WARN": 0, "INFO": 0},
        "registry_files": [],
        "registry_anchors": [],
        "md_files": [],
    }

    # --- Load registry ---
    if not registry_path.exists():
        issues.append(Issue("ERROR", f"Missing registry file: {rel(registry_path, root)}"))
        return finalize_report(data, issues)

    try:
        reg = yaml.safe_load(read_text(registry_path)) or {}
    except Exception as e:
        issues.append(Issue("ERROR", f"Failed to parse registry YAML: {e}", file=rel(registry_path, root)))
        return finalize_report(data, issues)

    reg_files = reg.get("files", []) or []
    reg_anchors = reg.get("anchors", {}) or {}

    # Surface registry entries (for the UI explorer)
    for entry in reg_files:
        data["registry_files"].append({
            "path": entry.get("path"),
            "title": entry.get("title"),
            "id": entry.get("id"),
            "tags": entry.get("tags") or [],
            "status": entry.get("status"),
        })

    for aid, meta in reg_anchors.items():
        if not isinstance(meta, dict):
            continue
        data["registry_anchors"].append({
            "anchor": aid,
            "title": meta.get("title"),
            "file": meta.get("file"),
            "aliases": meta.get("aliases") or [],
            "status": meta.get("status"),
        })

    # Validate uniqueness of file paths and IDs in registry
    seen_paths: Dict[str, int] = {}
    seen_ids: Dict[str, int] = {}
    for idx, entry in enumerate(reg_files):
        p = entry.get("path")
        fid = entry.get("id")
        if not p or not fid:
            issues.append(Issue("ERROR", "Registry file entry missing 'path' or 'id'.", file=rel(registry_path, root)))
            continue
        if p in seen_paths:
            issues.append(Issue("ERROR", f"Duplicate registry path: {p}", file=rel(registry_path, root)))
        else:
            seen_paths[p] = idx
        if fid in seen_ids:
            issues.append(Issue("ERROR", f"Duplicate registry id: {fid}", file=rel(registry_path, root)))
        else:
            seen_ids[fid] = idx

    # Check status: exists => file must exist
    for entry in reg_files:
        p = entry.get("path")
        status = (entry.get("status") or "").strip()
        if not p:
            continue
        disk_path = root / p
        if status == "exists" and not disk_path.exists():
            sug = best_path_suggestion(p, root, build_dir)
            msg = f"Registry says status: exists but file is missing: {p}"
            if sug:
                msg += f" (did you mean {sug}?)"
            issues.append(Issue("ERROR", msg, file=rel(registry_path, root)))

    # Detect build files missing from registry
    build_paths = [rel(p, root) for p in iter_md_files(build_dir)]
    data["md_files"] = build_paths
    missing_from_registry = sorted([p for p in build_paths if p not in seen_paths])
    if missing_from_registry:
        examples = ", ".join(missing_from_registry[:8])
        suffix = "" if len(missing_from_registry) <= 8 else f" … (+{len(missing_from_registry)-8} more)"
        issues.append(Issue("WARN", f"{len(missing_from_registry)} build file(s) are not listed in tag-registry.yml: {examples}{suffix}"))

    # --- Load glossary ---
    alias_terms: Dict[str, str] = {}
    if glossary_path.exists():
        try:
            g = yaml.safe_load(read_text(glossary_path)) or {}
            terms = g.get("terms", {}) or {}
            for k, v in terms.items():
                if isinstance(v, dict) and "canonical" in v:
                    alias_terms[str(k)] = str(v["canonical"])
                else:
                    alias_terms[str(k)] = str(v)
        except Exception as e:
            issues.append(Issue("WARN", f"Failed to parse glossary YAML: {e}", file=rel(glossary_path, root)))
    else:
        issues.append(Issue("INFO", f"No glossary file found at {rel(glossary_path, root)}; skipping glossary checks."))

    noncanonical_aliases = [a for a, c in alias_terms.items() if a != c]

    # --- Index registry titles/aliases for wikilink resolution ---
    known_link_targets: Dict[str, List[str]] = {}  # target_title -> [where]
    for entry in reg_files:
        title = (entry.get("title") or "").strip()
        p = (entry.get("path") or "").strip()
        if title:
            known_link_targets.setdefault(title, []).append(p)

    for aid, meta in reg_anchors.items():
        if not isinstance(meta, dict):
            continue
        title = (meta.get("title") or "").strip()
        if title:
            known_link_targets.setdefault(title, []).append(meta.get("file") or "(anchor)")
        for al in (meta.get("aliases") or []) or []:
            al = str(al).strip()
            if al:
                known_link_targets.setdefault(al, []).append(meta.get("file") or "(anchor)")

    # --- Scan markdown files ---
    md_headings: Dict[str, List[Tuple[str, int, str]]] = {}  # anchor -> [(file,line,title)]
    for p in iter_md_files(build_dir):
        r = rel(p, root)
        txt = read_text(p)

        # Headings
        heads = get_headings(txt)
        for level, title, hid, line in heads:
            md_headings.setdefault(hid, []).append((r, line, title))

        # Glossary alias misuse (ignore YAML front matter + fenced code)
        if noncanonical_aliases:
            clean = strip_front_matter_and_code(txt)
            for alias in noncanonical_aliases:
                if re.search(rf'(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])', clean):
                    issues.append(Issue("WARN", f"Found non-canonical glossary alias '{alias}' (use '{alias_terms[alias]}')", file=r))

        # Wikilinks
        for target, line in get_wikilinks(txt):
            if any(target.startswith(prefix) for prefix in FLAG_PREFIXES):
                continue
            # Drafting marker: [[LINK LATER: ... ]] is intentionally unresolved until a later pass
            if target.lower().startswith("link later:"):
                continue
            if target.startswith("id:") or target.startswith("#"):
                aid = target[3:].strip() if target.startswith("id:") else target[1:].strip()
                if aid and aid not in reg_anchors:
                    issues.append(Issue("WARN", f"Unresolved id-link [[{target}]] (anchor id not in registry)", file=r, line=line))
                continue

            if target not in known_link_targets:
                issues.append(Issue("WARN", f"Unresolved wiki-link [[{target}]] (not found in registry titles/anchor aliases)", file=r, line=line))

    # --- Anchor registry vs Markdown ---
    # 1) any Markdown anchor missing from registry anchors => warn
    for aid, locs in md_headings.items():
        if aid not in reg_anchors:
            sample = locs[0]
            issues.append(Issue("WARN", f"Anchor '{aid}' exists in Markdown but is missing from registry anchors.", file=sample[0], line=sample[1]))

    # 2) any registry anchor with status: exists should be present in its file
    for aid, meta in reg_anchors.items():
        if not isinstance(meta, dict):
            continue
        status = (meta.get("status") or "").strip()
        fpath = meta.get("file")
        if not fpath:
            continue
        disk = root / fpath
        if status == "exists" and not disk.exists():
            issues.append(Issue("ERROR", f"Registry anchor '{aid}' points to missing file: {fpath}", file=rel(registry_path, root)))
            continue
        if disk.exists():
            txt = read_text(disk)
            if not txt.strip():
                if status == "exists":
                    lvl = placeholder_level.upper()
                    if lvl != "IGNORE":
                        issues.append(Issue(lvl, f"Registry anchor '{aid}' is status: exists but file is empty (placeholder?).", file=fpath))
                continue
            if aid not in md_headings:
                issues.append(Issue("WARN", f"Registry anchor '{aid}' not found in Markdown scan.", file=fpath))

    return finalize_report(data, issues)

def finalize_report(data: dict, issues: List[Issue]) -> dict:
    data["issues"] = [i.to_dict() for i in issues]
    for i in issues:
        data["counts"][i.level] = data["counts"].get(i.level, 0) + 1
    return data

def print_issues(report: dict) -> int:
    issues = report.get("issues", [])
    # stable ordering
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    issues_sorted = sorted(issues, key=lambda x: (order.get(x["level"], 9), x.get("file") or "", x.get("line") or 0, x.get("msg") or ""))

    for it in issues_sorted:
        loc = ""
        if it.get("file"):
            loc += it["file"]
            if it.get("line"):
                loc += f":{it['line']}"
            loc += ": "
        print(f"{it['level']}: {loc}{it['msg']}")

    print("")
    c = report.get("counts", {})
    print(f"Summary: {c.get('ERROR',0)} error(s), {c.get('WARN',0)} warning(s), {c.get('INFO',0)} info")
    return 1 if c.get("ERROR", 0) else 0

def write_json(report: dict, out_path: str) -> None:
    Path(out_path).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote JSON report to: {out_path}")

# --------------------------
# Minimal clickthrough server
# --------------------------
CSS = """
:root { --bg:#0b0f14; --fg:#e6edf3; --muted:#9aa4af; --card:#111822; --line:#223043; --err:#ff6b6b; --warn:#ffd166; --info:#7bdff2; --link:#9ad1ff; }
* { box-sizing:border-box; }
body { margin:0; font:14px/1.45 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial; background:var(--bg); color:var(--fg); }
a { color:var(--link); text-decoration:none; }
a:hover { text-decoration:underline; }
header { padding:16px 18px; border-bottom:1px solid var(--line); background:linear-gradient(180deg, #0f1520, #0b0f14); position:sticky; top:0; z-index:10;}
h1 { margin:0 0 6px 0; font-size:18px; }
.small { color:var(--muted); font-size:12px; }
main { padding:18px; max-width:1200px; margin:0 auto; }
.grid { display:grid; gap:12px; grid-template-columns: 1fr; }
@media (min-width: 980px) { .grid { grid-template-columns: 2fr 1fr; } }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px; }
.pills { display:flex; gap:8px; flex-wrap:wrap; }
.pill { padding:4px 8px; border-radius:999px; border:1px solid var(--line); color:var(--muted); font-size:12px;}
.pill.err { border-color: color-mix(in srgb, var(--err) 50%, var(--line)); color:var(--err); }
.pill.warn { border-color: color-mix(in srgb, var(--warn) 50%, var(--line)); color:var(--warn); }
.pill.info { border-color: color-mix(in srgb, var(--info) 50%, var(--line)); color:var(--info); }
.controls { display:flex; gap:10px; flex-wrap:wrap; margin-top:10px; }
input[type="text"] { background:#0b1220; border:1px solid var(--line); color:var(--fg); padding:8px 10px; border-radius:10px; width:min(520px, 100%); }
select { background:#0b1220; border:1px solid var(--line); color:var(--fg); padding:8px 10px; border-radius:10px; }
table { width:100%; border-collapse:separate; border-spacing:0; }
th, td { text-align:left; padding:10px 10px; border-bottom:1px solid var(--line); vertical-align:top; }
th { color:var(--muted); font-weight:600; font-size:12px; }
tr:hover td { background: rgba(255,255,255,0.03); }
.badge { font-weight:700; }
.badge.ERROR{ color:var(--err); }
.badge.WARN{ color:var(--warn); }
.badge.INFO{ color:var(--info); }
code { background:#0b1220; border:1px solid var(--line); padding:2px 6px; border-radius:8px; }
pre { margin:0; padding:12px; background:#0b1220; border:1px solid var(--line); border-radius:12px; overflow:auto; }
.ln { display:block; }
.ln::before { content: attr(data-n); display:inline-block; width:56px; color:var(--muted); }
.hl { background: rgba(255, 209, 102, 0.12); outline: 1px solid rgba(255, 209, 102, 0.18); border-radius:4px; }
.topnav { display:flex; gap:10px; flex-wrap:wrap; margin-top:8px; }
"""

def page(title: str, body: str) -> bytes:
    doc = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head><body>
<header>
  <h1>{html.escape(title)}</h1>
  <div class="small">Read-only local dashboard • No files are modified</div>
  <div class="topnav">
    <a href="/">Issues</a>
    <a href="/registry">Registry</a>
    <a href="/files">Files</a>
  </div>
</header>
<main>{body}</main>
</body></html>"""
    return doc.encode("utf-8")

def urlq(params: dict) -> str:
    return urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}, doseq=True)

def issue_rows(report: dict, level: str, q: str) -> List[dict]:
    items = report.get("issues", [])
    if level and level != "ALL":
        items = [i for i in items if i.get("level") == level]
    if q:
        ql = q.lower()
        def hit(i: dict) -> bool:
            return (i.get("msg","").lower().find(ql) >= 0) or (i.get("file","").lower().find(ql) >= 0)
        items = [i for i in items if hit(i)]
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    items = sorted(items, key=lambda x: (order.get(x.get("level",""), 9), x.get("file") or "", x.get("line") or 0))
    return items

def render_issues(report: dict, level: str, q: str) -> str:
    c = report.get("counts", {})
    pills = f"""
    <div class="pills">
      <span class="pill err">ERROR {c.get('ERROR',0)}</span>
      <span class="pill warn">WARN {c.get('WARN',0)}</span>
      <span class="pill info">INFO {c.get('INFO',0)}</span>
    </div>"""

    controls = f"""
    <form class="controls" method="get" action="/">
      <select name="level">
        <option value="ALL" {"selected" if level=="ALL" else ""}>All</option>
        <option value="ERROR" {"selected" if level=="ERROR" else ""}>ERROR</option>
        <option value="WARN" {"selected" if level=="WARN" else ""}>WARN</option>
        <option value="INFO" {"selected" if level=="INFO" else ""}>INFO</option>
      </select>
      <input type="text" name="q" value="{html.escape(q)}" placeholder="Search (file path / message)"/>
      <button type="submit">Filter</button>
    </form>"""

    rows = issue_rows(report, level, q)

    tr = []
    for i, it in enumerate(rows):
        lvl = it.get("level","")
        f = it.get("file") or ""
        line = it.get("line")
        msg = it.get("msg","")
        file_link = ""
        if f:
            params = {"file": f, "line": line or ""}
            file_link = f'<a href="/view?{urlq(params)}">{html.escape(f)}</a>'
            if line:
                file_link += f':{int(line)}'
        else:
            file_link = "<span class='small'>(no file)</span>"

        tr.append(f"""
        <tr>
          <td class="badge {lvl}">{lvl}</td>
          <td>{file_link}</td>
          <td>{html.escape(msg)}</td>
        </tr>""")

    table = f"""
    <div class="card">
      <h2 style="margin:0 0 8px 0; font-size:16px;">Issues</h2>
      {controls}
      <div style="margin-top:12px;"></div>
      <table>
        <thead><tr><th>Level</th><th>Location</th><th>Message</th></tr></thead>
        <tbody>{''.join(tr) if tr else '<tr><td colspan="3" class="small">No issues match your filter.</td></tr>'}</tbody>
      </table>
    </div>"""

    right = f"""
    <div class="card">
      <h2 style="margin:0 0 8px 0; font-size:16px;">Repo</h2>
      {pills}
      <div style="margin-top:10px;" class="small">
        <div><b>Build:</b> <code>{html.escape(report.get('build_dir','build'))}</code></div>
        <div><b>Registry:</b> <code>{html.escape(report.get('registry','tag-registry.yml'))}</code></div>
        <div><b>Glossary:</b> <code>{html.escape(report.get('glossary','glossary.yml'))}</code></div>
      </div>
      <div style="margin-top:12px;" class="small">
        Tips:<br/>
        • Click a file path to open it at the relevant line.<br/>
        • Use “Registry” to browse anchors/files quickly.
      </div>
    </div>"""

    return f'<div class="grid">{table}{right}</div>'

def render_registry(report: dict) -> str:
    files = report.get("registry_files", [])
    anchors = report.get("registry_anchors", [])

    file_rows = []
    for it in files:
        p = it.get("path") or ""
        title = it.get("title") or ""
        status = it.get("status") or ""
        fid = it.get("id") or ""
        tags = ", ".join(it.get("tags") or [])
        link = f'<a href="/view?{urlq({"file": p})}">{html.escape(p)}</a>' if p else ""
        file_rows.append(f"""
        <tr>
          <td>{link}</td>
          <td>{html.escape(title)}</td>
          <td><code>{html.escape(fid)}</code></td>
          <td>{html.escape(status)}</td>
          <td class="small">{html.escape(tags)}</td>
        </tr>""")

    anchor_rows = []
    for it in anchors:
        a = it.get("anchor") or ""
        title = it.get("title") or ""
        f = it.get("file") or ""
        status = it.get("status") or ""
        aliases = ", ".join(it.get("aliases") or [])
        link = f'<a href="/view?{urlq({"file": f})}">{html.escape(f)}</a>' if f else ""
        anchor_rows.append(f"""
        <tr>
          <td><code>{html.escape(a)}</code></td>
          <td>{html.escape(title)}</td>
          <td>{link}</td>
          <td>{html.escape(status)}</td>
          <td class="small">{html.escape(aliases)}</td>
        </tr>""")

    return f"""
    <div class="card">
      <h2 style="margin:0 0 8px 0; font-size:16px;">Registry Files</h2>
      <table>
        <thead><tr><th>Path</th><th>Title</th><th>ID</th><th>Status</th><th>Tags</th></tr></thead>
        <tbody>{''.join(file_rows) if file_rows else '<tr><td colspan="5" class="small">No registry files found.</td></tr>'}</tbody>
      </table>
    </div>
    <div style="height:12px;"></div>
    <div class="card">
      <h2 style="margin:0 0 8px 0; font-size:16px;">Registry Anchors</h2>
      <table>
        <thead><tr><th>Anchor</th><th>Title</th><th>File</th><th>Status</th><th>Aliases</th></tr></thead>
        <tbody>{''.join(anchor_rows) if anchor_rows else '<tr><td colspan="5" class="small">No registry anchors found.</td></tr>'}</tbody>
      </table>
    </div>
    """

def render_files(report: dict) -> str:
    files = report.get("md_files", [])
    rows = []
    for p in sorted(files):
        rows.append(f"<tr><td><a href='/view?{urlq({'file': p})}'>{html.escape(p)}</a></td></tr>")
    return f"""
    <div class="card">
      <h2 style="margin:0 0 8px 0; font-size:16px;">build/**/*.md</h2>
      <table>
        <thead><tr><th>Path</th></tr></thead>
        <tbody>{''.join(rows) if rows else '<tr><td class="small">No markdown files found under build/.</td></tr>'}</tbody>
      </table>
    </div>
    """

def render_view(root: Path, file_rel: str, line: Optional[int]) -> Tuple[int, bytes]:
    p = safe_resolve_under_root(root, file_rel)
    if not p or not p.exists() or not p.is_file():
        body = f"<div class='card'>Could not open file: <code>{html.escape(file_rel)}</code></div>"
        return 404, page("File View", body)

    txt = read_text(p)
    lines = txt.splitlines()
    # Build a line-numbered <pre>
    start = 1
    end = len(lines)
    # For very large files, show around the requested line
    window = 450
    if line and end > window:
        lo = max(1, int(line) - window // 2)
        hi = min(end, lo + window - 1)
        lo = max(1, hi - window + 1)
    else:
        lo, hi = 1, end

    pre_lines = []
    for n in range(lo, hi + 1):
        s = lines[n - 1] if n - 1 < len(lines) else ""
        esc = html.escape(s)
        classes = "ln"
        if line and n == int(line):
            classes += " hl"
        pre_lines.append(f"<span id='L{n}' class='{classes}' data-n='{n:>4} '>{esc}</span>")

    jump = ""
    if line:
        jump = f"<div class='small'>Jump: <a href='#L{int(line)}'>#L{int(line)}</a></div>"

    body = f"""
    <div class="card">
      <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:space-between; align-items:center;">
        <div><b>File:</b> <code>{html.escape(file_rel)}</code></div>
        {jump}
      </div>
      <div style="margin-top:12px;">
        <pre>{''.join(pre_lines) if pre_lines else ''}</pre>
      </div>
    </div>
    """
    return 200, page(f"View: {file_rel}", body)

class Handler(BaseHTTPRequestHandler):
    # Injected at runtime
    REPORT: dict = {}
    ROOT: Path = Path(".")

    def _send(self, status: int, payload: bytes, content_type: str = "text/html; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == "/":
            level = (qs.get("level", ["ALL"])[0] or "ALL").upper()
            q = qs.get("q", [""])[0]
            body = render_issues(self.REPORT, level, q)
            self._send(200, page("Rulebook Sanity Check", body))
            return

        if path == "/registry":
            self._send(200, page("Registry", render_registry(self.REPORT)))
            return

        if path == "/files":
            self._send(200, page("Files", render_files(self.REPORT)))
            return

        if path == "/view":
            file_rel = qs.get("file", [""])[0]
            line_raw = qs.get("line", [""])[0]
            line = int(line_raw) if line_raw.strip().isdigit() else None
            status, payload = render_view(self.ROOT, file_rel, line)
            self._send(status, payload)
            return

        if path == "/report.json":
            self._send(200, json.dumps(self.REPORT, indent=2).encode("utf-8"), content_type="application/json; charset=utf-8")
            return

        self._send(404, page("Not Found", "<div class='card'>Not found.</div>"))

def serve(report: dict, root: Path, port: int) -> None:
    class _Handler(Handler):
        REPORT = report
        ROOT = root

    with socketserver.TCPServer(("127.0.0.1", port), _Handler) as httpd:
        print(f"Serving clickthrough UI at: http://127.0.0.1:{port}/")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()

def main() -> int:
    ap = argparse.ArgumentParser(description="Sanity checks for the rulebook Markdown repo (read-only).")
    ap.add_argument("--root", default=".", help="Repo root directory (default: .)")
    ap.add_argument("--build-dir", default="build", help="Build content directory (default: build)")
    ap.add_argument("--registry", default="tag-registry.yml", help="Tag/anchor registry YAML (default: tag-registry.yml)")
    ap.add_argument("--glossary", default="glossary.yml", help="Glossary YAML (default: glossary.yml)")
    ap.add_argument("--strict", action="store_true", help="Treat WARN as ERROR (CI mode)")
    ap.add_argument(
        "--placeholder-level",
        default="info",
        choices=["ignore", "info", "warn", "error"],
        help="How to report empty placeholder files referenced by status: exists anchors (default: info)",
    )
    ap.add_argument("--json", dest="json_out", default=None, help="Write a JSON report to this path")
    ap.add_argument("--serve", action="store_true", help="Start a local clickthrough UI (http://127.0.0.1:<port>/)")
    ap.add_argument("--port", type=int, default=8787, help="Port for --serve (default: 8787)")
    ap.add_argument("--open", dest="open_browser", action="store_true", help="Open the UI in your browser (best-effort)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    build_dir = root / args.build_dir
    registry_path = root / args.registry
    glossary_path = root / args.glossary

    report = compute_report(
        root=root,
        build_dir=build_dir,
        registry_path=registry_path,
        glossary_path=glossary_path,
        placeholder_level=args.placeholder_level,
    )

    if args.json_out:
        write_json(report, args.json_out)

    # Serve UI if requested
    if args.serve:
        if args.open_browser:
            try:
                import webbrowser
                webbrowser.open(f"http://127.0.0.1:{args.port}/")
            except Exception:
                pass
        try:
            serve(report, root, args.port)
        except KeyboardInterrupt:
            print("\nStopped.")
        return 0

    # CLI output
    exit_code = print_issues(report)

    # strict mode turns warns into failures
    if args.strict and report.get("counts", {}).get("WARN", 0):
        return 1
    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
