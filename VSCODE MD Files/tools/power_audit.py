#!/usr/bin/env python3
"""
power_audit.py

Phase 4 power-balance audit for compiled sequence compendiums.

Reads:
- dist/compendium.json
- meta/power_scale.yml

Flags:
- out-of-band cost-to-effect relationships
- too many hard controls at low sequences
- damage spikes over sequence budget
- missing progression (empty or stub-only sequences)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


DEFAULT_COMPENDIUM = "dist/compendium.json"
DEFAULT_POWER_SCALE = "meta/power_scale.yml"
DEFAULT_MD_OUT = "meta/power_audit_report.md"
DEFAULT_JSON_OUT = "meta/power_audit_report.json"

HARD_CONTROL_KEYWORDS = (
    "stun",
    "stunned",
    "immobil",
    "paraly",
    "dominat",
    "petrif",
    "freeze",
    "banish",
    "cannot take action",
    "cannot act",
    "lose an action",
    "lose actions",
    "no actions",
    "sleep state",
    "forced to skip",
)

MOBILITY_KEYWORDS = (
    "teleport",
    "blink",
    "flight",
    "fly",
    "door",
    "jump",
    "escape",
    "phase",
    "shift",
    "mirror transit",
)

SURVIVABILITY_KEYWORDS = (
    "armor",
    "shield",
    "resist",
    "damage reduction",
    "recover",
    "healing",
    "regeneration",
    "restore",
    "revive",
    "resurrection",
    "vitality",
)

INVESTIGATION_KEYWORDS = (
    "divination",
    "detect",
    "identify",
    "sense",
    "vision",
    "appraisal",
    "investigation",
    "premonition",
    "prophecy",
    "analyze",
)

DAMAGE_CONTEXT_RE = re.compile(r"(damage|harm|hit|strike|wound|burn|poison)", re.IGNORECASE)
DICE_RE = re.compile(r"(?P<count>\d+)d(?P<sides>\d+)", re.IGNORECASE)
INT_RE = re.compile(r"(?<![A-Za-z0-9_])([+\-]?\d+)(?![A-Za-z0-9_])")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    pathway: str
    sequence: int
    sequence_id: str
    ability_id: str = ""
    observed: Optional[float] = None
    expected_min: Optional[float] = None
    expected_max: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "pathway": self.pathway,
            "sequence": self.sequence,
            "sequence_id": self.sequence_id,
            "ability_id": self.ability_id,
            "observed": self.observed,
            "expected_min": self.expected_min,
            "expected_max": self.expected_max,
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


def as_float(value: Any, fallback: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return fallback


def avg_top(values: Sequence[float], top_n: int = 3) -> float:
    vals = [v for v in values if isinstance(v, (int, float))]
    if not vals:
        return 0.0
    vals_sorted = sorted((float(v) for v in vals), reverse=True)
    return mean(vals_sorted[: max(1, min(top_n, len(vals_sorted)))])


def to_int_sequence(value: Any) -> Optional[int]:
    try:
        seq = int(value)
    except Exception:
        return None
    if seq < 0 or seq > 9:
        return None
    return seq


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def has_any(text: str, needles: Iterable[str]) -> bool:
    return any(n in text for n in needles)


def extract_damage_candidates(text: str) -> List[str]:
    windows: List[str] = []
    if not text:
        return windows
    for m in DAMAGE_CONTEXT_RE.finditer(text):
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 80)
        windows.append(text[start:end])
    return windows


def estimate_expr_expected(expr: str) -> float:
    if not expr:
        return 0.0

    expected = 0.0
    consumed: List[Tuple[int, int]] = []
    for m in DICE_RE.finditer(expr):
        count = int(m.group("count"))
        sides = int(m.group("sides"))
        if count <= 0 or sides <= 0:
            continue
        expected += count * (sides + 1) / 2.0
        consumed.append((m.start(), m.end()))

    for m in INT_RE.finditer(expr):
        s, e = m.span(1)
        if any(cs <= s and e <= ce for cs, ce in consumed):
            continue
        try:
            expected += int(m.group(1))
        except Exception:
            continue
    return max(0.0, expected)


def estimate_damage_expected(ability: Dict[str, Any]) -> float:
    dice = ability.get("dice") if isinstance(ability.get("dice"), dict) else {}
    if isinstance(dice.get("damage_roll"), str) and dice.get("damage_roll").strip():
        return estimate_expr_expected(dice.get("damage_roll", ""))

    roll = str(ability.get("roll") or "")
    if "damage:" in roll.lower():
        parts = [p.strip() for p in roll.split(";") if p.strip()]
        for part in parts:
            if part.lower().startswith("damage:"):
                return estimate_expr_expected(part.split(":", 1)[1].strip())

    text = str(ability.get("text") or "")
    lowered = clean_text(text)
    windows = extract_damage_candidates(lowered)
    candidates = [estimate_expr_expected(w) for w in windows if DICE_RE.search(w)]
    if candidates:
        return max(candidates)
    if DICE_RE.search(lowered):
        return estimate_expr_expected(lowered)
    return 0.0


def is_hard_control(ability: Dict[str, Any]) -> bool:
    tags = {str(t).strip().lower() for t in (ability.get("tags") or []) if str(t).strip()}
    if "hard_control" in tags:
        return True
    text = clean_text(ability.get("text") or "")
    if has_any(text, HARD_CONTROL_KEYWORDS):
        return True
    return False


def spirituality_cost(ability: Dict[str, Any]) -> float:
    cost = ability.get("cost") if isinstance(ability.get("cost"), dict) else {}
    return max(0.0, as_float(cost.get("spirituality"), 0.0))


def is_stub_ability(ability: Dict[str, Any]) -> bool:
    status = str(ability.get("status") or "").strip().lower()
    if status == "stub":
        return True
    tags = {str(t).strip().lower() for t in (ability.get("tags") or []) if str(t).strip()}
    if "stub" in tags:
        return True
    text = clean_text(ability.get("text") or "")
    if "mechanics stub" in text or "canonical mechanics pending" in text:
        return True
    return False


def is_repeatable_hard_control(ability: Dict[str, Any]) -> bool:
    if not is_hard_control(ability):
        return False
    sp = spirituality_cost(ability)
    action = str(ability.get("action") or "").strip().lower()
    duration = clean_text(ability.get("duration") or "")
    cheap = sp <= 1.0
    repeatable_action = action in {"free", "swift", "cast", "attack", "move", "none"}
    repeatable_duration = any(token in duration for token in ("instant", "1 round", "sustained", "1 encounter"))
    return cheap and repeatable_action and repeatable_duration


def has_roll_cue_without_mapping(ability: Dict[str, Any]) -> bool:
    if is_stub_ability(ability):
        return False
    dice = ability.get("dice") if isinstance(ability.get("dice"), dict) else {}
    mapped = any(
        isinstance(dice.get(key), str) and str(dice.get(key)).strip()
        for key in ("check_roll", "damage_roll", "heal_roll", "effect_roll")
    )
    if mapped:
        return False
    text = clean_text(ability.get("text") or "")
    if DICE_RE.search(text):
        return True
    cues = ("difficulty value", "check", "test", "saving throw", "damage", "heal")
    return any(cue in text for cue in cues)


def compute_scores(ability: Dict[str, Any]) -> Dict[str, float]:
    tags = {str(t).strip().lower() for t in (ability.get("tags") or []) if str(t).strip()}
    text = clean_text(ability.get("text") or "")
    action = str(ability.get("action") or "").strip().lower()
    ability_type = str(ability.get("type") or "").strip().lower()
    opposed = str(ability.get("opposed_by") or "none").strip().lower()
    sp = spirituality_cost(ability)

    damage_expected = estimate_damage_expected(ability)
    hard_control = is_hard_control(ability)

    base = 0.45
    if ability_type == "passive":
        base += 0.25
    elif ability_type == "reaction":
        base += 0.30
    elif ability_type == "toggle":
        base += 0.20

    if action in {"attack", "cast"}:
        base += 0.30
    elif action in {"free", "swift"}:
        base += 0.15
    elif action == "full-round":
        base -= 0.08

    if opposed != "none":
        base += 0.25
    if "offense" in tags:
        base += 0.28
    if "control" in tags:
        base += 0.34
    if "debuff" in tags:
        base += 0.18
    if "buff" in tags:
        base += 0.12
    if hard_control:
        base += 0.95
    if damage_expected > 0:
        base += min(1.60, damage_expected / 10.0)
    if "sustained" in clean_text(ability.get("duration") or ""):
        base += 0.12

    base = max(0.0, base)
    at_will = base / (1.0 + sp * 0.90)
    resource_spend = base * (1.0 + min(6.0, sp) * 0.15)

    control = 0.0
    if "control" in tags:
        control += 0.55
    if "debuff" in tags:
        control += 0.30
    if hard_control:
        control += 1.25
    if opposed in {"willpower_defense", "constitution_defense"}:
        control += 0.15
    if action in {"free", "swift", "reaction"}:
        control += 0.08
    if sp >= 3:
        control -= 0.05

    mobility = 0.0
    if "mobility" in tags:
        mobility += 0.85
    if "stealth" in tags:
        mobility += 0.30
    if action == "move":
        mobility += 0.25
    if has_any(text, MOBILITY_KEYWORDS):
        mobility += 0.75

    survivability = 0.0
    if "defense" in tags:
        survivability += 0.75
    if "healing" in tags:
        survivability += 0.85
    if "buff" in tags:
        survivability += 0.20
    if has_any(text, SURVIVABILITY_KEYWORDS):
        survivability += 0.70
    if ability_type in {"passive", "reaction"}:
        survivability += 0.15

    investigation = 0.0
    if "divination" in tags:
        investigation += 0.95
    if "detection" in tags:
        investigation += 0.90
    if "utility" in tags:
        investigation += 0.20
    if has_any(text, INVESTIGATION_KEYWORDS):
        investigation += 0.65
    if opposed == "difficulty_value":
        investigation += 0.12

    return {
        "effect_base": round(base, 4),
        "spirituality_cost": round(sp, 4),
        "damage_expected": round(damage_expected, 4),
        "at_will_effectiveness": round(at_will, 4),
        "resource_spend_effectiveness": round(resource_spend, 4),
        "control_strength": round(max(0.0, control), 4),
        "mobility_escape": round(max(0.0, mobility), 4),
        "survivability": round(max(0.0, survivability), 4),
        "investigation_divination": round(max(0.0, investigation), 4),
    }


def parse_budgets(power_scale: Dict[str, Any]) -> Tuple[Dict[int, Dict[str, Any]], Dict[str, Any]]:
    raw_budgets = power_scale.get("sequence_budgets")
    if not isinstance(raw_budgets, dict):
        raise ValueError("power_scale.yml missing sequence_budgets mapping")

    budgets: Dict[int, Dict[str, Any]] = {}
    for key, payload in raw_budgets.items():
        seq = to_int_sequence(key)
        if seq is None:
            continue
        if not isinstance(payload, dict):
            continue
        budgets[seq] = payload

    guardrails = power_scale.get("guardrails")
    if not isinstance(guardrails, dict):
        guardrails = {}
    return budgets, guardrails


def add_finding(
    findings: List[Finding],
    *,
    severity: str,
    code: str,
    message: str,
    pathway: str,
    sequence: int,
    sequence_id: str,
    ability_id: str = "",
    observed: Optional[float] = None,
    expected_min: Optional[float] = None,
    expected_max: Optional[float] = None,
    ) -> None:
    findings.append(
        Finding(
            severity=severity,
            code=code,
            message=message,
            pathway=pathway,
            sequence=sequence,
            sequence_id=sequence_id,
            ability_id=ability_id,
            observed=observed,
            expected_min=expected_min,
            expected_max=expected_max,
        )
    )


def audit_compendium(
    *,
    compendium: Dict[str, Any],
    budgets: Dict[int, Dict[str, Any]],
    guardrails: Dict[str, Any],
) -> Tuple[List[Finding], Dict[str, Any]]:
    findings: List[Finding] = []
    sequences = compendium.get("sequences")
    if not isinstance(sequences, list):
        raise ValueError("compendium root missing sequences[]")

    stats: Dict[str, Any] = {
        "sequences_scanned": 0,
        "abilities_scanned": 0,
        "stub_abilities": 0,
        "hard_controls": 0,
    }

    low_window = guardrails.get("low_sequence_window") if isinstance(guardrails.get("low_sequence_window"), dict) else {}
    low_min = int(low_window.get("min_sequence", 7))
    low_max = int(low_window.get("max_sequence", 9))
    low_seq_guard = guardrails.get("low_sequence_hard_control") if isinstance(guardrails.get("low_sequence_hard_control"), dict) else {}
    low_seq_max_per_record = int(low_seq_guard.get("max_per_sequence_record", 1))
    low_seq_max_per_pathway = int(low_seq_guard.get("max_per_pathway_total", 2))
    low_repeatable_guard = (
        guardrails.get("low_sequence_repeatable_hard_control")
        if isinstance(guardrails.get("low_sequence_repeatable_hard_control"), dict)
        else {}
    )
    low_repeatable_max_per_pathway = int(low_repeatable_guard.get("max_per_pathway_total", 1))

    ratio_guard = guardrails.get("out_of_band_cost_ratio") if isinstance(guardrails.get("out_of_band_cost_ratio"), dict) else {}
    ratio_high = as_float(ratio_guard.get("max_above_sequence_band"), 0.70)
    ratio_low = as_float(ratio_guard.get("min_below_sequence_band"), 0.50)

    pathway_low_hard_control: Counter[str] = Counter()
    pathway_low_repeatable_hard_control: Counter[str] = Counter()
    sequence_presence: Dict[str, set] = defaultdict(set)

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        seq_id = str(seq.get("id") or "")
        pathway = str(seq.get("pathway") or "")
        seq_num = to_int_sequence(seq.get("sequence"))
        if seq_num is None:
            continue
        sequence_presence[pathway].add(seq_num)
        stats["sequences_scanned"] += 1

        abilities = seq.get("abilities")
        if not isinstance(abilities, list):
            add_finding(
                findings,
                severity="error",
                code="missing_abilities_array",
                message="Sequence is missing an abilities array.",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
            )
            continue

        if not abilities:
            add_finding(
                findings,
                severity="error",
                code="empty_sequence",
                message="Sequence has no abilities (missing progression).",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
            )
            continue

        seq_budget = budgets.get(seq_num)
        if not seq_budget:
            add_finding(
                findings,
                severity="warning",
                code="missing_sequence_budget",
                message=f"No power-scale budget found for sequence {seq_num}.",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
            )
            continue

        metric_values: Dict[str, List[float]] = defaultdict(list)
        non_stub_count = 0
        hard_control_count = 0
        hard_control_repeatable_count = 0

        seq_damage_max_expected = as_float(
            ((seq_budget.get("damage") or {}).get("max_expected_hit")),
            999.0,
        )
        seq_damage_max_burst = as_float(
            ((seq_budget.get("damage") or {}).get("max_burst_expected_hit")),
            999.0,
        )

        seq_resource_max = as_float(((seq_budget.get("resource_spend_effectiveness") or {}).get("max")), 999.0)
        seq_resource_min = as_float(((seq_budget.get("resource_spend_effectiveness") or {}).get("min")), 0.0)

        for ability in abilities:
            if not isinstance(ability, dict):
                continue
            stats["abilities_scanned"] += 1
            aid = str(ability.get("id") or "")
            stub = is_stub_ability(ability)
            if stub:
                stats["stub_abilities"] += 1
            else:
                non_stub_count += 1

            scores = compute_scores(ability)
            for metric in (
                "at_will_effectiveness",
                "resource_spend_effectiveness",
                "control_strength",
                "mobility_escape",
                "survivability",
                "investigation_divination",
            ):
                metric_values[metric].append(scores[metric])

            hard = is_hard_control(ability)
            if hard:
                hard_control_count += 1
                stats["hard_controls"] += 1
                if low_min <= seq_num <= low_max:
                    pathway_low_hard_control[pathway] += 1
                if is_repeatable_hard_control(ability):
                    hard_control_repeatable_count += 1
                    if low_min <= seq_num <= low_max:
                        pathway_low_repeatable_hard_control[pathway] += 1

            sp = spirituality_cost(ability)
            effect = scores["effect_base"]
            ratio = effect / (1.0 + sp)
            if scores["resource_spend_effectiveness"] > seq_resource_max and ratio > (1.0 + ratio_high):
                add_finding(
                    findings,
                    severity="warning",
                    code="out_of_band_cost_too_cheap",
                    message="Ability appears too cheap for its estimated effect profile.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    ability_id=aid,
                    observed=round(ratio, 4),
                    expected_max=round(1.0 + ratio_high, 4),
                )
            if sp >= 3.0 and scores["resource_spend_effectiveness"] < seq_resource_min * ratio_low:
                add_finding(
                    findings,
                    severity="info",
                    code="out_of_band_cost_too_expensive",
                    message="Ability may be over-costed for its estimated effect profile.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    ability_id=aid,
                    observed=scores["resource_spend_effectiveness"],
                    expected_min=round(seq_resource_min * ratio_low, 4),
                )

            dmg = scores["damage_expected"]
            if dmg > seq_damage_max_burst:
                add_finding(
                    findings,
                    severity="error",
                    code="damage_spike_burst",
                    message="Ability burst damage exceeds sequence burst budget.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    ability_id=aid,
                    observed=dmg,
                    expected_max=seq_damage_max_burst,
                )
            elif dmg > seq_damage_max_expected:
                add_finding(
                    findings,
                    severity="warning",
                    code="damage_spike_expected",
                    message="Ability expected damage exceeds sequence sustained budget.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    ability_id=aid,
                    observed=dmg,
                    expected_max=seq_damage_max_expected,
                )

            if has_roll_cue_without_mapping(ability):
                add_finding(
                    findings,
                    severity="info",
                    code="dice_mapping_missing",
                    message="Ability prose references roll/dice cues but structured dice fields are still null.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    ability_id=aid,
                )

        if non_stub_count == 0:
            add_finding(
                findings,
                severity="warning",
                code="stub_only_sequence",
                message="Sequence contains only stub abilities (progression incomplete).",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
            )

        if low_min <= seq_num <= low_max and hard_control_count > low_seq_max_per_record:
            add_finding(
                findings,
                severity="warning",
                code="too_many_hard_controls_low_sequence",
                message="Low-sequence record exceeds hard-control budget.",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
                observed=float(hard_control_count),
                expected_max=float(low_seq_max_per_record),
            )
        if low_min <= seq_num <= low_max and hard_control_repeatable_count > 1:
            add_finding(
                findings,
                severity="warning",
                code="repeatable_hard_control_density",
                message="Low-sequence record has multiple repeatable hard controls.",
                pathway=pathway,
                sequence=seq_num,
                sequence_id=seq_id,
                observed=float(hard_control_repeatable_count),
                expected_max=1.0,
            )

        for metric in (
            "at_will_effectiveness",
            "resource_spend_effectiveness",
            "control_strength",
            "mobility_escape",
            "survivability",
            "investigation_divination",
        ):
            band = seq_budget.get(metric) if isinstance(seq_budget.get(metric), dict) else {}
            bmin = as_float(band.get("min"), 0.0)
            bmax = as_float(band.get("max"), 999.0)
            observed = avg_top(metric_values.get(metric, []), top_n=3)
            if observed < bmin:
                add_finding(
                    findings,
                    severity="info",
                    code=f"{metric}_below_band",
                    message=f"Sequence aggregate {metric} appears below budget band.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    observed=round(observed, 4),
                    expected_min=bmin,
                )
            elif observed > bmax:
                sev = "warning" if metric in {"control_strength", "resource_spend_effectiveness"} else "info"
                add_finding(
                    findings,
                    severity=sev,
                    code=f"{metric}_above_band",
                    message=f"Sequence aggregate {metric} appears above budget band.",
                    pathway=pathway,
                    sequence=seq_num,
                    sequence_id=seq_id,
                    observed=round(observed, 4),
                    expected_max=bmax,
                )

    for pathway, count in sorted(pathway_low_hard_control.items()):
        if count > low_seq_max_per_pathway:
            add_finding(
                findings,
                severity="warning",
                code="too_many_hard_controls_pathway_low_sequence",
                message="Pathway low-sequence hard-control total exceeds guardrail.",
                pathway=pathway,
                sequence=-1,
                sequence_id=f"{pathway}-low-seq-window",
                observed=float(count),
                expected_max=float(low_seq_max_per_pathway),
            )

    for pathway, count in sorted(pathway_low_repeatable_hard_control.items()):
        if count > low_repeatable_max_per_pathway:
            add_finding(
                findings,
                severity="warning",
                code="too_many_repeatable_hard_controls_pathway_low_sequence",
                message="Pathway low-sequence repeatable hard-control total exceeds guardrail.",
                pathway=pathway,
                sequence=-1,
                sequence_id=f"{pathway}-low-seq-window",
                observed=float(count),
                expected_max=float(low_repeatable_max_per_pathway),
            )

    for pathway, seen in sorted(sequence_presence.items()):
        missing = [s for s in range(0, 10) if s not in seen]
        if missing:
            add_finding(
                findings,
                severity="error",
                code="missing_sequence_records",
                message=f"Pathway missing sequence record(s): {missing}",
                pathway=pathway,
                sequence=-1,
                sequence_id=f"{pathway}-progression",
            )

    findings.sort(key=lambda f: (f.severity, f.pathway, f.sequence, f.sequence_id, f.ability_id, f.code))
    return findings, stats


def render_markdown_report(
    *,
    repo: Path,
    compendium_path: Path,
    power_scale_path: Path,
    findings: Sequence[Finding],
    stats: Dict[str, Any],
    max_findings: int,
) -> str:
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    infos = [f for f in findings if f.severity == "info"]

    lines: List[str] = []
    lines.append("# Power Audit Report")
    lines.append("")
    lines.append(f"- repo: `{repo}`")
    lines.append(f"- compendium: `{compendium_path}`")
    lines.append(f"- power_scale: `{power_scale_path}`")
    lines.append(f"- sequences_scanned: **{stats.get('sequences_scanned', 0)}**")
    lines.append(f"- abilities_scanned: **{stats.get('abilities_scanned', 0)}**")
    lines.append(f"- stub_abilities: **{stats.get('stub_abilities', 0)}**")
    lines.append(f"- hard_controls: **{stats.get('hard_controls', 0)}**")
    lines.append(f"- findings: **{len(findings)}**")
    lines.append(f"  - errors: **{len(errors)}**")
    lines.append(f"  - warnings: **{len(warnings)}**")
    lines.append(f"  - info: **{len(infos)}**")
    lines.append("")

    if not findings:
        lines.append("No power-audit issues found.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Detailed Findings")
    lines.append("")

    display = list(findings[: max(1, max_findings)])
    for f in display:
        where = f"{f.pathway} / seq {f.sequence}" if f.sequence >= 0 else f.pathway
        ability = f" / {f.ability_id}" if f.ability_id else ""
        lines.append(f"- **[{f.severity.upper()}] {f.code}** - {where}{ability}")
        lines.append(f"  - {f.message}")
        if f.observed is not None:
            lines.append(f"  - observed: `{f.observed}`")
        if f.expected_min is not None:
            lines.append(f"  - expected_min: `{f.expected_min}`")
        if f.expected_max is not None:
            lines.append(f"  - expected_max: `{f.expected_max}`")
    if len(findings) > max_findings:
        hidden = len(findings) - max_findings
        lines.append("")
        lines.append(f"- ... `{hidden}` additional finding(s) hidden (use `--max-findings` to increase).")
    lines.append("")
    return "\n".join(lines)


def print_summary(
    *,
    repo: Path,
    compendium_path: Path,
    power_scale_path: Path,
    stats: Dict[str, Any],
    findings: Sequence[Finding],
) -> None:
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    infos = [f for f in findings if f.severity == "info"]
    print("Power audit report")
    print(f"repo: {repo}")
    print(f"compendium: {compendium_path}")
    print(f"power_scale: {power_scale_path}")
    print(f"sequences_scanned: {stats.get('sequences_scanned', 0)}")
    print(f"abilities_scanned: {stats.get('abilities_scanned', 0)}")
    print(f"stub_abilities: {stats.get('stub_abilities', 0)}")
    print(f"hard_controls: {stats.get('hard_controls', 0)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    print(f"info: {len(infos)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit sequence compendium power scaling and progression quality.")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument(
        "--compendium",
        default=DEFAULT_COMPENDIUM,
        help=f"Compendium JSON path (default: {DEFAULT_COMPENDIUM})",
    )
    parser.add_argument(
        "--power-scale",
        default=DEFAULT_POWER_SCALE,
        help=f"Power-scale YAML path (default: {DEFAULT_POWER_SCALE})",
    )
    parser.add_argument(
        "--out",
        default=DEFAULT_MD_OUT,
        help=f"Markdown report output path (default: {DEFAULT_MD_OUT})",
    )
    parser.add_argument(
        "--json-out",
        default=DEFAULT_JSON_OUT,
        help=f"JSON report output path (default: {DEFAULT_JSON_OUT})",
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=300,
        help="Max detailed findings in markdown output (default: 300).",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="Exit with code 0 even when errors/warnings exist.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    compendium_path = resolve_under_repo(repo, args.compendium)
    power_scale_path = resolve_under_repo(repo, args.power_scale)
    out_path = resolve_under_repo(repo, args.out)
    json_out_path = resolve_under_repo(repo, args.json_out)

    try:
        compendium = load_json(compendium_path)
        power_scale = load_yaml(power_scale_path)
    except Exception as exc:
        print(f"ERROR: failed to load audit inputs: {exc}", file=sys.stderr)
        return 2

    if not isinstance(compendium, dict):
        print("ERROR: compendium root must be an object.", file=sys.stderr)
        return 2
    if not isinstance(power_scale, dict):
        print("ERROR: power_scale root must be an object.", file=sys.stderr)
        return 2

    try:
        budgets, guardrails = parse_budgets(power_scale)
        findings, stats = audit_compendium(
            compendium=compendium,
            budgets=budgets,
            guardrails=guardrails,
        )
    except Exception as exc:
        print(f"ERROR: audit failed: {exc}", file=sys.stderr)
        return 2

    md = render_markdown_report(
        repo=repo,
        compendium_path=compendium_path,
        power_scale_path=power_scale_path,
        findings=findings,
        stats=stats,
        max_findings=max(1, args.max_findings),
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    payload = {
        "repo": str(repo),
        "compendium": str(compendium_path),
        "power_scale": str(power_scale_path),
        "stats": stats,
        "errors": len([f for f in findings if f.severity == "error"]),
        "warnings": len([f for f in findings if f.severity == "warning"]),
        "info": len([f for f in findings if f.severity == "info"]),
        "findings": [f.to_dict() for f in findings],
    }
    json_out_path.parent.mkdir(parents=True, exist_ok=True)
    json_out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print_summary(
        repo=repo,
        compendium_path=compendium_path,
        power_scale_path=power_scale_path,
        stats=stats,
        findings=findings,
    )
    print(f"wrote: {out_path}")
    print(f"wrote: {json_out_path}")

    has_blocking = any(f.severity in {"error", "warning"} for f in findings)
    if has_blocking and not args.exit_zero:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
