#!/usr/bin/env python3
"""sim_core_combat.py

Monte Carlo harness for Phase 1 core combat balance validation.

Example:
python "VSCODE MD Files/tools/sim_core_combat.py" --repo "VSCODE MD Files" --out "meta/balance_report.md" --json
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except Exception:
    raise SystemExit("ERROR: PyYAML is required. Install with: pip install pyyaml")


DEFAULT_TARGETS = "meta/balance_targets.yml"
DEFAULT_OUT = "meta/balance_report.md"


@dataclass(frozen=True)
class Band:
    minimum: float
    maximum: float


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return repo / path


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Targets file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Targets YAML must be a mapping/object at top level.")
    return data


def parse_band(raw: Any) -> Optional[Band]:
    if not isinstance(raw, dict):
        return None
    if "min" not in raw or "max" not in raw:
        return None
    return Band(float(raw["min"]), float(raw["max"]))


def format_band(band: Optional[Band], percent: bool = False) -> str:
    if band is None:
        return "-"
    if percent:
        return f"{band.minimum * 100:.1f}% - {band.maximum * 100:.1f}%"
    return f"{band.minimum:.2f} - {band.maximum:.2f}"


def band_midpoint(band: Optional[Band]) -> Optional[float]:
    if band is None:
        return None
    return (band.minimum + band.maximum) / 2.0


def evaluate_band(value: float, band: Optional[Band]) -> str:
    if band is None:
        return "N/A"
    if value < band.minimum:
        return "LOW"
    if value > band.maximum:
        return "HIGH"
    return "PASS"


def check_success_rate(bonus: float, difficulty_value: float) -> float:
    successes = 0
    for roll in range(1, 21):
        if roll == 20:
            successes += 1
            continue
        if roll == 1:
            continue
        if (roll + bonus) > difficulty_value:
            successes += 1
    return successes / 20.0


def compile_dice(expr: str) -> List[Tuple[int, int, int]]:
    text = expr.replace(" ", "")
    if not text:
        raise ValueError("Damage expression cannot be empty.")
    parts = text.replace("-", "+-").split("+")
    terms: List[Tuple[int, int, int]] = []
    for raw in parts:
        if not raw:
            continue
        sign = 1
        token = raw
        if token.startswith("-"):
            sign = -1
            token = token[1:]
        if "d" in token:
            count_text, sides_text = token.split("d", 1)
            count = int(count_text) if count_text else 1
            sides = int(sides_text)
            if count <= 0 or sides <= 0:
                raise ValueError(f"Invalid dice term in '{expr}': {raw}")
            terms.append((sign, count, sides))
        else:
            value = int(token)
            terms.append((sign, value, 0))
    if not terms:
        raise ValueError(f"Invalid damage expression: {expr}")
    return terms


def roll_compiled(terms: List[Tuple[int, int, int]], rng: random.Random) -> int:
    total = 0
    for sign, count, sides in terms:
        if sides == 0:
            total += sign * count
            continue
        subtotal = sum(rng.randint(1, sides) for _ in range(count))
        total += sign * subtotal
    return total


def max_compiled(terms: List[Tuple[int, int, int]]) -> int:
    total = 0
    for sign, count, sides in terms:
        if sides == 0:
            total += sign * count
            continue
        total += sign * (count * sides)
    return total


def physical_defense(statline: Dict[str, Any], firearm: bool) -> float:
    base = 10 + float(statline.get("armor", 0))
    quick_dodge = bool(statline.get("quick_dodge", False))
    if (not firearm) or quick_dodge:
        base += float(statline.get("agility", 0)) + float(statline.get("dodge", 0))
    return base


def target_defense(statline: Dict[str, Any], defense_name: str, firearm: bool = False) -> float:
    key = defense_name.strip().lower()
    if key == "physical":
        return physical_defense(statline, firearm=firearm)
    if key == "willpower":
        return 10 + float(statline.get("willpower", 0))
    if key == "constitution":
        return 10 + float(statline.get("constitution", 0))
    raise ValueError(f"Unsupported defense type: {defense_name}")


def resolve_attack(
    attacker: Dict[str, Any],
    defender: Dict[str, Any],
    *,
    style: str,
    rng: random.Random,
    cast_defense: str = "willpower",
) -> Dict[str, Any]:
    style_key = style.strip().lower()
    if style_key == "melee":
        bonus = float(attacker.get("attack_bonus", 0))
        damage_expr = str(attacker.get("melee_damage", "1"))
        defense = target_defense(defender, "physical", firearm=False)
        sp_cost = 0.0
    elif style_key == "firearm":
        bonus = float(attacker.get("firearm_bonus", 0))
        damage_expr = str(attacker.get("firearm_damage", "1"))
        defense = target_defense(defender, "physical", firearm=True)
        sp_cost = 0.0
    elif style_key == "cast":
        bonus = float(attacker.get("cast_bonus", 0))
        damage_expr = str(attacker.get("cast_damage", "1"))
        defense = target_defense(defender, cast_defense, firearm=False)
        sp_cost = float(attacker.get("sp_per_cast", 1))
    else:
        raise ValueError(f"Unsupported style: {style}")

    roll = rng.randint(1, 20)
    crit = roll == 20
    if roll == 1:
        hit = False
    elif crit:
        hit = True
    else:
        hit = (roll + bonus) > defense

    damage = 0
    if hit:
        terms = compile_dice(damage_expr)
        damage = roll_compiled(terms, rng)
        if crit:
            crit_floor = math.ceil(max_compiled(terms) / 2)
            damage = max(damage, crit_floor)
        reduction = float(defender.get("damage_reduction", 0))
        damage = max(1, int(round(damage - reduction)))

    return {
        "hit": hit,
        "crit": crit,
        "damage": float(damage),
        "sp_cost": sp_cost,
        "defense": defense,
    }


def percentile(values: List[float], q: float) -> float:
    if not values:
        return 0.0
    if q <= 0:
        return float(min(values))
    if q >= 1:
        return float(max(values))
    ordered = sorted(values)
    idx = max(0, min(len(ordered) - 1, math.ceil(q * len(ordered)) - 1))
    return float(ordered[idx])


def simulate_single_exchange(
    attacker: Dict[str, Any],
    defender: Dict[str, Any],
    *,
    style: str,
    trials: int,
    rng: random.Random,
    cast_defense: str,
) -> Dict[str, float]:
    hits = 0
    crits = 0
    total_damage = 0.0
    total_sp = 0.0
    for _ in range(trials):
        out = resolve_attack(attacker, defender, style=style, rng=rng, cast_defense=cast_defense)
        if out["hit"]:
            hits += 1
        if out["crit"]:
            crits += 1
        total_damage += out["damage"]
        total_sp += out["sp_cost"]

    hit_rate = hits / trials
    crit_rate = crits / trials
    dpr = total_damage / trials
    avg_damage_on_hit = (total_damage / hits) if hits else 0.0
    avg_sp_per_attack = total_sp / trials
    return {
        "hit_rate": hit_rate,
        "crit_rate": crit_rate,
        "dpr": dpr,
        "avg_damage_on_hit": avg_damage_on_hit,
        "avg_sp_per_attack": avg_sp_per_attack,
    }


def simulate_time_to_down(
    attacker: Dict[str, Any],
    defender: Dict[str, Any],
    *,
    style: str,
    trials: int,
    max_rounds: int,
    rng: random.Random,
    cast_defense: str,
) -> Dict[str, float]:
    rounds_samples: List[float] = []
    sp_samples: List[float] = []
    timeouts = 0
    vitality = float(defender.get("vitality", 1))

    for _ in range(trials):
        hp = vitality
        rounds = 0
        spent = 0.0
        while hp > 0 and rounds < max_rounds:
            rounds += 1
            out = resolve_attack(attacker, defender, style=style, rng=rng, cast_defense=cast_defense)
            hp -= out["damage"]
            spent += out["sp_cost"]
        if hp > 0:
            timeouts += 1
            rounds_samples.append(float(max_rounds + 1))
        else:
            rounds_samples.append(float(rounds))
        sp_samples.append(spent)

    avg_rounds = statistics.fmean(rounds_samples) if rounds_samples else 0.0
    med_rounds = statistics.median(rounds_samples) if rounds_samples else 0.0
    p90_rounds = percentile(rounds_samples, 0.9)
    avg_sp = statistics.fmean(sp_samples) if sp_samples else 0.0
    timeout_rate = (timeouts / trials) if trials else 0.0
    return {
        "avg_rounds_to_down": avg_rounds,
        "median_rounds_to_down": float(med_rounds),
        "p90_rounds_to_down": p90_rounds,
        "avg_sp_spend": avg_sp,
        "timeout_rate": timeout_rate,
    }


def run_check_targets(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    for item in config.get("check_targets", []):
        bonus = float(item.get("bonus", 0))
        dv = float(item.get("difficulty_value", 0))
        rate = check_success_rate(bonus, dv)
        expected = parse_band(item.get("expected"))
        status = evaluate_band(rate, expected)
        rows.append(
            {
                "id": str(item.get("id", "unnamed_check")),
                "bonus": bonus,
                "difficulty_value": dv,
                "success_rate": rate,
                "expected": expected,
                "status": status,
            }
        )
    return rows


def run_control_targets(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    for item in config.get("control_targets", []):
        bonus = float(item.get("bonus", 0))
        dv = float(item.get("difficulty_value", 0))
        rate = check_success_rate(bonus, dv)
        expected = parse_band(item.get("expected"))
        status = evaluate_band(rate, expected)
        rows.append(
            {
                "id": str(item.get("id", "unnamed_control")),
                "bonus": bonus,
                "difficulty_value": dv,
                "apply_rate": rate,
                "expected": expected,
                "status": status,
                "notes": str(item.get("notes", "")),
            }
        )
    return rows


def run_matchups(
    config: Dict[str, Any],
    *,
    trials: int,
    max_rounds: int,
    rng: random.Random,
) -> List[Dict[str, Any]]:
    statlines = config.get("statlines", {})
    if not isinstance(statlines, dict):
        raise ValueError("statlines must be a mapping in balance_targets.yml")

    rows = []
    for item in config.get("matchups", []):
        attacker_id = str(item.get("attacker"))
        defender_id = str(item.get("defender"))
        style = str(item.get("style", "melee"))
        cast_defense = str(item.get("cast_defense", "willpower"))
        attacker = statlines.get(attacker_id)
        defender = statlines.get(defender_id)
        if attacker is None or defender is None:
            raise ValueError(f"Unknown attacker/defender statline in matchup '{item.get('id', '?')}'")

        single = simulate_single_exchange(
            attacker,
            defender,
            style=style,
            trials=trials,
            rng=rng,
            cast_defense=cast_defense,
        )
        ttd = simulate_time_to_down(
            attacker,
            defender,
            style=style,
            trials=trials,
            max_rounds=max_rounds,
            rng=rng,
            cast_defense=cast_defense,
        )

        expected_cfg = item.get("expected", {}) if isinstance(item.get("expected"), dict) else {}
        hit_band = parse_band(expected_cfg.get("hit_rate"))
        rounds_band = parse_band(expected_cfg.get("rounds_to_down"))
        sp_band = parse_band(expected_cfg.get("sp_spend"))

        hit_status = evaluate_band(single["hit_rate"], hit_band)
        rounds_status = evaluate_band(ttd["avg_rounds_to_down"], rounds_band)
        sp_status = evaluate_band(ttd["avg_sp_spend"], sp_band)

        statuses = [s for s in (hit_status, rounds_status, sp_status) if s != "N/A"]
        overall = "PASS" if statuses and all(s == "PASS" for s in statuses) else "CHECK"
        if not statuses:
            overall = "N/A"

        rows.append(
            {
                "id": str(item.get("id", "unnamed_matchup")),
                "group": item.get("group"),
                "attacker": attacker_id,
                "defender": defender_id,
                "style": style,
                "cast_defense": cast_defense,
                "single": single,
                "ttd": ttd,
                "expected": {
                    "hit_rate": hit_band,
                    "rounds_to_down": rounds_band,
                    "sp_spend": sp_band,
                },
                "status": {
                    "hit_rate": hit_status,
                    "rounds_to_down": rounds_status,
                    "sp_spend": sp_status,
                    "overall": overall,
                },
            }
        )

    return rows


def summarize_firearm_gaps(matchups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for row in matchups:
        group = row.get("group")
        if not group:
            continue
        style = str(row.get("style", "")).lower()
        if style not in {"melee", "firearm"}:
            continue
        grouped.setdefault(str(group), {})[style] = row

    gaps = []
    for group, styles in grouped.items():
        if "melee" not in styles or "firearm" not in styles:
            continue
        melee = styles["melee"]["single"]["hit_rate"]
        firearm = styles["firearm"]["single"]["hit_rate"]
        gaps.append(
            {
                "group": group,
                "melee_hit_rate": melee,
                "firearm_hit_rate": firearm,
                "gap": firearm - melee,
            }
        )
    return gaps


def build_patch_recommendations(
    config: Dict[str, Any],
    matchup_rows: List[Dict[str, Any]],
    firearm_gaps: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    statlines = config.get("statlines", {})
    recs: List[Dict[str, Any]] = []
    priority = 1

    rounds_high_rows = [row for row in matchup_rows if row["status"]["rounds_to_down"] == "HIGH"]
    if rounds_high_rows:
        vitality_multipliers: List[float] = []
        dpr_multipliers: List[float] = []
        median_dr_values: List[float] = []
        hit_pass_count = 0
        affected = []

        for row in rounds_high_rows:
            expected_round_band = row["expected"]["rounds_to_down"]
            target_mid = band_midpoint(expected_round_band)
            current_rounds = float(row["ttd"]["avg_rounds_to_down"])
            defender_id = str(row["defender"])
            defender_statline = statlines.get(defender_id, {})
            defender_vitality = float(defender_statline.get("vitality", 0))
            defender_dr = float(defender_statline.get("damage_reduction", 0))
            dpr = float(row["single"]["dpr"])

            if row["status"]["hit_rate"] == "PASS":
                hit_pass_count += 1
            affected.append(str(row["id"]))
            median_dr_values.append(defender_dr)

            if target_mid and target_mid > 0 and current_rounds > 0:
                vitality_multipliers.append(target_mid / current_rounds)
            if target_mid and target_mid > 0 and defender_vitality > 0 and dpr > 0:
                required_dpr = defender_vitality / target_mid
                dpr_multipliers.append(required_dpr / dpr)

        hit_pass_ratio = hit_pass_count / len(rounds_high_rows)
        affected_text = ", ".join(sorted(affected))

        if vitality_multipliers and hit_pass_ratio >= 0.7:
            median_vit_mult = statistics.median(vitality_multipliers)
            reduction = max(0.0, min(0.50, 1.0 - median_vit_mult))
            if reduction >= 0.05:
                recs.append(
                    {
                        "priority": priority,
                        "knob": "Vitality",
                        "recommendation": f"Reduce defender Vitality baselines by about {reduction * 100:.0f}% for affected tiers.",
                        "rationale": "Hit rates are mostly in-band, but time-to-down is consistently high.",
                        "scope": affected_text,
                    }
                )
                priority += 1

        if dpr_multipliers and hit_pass_ratio >= 0.7:
            median_dpr_mult = statistics.median(dpr_multipliers)
            boost = max(0.0, min(1.50, median_dpr_mult - 1.0))
            if boost >= 0.08:
                recs.append(
                    {
                        "priority": priority,
                        "knob": "Damage Dice",
                        "recommendation": f"Increase base damage packages by about {boost * 100:.0f}% (or equivalent dice step-up).",
                        "rationale": "Current DPR is too low for target combat length.",
                        "scope": affected_text,
                    }
                )
                priority += 1

        if median_dr_values and statistics.median(median_dr_values) >= 1:
            recs.append(
                {
                    "priority": priority,
                    "knob": "Damage Reduction",
                    "recommendation": "Reduce defender damage reduction by 1 in affected peer tiers before larger systemic edits.",
                    "rationale": "Flat DR suppresses low/mid damage packets and inflates rounds-to-down.",
                    "scope": affected_text,
                }
            )
            priority += 1

    hit_low_rows = [row for row in matchup_rows if row["status"]["hit_rate"] == "LOW"]
    if hit_low_rows:
        recs.append(
            {
                "priority": priority,
                "knob": "Defense",
                "recommendation": "Lower target defense baselines by 1-2 points, or raise attacker hit bonuses by 1.",
                "rationale": "Hit rates are below configured floor.",
                "scope": ", ".join(sorted(str(row["id"]) for row in hit_low_rows)),
            }
        )
        priority += 1

    hit_high_rows = [row for row in matchup_rows if row["status"]["hit_rate"] == "HIGH"]
    if hit_high_rows:
        recs.append(
            {
                "priority": priority,
                "knob": "Defense",
                "recommendation": "Raise target defense baselines by 1-2 points, or lower attacker hit bonuses by 1.",
                "rationale": "Hit rates are above configured ceiling.",
                "scope": ", ".join(sorted(str(row["id"]) for row in hit_high_rows)),
            }
        )
        priority += 1

    sp_high_rows = [row for row in matchup_rows if row["status"]["sp_spend"] == "HIGH"]
    if sp_high_rows:
        recs.append(
            {
                "priority": priority,
                "knob": "Spirituality Cost",
                "recommendation": "Reduce `sp_per_cast` by 1 for long-fight casting profiles, or increase cast damage efficiency.",
                "rationale": "Average SP spend exceeds target budget in cast matchups.",
                "scope": ", ".join(sorted(str(row["id"]) for row in sp_high_rows)),
            }
        )
        priority += 1

    gap_limit_raw = config.get("global_targets", {}).get("firearm_hit_gap_max_without_quick_dodge")
    if gap_limit_raw is not None:
        gap_limit = float(gap_limit_raw)
        high_gap_rows = [row for row in firearm_gaps if row["gap"] > gap_limit]
        if high_gap_rows:
            recs.append(
                {
                    "priority": priority,
                    "knob": "Defense",
                    "recommendation": "Tighten firearm-vs-defense interaction (Armor contribution, Quick Dodge gating, or firearm bonuses).",
                    "rationale": "Firearm hit-rate gap exceeds configured maximum.",
                    "scope": ", ".join(sorted(str(row["group"]) for row in high_gap_rows)),
                }
            )
            priority += 1

    if not recs:
        recs.append(
            {
                "priority": 1,
                "knob": "None",
                "recommendation": "No automatic patch flags. Current simulation outputs are within configured targets.",
                "rationale": "No out-of-band metrics were detected.",
                "scope": "global",
            }
        )
    return recs


def render_markdown(
    *,
    config: Dict[str, Any],
    check_rows: List[Dict[str, Any]],
    control_rows: List[Dict[str, Any]],
    matchup_rows: List[Dict[str, Any]],
    firearm_gaps: List[Dict[str, Any]],
    recommendations: List[Dict[str, Any]],
    trials: int,
    max_rounds: int,
) -> str:
    lines: List[str] = []
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines.append("# Core Combat Simulation Report")
    lines.append("")
    lines.append(f"- Generated (UTC): `{timestamp}`")
    lines.append(f"- Trials per simulation: **{trials}**")
    lines.append(f"- Max rounds per encounter trial: **{max_rounds}**")
    lines.append("")

    assumptions = config.get("assumptions", {})
    if assumptions:
        lines.append("## Assumptions")
        for key, value in assumptions.items():
            lines.append(f"- {key}: `{value}`")
        lines.append("")

    lines.append("## Check Targets")
    if not check_rows:
        lines.append("- No check targets configured.")
    else:
        lines.append("| ID | Bonus | DV | Success Rate | Target Band | Status |")
        lines.append("|---|---:|---:|---:|---|---|")
        for row in check_rows:
            lines.append(
                "| {id} | {bonus:.1f} | {dv:.1f} | {rate:.1f}% | {band} | {status} |".format(
                    id=row["id"],
                    bonus=row["bonus"],
                    dv=row["difficulty_value"],
                    rate=row["success_rate"] * 100.0,
                    band=format_band(row["expected"], percent=True),
                    status=row["status"],
                )
            )
    lines.append("")

    lines.append("## Control Targets")
    if not control_rows:
        lines.append("- No control targets configured.")
    else:
        lines.append("| ID | Bonus | DV | Apply Rate | Target Band | Status |")
        lines.append("|---|---:|---:|---:|---|---|")
        for row in control_rows:
            lines.append(
                "| {id} | {bonus:.1f} | {dv:.1f} | {rate:.1f}% | {band} | {status} |".format(
                    id=row["id"],
                    bonus=row["bonus"],
                    dv=row["difficulty_value"],
                    rate=row["apply_rate"] * 100.0,
                    band=format_band(row["expected"], percent=True),
                    status=row["status"],
                )
            )
        if any(row.get("notes") for row in control_rows):
            lines.append("")
            for row in control_rows:
                notes = row.get("notes")
                if notes:
                    lines.append(f"- `{row['id']}`: {notes}")
    lines.append("")

    lines.append("## Matchups")
    if not matchup_rows:
        lines.append("- No matchups configured.")
    else:
        lines.append(
            "| ID | Style | Hit % | Crit % | DPR | Avg Dmg/Hit | Avg Rounds | P90 Rounds | Avg SP | Timeout % | Result |"
        )
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
        for row in matchup_rows:
            single = row["single"]
            ttd = row["ttd"]
            lines.append(
                "| {id} | {style} | {hit:.1f}% | {crit:.1f}% | {dpr:.2f} | {dph:.2f} | {avg_r:.2f} | {p90:.2f} | {sp:.2f} | {timeout:.1f}% | {result} |".format(
                    id=row["id"],
                    style=row["style"],
                    hit=single["hit_rate"] * 100.0,
                    crit=single["crit_rate"] * 100.0,
                    dpr=single["dpr"],
                    dph=single["avg_damage_on_hit"],
                    avg_r=ttd["avg_rounds_to_down"],
                    p90=ttd["p90_rounds_to_down"],
                    sp=ttd["avg_sp_spend"],
                    timeout=ttd["timeout_rate"] * 100.0,
                    result=row["status"]["overall"],
                )
            )

        lines.append("")
        lines.append("### Matchup Target Checks")
        lines.append("| ID | Hit Target | Hit Status | Rounds Target | Rounds Status | SP Target | SP Status |")
        lines.append("|---|---|---|---|---|---|---|")
        for row in matchup_rows:
            lines.append(
                "| {id} | {hit_target} | {hit_status} | {rounds_target} | {rounds_status} | {sp_target} | {sp_status} |".format(
                    id=row["id"],
                    hit_target=format_band(row["expected"]["hit_rate"], percent=True),
                    hit_status=row["status"]["hit_rate"],
                    rounds_target=format_band(row["expected"]["rounds_to_down"]),
                    rounds_status=row["status"]["rounds_to_down"],
                    sp_target=format_band(row["expected"]["sp_spend"]),
                    sp_status=row["status"]["sp_spend"],
                )
            )
    lines.append("")

    lines.append("## Firearm Gap Check")
    if not firearm_gaps:
        lines.append("- No paired melee/firearm groups configured.")
    else:
        gap_limit = config.get("global_targets", {}).get("firearm_hit_gap_max_without_quick_dodge")
        lines.append("| Group | Melee Hit % | Firearm Hit % | Gap | Target Max | Status |")
        lines.append("|---|---:|---:|---:|---:|---|")
        for row in firearm_gaps:
            target_max = float(gap_limit) if gap_limit is not None else None
            status = "N/A" if target_max is None else ("PASS" if row["gap"] <= target_max else "HIGH")
            lines.append(
                "| {group} | {melee:.1f}% | {firearm:.1f}% | {gap:.1f}% | {target} | {status} |".format(
                    group=row["group"],
                    melee=row["melee_hit_rate"] * 100.0,
                    firearm=row["firearm_hit_rate"] * 100.0,
                    gap=row["gap"] * 100.0,
                    target=f"{target_max * 100.0:.1f}%" if target_max is not None else "-",
                    status=status,
                )
            )
    lines.append("")

    lines.append("## Recommended Patch Set")
    if not recommendations:
        lines.append("- No recommendations generated.")
    else:
        lines.append("| Priority | Knob | Recommendation | Rationale | Scope |")
        lines.append("|---:|---|---|---|---|")
        for rec in sorted(recommendations, key=lambda item: int(item.get("priority", 999))):
            lines.append(
                "| {priority} | {knob} | {recommendation} | {rationale} | {scope} |".format(
                    priority=rec.get("priority", "-"),
                    knob=str(rec.get("knob", "")).replace("|", "/"),
                    recommendation=str(rec.get("recommendation", "")).replace("|", "/"),
                    rationale=str(rec.get("rationale", "")).replace("|", "/"),
                    scope=str(rec.get("scope", "")).replace("|", "/"),
                )
            )
    lines.append("")

    lines.append("## Notes")
    lines.append("- `Result=CHECK` means at least one configured target band was out of range.")
    lines.append("- Timeout indicates trials where the defender was still standing after max rounds.")
    return "\n".join(lines).rstrip() + "\n"


def json_ready(value: Any) -> Any:
    if isinstance(value, Band):
        return {"min": value.minimum, "max": value.maximum}
    if isinstance(value, dict):
        return {k: json_ready(v) for k, v in value.items()}
    if isinstance(value, list):
        return [json_ready(v) for v in value]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Run core combat Monte Carlo balance checks.")
    parser.add_argument("--repo", default=".", help="Repo root path (default: current directory).")
    parser.add_argument("--targets", default=DEFAULT_TARGETS, help=f"Balance target YAML path (default: {DEFAULT_TARGETS}).")
    parser.add_argument("--out", default=DEFAULT_OUT, help=f"Markdown report output path (default: {DEFAULT_OUT}).")
    parser.add_argument("--trials", type=int, default=20000, help="Trials per simulation (default: 20000).")
    parser.add_argument("--max-rounds", type=int, default=30, help="Max rounds per encounter trial before timeout (default: 30).")
    parser.add_argument("--seed", type=int, default=20260220, help="Random seed for reproducibility.")
    parser.add_argument(
        "--json",
        nargs="?",
        const="",
        help="Write JSON output. Optionally provide a path; if omitted, writes next to --out with .json suffix.",
    )
    args = parser.parse_args()

    if args.trials <= 0:
        raise SystemExit("ERROR: --trials must be > 0")
    if args.max_rounds <= 0:
        raise SystemExit("ERROR: --max-rounds must be > 0")

    repo = Path(args.repo).resolve()
    targets_path = resolve_under_repo(repo, args.targets)
    out_path = resolve_under_repo(repo, args.out)
    config = load_yaml(targets_path)

    rng = random.Random(args.seed)
    check_rows = run_check_targets(config)
    control_rows = run_control_targets(config)
    matchup_rows = run_matchups(
        config,
        trials=args.trials,
        max_rounds=args.max_rounds,
        rng=rng,
    )
    firearm_gaps = summarize_firearm_gaps(matchup_rows)
    recommendations = build_patch_recommendations(config, matchup_rows, firearm_gaps)

    markdown = render_markdown(
        config=config,
        check_rows=check_rows,
        control_rows=control_rows,
        matchup_rows=matchup_rows,
        firearm_gaps=firearm_gaps,
        recommendations=recommendations,
        trials=args.trials,
        max_rounds=args.max_rounds,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")

    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "seed": args.seed,
        "trials": args.trials,
        "max_rounds": args.max_rounds,
        "targets_path": str(targets_path),
        "check_targets": json_ready(check_rows),
        "control_targets": json_ready(control_rows),
        "matchups": json_ready(matchup_rows),
        "firearm_gaps": json_ready(firearm_gaps),
        "recommended_patch_set": json_ready(recommendations),
    }

    if args.json is not None:
        if args.json == "":
            json_path = out_path.with_suffix(".json")
        else:
            json_path = resolve_under_repo(repo, args.json)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Wrote JSON report: {json_path}")

    print(f"Wrote markdown report: {out_path}")
    print(f"Matchups simulated: {len(matchup_rows)}")
    print(f"Checks simulated: {len(check_rows)}")
    print(f"Control targets simulated: {len(control_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
