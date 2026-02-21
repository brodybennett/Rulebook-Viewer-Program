#!/usr/bin/env python3
"""
lint_compendium.py

Validate extracted compendium JSON against:
- required ability fields from meta/ability_schema.yml
- ID patterns and uniqueness
- roll syntax contract
- canonical pathway/sequence names
- canonical enum locks (attributes/skills/action/conditions/damage types)
- sequence-level structural gates
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

try:
    from lint_roll_syntax import lint_roll_snippet, load_roll_registry
except Exception as exc:
    print(f"ERROR: failed to import roll syntax helpers: {exc}", file=sys.stderr)
    raise SystemExit(2)


DEFAULT_COMPENDIUM = "dist/compendium.json"
DEFAULT_SCHEMA = "meta/ability_schema.yml"
DEFAULT_CANON_PATHWAYS = "meta/canon_pathways.yml"
DEFAULT_CANON_SEQUENCES = "meta/canon_sequences.yml"
DEFAULT_CANON_ENUMS = "meta/canonical_enums.yml"
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    file: str
    line: int
    sequence_id: str
    ability_id: str
    expected: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "file": self.file,
            "line": self.line,
            "sequence_id": self.sequence_id,
            "ability_id": self.ability_id,
            "expected": self.expected,
        }


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(str(path))
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(str(path))
    return yaml.safe_load(path.read_text(encoding="utf-8", errors="replace"))


def load_enum_ids(data: Dict[str, Any], section: str) -> set[str]:
    raw = data.get(section)
    if not isinstance(raw, list):
        raise ValueError(f"canonical_enums.{section} must be a list.")
    out: set[str] = set()
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"canonical_enums.{section} items must be mappings.")
        token = str(item.get("id") or "").strip().lower()
        if not token:
            raise ValueError(f"canonical_enums.{section} contains an empty id.")
        out.add(token)
    return out


def norm_key(text: str) -> str:
    return re.sub(r"\s+", " ", str(text).strip().lower())


def add_finding(
    findings: List[Finding],
    *,
    severity: str,
    code: str,
    message: str,
    file: str,
    line: int,
    sequence_id: str,
    ability_id: str = "",
    expected: Optional[str] = None,
) -> None:
    findings.append(
        Finding(
            severity=severity,
            code=code,
            message=message,
            file=file,
            line=max(1, int(line) if isinstance(line, int) else 1),
            sequence_id=sequence_id,
            ability_id=ability_id,
            expected=expected,
        )
    )


def load_canon_pathways(data: Dict[str, Any]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    raw = data.get("pathways")
    if not isinstance(raw, list):
        return out
    for item in raw:
        if not isinstance(item, dict):
            continue
        slug = norm_key(item.get("slug", ""))
        if not slug:
            continue
        out[slug] = str(item.get("canonical") or slug.title()).strip()
    return out


def load_canon_sequences(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    raw = data.get("pathways")
    if not isinstance(raw, dict):
        return out
    for slug, payload in raw.items():
        slug_key = norm_key(slug)
        if not isinstance(payload, dict):
            continue
        canonical_pathway = str(payload.get("canonical_pathway") or slug_key.title()).strip()
        seq_map = payload.get("sequences")
        parsed: Dict[int, str] = {}
        if isinstance(seq_map, dict):
            for k, v in seq_map.items():
                try:
                    seq_num = int(str(k).strip())
                except ValueError:
                    continue
                parsed[seq_num] = str(v).strip()
        out[slug_key] = {
            "canonical_pathway": canonical_pathway,
            "sequences": parsed,
        }
    return out


def find_h2_index(order: List[str], needle: str) -> Optional[int]:
    target = norm_key(needle)
    for idx, raw in enumerate(order):
        if target in norm_key(raw):
            return idx
    return None


def validate_ability_field_types(
    *,
    ability: Dict[str, Any],
    file: str,
    line: int,
    sequence_id: str,
    findings: List[Finding],
) -> None:
    if not isinstance(ability.get("id"), str) or not ability.get("id", "").strip():
        add_finding(
            findings,
            severity="error",
            code="invalid_id_type",
            message="Ability `id` must be a non-empty string.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )
    if not isinstance(ability.get("name"), str) or not ability.get("name", "").strip():
        add_finding(
            findings,
            severity="error",
            code="invalid_name_type",
            message="Ability `name` must be a non-empty string.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )
    if not isinstance(ability.get("pathway"), str) or not ability.get("pathway", "").strip():
        add_finding(
            findings,
            severity="error",
            code="invalid_pathway_type",
            message="Ability `pathway` must be a non-empty string.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )
    if not isinstance(ability.get("sequence"), int):
        add_finding(
            findings,
            severity="error",
            code="invalid_sequence_type",
            message="Ability `sequence` must be an integer.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )

    for key in ("status", "type", "action", "range", "target", "duration", "text"):
        value = ability.get(key)
        if not isinstance(value, str) or not value.strip():
            add_finding(
                findings,
                severity="error",
                code=f"invalid_{key}_type",
                message=f"Ability `{key}` must be a non-empty string.",
                file=file,
                line=line,
                sequence_id=sequence_id,
                ability_id=str(ability.get("id") or ""),
            )

    cost = ability.get("cost")
    if not isinstance(cost, dict):
        add_finding(
            findings,
            severity="error",
            code="invalid_cost_type",
            message="Ability `cost` must be an object/map.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )

    roll = ability.get("roll")
    if roll is not None and not isinstance(roll, str):
        add_finding(
            findings,
            severity="error",
            code="invalid_roll_type",
            message="Ability `roll` must be a string or null.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )

    dice = ability.get("dice")
    if not isinstance(dice, dict):
        add_finding(
            findings,
            severity="error",
            code="invalid_dice_type",
            message="Ability `dice` must be an object/map.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )
    else:
        required_dice = ("check_roll", "damage_roll", "heal_roll", "effect_roll", "notes")
        for key in required_dice:
            if key not in dice:
                add_finding(
                    findings,
                    severity="error",
                    code="missing_dice_field",
                    message=f"Ability `dice` is missing `{key}`.",
                    file=file,
                    line=line,
                    sequence_id=sequence_id,
                    ability_id=str(ability.get("id") or ""),
                )
        for key in ("check_roll", "damage_roll", "heal_roll", "effect_roll"):
            val = dice.get(key)
            if val is not None and not isinstance(val, str):
                add_finding(
                    findings,
                    severity="error",
                    code="invalid_dice_roll_type",
                    message=f"Ability `dice.{key}` must be a string or null.",
                    file=file,
                    line=line,
                    sequence_id=sequence_id,
                    ability_id=str(ability.get("id") or ""),
                )
        notes = dice.get("notes")
        if not isinstance(notes, str) or not notes.strip():
            add_finding(
                findings,
                severity="error",
                code="invalid_dice_notes_type",
                message="Ability `dice.notes` must be a non-empty string.",
                file=file,
                line=line,
                sequence_id=sequence_id,
                ability_id=str(ability.get("id") or ""),
            )

    scaling = ability.get("scaling")
    if not isinstance(scaling, list):
        add_finding(
            findings,
            severity="error",
            code="invalid_scaling_type",
            message="Ability `scaling` must be an array.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )

    tags = ability.get("tags")
    if not isinstance(tags, list) or not tags:
        add_finding(
            findings,
            severity="error",
            code="invalid_tags_type",
            message="Ability `tags` must be a non-empty array.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )
    elif not all(isinstance(tag, str) and tag.strip() for tag in tags):
        add_finding(
            findings,
            severity="error",
            code="invalid_tags_items",
            message="Ability `tags` entries must be non-empty strings.",
            file=file,
            line=line,
            sequence_id=sequence_id,
            ability_id=str(ability.get("id") or ""),
        )

    for key in ("conditions", "damage_types"):
        if key not in ability:
            continue
        value = ability.get(key)
        if not isinstance(value, list):
            add_finding(
                findings,
                severity="error",
                code=f"invalid_{key}_type",
                message=f"Ability `{key}` must be an array when present.",
                file=file,
                line=line,
                sequence_id=sequence_id,
                ability_id=str(ability.get("id") or ""),
            )
            continue
        if not all(isinstance(item, str) and item.strip() for item in value):
            add_finding(
                findings,
                severity="error",
                code=f"invalid_{key}_items",
                message=f"Ability `{key}` entries must be non-empty strings.",
                file=file,
                line=line,
                sequence_id=sequence_id,
                ability_id=str(ability.get("id") or ""),
            )


def lint_compendium(
    *,
    compendium: Dict[str, Any],
    schema: Dict[str, Any],
    canon_pathways: Dict[str, str],
    canon_sequences: Dict[str, Dict[str, Any]],
    canonical_enums: Dict[str, Any],
) -> Tuple[List[Finding], Dict[str, int]]:
    findings: List[Finding] = []
    stats = {
        "sequences_scanned": 0,
        "abilities_scanned": 0,
    }

    ability_schema = schema.get("ability_schema") if isinstance(schema, dict) else None
    if not isinstance(ability_schema, dict):
        add_finding(
            findings,
            severity="error",
            code="schema_missing_ability_schema",
            message="ability_schema.yml is missing `ability_schema` mapping.",
            file="<schema>",
            line=1,
            sequence_id="",
        )
        return findings, stats

    required_fields = ability_schema.get("required")
    if not isinstance(required_fields, list):
        required_fields = []

    id_pattern_raw = str(ability_schema.get("id_pattern") or "")
    id_pattern = re.compile(id_pattern_raw) if id_pattern_raw else None

    fields = ability_schema.get("fields") if isinstance(ability_schema.get("fields"), dict) else {}
    status_enum = set(fields.get("status", {}).get("enum", []))
    type_enum = set(fields.get("type", {}).get("enum", []))
    action_enum = set(fields.get("action", {}).get("enum", []))
    opposed_enum = set(fields.get("opposed_by", {}).get("enum", []))
    key_pattern_raw = str(fields.get("cost", {}).get("key_pattern") or "")
    cost_key_pattern = re.compile(key_pattern_raw) if key_pattern_raw else None
    schema_conditions_enum = set(fields.get("conditions", {}).get("enum", []))
    schema_damage_types_enum = set(fields.get("damage_types", {}).get("enum", []))

    try:
        enum_attr_ids = load_enum_ids(canonical_enums, "attributes")
        enum_skill_ids = load_enum_ids(canonical_enums, "skills")
        enum_condition_ids = load_enum_ids(canonical_enums, "conditions")
        enum_action_ids = load_enum_ids(canonical_enums, "action_types")
        enum_damage_type_ids = load_enum_ids(canonical_enums, "damage_types")
    except Exception as exc:
        add_finding(
            findings,
            severity="error",
            code="canonical_enums_invalid",
            message=f"Failed to load canonical enum IDs: {exc}",
            file="<canon-enums>",
            line=1,
            sequence_id="",
        )
        enum_attr_ids = set()
        enum_skill_ids = set()
        enum_condition_ids = set()
        enum_action_ids = set()
        enum_damage_type_ids = set()

    if action_enum and enum_action_ids and action_enum != enum_action_ids:
        add_finding(
            findings,
            severity="error",
            code="schema_action_enum_drift",
            message="Schema `action` enum does not match canonical_enums action_types.",
            file="<schema>",
            line=1,
            sequence_id="",
            expected=", ".join(sorted(enum_action_ids)),
        )

    if schema_conditions_enum and enum_condition_ids and schema_conditions_enum != enum_condition_ids:
        add_finding(
            findings,
            severity="error",
            code="schema_conditions_enum_drift",
            message="Schema `conditions` enum does not match canonical_enums conditions.",
            file="<schema>",
            line=1,
            sequence_id="",
            expected=", ".join(sorted(enum_condition_ids)),
        )

    if schema_damage_types_enum and enum_damage_type_ids and schema_damage_types_enum != enum_damage_type_ids:
        add_finding(
            findings,
            severity="error",
            code="schema_damage_types_enum_drift",
            message="Schema `damage_types` enum does not match canonical_enums damage_types.",
            file="<schema>",
            line=1,
            sequence_id="",
            expected=", ".join(sorted(enum_damage_type_ids)),
        )

    try:
        roll_registry = load_roll_registry(schema)
    except Exception as exc:
        add_finding(
            findings,
            severity="error",
            code="schema_roll_registry_invalid",
            message=f"Failed to load roll registry from schema: {exc}",
            file="<schema>",
            line=1,
            sequence_id="",
        )
        roll_registry = None

    if roll_registry is not None and enum_attr_ids and roll_registry.tokens.get("attr", set()) != enum_attr_ids:
        add_finding(
            findings,
            severity="error",
            code="schema_attr_registry_drift",
            message="Schema roll_registry.attr does not match canonical_enums attributes.",
            file="<schema>",
            line=1,
            sequence_id="",
            expected=", ".join(sorted(enum_attr_ids)),
        )
    if roll_registry is not None and enum_skill_ids and roll_registry.tokens.get("skill", set()) != enum_skill_ids:
        add_finding(
            findings,
            severity="error",
            code="schema_skill_registry_drift",
            message="Schema roll_registry.skill does not match canonical_enums skills.",
            file="<schema>",
            line=1,
            sequence_id="",
            expected=", ".join(sorted(enum_skill_ids)),
        )

    sequences = compendium.get("sequences") if isinstance(compendium, dict) else None
    if not isinstance(sequences, list):
        add_finding(
            findings,
            severity="error",
            code="compendium_sequences_missing",
            message="Compendium root must contain `sequences` array.",
            file="<compendium>",
            line=1,
            sequence_id="",
        )
        return findings, stats

    seen_ability_ids: Dict[str, str] = {}

    for seq in sequences:
        if not isinstance(seq, dict):
            add_finding(
                findings,
                severity="error",
                code="invalid_sequence_item",
                message="Each sequence record must be an object.",
                file="<compendium>",
                line=1,
                sequence_id="",
            )
            continue

        stats["sequences_scanned"] += 1
        seq_id = str(seq.get("id") or "")
        file = str(seq.get("file") or "<unknown>")
        sequence_num = seq.get("sequence")
        pathway = norm_key(seq.get("pathway") or "")

        if not seq_id:
            add_finding(
                findings,
                severity="error",
                code="sequence_id_missing",
                message="Sequence record is missing `id`.",
                file=file,
                line=1,
                sequence_id="",
            )
            seq_id = "<missing-sequence-id>"

        if not isinstance(sequence_num, int):
            add_finding(
                findings,
                severity="error",
                code="sequence_number_invalid",
                message="Sequence `sequence` must be an integer.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )
            continue

        expected_seq_id = f"{pathway}-seq-{sequence_num:02d}"
        if seq_id != expected_seq_id:
            add_finding(
                findings,
                severity="error",
                code="sequence_id_mismatch",
                message=f"Sequence id must match `{expected_seq_id}`.",
                file=file,
                line=1,
                sequence_id=seq_id,
                expected=expected_seq_id,
            )

        if pathway not in canon_pathways:
            add_finding(
                findings,
                severity="error",
                code="unknown_pathway",
                message=f"Unknown pathway slug `{pathway}`.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )

        canonical_sequence_name = canon_sequences.get(pathway, {}).get("sequences", {}).get(sequence_num)
        if not canonical_sequence_name:
            add_finding(
                findings,
                severity="error",
                code="canonical_sequence_missing",
                message=f"No canonical name found for pathway `{pathway}` sequence `{sequence_num}`.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )
        else:
            compiled_name = str(seq.get("sequence_name") or "").strip()
            if compiled_name != canonical_sequence_name:
                add_finding(
                    findings,
                    severity="warning",
                    code="noncanonical_sequence_name",
                    message=(
                        f"Sequence name `{compiled_name}` does not match canonical `{canonical_sequence_name}`."
                    ),
                    file=file,
                    line=1,
                    sequence_id=seq_id,
                    expected=canonical_sequence_name,
                )

        sections = seq.get("sections") if isinstance(seq.get("sections"), dict) else {}
        h2_order = sections.get("h2_order") if isinstance(sections.get("h2_order"), list) else []
        adv_idx = find_h2_index([str(x) for x in h2_order], "advancement") if h2_order else None
        ex_idx = find_h2_index([str(x) for x in h2_order], "extraordinary abilities") if h2_order else None
        if adv_idx is not None and ex_idx is not None and adv_idx > ex_idx:
            add_finding(
                findings,
                severity="error",
                code="section_order_invalid",
                message="`Advancement` section must appear before `Extraordinary Abilities`.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )

        if not sections.get("has_extraordinary_abilities"):
            add_finding(
                findings,
                severity="error",
                code="missing_extraordinary_abilities",
                message="Sequence is missing an extraordinary abilities section.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )

        if not sections.get("has_attribute_gain"):
            add_finding(
                findings,
                severity="error",
                code="missing_attribute_gain",
                message="Sequence is missing an attribute gain section.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )

        abilities = seq.get("abilities")
        if not isinstance(abilities, list):
            add_finding(
                findings,
                severity="error",
                code="abilities_not_array",
                message="Sequence `abilities` must be an array.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )
            continue

        if not abilities:
            add_finding(
                findings,
                severity="error",
                code="no_abilities",
                message="Sequence has no compiled abilities.",
                file=file,
                line=1,
                sequence_id=seq_id,
            )

        for ability in abilities:
            stats["abilities_scanned"] += 1
            if not isinstance(ability, dict):
                add_finding(
                    findings,
                    severity="error",
                    code="invalid_ability_item",
                    message="Ability entry must be an object.",
                    file=file,
                    line=1,
                    sequence_id=seq_id,
                )
                continue

            ability_id = str(ability.get("id") or "")
            source = ability.get("_source") if isinstance(ability.get("_source"), dict) else {}
            line = int(source.get("line") or 1)

            for key in required_fields:
                if key not in ability:
                    add_finding(
                        findings,
                        severity="error",
                        code="missing_required_field",
                        message=f"Missing required ability field `{key}`.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )

            validate_ability_field_types(
                ability=ability,
                file=file,
                line=line,
                sequence_id=seq_id,
                findings=findings,
            )

            if id_pattern and isinstance(ability.get("id"), str) and ability.get("id"):
                if not id_pattern.fullmatch(ability["id"]):
                    add_finding(
                        findings,
                        severity="error",
                        code="ability_id_pattern",
                        message="Ability id does not match schema id_pattern.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                        expected=id_pattern.pattern,
                    )

            if ability_id:
                owner = seen_ability_ids.get(ability_id)
                if owner and owner != seq_id:
                    add_finding(
                        findings,
                        severity="error",
                        code="duplicate_ability_id",
                        message=f"Ability id `{ability_id}` is duplicated across sequences ({owner}, {seq_id}).",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )
                else:
                    seen_ability_ids[ability_id] = seq_id

            expected_prefix = f"{pathway}-seq-{sequence_num:02d}-"
            if isinstance(ability.get("id"), str) and ability.get("id") and not ability["id"].startswith(expected_prefix):
                add_finding(
                    findings,
                    severity="error",
                    code="ability_id_prefix",
                    message=f"Ability id must start with `{expected_prefix}`.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=expected_prefix,
                )

            if norm_key(ability.get("pathway", "")) != pathway:
                add_finding(
                    findings,
                    severity="error",
                    code="ability_pathway_mismatch",
                    message="Ability pathway does not match parent sequence pathway.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=pathway,
                )
            if ability.get("sequence") != sequence_num:
                add_finding(
                    findings,
                    severity="error",
                    code="ability_sequence_mismatch",
                    message="Ability sequence does not match parent sequence number.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=str(sequence_num),
                )

            if type_enum and isinstance(ability.get("type"), str) and ability.get("type") not in type_enum:
                add_finding(
                    findings,
                    severity="error",
                    code="type_not_enum",
                    message=f"Ability type `{ability.get('type')}` not in schema enum.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=", ".join(sorted(type_enum)),
                )

            if status_enum and isinstance(ability.get("status"), str) and ability.get("status") not in status_enum:
                add_finding(
                    findings,
                    severity="error",
                    code="status_not_enum",
                    message=f"Ability status `{ability.get('status')}` not in schema enum.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=", ".join(sorted(status_enum)),
                )

            effective_action_enum = enum_action_ids or action_enum
            if effective_action_enum and isinstance(ability.get("action"), str) and ability.get("action") not in effective_action_enum:
                add_finding(
                    findings,
                    severity="error",
                    code="action_not_enum",
                    message=f"Ability action `{ability.get('action')}` not in schema enum.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=", ".join(sorted(effective_action_enum)),
                )

            opposed = ability.get("opposed_by")
            if opposed is None:
                opposed = "none"
            if opposed_enum and isinstance(opposed, str) and opposed not in opposed_enum:
                add_finding(
                    findings,
                    severity="error",
                    code="opposed_by_not_enum",
                    message=f"Ability opposed_by `{opposed}` not in schema enum.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                    expected=", ".join(sorted(opposed_enum)),
                )

            cost = ability.get("cost") if isinstance(ability.get("cost"), dict) else {}
            for k, v in cost.items():
                key = str(k)
                if cost_key_pattern and not cost_key_pattern.fullmatch(key):
                    add_finding(
                        findings,
                        severity="error",
                        code="cost_key_invalid",
                        message=f"Cost key `{key}` does not match schema key_pattern.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                        expected=cost_key_pattern.pattern,
                    )
                if not isinstance(v, (int, float)):
                    add_finding(
                        findings,
                        severity="error",
                        code="cost_value_invalid",
                        message=f"Cost value for `{key}` must be numeric.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )
                elif float(v) < 0:
                    add_finding(
                        findings,
                        severity="error",
                        code="cost_value_negative",
                        message=f"Cost value for `{key}` cannot be negative.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )

            tags = ability.get("tags") if isinstance(ability.get("tags"), list) else []
            for tag in tags:
                if not isinstance(tag, str) or not TAG_RE.fullmatch(tag):
                    add_finding(
                        findings,
                        severity="error",
                        code="tag_invalid",
                        message=f"Tag `{tag}` must be lowercase token format.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )

            conditions = ability.get("conditions") if isinstance(ability.get("conditions"), list) else []
            if "conditions" in ability and not isinstance(ability.get("conditions"), list):
                add_finding(
                    findings,
                    severity="error",
                    code="conditions_not_array",
                    message="Ability `conditions` must be an array.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                )
            for condition_id in conditions:
                if not isinstance(condition_id, str):
                    add_finding(
                        findings,
                        severity="error",
                        code="condition_id_type_invalid",
                        message=f"Condition entry `{condition_id}` must be a string ID.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )
                    continue
                if enum_condition_ids and condition_id not in enum_condition_ids:
                    add_finding(
                        findings,
                        severity="error",
                        code="condition_id_unknown",
                        message=f"Condition ID `{condition_id}` is not in canonical_enums.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                        expected=", ".join(sorted(enum_condition_ids)),
                    )

            damage_types = ability.get("damage_types") if isinstance(ability.get("damage_types"), list) else []
            if "damage_types" in ability and not isinstance(ability.get("damage_types"), list):
                add_finding(
                    findings,
                    severity="error",
                    code="damage_types_not_array",
                    message="Ability `damage_types` must be an array.",
                    file=file,
                    line=line,
                    sequence_id=seq_id,
                    ability_id=ability_id,
                )
            for damage_id in damage_types:
                if not isinstance(damage_id, str):
                    add_finding(
                        findings,
                        severity="error",
                        code="damage_type_id_type_invalid",
                        message=f"Damage type entry `{damage_id}` must be a string ID.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                    )
                    continue
                if enum_damage_type_ids and damage_id not in enum_damage_type_ids:
                    add_finding(
                        findings,
                        severity="error",
                        code="damage_type_id_unknown",
                        message=f"Damage type ID `{damage_id}` is not in canonical_enums.",
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                        expected=", ".join(sorted(enum_damage_type_ids)),
                    )

            roll = ability.get("roll")
            if isinstance(roll, str) and roll.strip() and roll_registry is not None:
                _, issues = lint_roll_snippet(roll, roll_registry, strict_style=True)
                for issue in issues:
                    add_finding(
                        findings,
                        severity="error",
                        code=f"roll_{issue.code}",
                        message=issue.message,
                        file=file,
                        line=line,
                        sequence_id=seq_id,
                        ability_id=ability_id,
                        expected=issue.expected,
                    )

    findings.sort(key=lambda f: (f.severity, f.file, f.line, f.sequence_id, f.ability_id, f.code))
    return findings, stats


def print_report(
    *,
    repo: Path,
    compendium_path: Path,
    schema_path: Path,
    stats: Dict[str, int],
    findings: List[Finding],
    max_findings: int,
) -> None:
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    print("Compendium lint report")
    print(f"repo: {repo}")
    print(f"compendium: {compendium_path}")
    print(f"schema: {schema_path}")
    print(f"sequences_scanned: {stats.get('sequences_scanned', 0)}")
    print(f"abilities_scanned: {stats.get('abilities_scanned', 0)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    print("")

    if not findings:
        print("No compendium lint issues found.")
        return

    print("Detailed findings:")
    for finding in findings[: max(1, max_findings)]:
        detail = (
            f"{finding.file}:{finding.line}: [{finding.severity}/{finding.code}] {finding.message} "
            f"(sequence={finding.sequence_id}"
        )
        if finding.ability_id:
            detail += f", ability={finding.ability_id}"
        detail += ")"
        print(detail)
        if finding.expected:
            print(f"  expected: {finding.expected}")

    if len(findings) > max_findings:
        hidden = len(findings) - max_findings
        print("")
        print(f"... {hidden} additional finding(s) hidden (use --max-findings to increase).")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint compiled compendium JSON.")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument(
        "--compendium",
        default=DEFAULT_COMPENDIUM,
        help=f"Compendium JSON path (default: {DEFAULT_COMPENDIUM})",
    )
    parser.add_argument(
        "--schema",
        default=DEFAULT_SCHEMA,
        help=f"Ability schema path (default: {DEFAULT_SCHEMA})",
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
        "--canon-enums",
        default=DEFAULT_CANON_ENUMS,
        help=f"Canonical enums file (default: {DEFAULT_CANON_ENUMS})",
    )
    parser.add_argument(
        "--json-out",
        default=None,
        help="Optional path for JSON report output.",
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=250,
        help="Max detailed findings to print (default: 250).",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="Exit with code 0 even when lint errors exist.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    compendium_path = resolve_under_repo(repo, args.compendium)
    schema_path = resolve_under_repo(repo, args.schema)
    canon_pathways_path = resolve_under_repo(repo, args.canon_pathways)
    canon_sequences_path = resolve_under_repo(repo, args.canon_sequences)
    canon_enums_path = resolve_under_repo(repo, args.canon_enums)

    try:
        compendium = load_json(compendium_path)
        schema = load_yaml(schema_path)
        canon_pathways_raw = load_yaml(canon_pathways_path)
        canon_sequences_raw = load_yaml(canon_sequences_path)
        canon_enums_raw = load_yaml(canon_enums_path)
    except Exception as exc:
        print(f"ERROR: failed to load lint inputs: {exc}", file=sys.stderr)
        return 2

    if not isinstance(schema, dict):
        print("ERROR: schema root must be an object.", file=sys.stderr)
        return 2
    if (
        not isinstance(canon_pathways_raw, dict)
        or not isinstance(canon_sequences_raw, dict)
        or not isinstance(canon_enums_raw, dict)
    ):
        print("ERROR: canonical files must have object roots.", file=sys.stderr)
        return 2

    canon_pathways = load_canon_pathways(canon_pathways_raw)
    canon_sequences = load_canon_sequences(canon_sequences_raw)

    findings, stats = lint_compendium(
        compendium=compendium,
        schema=schema,
        canon_pathways=canon_pathways,
        canon_sequences=canon_sequences,
        canonical_enums=canon_enums_raw,
    )

    print_report(
        repo=repo,
        compendium_path=compendium_path,
        schema_path=schema_path,
        stats=stats,
        findings=findings,
        max_findings=max(1, args.max_findings),
    )

    if args.json_out:
        out_path = resolve_under_repo(repo, args.json_out)
        out = {
            "repo": str(repo),
            "compendium": str(compendium_path),
            "schema": str(schema_path),
            "canonical_enums": str(canon_enums_path),
            "sequences_scanned": stats.get("sequences_scanned", 0),
            "abilities_scanned": stats.get("abilities_scanned", 0),
            "errors": len([f for f in findings if f.severity == "error"]),
            "warnings": len([f for f in findings if f.severity == "warning"]),
            "findings": [f.to_dict() for f in findings],
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print("")
        print(f"Wrote JSON report: {out_path}")

    has_errors = any(f.severity == "error" for f in findings)
    if has_errors and not args.exit_zero:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
