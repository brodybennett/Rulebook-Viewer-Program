#!/usr/bin/env python3
"""congruence_audit.py

Scan markdown rulebook drafts and report likely congruence risks:
- unresolved markers: [[UNCLEAR: ...]] / [[LINK LATER: ...]]
- heading title collisions
- definition drift for repeated bold-term definitions (**Term:** ...)
- mechanic field drift for repeated heading blocks (Cost/Use/Effect)

python "VSCODE MD Files/tools/congruence_audit.py" --repo "VSCODE MD Files" --content-root draft --out "reports/audit/congruence_report.md" --json

Read-only with respect to source content; writes report artifacts only.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from find_heading_collisions import (
    DEFAULT_CONTENT_ROOT,
    HEADING_RE,
    _resolve_content_root,
    _slugify_anchor,
    _unique_anchor,
    iter_md,
    rel,
)

UNCLEAR_RE = re.compile(r"\[\[\s*UNCLEAR\s*:(?P<body>[^\]]*?)\]\]", re.IGNORECASE)
LINK_LATER_RE = re.compile(r"\[\[\s*LINK\s+LATER\s*:(?P<body>[^\]]*?)\]\]", re.IGNORECASE)
DEFINITION_RE = re.compile(
    r"^\s*(?:[-*+]\s+|\d+\.\s+|>\s+)?\*\*(?P<term>[^\n*]{2,100}?)\s*:\*\*\s*(?P<definition>.+?)\s*$"
)
FIELD_RE = re.compile(r"\*\*(?P<field>Cost|Use|Effect)\s*:\*\*\s*(?P<value>.*)", re.IGNORECASE)

MD_LINK_RE = re.compile(r"\[([^\]]+?)\]\([^)]+?\)")
WIKILINK_WITH_DISPLAY_RE = re.compile(r"\[\[([^\]|]+?)\|([^\]]+?)\]\]")
WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
INLINE_CODE_RE = re.compile(r"`([^`]+?)`")
FLAG_LINK_PREFIXES = ("unclear:", "todo:", "note:", "link later:")

KEY_FIELDS = ("cost", "use", "effect")
MIN_DEF_SIG_LEN = 8
DEF_SEQ_MATCH_THRESHOLD = 0.9
DEF_JACCARD_THRESHOLD = 0.75
GENERIC_DEFINITION_TERMS = {
    "action",
    "actions",
    "additional effect",
    "advancement ritual",
    "aftereffects",
    "attribute gain",
    "auxiliary materials",
    "benefit",
    "big failure",
    "big success",
    "check",
    "checks",
    "damage",
    "duration",
    "effect on success",
    "example",
    "examples",
    "gm note",
    "limit",
    "limits",
    "lore",
    "main material",
    "main materials",
    "manifestation",
    "note",
    "notes",
    "on success",
    "passive",
    "prerequisite",
    "prerequisites",
    "process",
    "range",
    "reference",
    "references",
    "requirement",
    "requirements",
    "resolution",
    "scaling",
    "skill gain",
    "skill increase",
    "special",
    "special case",
    "special cases",
    "target",
    "targeting",
    "targeting and range",
    "test",
    "timing",
    "traits",
    "trigger",
    "triggers",
    "type",
    "warning",
}
GENERIC_BLOCK_TITLES = {
    "attribute gain",
    "skill gain",
    "skill increase",
}


@dataclass
class Finding:
    file: str
    line: int
    excerpt: str


def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def _normalize_key(text: str) -> str:
    cleaned = text.strip().casefold()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def _strip_inline_markdown(text: str) -> str:
    text = WIKILINK_WITH_DISPLAY_RE.sub(lambda m: m.group(2), text)
    text = WIKILINK_RE.sub(lambda m: m.group(1), text)
    text = MD_LINK_RE.sub(lambda m: m.group(1), text)
    text = INLINE_CODE_RE.sub(lambda m: m.group(1), text)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"[*_~]", "", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return _normalize_ws(text)


def _norm_signature(text: str) -> str:
    text = _strip_inline_markdown(text).casefold()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return _normalize_ws(text)


def _short_excerpt(text: str, width: int = 160) -> str:
    compact = _normalize_ws(text)
    if len(compact) <= width:
        return compact
    return compact[: max(0, width - 3)] + "..."


def _resolve_output_path(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def _is_meaningfully_different(a_sig: str, b_sig: str) -> bool:
    if a_sig == b_sig:
        return False
    if not a_sig or not b_sig:
        return True

    seq = SequenceMatcher(None, a_sig, b_sig).ratio()
    tokens_a = set(a_sig.split())
    tokens_b = set(b_sig.split())
    if not tokens_a or not tokens_b:
        return seq < DEF_SEQ_MATCH_THRESHOLD

    jaccard = len(tokens_a & tokens_b) / len(tokens_a | tokens_b)
    return seq < DEF_SEQ_MATCH_THRESHOLD and jaccard < DEF_JACCARD_THRESHOLD


def _is_definition_term_candidate(term_key: str) -> bool:
    if term_key in KEY_FIELDS:
        return False
    normalized = term_key.replace("-", " ")
    normalized = _normalize_ws(normalized)
    if normalized in GENERIC_DEFINITION_TERMS:
        return False
    if re.match(r"^sequence\s+\d+\b", normalized):
        return False
    if re.match(r"^difficulty(?:\s+value)?\s+\d+\b", normalized):
        return False
    return len(normalized) >= 3


def _extract_field_items(block_lines: List[str], start_line: int) -> Dict[str, List[Dict[str, Any]]]:
    out: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    active_field: Optional[str] = None
    active_item: Optional[Dict[str, Any]] = None

    for i, line in enumerate(block_lines, start=start_line):
        m = FIELD_RE.search(line)
        if m:
            field = m.group("field").strip().casefold()
            value = _normalize_ws(m.group("value"))
            item = {
                "line": i,
                "value": value,
                "signature": _norm_signature(value),
            }
            out[field].append(item)
            active_field = field
            active_item = item
            continue

        if not active_item or not active_field:
            continue

        stripped = line.strip()
        if not stripped:
            active_field = None
            active_item = None
            continue

        if line.lstrip().startswith("#") or FIELD_RE.search(line):
            active_field = None
            active_item = None
            continue

        if line.startswith("  ") or line.startswith("\t") or line.lstrip().startswith(("-", "*", "+", ">")):
            append_value = _normalize_ws(stripped)
            if append_value:
                active_item["value"] = _normalize_ws(f"{active_item['value']} {append_value}")
                active_item["signature"] = _norm_signature(active_item["value"])
            continue

        active_field = None
        active_item = None

    return out


def _scan_markdown(
    md_files: Iterable[Path], repo: Path
) -> Tuple[
    Dict[str, List[Finding]],
    Dict[str, List[Dict[str, Any]]],
    Dict[str, List[Dict[str, Any]]],
    Dict[str, List[Dict[str, Any]]],
    Dict[str, List[Finding]],
]:
    markers: Dict[str, List[Finding]] = {"unclear": [], "link_later": []}
    heading_hits: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    definition_hits: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    block_hits: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    wikilink_heading_refs: Dict[str, List[Finding]] = defaultdict(list)

    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        file_rel = rel(md, repo)

        file_headings: List[Dict[str, Any]] = []
        used: set = set()
        counts: Dict[str, int] = {}

        for line_no, line in enumerate(lines, start=1):
            heading_match = HEADING_RE.match(line.rstrip())
            if heading_match:
                level = len(heading_match.group("h"))
                title = _normalize_ws(heading_match.group("title"))
                explicit_anchor = heading_match.group("id")
                if explicit_anchor:
                    anchor = explicit_anchor
                    used.add(anchor)
                else:
                    anchor = _unique_anchor(_slugify_anchor(title), used, counts)

                heading_entry = {
                    "file": file_rel,
                    "line": line_no,
                    "level": level,
                    "anchor": anchor,
                    "excerpt": _short_excerpt(line),
                    "title": title,
                }
                heading_hits[title].append(heading_entry)
                file_headings.append({**heading_entry, "idx0": line_no - 1})

            for m in UNCLEAR_RE.finditer(line):
                excerpt = _short_excerpt(m.group(0))
                markers["unclear"].append(Finding(file=file_rel, line=line_no, excerpt=excerpt))

            for m in LINK_LATER_RE.finditer(line):
                excerpt = _short_excerpt(m.group(0))
                markers["link_later"].append(Finding(file=file_rel, line=line_no, excerpt=excerpt))

            for m in WIKILINK_RE.finditer(line):
                inner = m.group(1).strip()
                if "|" in inner:
                    target = inner.split("|", 1)[0].strip()
                else:
                    target = inner
                if not target:
                    continue
                low_target = target.casefold()
                if low_target.startswith("id:") or target.startswith("#"):
                    continue
                if any(low_target.startswith(prefix) for prefix in FLAG_LINK_PREFIXES):
                    continue
                wikilink_heading_refs[_normalize_key(target)].append(
                    Finding(file=file_rel, line=line_no, excerpt=_short_excerpt(m.group(0)))
                )

            if line.lstrip().startswith(">"):
                continue

            def_match = DEFINITION_RE.match(line.rstrip())
            if not def_match:
                continue

            raw_term = _normalize_ws(def_match.group("term"))
            term_key = _normalize_key(raw_term)
            if not _is_definition_term_candidate(term_key):
                continue

            raw_definition = _normalize_ws(def_match.group("definition"))
            sig = _norm_signature(raw_definition)
            if len(sig) < MIN_DEF_SIG_LEN:
                continue

            definition_hits[term_key].append(
                {
                    "term": raw_term,
                    "file": file_rel,
                    "line": line_no,
                    "excerpt": _short_excerpt(line),
                    "definition": raw_definition,
                    "signature": sig,
                }
            )

        for idx, heading in enumerate(file_headings):
            if heading["level"] < 3:
                continue

            start_idx = heading["idx0"] + 1
            end_idx = len(lines)
            for nxt in file_headings[idx + 1 :]:
                if nxt["level"] <= heading["level"]:
                    end_idx = nxt["idx0"]
                    break

            block_lines = lines[start_idx:end_idx]
            fields = _extract_field_items(block_lines, start_idx + 1)
            field_values: Dict[str, Dict[str, Any]] = {}
            for field in KEY_FIELDS:
                items = fields.get(field, [])
                joined = " | ".join(item["value"] for item in items if item["value"])
                signature = _norm_signature(joined)
                field_values[field] = {
                    "signature": signature,
                    "display": _short_excerpt(joined, width=180) if joined else "",
                    "items": items,
                }

            title_key = _normalize_key(heading["title"])
            block_hits[title_key].append(
                {
                    "title": heading["title"],
                    "file": heading["file"],
                    "line": heading["line"],
                    "level": heading["level"],
                    "excerpt": heading["excerpt"],
                    "fields": field_values,
                }
            )

    return markers, heading_hits, definition_hits, block_hits, wikilink_heading_refs


def _analyze_heading_collisions(
    heading_hits: Dict[str, List[Dict[str, Any]]],
    wikilink_heading_refs: Dict[str, List[Finding]],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    linked_collisions: List[Dict[str, Any]] = []
    unlinked_collisions: List[Dict[str, Any]] = []
    for title, entries in heading_hits.items():
        if len(entries) < 2:
            continue
        ordered_entries = sorted(entries, key=lambda x: (x["file"], x["line"]))
        refs = wikilink_heading_refs.get(_normalize_key(title), [])
        collision = {
            "title": title,
            "count": len(entries),
            "entries": ordered_entries,
            "linked_count": len(refs),
            "link_refs": [asdict(r) for r in refs[:80]],
        }
        if refs:
            linked_collisions.append(collision)
        else:
            unlinked_collisions.append(collision)
    linked_collisions.sort(key=lambda x: (-x["linked_count"], -x["count"], x["title"].casefold()))
    unlinked_collisions.sort(key=lambda x: (-x["count"], x["title"].casefold()))
    return linked_collisions, unlinked_collisions


def _analyze_definition_drift(definition_hits: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []

    for term_key, entries in definition_hits.items():
        if len(entries) < 2:
            continue
        if len({e["file"] for e in entries}) < 2:
            continue

        by_signature: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for entry in entries:
            by_signature[entry["signature"]].append(entry)
        if len(by_signature) < 2:
            continue

        max_signature_count = max(len(v) for v in by_signature.values())
        variant_count = len(by_signature)
        if max_signature_count < 2:
            continue
        if variant_count > 8 and (variant_count / len(entries)) > 0.5:
            continue

        signatures = list(by_signature.keys())
        meaningfully_diff = any(
            _is_meaningfully_different(a_sig, b_sig) for a_sig, b_sig in combinations(signatures, 2)
        )
        if not meaningfully_diff:
            continue

        term_display = Counter(e["term"] for e in entries).most_common(1)[0][0]
        variants = []
        for sig, sig_entries in sorted(by_signature.items(), key=lambda kv: (-len(kv[1]), kv[1][0]["definition"])):
            variants.append(
                {
                    "count": len(sig_entries),
                    "sample": _short_excerpt(sig_entries[0]["definition"], width=180),
                    "sample_file": sig_entries[0]["file"],
                    "sample_line": sig_entries[0]["line"],
                }
            )

        findings.append(
            {
                "term_key": term_key,
                "term": term_display,
                "count": len(entries),
                "variant_count": len(variants),
                "variants": variants,
                "entries": sorted(entries, key=lambda x: (x["file"], x["line"])),
            }
        )

    findings.sort(key=lambda x: (-x["count"], x["term"].casefold()))
    return findings


def _analyze_mechanic_field_drift(block_hits: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []

    for title_key, all_entries in block_hits.items():
        if title_key in GENERIC_BLOCK_TITLES:
            continue
        if re.match(r"^sequence\s+\d+\b", title_key):
            continue
        if len(all_entries) < 2:
            continue

        entries = [
            entry
            for entry in all_entries
            if any(entry["fields"][field]["signature"] for field in KEY_FIELDS)
        ]
        if len(entries) < 2:
            continue

        conflicts: List[Dict[str, Any]] = []
        for field in KEY_FIELDS:
            present = [e for e in entries if e["fields"][field]["signature"]]
            missing = [e for e in entries if not e["fields"][field]["signature"]]

            by_signature: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
            for e in present:
                by_signature[e["fields"][field]["signature"]].append(e)

            has_conflicting_values = False
            if len(by_signature) >= 2:
                signatures = list(by_signature.keys())
                has_conflicting_values = any(
                    _is_meaningfully_different(a_sig, b_sig) for a_sig, b_sig in combinations(signatures, 2)
                )

            has_missing_values = bool(present and missing)
            if not has_conflicting_values and not has_missing_values:
                continue

            variants: List[Dict[str, Any]] = []
            for sig, sig_entries in sorted(
                by_signature.items(),
                key=lambda kv: (
                    -len(kv[1]),
                    kv[1][0]["fields"][field]["display"].casefold(),
                ),
            ):
                variants.append(
                    {
                        "count": len(sig_entries),
                        "value": sig_entries[0]["fields"][field]["display"],
                        "sample_file": sig_entries[0]["file"],
                        "sample_line": sig_entries[0]["line"],
                    }
                )
            dominant_variant_count = max((variant["count"] for variant in variants), default=0)

            reason = "conflicting values"
            if has_conflicting_values and has_missing_values:
                reason = "conflicting values + missing field in some blocks"
            elif has_missing_values:
                reason = "missing field in some blocks"

            conflicts.append(
                {
                    "field": field,
                    "reason": reason,
                    "present_count": len(present),
                    "total_count": len(entries),
                    "dominant_variant_count": dominant_variant_count,
                    "variants": variants,
                }
            )

        if not conflicts:
            continue
        # Heuristic: treat as actionable drift only when repeated variants are strong enough.
        # This suppresses false positives where a heading is reused across pathways/sequences
        # and only a tiny sample happens to share one generic field.
        repeated_signal = any(
            conflict.get("dominant_variant_count", 0) >= 3
            or (
                conflict.get("dominant_variant_count", 0) >= 2
                and conflict.get("total_count", 0) >= 5
            )
            for conflict in conflicts
        )
        if not repeated_signal:
            continue

        title_display = Counter(e["title"] for e in entries).most_common(1)[0][0]
        findings.append(
            {
                "title_key": title_key,
                "title": title_display,
                "count": len(entries),
                "conflicts": conflicts,
                "entries": sorted(entries, key=lambda x: (x["file"], x["line"])),
            }
        )

    findings.sort(key=lambda x: (-x["count"], x["title"].casefold()))
    return findings


def _render_report(
    *,
    repo: Path,
    content_dir: Path,
    md_count: int,
    markers: Dict[str, List[Finding]],
    definition_drift: List[Dict[str, Any]],
    mechanic_drift: List[Dict[str, Any]],
    heading_collisions: List[Dict[str, Any]],
    unlinked_heading_collisions: List[Dict[str, Any]],
) -> str:
    unclear = markers["unclear"]
    link_later = markers["link_later"]

    lines: List[str] = []
    lines.append("# Congruence Audit Report")
    lines.append("")
    lines.append(f"- Generated (UTC): `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`")
    lines.append(f"- Repo: `{repo}`")
    lines.append(f"- Content root: `{rel(content_dir, repo)}`")
    lines.append(f"- Markdown files scanned: **{md_count}**")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- High: **{len(definition_drift) + len(mechanic_drift)}**")
    lines.append(f"- Medium: **{len(heading_collisions)}**")
    lines.append(f"- Low: **{len(unclear) + len(link_later) + len(unlinked_heading_collisions)}**")
    lines.append("")
    lines.append("- High details:")
    lines.append(f"  - Definition drift terms: **{len(definition_drift)}**")
    lines.append(f"  - Mechanic field drift blocks: **{len(mechanic_drift)}**")
    lines.append("- Medium details:")
    lines.append(f"  - Heading collisions: **{len(heading_collisions)}**")
    lines.append("- Low details:")
    lines.append(f"  - `[[UNCLEAR: ...]]` markers: **{len(unclear)}**")
    lines.append(f"  - `[[LINK LATER: ...]]` markers: **{len(link_later)}**")
    lines.append(f"  - Unreferenced heading collisions: **{len(unlinked_heading_collisions)}**")
    lines.append("")
    lines.append("## High Severity")
    lines.append("")

    if not definition_drift and not mechanic_drift:
        lines.append("- No high-severity drift findings.")
        lines.append("")
    else:
        lines.append("### Definition Drift (`**Term:** ...`)")
        lines.append("")
        if not definition_drift:
            lines.append("- None detected.")
            lines.append("")
        else:
            for finding in definition_drift:
                lines.append(
                    f"#### Term: `{finding['term']}` ({finding['count']} occurrences, {finding['variant_count']} variants)"
                )
                lines.append("")
                for variant in finding["variants"][:6]:
                    lines.append(
                        f"- Variant (x{variant['count']}): `{variant['sample']}` "
                        f"(sample: `{variant['sample_file']}:{variant['sample_line']}`)"
                    )
                lines.append("- Locations:")
                for entry in finding["entries"][:40]:
                    lines.append(f"  - `{entry['file']}:{entry['line']}` - `{entry['excerpt']}`")
                if len(finding["entries"]) > 40:
                    lines.append(f"  - ... +{len(finding['entries']) - 40} more locations")
                lines.append("")

        lines.append("### Mechanic Field Drift (repeated heading blocks)")
        lines.append("")
        if not mechanic_drift:
            lines.append("- None detected.")
            lines.append("")
        else:
            for finding in mechanic_drift:
                lines.append(f"#### Block Title: `{finding['title']}` ({finding['count']} occurrences)")
                lines.append("")
                for conflict in finding["conflicts"]:
                    lines.append(
                        f"- Field `**{conflict['field'].title()}:**` -> {conflict['reason']} "
                        f"({conflict['present_count']}/{conflict['total_count']} blocks have this field)"
                    )
                    for variant in conflict["variants"][:5]:
                        lines.append(
                            f"  - Variant (x{variant['count']}): `{variant['value']}` "
                            f"(sample: `{variant['sample_file']}:{variant['sample_line']}`)"
                        )
                lines.append("- Locations:")
                for entry in finding["entries"][:40]:
                    field_view = ", ".join(
                        f"{field.title()}={entry['fields'][field]['display'] or '<missing>'}" for field in KEY_FIELDS
                    )
                    lines.append(f"  - `{entry['file']}:{entry['line']}` - `{entry['excerpt']}` | {field_view}")
                if len(finding["entries"]) > 40:
                    lines.append(f"  - ... +{len(finding['entries']) - 40} more locations")
                lines.append("")

    lines.append("## Medium Severity")
    lines.append("")
    lines.append("### Heading Collisions")
    lines.append("")
    if not heading_collisions:
        lines.append("- No heading-collision titles are currently referenced by plain `[[Title]]` links.")
        lines.append("")
    else:
        for collision in heading_collisions:
            lines.append(
                f"#### Heading: `{collision['title']}` (x{collision['count']}, linked {collision['linked_count']}x)"
            )
            lines.append("")
            lines.append("- Link references:")
            for ref in collision["link_refs"][:20]:
                lines.append(f"  - `{ref['file']}:{ref['line']}` - `{ref['excerpt']}`")
            if len(collision["link_refs"]) > 20:
                lines.append(f"  - ... +{len(collision['link_refs']) - 20} more link references")
            lines.append("- Heading locations:")
            for entry in collision["entries"][:40]:
                lines.append(
                    f"- `{entry['file']}:{entry['line']}` (h{entry['level']}, `# {entry['anchor']}`) "
                    f"`{entry['excerpt']}`"
                )
            if len(collision["entries"]) > 40:
                lines.append(f"- ... +{len(collision['entries']) - 40} more locations")
            lines.append("")

    lines.append("## Low Severity")
    lines.append("")
    lines.append("### `[[UNCLEAR: ...]]` Markers")
    lines.append("")
    if not unclear:
        lines.append("- None found.")
    else:
        for finding in unclear:
            lines.append(f"- `{finding.file}:{finding.line}` - `{finding.excerpt}`")
    lines.append("")
    lines.append("### `[[LINK LATER: ...]]` Markers")
    lines.append("")
    if not link_later:
        lines.append("- None found.")
    else:
        for finding in link_later:
            lines.append(f"- `{finding.file}:{finding.line}` - `{finding.excerpt}`")
    lines.append("")
    lines.append("### Unreferenced Heading Collisions")
    lines.append("")
    if not unlinked_heading_collisions:
        lines.append("- None.")
    else:
        lines.append(
            "- These collisions currently have no plain `[[Title]]` references, so they are lower-priority unless you plan to link to them by title."
        )
        for collision in unlinked_heading_collisions[:40]:
            lines.append(f"- `{collision['title']}` (x{collision['count']})")
        if len(unlinked_heading_collisions) > 40:
            lines.append(f"- ... +{len(unlinked_heading_collisions) - 40} more")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit markdown rulebook congruence risks.")
    parser.add_argument("--repo", type=str, default=".", help="Repo root")
    parser.add_argument(
        "--content-root",
        type=str,
        default=DEFAULT_CONTENT_ROOT,
        help="Content folder to scan (default: draft; falls back to build if missing)",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="reports/audit/congruence_report.md",
        help="Markdown report path (relative to --repo unless absolute). Use '-' for stdout.",
    )
    parser.add_argument(
        "--json",
        nargs="?",
        const="",
        default=None,
        help="Optional JSON output path. If provided without a value, uses --out with .json suffix.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    content_dir = _resolve_content_root(repo, args.content_root)
    if not content_dir.exists():
        print(f"ERROR: missing content root: {rel(content_dir, repo)}")
        return 2

    md_files = iter_md(repo, args.content_root)
    markers, heading_hits, definition_hits, block_hits, wikilink_heading_refs = _scan_markdown(md_files, repo)

    heading_collisions, unlinked_heading_collisions = _analyze_heading_collisions(
        heading_hits, wikilink_heading_refs
    )
    definition_drift = _analyze_definition_drift(definition_hits)
    mechanic_drift = _analyze_mechanic_field_drift(block_hits)

    report_md = _render_report(
        repo=repo,
        content_dir=content_dir,
        md_count=len(md_files),
        markers=markers,
        definition_drift=definition_drift,
        mechanic_drift=mechanic_drift,
        heading_collisions=heading_collisions,
        unlinked_heading_collisions=unlinked_heading_collisions,
    )

    if args.out == "-":
        print(report_md)
    else:
        out_path = _resolve_output_path(repo, args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report_md, encoding="utf-8")
        print(f"Wrote markdown report: {rel(out_path, repo)}")

    if args.json is not None:
        if args.json:
            json_path = _resolve_output_path(repo, args.json)
        elif args.out == "-":
            json_path = _resolve_output_path(repo, "reports/audit/congruence_report.json")
        else:
            out_path = _resolve_output_path(repo, args.out)
            json_path = out_path.with_suffix(".json")

        json_payload = {
            "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "repo": str(repo),
            "content_root": rel(content_dir, repo),
            "markdown_files_scanned": len(md_files),
            "summary": {
                "high": len(definition_drift) + len(mechanic_drift),
                "medium": len(heading_collisions),
                "low": len(markers["unclear"]) + len(markers["link_later"]) + len(unlinked_heading_collisions),
                "definition_drift_terms": len(definition_drift),
                "mechanic_field_drift_blocks": len(mechanic_drift),
                "heading_collisions": len(heading_collisions),
                "unreferenced_heading_collisions": len(unlinked_heading_collisions),
                "unclear_markers": len(markers["unclear"]),
                "link_later_markers": len(markers["link_later"]),
            },
            "high": {
                "definition_drift": definition_drift,
                "mechanic_field_drift": mechanic_drift,
            },
            "medium": {
                "heading_collisions": heading_collisions,
            },
            "low": {
                "unreferenced_heading_collisions": unlinked_heading_collisions,
                "unclear_markers": [asdict(f) for f in markers["unclear"]],
                "link_later_markers": [asdict(f) for f in markers["link_later"]],
            },
        }
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")
        print(f"Wrote JSON report: {rel(json_path, repo)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
