#!/usr/bin/env python3
"""
extract_compendium.py

Compile sequence markdown into a database-ready JSON compendium.

This extractor supports:
- legacy prose-only ability sections
- embedded `yaml ability` blocks
- canonical pathway/sequence naming from meta registries

Default output:
  dist/compendium.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


DEFAULT_CONTENT_ROOT = "draft/sequences"
DEFAULT_CANON_PATHWAYS = "meta/canon_pathways.yml"
DEFAULT_CANON_SEQUENCES = "meta/canon_sequences.yml"
DEFAULT_CANON_TERMS = "meta/canon_terms.yml"
DEFAULT_OUT = "dist/compendium.json"

SEQUENCE_FILE_RE = re.compile(r"^seq-(\d{1,2})\.md$", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ANCHOR_SUFFIX_RE = re.compile(r"\s+\{#[^}]+\}\s*$")
TITLE_RE = re.compile(r"Sequence\s+(\d{1,2})\s*:\s*(.+)$", re.IGNORECASE)
FENCE_START_RE = re.compile(r"^\s*```(?:yaml|yml)\s+ability\s*$", re.IGNORECASE)
FENCE_END_RE = re.compile(r"^\s*```\s*$")

BOLD_LABEL_RE = re.compile(
    r"^\s*(?:[-*+]\s+|\d+\.\s+)?\*\*(?P<label>[^:*]{1,80})\s*:\s*\*\*\s*(?P<value>.*)$"
)
PLAIN_LABEL_RE = re.compile(
    r"^\s*(?:[-*+]\s+|\d+\.\s+)?(?P<label>Use|Cost|Effect|Limits|Limit|Range|Target|Duration|Targeting and range)\s*:\s*(?P<value>.+)$",
    re.IGNORECASE,
)

ATTRIBUTE_LINE_RE = re.compile(r"\battribute\s+gain\b", re.IGNORECASE)
SKILL_LINE_RE = re.compile(r"\bskill\s+(?:gain|increase)\b", re.IGNORECASE)
ATTR_CHUNK_RE = re.compile(r"(?P<name>[A-Za-z][A-Za-z ()/\-']+?)\s*(?P<delta>[+\-]\d+)\b")
SKILL_CHUNK_RE = re.compile(r"(?P<name>[A-Za-z][A-Za-z ()/\-']+?)\s*(?:\+|plus\s+)(?P<delta>\d+)\b", re.IGNORECASE)

RESOURCE_PATTERNS: Dict[str, Sequence[str]] = {
    "vitality": (r"vitality", r"hp"),
    "spirituality": (r"spirituality", r"spirit(?:uality)? points?", r"spirit points?"),
    "sanity": (r"sanity",),
    "rationality": (r"rationality",),
    "luck": (r"luck",),
}

LABEL_KEYS = (
    "use",
    "cost",
    "effect",
    "limits",
    "limit",
    "range",
    "target",
    "duration",
    "targeting and range",
)

TAG_HINTS: Sequence[Tuple[str, Sequence[str]]] = (
    ("ritual", ("ritual",)),
    ("divination", ("divination", "premonition", "prophecy", "fate", "dream omen")),
    ("detection", ("vision", "detect", "identify", "perception", "sense", "scout")),
    ("healing", ("heal", "recovery", "regeneration", "restore")),
    ("stealth", ("stealth", "hide", "invisible", "conceal")),
    ("mobility", ("teleport", "move", "travel", "flight", "fly", "door", "jump")),
    ("control", ("restrain", "bind", "dominate", "control", "taunt", "pull into dream")),
    ("debuff", ("curse", "weaken", "slow", "poison", "fear")),
    ("buff", ("enhance", "boost", "increase", "improve")),
    ("defense", ("shield", "armor", "defense", "guard", "resist")),
    ("offense", ("attack", "damage", "strike", "blast", "slash", "thunder", "flame")),
    ("social", ("persuade", "deception", "charisma", "eloquence", "intimidation")),
)


@dataclass(frozen=True)
class Heading:
    level: int
    title: str
    key: str
    line_no: int  # 1-based within body


def ascii_clean(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    cleaned = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", cleaned).strip()


def norm_key(text: str) -> str:
    return re.sub(r"\s+", " ", ascii_clean(text).lower()).strip()


def slugify(text: str) -> str:
    raw = ascii_clean(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", raw).strip("-")
    return slug or "ability"


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(str(path))
    return yaml.safe_load(path.read_text(encoding="utf-8", errors="replace"))


def iter_sequence_files(scan_root: Path, allowed_pathways: Optional[set[str]] = None) -> Iterable[Path]:
    if not scan_root.exists() or not scan_root.is_dir():
        return []
    files = sorted(p for p in scan_root.rglob("seq-*.md") if p.is_file())
    if not allowed_pathways:
        return files
    out: List[Path] = []
    for path in files:
        pathway = path.parent.name.strip().lower()
        if pathway in allowed_pathways:
            out.append(path)
    return out


def split_front_matter(text: str) -> Tuple[Dict[str, Any], List[str], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines, 1

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, lines, 1

    raw = "\n".join(lines[1:end])
    try:
        parsed = yaml.safe_load(raw) if raw.strip() else {}
    except yaml.YAMLError:
        parsed = {}
    if not isinstance(parsed, dict):
        parsed = {}

    body = lines[end + 1 :]
    body_start = end + 2
    return parsed, body, body_start


def strip_anchor_suffix(title: str) -> str:
    return ANCHOR_SUFFIX_RE.sub("", title).strip()


def extract_headings(lines: Sequence[str]) -> List[Heading]:
    out: List[Heading] = []
    for idx, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line.rstrip())
        if not m:
            continue
        level = len(m.group(1))
        raw_title = strip_anchor_suffix(m.group(2))
        out.append(Heading(level=level, title=raw_title, key=norm_key(raw_title), line_no=idx))
    return out


def find_section_heading(headings: Sequence[Heading], level: int, contains_key: str) -> Optional[int]:
    needle = norm_key(contains_key)
    for i, h in enumerate(headings):
        if h.level != level:
            continue
        if needle in h.key:
            return i
    return None


def section_bounds(headings: Sequence[Heading], idx: int, total_lines: int) -> Tuple[int, int]:
    start = headings[idx].line_no
    level = headings[idx].level
    end = total_lines + 1
    for nxt in headings[idx + 1 :]:
        if nxt.level <= level:
            end = nxt.line_no
            break
    return start, end


def get_section_lines(lines: Sequence[str], start_line: int, end_line: int) -> List[str]:
    return list(lines[start_line - 1 : end_line - 1])


def parse_title_sequence_name(front_matter: Dict[str, Any]) -> Optional[str]:
    title = front_matter.get("title")
    if not isinstance(title, str):
        return None
    m = TITLE_RE.search(title.strip())
    if not m:
        return None
    return ascii_clean(m.group(2))


def extract_first_h2_name(headings: Sequence[Heading], body_lines: Sequence[str]) -> Optional[str]:
    for h in headings:
        if h.level == 2:
            if "advancement" in h.key or "extraordinary" in h.key or "notes" in h.key:
                continue
            return ascii_clean(h.title)

    # Fallback: parse first explicit H2 line if malformed heading text.
    for line in body_lines:
        m = re.match(r"^\s*##\s+(.+?)\s*$", line)
        if m:
            candidate = ascii_clean(strip_anchor_suffix(m.group(1)))
            if candidate:
                return candidate
    return None


def load_canon_pathways(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    raw = data.get("pathways")
    if not isinstance(raw, list):
        return out
    for item in raw:
        if not isinstance(item, dict):
            continue
        slug = norm_key(str(item.get("slug") or ""))
        if not slug:
            continue
        out[slug] = {
            "canonical": ascii_clean(str(item.get("canonical") or slug.title())),
            "aliases": [ascii_clean(str(a)) for a in item.get("aliases", []) if str(a).strip()],
        }
    return out


def load_canon_sequences(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    raw = data.get("pathways")
    if not isinstance(raw, dict):
        return out
    for slug, payload in raw.items():
        slug_key = norm_key(str(slug))
        if not isinstance(payload, dict):
            continue
        canonical_pathway = ascii_clean(str(payload.get("canonical_pathway") or slug_key.title()))
        seq_map = payload.get("sequences", {})
        parsed_seqs: Dict[int, str] = {}
        if isinstance(seq_map, dict):
            for k, v in seq_map.items():
                try:
                    seq_num = int(str(k).strip())
                except ValueError:
                    continue
                parsed_seqs[seq_num] = ascii_clean(str(v))
        out[slug_key] = {
            "canonical_pathway": canonical_pathway,
            "sequences": parsed_seqs,
        }
    return out


def load_attribute_aliases(canon_terms: Dict[str, Any]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    attrs = canon_terms.get("canonical_attributes")
    if not isinstance(attrs, list):
        return out

    for item in attrs:
        if not isinstance(item, dict):
            continue
        name = ascii_clean(str(item.get("name") or "")).strip()
        if not name:
            continue
        abbr = ascii_clean(str(item.get("abbreviation") or "")).upper()
        display = ascii_clean(str(item.get("display") or ""))
        canonical = display if display else (f"{name} ({abbr})" if abbr else name)

        out[norm_key(name)] = canonical
        if abbr:
            out[norm_key(f"{name} ({abbr})")] = canonical
            out[norm_key(abbr)] = canonical
        aliases = item.get("aliases", [])
        if isinstance(aliases, list):
            for alias in aliases:
                alias_s = ascii_clean(str(alias))
                if alias_s:
                    out[norm_key(alias_s)] = canonical
    return out


def collect_labels(lines: Sequence[str]) -> Dict[str, List[str]]:
    labels: Dict[str, List[str]] = defaultdict(list)
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        m = BOLD_LABEL_RE.match(stripped)
        if m:
            label = norm_key(m.group("label"))
            if label in LABEL_KEYS:
                labels[label].append(ascii_clean(m.group("value")))
            continue

        m = PLAIN_LABEL_RE.match(stripped)
        if m:
            label = norm_key(m.group("label"))
            if label in LABEL_KEYS:
                labels[label].append(ascii_clean(m.group("value")))
    return labels


def first_label(labels: Dict[str, List[str]], *keys: str) -> str:
    for key in keys:
        norm = norm_key(key)
        values = labels.get(norm)
        if values:
            return values[0]
    return ""


def parse_cost(raw: str) -> Dict[str, float | int]:
    text = norm_key(raw)
    if not text:
        return {}
    if "no cost" in text or "no spirituality expenditure" in text or text in {"none", "n/a"}:
        return {}

    out: Dict[str, float] = defaultdict(float)
    for resource, patterns in RESOURCE_PATTERNS.items():
        for pattern in patterns:
            regex = re.compile(rf"(?P<amount>\d+(?:\.\d+)?)\s*(?:x\s*)?(?:{pattern})\b")
            for m in regex.finditer(text):
                amount = float(m.group("amount"))
                out[resource] += amount

    normalized: Dict[str, float | int] = {}
    for k, v in out.items():
        if abs(v - round(v)) < 1e-9:
            normalized[k] = int(round(v))
        else:
            normalized[k] = round(v, 3)
    return normalized


def infer_action(use_value: str, body_text: str) -> str:
    merged = norm_key(f"{use_value} {body_text}")
    if "full-round action" in merged or "full round action" in merged:
        return "full-round"
    if "swift action" in merged:
        return "swift"
    if "free action" in merged:
        return "free"
    if "move action" in merged:
        return "move"
    if "attack action" in merged:
        return "attack"
    if "casting action" in merged or "cast action" in merged or "spell-casting action" in merged:
        return "cast"
    if "passive" in merged or "no action" in merged:
        return "none"
    return "cast"


def infer_type(action: str, use_value: str, title: str, body_text: str) -> str:
    merged = norm_key(f"{use_value} {title} {body_text}")
    if "reaction" in merged:
        return "reaction"
    if action == "none":
        return "passive"
    if "while active" in merged or "toggle" in merged:
        return "toggle"
    return "active"


def infer_opposed_by(body_text: str) -> str:
    text = norm_key(body_text)
    if "physical defense" in text:
        return "physical_defense"
    if "willpower defense" in text or "will defense" in text:
        return "willpower_defense"
    if "constitution defense" in text:
        return "constitution_defense"
    if "difficulty value" in text or re.search(r"\bdv\b", text):
        return "difficulty_value"
    return "none"


def infer_range(labels: Dict[str, List[str]], body_text: str) -> str:
    value = first_label(labels, "targeting and range", "range")
    if value:
        return value
    text = norm_key(body_text)
    if "line of sight" in text:
        return "line of sight"
    m = re.search(r"within\s+(\d{1,4})\s*(?:m|meter|meters)\b", text)
    if m:
        return f"{m.group(1)}m"
    return "self"


def infer_target(labels: Dict[str, List[str]], body_text: str, range_value: str) -> str:
    value = first_label(labels, "target")
    if value:
        return value
    text = norm_key(body_text)
    if "select" in text or "target" in text or "targets" in text:
        return "designated target(s)"
    if norm_key(range_value) == "self":
        return "self"
    return "designated target(s)"


def infer_duration(labels: Dict[str, List[str]], body_text: str) -> str:
    value = first_label(labels, "duration")
    if value:
        return value
    text = norm_key(body_text)
    if "per round" in text or "while active" in text or "maintain" in text or "sustained" in text:
        return "sustained"
    return "instant"


def infer_tags(title: str, body_text: str) -> List[str]:
    merged = norm_key(f"{title} {body_text}")
    tags: List[str] = []
    for tag, hints in TAG_HINTS:
        if any(hint in merged for hint in hints):
            tags.append(tag)
    if not tags:
        tags.append("utility")
    deduped: List[str] = []
    seen: set[str] = set()
    for tag in tags:
        if tag in seen:
            continue
        seen.add(tag)
        deduped.append(tag)
    return deduped


def parse_yaml_ability(lines: Sequence[str]) -> Tuple[Optional[Dict[str, Any]], bool, Optional[str]]:
    i = 0
    while i < len(lines):
        if not FENCE_START_RE.match(lines[i]):
            i += 1
            continue

        j = i + 1
        while j < len(lines) and not FENCE_END_RE.match(lines[j]):
            j += 1
        if j >= len(lines):
            return None, True, "Unclosed yaml ability fenced block."

        block_text = "\n".join(lines[i + 1 : j])
        try:
            payload = yaml.safe_load(block_text)
        except yaml.YAMLError as exc:
            return None, True, f"Invalid YAML ability block: {exc}"
        if isinstance(payload, dict):
            return payload, True, None
        return None, True, "yaml ability block root must be a mapping."
    return None, False, None


def strip_yaml_ability_blocks(lines: Sequence[str]) -> List[str]:
    out: List[str] = []
    i = 0
    while i < len(lines):
        if not FENCE_START_RE.match(lines[i]):
            out.append(lines[i])
            i += 1
            continue
        i += 1
        while i < len(lines) and not FENCE_END_RE.match(lines[i]):
            i += 1
        if i < len(lines):
            i += 1
    return out


def infer_text(title: str, lines: Sequence[str]) -> str:
    cleaned_lines: List[str] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("```"):
            continue
        if line.startswith(">"):
            continue
        line = re.sub(r"^\s*[-*+]\s*", "", line)
        line = re.sub(r"^\s*\d+\.\s*", "", line)
        line = line.replace("**", "").replace("`", "")
        line = ascii_clean(line)
        if not line:
            continue
        cleaned_lines.append(line)
        if len(cleaned_lines) >= 8:
            break
    if not cleaned_lines:
        return f"{ascii_clean(title)} ability details are defined in the source markdown."
    text = " ".join(cleaned_lines)
    if len(text) > 700:
        text = text[:697].rstrip() + "..."
    return text

def extract_attribute_gain(
    heading_title: str,
    lines: Sequence[str],
    attr_aliases: Dict[str, str],
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "heading": ascii_clean(heading_title),
        "attributes": [],
        "skills": [],
        "raw": [ascii_clean(line) for line in lines if ascii_clean(line)],
    }

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        value = ""
        if ATTRIBUTE_LINE_RE.search(stripped):
            m = re.search(r":\s*(.+)$", stripped)
            value = m.group(1) if m else stripped
            for chunk in value.split(","):
                cm = ATTR_CHUNK_RE.search(chunk)
                if not cm:
                    continue
                raw_name = ascii_clean(cm.group("name"))
                key = norm_key(raw_name)
                canonical = attr_aliases.get(key, raw_name)
                payload["attributes"].append(
                    {
                        "name": canonical,
                        "delta": int(cm.group("delta")),
                    }
                )
        elif SKILL_LINE_RE.search(stripped):
            m = re.search(r":\s*(.+)$", stripped)
            value = m.group(1) if m else stripped
            for chunk in value.split(","):
                cm = SKILL_CHUNK_RE.search(chunk)
                if not cm:
                    continue
                payload["skills"].append(
                    {
                        "name": ascii_clean(cm.group("name")),
                        "delta": int(cm.group("delta")),
                    }
                )

    return payload


def is_attribute_heading(title: str, section_lines: Sequence[str]) -> bool:
    key = norm_key(title)
    if "attribute" in key and ("gain" in key or "enhancement" in key):
        return True
    for line in section_lines:
        if ATTRIBUTE_LINE_RE.search(line):
            return True
    return False


def parse_sequence_number(path: Path) -> Optional[int]:
    m = SEQUENCE_FILE_RE.match(path.name)
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def build_ability_record(
    *,
    heading: Heading,
    ability_lines: Sequence[str],
    generated_slug: str,
    pathway_slug: str,
    sequence_num: int,
    seq_id: str,
    abs_line: int,
) -> Tuple[Dict[str, Any], bool, Optional[str]]:
    payload, has_yaml, yaml_error = parse_yaml_ability(ability_lines)
    content_lines = strip_yaml_ability_blocks(ability_lines)
    labels = collect_labels(content_lines)
    body_text = infer_text(heading.title, content_lines)

    raw_cost = first_label(labels, "cost")
    inferred_cost = parse_cost(raw_cost or body_text)
    use_value = first_label(labels, "use")
    action = infer_action(use_value, body_text)
    ability_type = infer_type(action, use_value, heading.title, body_text)
    range_value = infer_range(labels, body_text)
    target_value = infer_target(labels, body_text, range_value)
    duration_value = infer_duration(labels, body_text)
    opposed_by = infer_opposed_by(body_text)
    tags = infer_tags(heading.title, body_text)

    generated_id = f"{seq_id}-{generated_slug}"
    record: Dict[str, Any] = {}
    if isinstance(payload, dict):
        record.update(payload)

    # Hard bind to sequence identity for consistency.
    record["pathway"] = pathway_slug
    record["sequence"] = sequence_num

    if not isinstance(record.get("id"), str) or not str(record.get("id")).strip():
        record["id"] = generated_id
    if not isinstance(record.get("name"), str) or not str(record.get("name")).strip():
        record["name"] = ascii_clean(heading.title)

    if not isinstance(record.get("type"), str) or not str(record.get("type")).strip():
        record["type"] = ability_type
    if not isinstance(record.get("action"), str) or not str(record.get("action")).strip():
        record["action"] = action

    if not isinstance(record.get("cost"), dict):
        record["cost"] = inferred_cost
    if "roll" not in record:
        record["roll"] = None
    if "opposed_by" not in record or record.get("opposed_by") in ("", None):
        record["opposed_by"] = opposed_by

    if not isinstance(record.get("range"), str) or not str(record.get("range")).strip():
        record["range"] = range_value
    if not isinstance(record.get("target"), str) or not str(record.get("target")).strip():
        record["target"] = target_value
    if not isinstance(record.get("duration"), str) or not str(record.get("duration")).strip():
        record["duration"] = duration_value

    if not isinstance(record.get("scaling"), list):
        record["scaling"] = []
    if not isinstance(record.get("tags"), list) or not record.get("tags"):
        record["tags"] = tags

    if not isinstance(record.get("text"), str) or not str(record.get("text")).strip():
        record["text"] = body_text

    # Normalize a few fields for stable linting.
    record["id"] = str(record["id"]).strip().lower()
    record["id"] = re.sub(r"[^a-z0-9\-]+", "-", record["id"]).strip("-")
    record["name"] = ascii_clean(str(record["name"]))
    record["type"] = norm_key(str(record["type"]))
    record["action"] = norm_key(str(record["action"]))
    record["opposed_by"] = norm_key(str(record["opposed_by"])) if record.get("opposed_by") is not None else "none"
    record["range"] = ascii_clean(str(record["range"]))
    record["target"] = ascii_clean(str(record["target"]))
    record["duration"] = ascii_clean(str(record["duration"]))
    record["text"] = ascii_clean(str(record["text"]))

    normalized_cost: Dict[str, float | int] = {}
    for k, v in (record.get("cost") or {}).items():
        key = norm_key(str(k)).replace(" ", "_")
        try:
            num = float(v)
        except Exception:
            continue
        if num < 0:
            num = 0
        if abs(num - round(num)) < 1e-9:
            normalized_cost[key] = int(round(num))
        else:
            normalized_cost[key] = round(num, 3)
    record["cost"] = normalized_cost

    norm_tags: List[str] = []
    for tag in record.get("tags", []):
        if not isinstance(tag, str):
            continue
        token = norm_key(tag).replace(" ", "_")
        token = re.sub(r"[^a-z0-9_]+", "_", token).strip("_")
        if token:
            norm_tags.append(token)
    deduped_tags: List[str] = []
    seen_tags: set[str] = set()
    for token in norm_tags:
        if token in seen_tags:
            continue
        seen_tags.add(token)
        deduped_tags.append(token)
    record["tags"] = deduped_tags or ["utility"]

    record["_source"] = {
        "line": abs_line,
        "heading": ascii_clean(heading.title),
        "has_yaml": has_yaml,
    }

    if not record["text"]:
        record["text"] = f"{record['name']} ability details are defined in the source markdown."

    return record, has_yaml, yaml_error


def resolve_ability_id_collisions(abilities: List[Dict[str, Any]]) -> None:
    seen: Dict[str, int] = {}
    for ability in abilities:
        raw_id = str(ability.get("id") or "").strip().lower()
        if not raw_id:
            continue
        seen[raw_id] = seen.get(raw_id, 0) + 1
        if seen[raw_id] == 1:
            ability["id"] = raw_id
            continue
        ability["id"] = f"{raw_id}-{seen[raw_id]}"


def make_imputed_ability(
    *,
    seq_id: str,
    pathway_slug: str,
    sequence_num: int,
    sequence_name: str,
    line: int,
) -> Dict[str, Any]:
    return {
        "id": f"{seq_id}-imputed-sequence-authority",
        "name": f"{ascii_clean(sequence_name)} Authority",
        "pathway": pathway_slug,
        "sequence": sequence_num,
        "type": "passive",
        "action": "none",
        "cost": {},
        "roll": None,
        "opposed_by": "none",
        "range": "self",
        "target": "self",
        "duration": "instant",
        "scaling": [],
        "tags": ["utility"],
        "text": "Imputed placeholder ability because source sequence lacks explicit extraordinary ability content.",
        "_source": {
            "line": line,
            "heading": "Imputed Sequence Authority",
            "has_yaml": False,
            "imputed": True,
        },
    }


def relative_path(path: Path, repo: Path) -> str:
    return path.relative_to(repo).as_posix()


def extract_sequence_record(
    *,
    repo: Path,
    path: Path,
    canon_pathways: Dict[str, Dict[str, Any]],
    canon_sequences: Dict[str, Dict[str, Any]],
    attr_aliases: Dict[str, str],
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, int]]:
    warnings: List[Dict[str, Any]] = []
    counters = {
        "abilities_compiled": 0,
        "abilities_from_yaml": 0,
        "abilities_inferred": 0,
    }

    rel_path = relative_path(path, repo)
    pathway_slug = norm_key(path.parent.name)
    sequence_num = parse_sequence_number(path)
    if sequence_num is None:
        raise ValueError(f"Could not parse sequence number from file name: {rel_path}")

    seq_id = f"{pathway_slug}-seq-{sequence_num:02d}"
    source_text = path.read_text(encoding="utf-8", errors="replace")
    front_matter, body_lines, body_start_line = split_front_matter(source_text)
    headings = extract_headings(body_lines)

    canonical_pathway = canon_sequences.get(pathway_slug, {}).get(
        "canonical_pathway",
        canon_pathways.get(pathway_slug, {}).get("canonical", pathway_slug.title()),
    )
    canonical_pathway = ascii_clean(str(canonical_pathway))

    canonical_sequence_name = canon_sequences.get(pathway_slug, {}).get("sequences", {}).get(sequence_num)
    if not canonical_sequence_name:
        canonical_sequence_name = parse_title_sequence_name(front_matter) or extract_first_h2_name(headings, body_lines) or f"Sequence {sequence_num}"
    canonical_sequence_name = ascii_clean(canonical_sequence_name)

    source_sequence_name = parse_title_sequence_name(front_matter) or extract_first_h2_name(headings, body_lines) or canonical_sequence_name
    source_sequence_name = ascii_clean(source_sequence_name)

    h2_titles = [ascii_clean(h.title) for h in headings if h.level == 2]
    advancement_idx = find_section_heading(headings, 2, "advancement")
    extraordinary_idx = find_section_heading(headings, 2, "extraordinary abilities")

    has_advancement = advancement_idx is not None
    has_extraordinary = extraordinary_idx is not None
    imputed_extraordinary = False
    imputed_attribute = False

    attribute_payload: Dict[str, Any] = {
        "heading": "Attribute Gain",
        "attributes": [],
        "skills": [],
        "raw": [],
    }

    abilities: List[Dict[str, Any]] = []
    if extraordinary_idx is None:
        imputed_extraordinary = True
        warnings.append(
            {
                "file": rel_path,
                "line": body_start_line,
                "code": "missing_extraordinary_section",
                "message": "Missing `## Extraordinary Abilities` section.",
            }
        )
        abilities.append(
            make_imputed_ability(
                seq_id=seq_id,
                pathway_slug=pathway_slug,
                sequence_num=sequence_num,
                sequence_name=canonical_sequence_name,
                line=body_start_line,
            )
        )
        counters["abilities_compiled"] += 1
        counters["abilities_inferred"] += 1
    else:
        ex_start, ex_end = section_bounds(headings, extraordinary_idx, len(body_lines))
        h3 = [h for h in headings if h.level == 3 and ex_start < h.line_no < ex_end]
        ability_heads: List[Heading] = []

        for i, h in enumerate(h3):
            next_line = h3[i + 1].line_no if i + 1 < len(h3) else ex_end
            section_lines = get_section_lines(body_lines, h.line_no + 1, next_line)
            if is_attribute_heading(h.title, section_lines):
                attribute_payload = extract_attribute_gain(h.title, section_lines, attr_aliases)
                continue
            ability_heads.append(h)

        slug_counts: Dict[str, int] = defaultdict(int)
        generated_slugs: Dict[int, str] = {}
        for h in ability_heads:
            base = slugify(h.title)
            slug_counts[base] += 1
            generated_slugs[h.line_no] = base if slug_counts[base] == 1 else f"{base}-{slug_counts[base]}"

        for i, h in enumerate(ability_heads):
            next_line = ability_heads[i + 1].line_no if i + 1 < len(ability_heads) else ex_end
            section_lines = get_section_lines(body_lines, h.line_no + 1, next_line)
            abs_line = body_start_line + h.line_no - 1
            ability, has_yaml, yaml_error = build_ability_record(
                heading=h,
                ability_lines=section_lines,
                generated_slug=generated_slugs.get(h.line_no, slugify(h.title)),
                pathway_slug=pathway_slug,
                sequence_num=sequence_num,
                seq_id=seq_id,
                abs_line=abs_line,
            )
            abilities.append(ability)
            counters["abilities_compiled"] += 1
            if has_yaml:
                counters["abilities_from_yaml"] += 1
            else:
                counters["abilities_inferred"] += 1
            if yaml_error:
                warnings.append(
                    {
                        "file": rel_path,
                        "line": abs_line,
                        "code": "invalid_yaml_ability",
                        "message": yaml_error,
                    }
                )

    if not abilities:
        imputed_extraordinary = True
        warnings.append(
            {
                "file": rel_path,
                "line": body_start_line,
                "code": "imputed_ability",
                "message": "No explicit abilities found; injected an imputed placeholder ability.",
            }
        )
        abilities.append(
            make_imputed_ability(
                seq_id=seq_id,
                pathway_slug=pathway_slug,
                sequence_num=sequence_num,
                sequence_name=canonical_sequence_name,
                line=body_start_line,
            )
        )
        counters["abilities_compiled"] += 1
        counters["abilities_inferred"] += 1

    if not (attribute_payload.get("attributes") or attribute_payload.get("raw")):
        imputed_attribute = True
        warnings.append(
            {
                "file": rel_path,
                "line": body_start_line,
                "code": "imputed_attribute_gain",
                "message": "No explicit attribute gain found; injected an imputed placeholder attribute gain section.",
            }
        )
        attribute_payload = {
            "heading": "Attribute Gain",
            "attributes": [],
            "skills": [],
            "raw": [
                "Imputed placeholder: source sequence is missing explicit attribute gain details.",
            ],
            "imputed": True,
        }

    resolve_ability_id_collisions(abilities)

    sequence_record: Dict[str, Any] = {
        "id": seq_id,
        "pathway": pathway_slug,
        "canonical_pathway": canonical_pathway,
        "sequence": sequence_num,
        "sequence_name": canonical_sequence_name,
        "source_sequence_name": source_sequence_name,
        "file": rel_path,
        "front_matter_id": ascii_clean(str(front_matter.get("id") or "")),
        "sections": {
            "h2_order": h2_titles,
            "has_advancement": has_advancement,
            "has_extraordinary_abilities": has_extraordinary or imputed_extraordinary,
            "has_attribute_gain": bool(attribute_payload.get("attributes") or attribute_payload.get("raw")) or imputed_attribute,
            "imputed_extraordinary_abilities": imputed_extraordinary,
            "imputed_attribute_gain": imputed_attribute,
        },
        "attribute_gain": attribute_payload,
        "abilities": abilities,
    }

    return sequence_record, warnings, counters


def build_pathway_summary(sequences: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_pathway: Dict[str, Dict[str, Any]] = defaultdict(
        lambda: {"slug": "", "canonical_pathway": "", "sequence_count": 0, "ability_count": 0}
    )
    for seq in sequences:
        slug = str(seq.get("pathway") or "")
        row = by_pathway[slug]
        row["slug"] = slug
        row["canonical_pathway"] = str(seq.get("canonical_pathway") or "")
        row["sequence_count"] += 1
        row["ability_count"] += len(seq.get("abilities") or [])
    return sorted(by_pathway.values(), key=lambda x: x["slug"])

def main() -> int:
    parser = argparse.ArgumentParser(description="Extract sequence markdown into a database-ready compendium JSON.")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument(
        "--content-root",
        default=DEFAULT_CONTENT_ROOT,
        help=f"Sequence content root under repo (default: {DEFAULT_CONTENT_ROOT})",
    )
    parser.add_argument(
        "--canon-pathways",
        default=DEFAULT_CANON_PATHWAYS,
        help=f"Canonical pathways file (default: {DEFAULT_CANON_PATHWAYS})",
    )
    parser.add_argument(
        "--canon-sequences",
        default=DEFAULT_CANON_SEQUENCES,
        help=f"Canonical sequence names file (default: {DEFAULT_CANON_SEQUENCES})",
    )
    parser.add_argument(
        "--canon-terms",
        default=DEFAULT_CANON_TERMS,
        help=f"Canonical terms file for attributes (default: {DEFAULT_CANON_TERMS})",
    )
    parser.add_argument(
        "--out",
        default=DEFAULT_OUT,
        help=f"Output JSON path (default: {DEFAULT_OUT})",
    )
    parser.add_argument(
        "--pathway",
        action="append",
        default=[],
        help="Optional pathway slug to include (repeatable). If omitted, include all pathways.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Write pretty JSON (indented).",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    content_root = resolve_under_repo(repo, args.content_root)
    canon_pathways_path = resolve_under_repo(repo, args.canon_pathways)
    canon_sequences_path = resolve_under_repo(repo, args.canon_sequences)
    canon_terms_path = resolve_under_repo(repo, args.canon_terms)
    out_path = resolve_under_repo(repo, args.out)

    if not content_root.exists():
        print(f"ERROR: content root not found: {content_root}", file=sys.stderr)
        return 2

    try:
        canon_pathways_data = load_yaml(canon_pathways_path)
        canon_sequences_data = load_yaml(canon_sequences_path)
        canon_terms_data = load_yaml(canon_terms_path)
    except Exception as exc:
        print(f"ERROR: failed to load canon files: {exc}", file=sys.stderr)
        return 2

    if not isinstance(canon_pathways_data, dict) or not isinstance(canon_sequences_data, dict):
        print("ERROR: canonical files must have mapping/object roots.", file=sys.stderr)
        return 2
    if not isinstance(canon_terms_data, dict):
        canon_terms_data = {}

    canon_pathways = load_canon_pathways(canon_pathways_data)
    canon_sequences = load_canon_sequences(canon_sequences_data)
    attr_aliases = load_attribute_aliases(canon_terms_data)

    requested_pathways = {norm_key(x) for x in args.pathway if norm_key(x)}
    files = list(iter_sequence_files(content_root, requested_pathways if requested_pathways else None))

    sequences: List[Dict[str, Any]] = []
    warnings: List[Dict[str, Any]] = []
    totals = {
        "files_scanned": 0,
        "sequences_compiled": 0,
        "abilities_compiled": 0,
        "abilities_from_yaml": 0,
        "abilities_inferred": 0,
        "sequences_missing_attribute_gain": 0,
        "sequences_missing_extraordinary_abilities": 0,
    }

    for md in files:
        totals["files_scanned"] += 1
        try:
            record, record_warnings, counters = extract_sequence_record(
                repo=repo,
                path=md,
                canon_pathways=canon_pathways,
                canon_sequences=canon_sequences,
                attr_aliases=attr_aliases,
            )
        except Exception as exc:
            warnings.append(
                {
                    "file": relative_path(md, repo),
                    "line": 1,
                    "code": "extract_failed",
                    "message": str(exc),
                }
            )
            continue

        sequences.append(record)
        warnings.extend(record_warnings)
        totals["sequences_compiled"] += 1
        totals["abilities_compiled"] += counters["abilities_compiled"]
        totals["abilities_from_yaml"] += counters["abilities_from_yaml"]
        totals["abilities_inferred"] += counters["abilities_inferred"]

        sections = record.get("sections") or {}
        if not sections.get("has_attribute_gain"):
            totals["sequences_missing_attribute_gain"] += 1
        if not sections.get("has_extraordinary_abilities"):
            totals["sequences_missing_extraordinary_abilities"] += 1

    sequences = sorted(sequences, key=lambda s: (str(s.get("pathway")), int(s.get("sequence", 99))))

    payload = {
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "repo": str(repo),
        "content_root": str(content_root),
        "requested_pathways": sorted(requested_pathways),
        "stats": {
            **totals,
            "pathways_compiled": len({str(s.get("pathway")) for s in sequences}),
            "warnings_count": len(warnings),
        },
        "pathways": build_pathway_summary(sequences),
        "warnings": warnings,
        "sequences": sequences,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(payload, indent=2 if args.pretty else None, ensure_ascii=True),
        encoding="utf-8",
    )

    print("Compendium extract complete")
    print(f"repo: {repo}")
    print(f"content_root: {content_root}")
    if requested_pathways:
        print(f"pathway_filter: {sorted(requested_pathways)}")
    print(f"files_scanned: {totals['files_scanned']}")
    print(f"sequences_compiled: {totals['sequences_compiled']}")
    print(f"abilities_compiled: {totals['abilities_compiled']}")
    print(f"abilities_from_yaml: {totals['abilities_from_yaml']}")
    print(f"abilities_inferred: {totals['abilities_inferred']}")
    print(f"warnings: {len(warnings)}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
