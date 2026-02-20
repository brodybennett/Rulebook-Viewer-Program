#!/usr/bin/env python3
"""
refactor_sequences_schema.py

Batch-refactor sequence markdown files into the Phase 3 schema format:
- normalize front matter
- normalize Advancement / Extraordinary Abilities sections
- enforce Attribute Gain section
- embed yaml ability blocks under each ability heading
- impute sparse high-sequence content with lore-themed placeholders
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import yaml

DEFAULT_COMPENDIUM = "dist/compendium.json"
DEFAULT_CONTENT_ROOT = "draft/sequences"
DEFAULT_CANON_PATHWAYS = "meta/canon_pathways.yml"
DEFAULT_CANON_SEQUENCES = "meta/canon_sequences.yml"

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+(.+?)\s*$")
ANCHOR_SUFFIX_RE = re.compile(r"\s+\{#[^}]+\}\s*$")
FENCE_START_RE = re.compile(r"^\s*```(?:yaml|yml)\s+ability\s*$", re.IGNORECASE)
FENCE_END_RE = re.compile(r"^\s*```\s*$")
ATTRIBUTE_LABEL_RE = re.compile(r"\*\*\s*attribute\s+gain\s*:\s*\*\*", re.IGNORECASE)
METER_RANGE_RE = re.compile(r"^\s*(\d{1,4})\s*m\s*$", re.IGNORECASE)

# Lore motifs are summarized from LoTM Wiki pathway overview/abilities pages.
IMPUTED_LIMIT_TEXT = "Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed."

IMPUTED_ABILITY_LIBRARY: Dict[str, List[Dict[str, Any]]] = {
    "abyss": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["offense", "debuff", "control"],
            "text": "You embody abyssal depravity and corruption, turning malice, filth, and curse-laden intent into constant supernatural pressure.",
        },
        {
            "name_template": "Corruption Bloom",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "constitution_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["debuff", "offense", "control"],
            "text": "You plant abyssal corruption in body and spirit, degrading resistance and making later curse effects harder to purge.",
        },
        {
            "name_template": "Profane Curse Weave",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "willpower_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["debuff", "control", "offense"],
            "text": "You layer conditional curses that punish movement, betrayal, or reckless action until the target breaks the bind.",
        },
    ],
    "black-emperor": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["control", "debuff", "utility"],
            "text": "You radiate imperial disorder, twisting rules and institutions so authority and exploitation become tools of your will.",
        },
        {
            "name_template": "Disorder Edict",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["control", "debuff", "utility"],
            "text": "You issue contradictory imperial decrees that warp normal behavior and force targets into exploitable legal and social traps.",
        },
        {
            "name_template": "Resurrection Through Order",
            "type": "reaction",
            "action": "none",
            "cost": {"spirituality": 5},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["defense", "utility", "buff"],
            "text": "When slain within your established order, you anchor to your own rules and attempt a temporary imperial reconstitution.",
        },
    ],
    "death": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["summon", "control", "debuff"],
            "text": "You embody death authority and river-like underworld law, granting natural command over spirits, corpses, and endings.",
        },
        {
            "name_template": "Underworld Command",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["summon", "control", "utility"],
            "text": "You issue death-path commands to spirits and undead, suppressing rebellion and redirecting lower entities to your chosen task.",
        },
        {
            "name_template": "River of Death",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "constitution_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["offense", "debuff", "control"],
            "text": "You invoke underworld chill and grave pressure, numbing vitality while inviting nearby dead spirits to converge on the target.",
        },
    ],
    "demoness": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["debuff", "control", "social"],
            "text": "You embody calamity-tinted charm and cursecraft, blending seduction, deceit, and misfortune into a single supernatural style.",
        },
        {
            "name_template": "Mirror Transit",
            "type": "active",
            "action": "move",
            "cost": {"spirituality": 2},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["mobility", "stealth", "utility"],
            "text": "You traverse adjacent reflections to reposition and evade pursuit, using mirror pathways as short-range movement channels.",
        },
        {
            "name_template": "Calamity Hex",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "willpower_defense",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["debuff", "control", "offense"],
            "text": "You stamp a target with Demoness misfortune, biasing outcomes toward errors, social collapse, and escalating disaster.",
        },
    ],
    "earth": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["healing", "buff", "utility"],
            "text": "You carry maternal life authority, accelerating growth, recovery, and biological resilience in natural and living systems.",
        },
        {
            "name_template": "Life Weaving",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "none",
            "range": "touch",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["healing", "buff", "utility"],
            "text": "You weave life force through flesh and roots, restoring injuries and stabilizing allies against decay and poison effects.",
        },
        {
            "name_template": "Flesh and Flora Shaping",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "constitution_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["control", "healing", "offense"],
            "text": "You force abrupt growth or mutation in organisms and plant matter, creating restraining biomass or restorative biological channels.",
        },
    ],
    "fate": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["divination", "control", "utility"],
            "text": "You align with fate threads and luck currents, sensing probability turns and nudging outcomes toward chosen trajectories.",
        },
        {
            "name_template": "Luck Weaving",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "none",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["buff", "debuff", "control"],
            "text": "You redistribute good and bad luck across nearby actors, advantaging allies while drawing misfortune toward enemies.",
        },
        {
            "name_template": "Destiny Premonition",
            "type": "reaction",
            "action": "none",
            "cost": {"spirituality": 1},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["divination", "utility", "defense"],
            "text": "A brief future-sight flashes before danger resolves, letting you react to imminent threats and choose a safer line.",
        },
    ],
    "hanged-man": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["offense", "debuff", "control"],
            "text": "You command shadowed corruption and flesh mutation, channeling sacrificial power through unstable yet forceful transformations.",
        },
        {
            "name_template": "Shadow Mutation",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "constitution_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["offense", "debuff", "control"],
            "text": "You trigger rapid mutation in shadow-touched flesh, reducing combat efficiency while exposing exploitable monstrous weaknesses.",
        },
        {
            "name_template": "Sacrificial Exchange",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["control", "debuff", "utility"],
            "text": "You invoke symbolic sacrifice to transfer harm, burden, or corruption between linked targets according to occult equivalence.",
        },
    ],
    "moon": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["healing", "summon", "buff"],
            "text": "You attune to moonlight vitality and bloodline influence, supporting regeneration, summons, and nocturnal growth effects.",
        },
        {
            "name_template": "Moonlit Regeneration",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "none",
            "range": "touch",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["healing", "buff", "utility"],
            "text": "You bathe a target in moonlit essence, speeding tissue recovery, blood stabilization, and resistance to corrosive effects.",
        },
        {
            "name_template": "Bloodline Summoning",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "none",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["summon", "control", "offense"],
            "text": "You call blood-affinitive entities or spirit-beasts and bind them through lineage resonance to support your current objective.",
        },
    ],
    "mutant": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["debuff", "defense", "control"],
            "text": "You channel chained curse authority, balancing madness suppression against violent transformation and spirit-flesh instability.",
        },
        {
            "name_template": "Chain of Reason",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["control", "debuff", "defense"],
            "text": "You bind a target's mental state with suppressive chain marks, dampening frenzy spikes and limiting extreme actions.",
        },
        {
            "name_template": "Cursed Metamorphosis",
            "type": "toggle",
            "action": "free",
            "cost": {"spirituality": 1},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "sustained",
            "tags": ["buff", "offense", "defense"],
            "text": "You assume a chained monstrous form, gaining physical threat at the cost of tighter sanity and control requirements.",
        },
    ],
    "mystery-pryer": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["utility", "divination", "offense"],
            "text": "You hold broad occult scholarship authority, integrating hidden formulas, arcane correspondences, and practical spell logic.",
        },
        {
            "name_template": "Spell Formula Projection",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["offense", "utility", "divination"],
            "text": "You externalize learned spell formulas as structured arcane attacks, combining analysis precision with direct mystic impact.",
        },
        {
            "name_template": "Occult Appraisal",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 1},
            "opposed_by": "difficulty_value",
            "range": "self",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["divination", "detection", "utility"],
            "text": "You rapidly appraise hidden properties, ritual traces, and mystical vulnerabilities by applying Hermit-path analytical frameworks.",
        },
    ],
    "night": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["stealth", "control", "debuff"],
            "text": "You embody darkness and dream authority, masking presence while letting fear, slumber, and concealment spread naturally.",
        },
        {
            "name_template": "Dream Infiltration",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["control", "debuff", "stealth"],
            "text": "You drag a target's awareness toward a dreamlike state, disrupting judgment and opening them to nightmare suggestion.",
        },
        {
            "name_template": "Night Veil",
            "type": "toggle",
            "action": "free",
            "cost": {"spirituality": 1},
            "opposed_by": "none",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "sustained",
            "tags": ["stealth", "defense", "control"],
            "text": "You spread layered darkness that obscures movement and weakens hostile perception while allies operate under your concealment.",
        },
    ],
    "paragon": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["utility", "buff", "defense"],
            "text": "You command civilization-level analysis and craftsmanship logic, allowing rapid optimization of tools, tactics, and systems.",
        },
        {
            "name_template": "Total Appraisal",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 1},
            "opposed_by": "difficulty_value",
            "range": "self",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["detection", "utility", "buff"],
            "text": "You instantly appraise structure, function, and flaws in artifacts, mechanisms, or formations to expose practical exploit points.",
        },
        {
            "name_template": "Civilization Construct",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 3},
            "opposed_by": "none",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["defense", "utility", "offense"],
            "text": "You manifest a temporary engineered construct or framework that supports allied action and constrains enemy movement lanes.",
        },
    ],
    "reader": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["utility", "divination", "buff"],
            "text": "You hold White Tower style cognitive authority, reconstructing truth from fragments and rapidly assimilating hidden knowledge.",
        },
        {
            "name_template": "Thought Reconstruction",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "line of sight",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["divination", "utility", "detection"],
            "text": "You rebuild a target's likely intent chain from micro-signals, exposing lies, hesitation points, and exploitable reasoning gaps.",
        },
        {
            "name_template": "Knowledge Cascade",
            "type": "toggle",
            "action": "free",
            "cost": {"spirituality": 1},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "sustained",
            "tags": ["buff", "utility", "divination"],
            "text": "You enter a high-load calculation state that boosts analysis and ritual interpretation while steadily consuming mental resources.",
        },
    ],
    "red-priest": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["offense", "control", "buff"],
            "text": "You embody war authority, converting conflict momentum into personal strength, command pressure, and battlefield initiative.",
        },
        {
            "name_template": "War Provocation",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "willpower_defense",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["control", "debuff", "social"],
            "text": "You ignite hostility and tunnel vision in enemies, forcing poor tactical choices and destabilizing coordinated formations.",
        },
        {
            "name_template": "Flame Command",
            "type": "active",
            "action": "attack",
            "cost": {"spirituality": 3},
            "opposed_by": "physical_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["offense", "control", "buff"],
            "text": "You direct battlefield fire like a general's blade, striking priority targets and shaping movement through heat and fear.",
        },
    ],
    "sun": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["offense", "healing", "buff"],
            "text": "You channel solar holiness and purification authority, burning corruption while stabilizing allies under radiant order.",
        },
        {
            "name_template": "Purifying Radiance",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "constitution_defense",
            "range": "30m",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["offense", "healing", "buff"],
            "text": "You release concentrated sunlight that harms tainted entities and strips hostile curse residue from protected allies.",
        },
        {
            "name_template": "Holy Covenant",
            "type": "active",
            "action": "cast",
            "cost": {"spirituality": 2},
            "opposed_by": "none",
            "range": "touch",
            "target": "designated target(s)",
            "duration": "1 encounter",
            "tags": ["buff", "defense", "utility"],
            "text": "You establish a sacred contract that strengthens resolve and punishes clear oath-breaking under your witnessed light.",
        },
    ],
    "war-god": [
        {
            "name_template": "{seq_name} Authority",
            "type": "passive",
            "action": "none",
            "cost": {},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "instant",
            "tags": ["offense", "defense", "buff"],
            "text": "You assert giant war authority with dawn and twilight symbolism, gaining overwhelming martial pressure and protective momentum.",
        },
        {
            "name_template": "Giant Battle Form",
            "type": "toggle",
            "action": "free",
            "cost": {"spirituality": 1},
            "opposed_by": "none",
            "range": "self",
            "target": "self",
            "duration": "sustained",
            "tags": ["offense", "defense", "buff"],
            "text": "You invoke giant physiology traits, increasing reach and durability while drawing enemy focus to your frontline presence.",
        },
        {
            "name_template": "Dawn-Twilight Strike",
            "type": "active",
            "action": "attack",
            "cost": {"spirituality": 3},
            "opposed_by": "physical_defense",
            "range": "20m",
            "target": "designated target(s)",
            "duration": "instant",
            "tags": ["offense", "control", "buff"],
            "text": "You deliver a colossal strike carrying alternating dawn and dusk force that staggers defenses and opens space for allies.",
        },
    ],
}


@dataclass
class HSection:
    title: str
    key: str
    start: int
    end: int


@dataclass
class H3Section:
    title: str
    key: str
    start: int
    end: int


def ascii_clean(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", str(text))
    cleaned = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", cleaned).strip()


def norm_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", ascii_clean(text).lower()).strip()


def slugify(text: str) -> str:
    raw = ascii_clean(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", raw).strip("-")
    return slug or "ability"


def split_front_matter(text: str) -> Tuple[Dict[str, Any], List[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, lines

    raw = "\n".join(lines[1:end])
    parsed = yaml.safe_load(raw) if raw.strip() else {}
    if not isinstance(parsed, dict):
        parsed = {}
    return parsed, lines[end + 1 :]


def render_front_matter(data: Dict[str, Any]) -> List[str]:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=False).strip()
    return ["---", *text.splitlines(), "---", ""]


def parse_h2_sections(lines: Sequence[str]) -> List[HSection]:
    idxs: List[Tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = H2_RE.match(line.strip())
        if m:
            idxs.append((i, ANCHOR_SUFFIX_RE.sub("", m.group(1)).strip()))
    out: List[HSection] = []
    for j, (start, title) in enumerate(idxs):
        end = idxs[j + 1][0] if j + 1 < len(idxs) else len(lines)
        out.append(HSection(title=title, key=norm_key(title), start=start, end=end))
    return out


def parse_h3_sections(lines: Sequence[str], start: int, end: int) -> List[H3Section]:
    idxs: List[Tuple[int, str]] = []
    for i in range(start + 1, end):
        m = H3_RE.match(lines[i].strip())
        if m:
            idxs.append((i, ANCHOR_SUFFIX_RE.sub("", m.group(1)).strip()))
    out: List[H3Section] = []
    for j, (s, title) in enumerate(idxs):
        e = idxs[j + 1][0] if j + 1 < len(idxs) else end
        out.append(H3Section(title=title, key=norm_key(title), start=s, end=e))
    return out


def find_h2(sections: Sequence[HSection], needle: str) -> Optional[HSection]:
    n = norm_key(needle)
    for sec in sections:
        if n in sec.key:
            return sec
    return None


def ensure_h1(lines: List[str], canonical_pathway: str, sequence_num: int) -> List[str]:
    for i, line in enumerate(lines):
        if H2_RE.match(line.strip()):
            break
        if H1_RE.match(line.strip()):
            lines[i] = f"# {canonical_pathway} Pathway: Sequence {sequence_num}"
            return lines
    insert_at = 0
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1
    lines[insert_at:insert_at] = [f"# {canonical_pathway} Pathway: Sequence {sequence_num}", ""]
    return lines


def ensure_h2_sequence_name(lines: List[str], sequence_name: str) -> List[str]:
    sections = parse_h2_sections(lines)
    if not sections:
        lines.append(f"## {sequence_name}")
        lines.append("")
        return lines
    first = sections[0]
    if any(k in first.key for k in ("advancement", "extraordinary", "notes")):
        lines[first.start:first.start] = [f"## {sequence_name}", ""]
    else:
        lines[first.start] = f"## {sequence_name}"
    return lines

def build_advancement_block() -> List[str]:
    return [
        "## Advancement",
        "",
        "### Main Materials",
        "",
        "- **Main Materials:** TBD.",
        "",
        "### Auxiliary Materials",
        "",
        "- **Auxiliary Materials:** TBD.",
        "",
        "### Advancement Ritual",
        "",
        "- **Advancement Ritual:** TBD.",
        "",
    ]


def format_attribute_gain(payload: Dict[str, Any]) -> List[str]:
    attrs = payload.get("attributes") if isinstance(payload.get("attributes"), list) else []
    skills = payload.get("skills") if isinstance(payload.get("skills"), list) else []

    out = ["### Attribute Gain", ""]
    if attrs:
        chunks = [f"{a.get('name', 'Unknown')} {a.get('delta', 0):+d}" for a in attrs if isinstance(a, dict)]
        out.append(f"- **Attribute Gain:** {'; '.join(chunks)}")
    else:
        out.append("- **Attribute Gain:** Not explicitly specified in source (schema placeholder).")

    if skills:
        chunks = [f"{s.get('name', 'Unknown')} +{int(s.get('delta', 0))} level" for s in skills if isinstance(s, dict)]
        out.append(f"- **Skill Gain:** {'; '.join(chunks)}")
    out.append("")
    return out


def ability_payload(a: Dict[str, Any], pathway: str, seq_num: int, fallback_name: str) -> Dict[str, Any]:
    name = ascii_clean(a.get("name") or fallback_name)
    aid = str(a.get("id") or "").strip().lower()
    if not aid:
        aid = f"{pathway}-seq-{seq_num:02d}-{slugify(name)}"

    payload = {
        "id": re.sub(r"[^a-z0-9\-]+", "-", aid).strip("-"),
        "name": name,
        "pathway": pathway,
        "sequence": int(seq_num),
        "type": str(a.get("type") or "active").strip().lower(),
        "action": str(a.get("action") or "cast").strip().lower(),
        "cost": a.get("cost") if isinstance(a.get("cost"), dict) else {},
        "roll": a.get("roll") if isinstance(a.get("roll"), str) else None,
        "opposed_by": str(a.get("opposed_by") or "none").strip().lower(),
        "range": ascii_clean(a.get("range") or "self"),
        "target": ascii_clean(a.get("target") or "self"),
        "duration": ascii_clean(a.get("duration") or "instant"),
        "scaling": a.get("scaling") if isinstance(a.get("scaling"), list) else [],
        "tags": [str(t).strip().lower() for t in (a.get("tags") or ["utility"]) if str(t).strip()],
        "text": ascii_clean(a.get("text") or f"{name} ability details are retained in section prose."),
    }
    if not payload["tags"]:
        payload["tags"] = ["utility"]
    return payload


def render_yaml_ability(payload: Dict[str, Any]) -> List[str]:
    ordered = {
        "id": payload["id"],
        "name": payload["name"],
        "pathway": payload["pathway"],
        "sequence": payload["sequence"],
        "type": payload["type"],
        "action": payload["action"],
        "cost": payload["cost"],
        "roll": payload["roll"],
        "opposed_by": payload["opposed_by"],
        "range": payload["range"],
        "target": payload["target"],
        "duration": payload["duration"],
        "scaling": payload["scaling"],
        "tags": payload["tags"],
        "text": payload["text"],
    }
    body = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=False).strip()
    return ["```yaml ability", *body.splitlines(), "```"]


def is_attribute_h3(h3: H3Section, lines: Sequence[str]) -> bool:
    if "attribute" in h3.key and ("gain" in h3.key or "enhancement" in h3.key):
        return True
    for raw in lines[h3.start + 1 : h3.end]:
        if ATTRIBUTE_LABEL_RE.search(raw):
            return True
    return False


def replace_or_insert_yaml(lines: List[str], h3: H3Section, yaml_lines: List[str]) -> List[str]:
    insert_at = h3.start + 1
    while insert_at < h3.end and not lines[insert_at].strip():
        insert_at += 1

    if insert_at < h3.end and FENCE_START_RE.match(lines[insert_at]):
        j = insert_at + 1
        while j < h3.end and not FENCE_END_RE.match(lines[j]):
            j += 1
        if j < h3.end:
            j += 1
        lines[insert_at:j] = [*yaml_lines, ""]
        return lines

    lines[insert_at:insert_at] = [*yaml_lines, ""]
    return lines


def ensure_effect_limits(lines: List[str], h3: H3Section, text: str, imputed: bool) -> List[str]:
    block = [x.strip().lower() for x in lines[h3.start + 1 : h3.end] if x.strip()]
    has_effect = any(x.startswith("- **effect:**") for x in block)
    has_limits = any(x.startswith("- **limits:**") for x in block)

    add: List[str] = []
    if not has_effect:
        add.append(f"- **Effect:** {text}")
    if not has_limits:
        if imputed:
            add.append(f"- **Limits:** {IMPUTED_LIMIT_TEXT}")
        else:
            add.append("- **Limits:** As described in this section's prose.")

    if add:
        insert_at = h3.end
        while insert_at > h3.start and not lines[insert_at - 1].strip():
            insert_at -= 1
        lines[insert_at:insert_at] = ["", *add, ""]
    return lines


def is_sparse_imputed_ability(ability: Dict[str, Any]) -> bool:
    src = ability.get("_source") if isinstance(ability.get("_source"), dict) else {}
    if src.get("imputed"):
        return True

    text = ascii_clean(ability.get("text") or "").lower()
    if text.startswith("imputed lore baseline:"):
        return True
    if "imputed placeholder ability because source sequence lacks explicit extraordinary ability content" in text:
        return True
    return False


def scale_meter_range(raw_range: str, delta: int) -> str:
    m = METER_RANGE_RE.match(str(raw_range or "").strip())
    if not m:
        return ascii_clean(raw_range or "self")
    meters = max(1, int(m.group(1)) + int(delta))
    return f"{meters}m"


def tune_imputed_payload_for_sequence(payload: Dict[str, Any], seq_num: int) -> Dict[str, Any]:
    tuned = dict(payload)
    ability_type = str(tuned.get("type") or "").strip().lower()
    action = str(tuned.get("action") or "").strip().lower()
    cost = tuned.get("cost") if isinstance(tuned.get("cost"), dict) else {}
    range_text = ascii_clean(tuned.get("range") or "self")

    if ability_type == "active" and action == "cast":
        if seq_num == 2:
            tuned["action"] = "full-round"
        elif seq_num == 0:
            tuned["action"] = "swift"

    spirit = cost.get("spirituality")
    if isinstance(spirit, (int, float)) and spirit > 0:
        if seq_num == 2:
            spirit = spirit + 1
        elif seq_num == 0:
            spirit = max(1, spirit - 1)
        cost = dict(cost)
        if isinstance(spirit, float) and abs(spirit - round(spirit)) < 1e-9:
            spirit = int(round(spirit))
        cost["spirituality"] = spirit
        tuned["cost"] = cost

    if seq_num == 1 and METER_RANGE_RE.match(range_text):
        tuned["range"] = scale_meter_range(range_text, 10)
    elif seq_num == 0 and METER_RANGE_RE.match(range_text):
        tuned["range"] = scale_meter_range(range_text, 20)

    return tuned


def build_imputed_payloads(pathway: str, seq_name: str, seq_num: int) -> List[Dict[str, Any]]:
    templates = IMPUTED_ABILITY_LIBRARY.get(pathway)
    if not templates:
        templates = [
            {
                "name_template": "{seq_name} Authority",
                "type": "passive",
                "action": "none",
                "cost": {},
                "opposed_by": "none",
                "range": "self",
                "target": "self",
                "duration": "instant",
                "tags": ["utility", "control", "buff"],
                "text": "You manifest the pathway's core authority as a stable baseline for narrative and mechanical refinement.",
            },
            {
                "name_template": "Domain Suppression",
                "type": "active",
                "action": "cast",
                "cost": {"spirituality": 2},
                "opposed_by": "willpower_defense",
                "range": "line of sight",
                "target": "designated target(s)",
                "duration": "1 encounter",
                "tags": ["control", "debuff", "utility"],
                "text": "You project your pathway domain to suppress hostile actions and impose thematic constraints on opponents.",
            },
            {
                "name_template": "Domain Manifestation",
                "type": "active",
                "action": "cast",
                "cost": {"spirituality": 3},
                "opposed_by": "none",
                "range": "20m",
                "target": "designated target(s)",
                "duration": "sustained",
                "tags": ["buff", "offense", "defense"],
                "text": "You externalize pathway authority as a short-lived manifestation that supports allies and pressures enemies.",
            },
        ]

    out: List[Dict[str, Any]] = []
    seen_ids: Dict[str, int] = defaultdict(int)
    for template in templates:
        name_template = str(template.get("name_template") or "{seq_name} Authority")
        name = ascii_clean(name_template.format(seq_name=seq_name)).strip() or f"{seq_name} Authority"
        aid = f"{pathway}-seq-{seq_num:02d}-{slugify(name)}"
        seen_ids[aid] += 1
        if seen_ids[aid] > 1:
            aid = f"{aid}-{seen_ids[aid]}"

        tags = [str(t).strip().lower() for t in template.get("tags", []) if str(t).strip()]
        if not tags:
            tags = ["utility"]

        payload = {
                "id": aid,
                "name": name,
                "pathway": pathway,
                "sequence": int(seq_num),
                "type": str(template.get("type") or "active").strip().lower(),
                "action": str(template.get("action") or "cast").strip().lower(),
                "cost": template.get("cost") if isinstance(template.get("cost"), dict) else {},
                "roll": template.get("roll") if isinstance(template.get("roll"), str) else None,
                "opposed_by": str(template.get("opposed_by") or "none").strip().lower(),
                "range": ascii_clean(template.get("range") or "self"),
                "target": ascii_clean(template.get("target") or "self"),
                "duration": ascii_clean(template.get("duration") or "instant"),
                "scaling": template.get("scaling") if isinstance(template.get("scaling"), list) else [],
                "tags": tags,
                "text": ascii_clean(template.get("text") or f"{name} imputed lore baseline."),
                "_source": {
                    "heading": name,
                    "imputed": True,
                },
            }
        if seq_num in {0, 1, 2}:
            payload = tune_imputed_payload_for_sequence(payload, seq_num)
        out.append(payload)
    return out


def should_expand_imputed_sequence(abilities: List[Dict[str, Any]]) -> bool:
    if not abilities:
        return True
    flags = [is_sparse_imputed_ability(a) for a in abilities if isinstance(a, dict)]
    return bool(flags) and all(flags)


def build_imputed_extraordinary_section(
    *,
    attr_payload: Dict[str, Any],
    imputed_payloads: List[Dict[str, Any]],
) -> List[str]:
    block: List[str] = ["## Extraordinary Abilities", ""]
    block.extend(format_attribute_gain(attr_payload))
    for payload in imputed_payloads:
        block.extend(
            [
                f"### {payload['name']}",
                "",
                *render_yaml_ability(payload),
                "",
                f"- **Effect:** {payload['text']}",
                f"- **Limits:** {IMPUTED_LIMIT_TEXT}",
                "",
            ]
        )
    return block


def impute_lore_for_sparse(pathway: str, seq_name: str, seq_num: int, ability: Dict[str, Any]) -> Dict[str, Any]:
    imputed = build_imputed_payloads(pathway, seq_name, seq_num)
    if not imputed:
        return ability
    payload = imputed[0]
    ability.update(
        {
            "id": payload["id"],
            "name": payload["name"],
            "type": payload["type"],
            "action": payload["action"],
            "cost": payload["cost"],
            "roll": payload["roll"],
            "opposed_by": payload["opposed_by"],
            "range": payload["range"],
            "target": payload["target"],
            "duration": payload["duration"],
            "scaling": payload["scaling"],
            "tags": payload["tags"],
            "text": payload["text"],
        }
    )
    return ability


def ensure_sections(lines: List[str]) -> List[str]:
    sections = parse_h2_sections(lines)
    adv = find_h2(sections, "advancement")
    ex = find_h2(sections, "extraordinary abilities")

    if adv is None:
        idx = ex.start if ex else len(lines)
        lines[idx:idx] = build_advancement_block()

    sections = parse_h2_sections(lines)
    adv = find_h2(sections, "advancement")
    ex = find_h2(sections, "extraordinary abilities")

    if ex is None:
        lines.extend(["## Extraordinary Abilities", ""])

    sections = parse_h2_sections(lines)
    adv = find_h2(sections, "advancement")
    ex = find_h2(sections, "extraordinary abilities")

    if adv and ex and adv.start > ex.start:
        adv_block = lines[adv.start:adv.end]
        ex_block = lines[ex.start:ex.end]
        prefix = lines[:ex.start]
        between = lines[ex.end:adv.start]
        suffix = lines[adv.end:]
        lines = prefix + adv_block + [""] + between + ex_block + suffix

    sections = parse_h2_sections(lines)
    for sec in sections:
        if "advancement" in sec.key:
            lines[sec.start] = "## Advancement"
        if "extraordinary" in sec.key and "abilities" in sec.key:
            lines[sec.start] = "## Extraordinary Abilities"
    return lines

def refactor_file(
    *,
    repo: Path,
    rec: Dict[str, Any],
    canon_pathways: Dict[str, str],
) -> Tuple[bool, str]:
    rel = rec.get("file")
    if not isinstance(rel, str) or not rel.strip():
        return False, "missing file path in compendium record"
    path = repo / rel
    if not path.exists():
        return False, f"file not found: {rel}"

    text = path.read_text(encoding="utf-8", errors="replace")
    front_matter, body = split_front_matter(text)

    pathway = str(rec.get("pathway") or path.parent.name).strip().lower()
    seq_num = int(rec.get("sequence") or 0)
    seq_name = ascii_clean(rec.get("sequence_name") or f"Sequence {seq_num}")
    seq_id = f"{pathway}-seq-{seq_num:02d}"
    canonical_pathway = ascii_clean(rec.get("canonical_pathway") or canon_pathways.get(pathway, pathway.title()))

    # Front matter normalization.
    fm = dict(front_matter)
    fm["title"] = f"Sequence {seq_num}: {seq_name}"
    fm["id"] = seq_id
    fm["tags"] = [f"pathway:{pathway}", f"sequence:{seq_num}"]

    lines = list(body)
    lines = ensure_h1(lines, canonical_pathway, seq_num)
    lines = ensure_h2_sequence_name(lines, seq_name)
    lines = ensure_sections(lines)

    sections = parse_h2_sections(lines)
    ex = find_h2(sections, "extraordinary abilities")
    if not ex:
        return False, f"failed to create extraordinary section: {rel}"

    raw_abilities = rec.get("abilities") if isinstance(rec.get("abilities"), list) else []
    abilities = [a for a in raw_abilities if isinstance(a, dict)]
    has_imputed_limit_marker = IMPUTED_LIMIT_TEXT in text
    expand_imputed = should_expand_imputed_sequence(abilities) or has_imputed_limit_marker
    attr_payload = rec.get("attribute_gain") if isinstance(rec.get("attribute_gain"), dict) else {}

    # Ensure Attribute Gain section first inside Extraordinary.
    h3 = parse_h3_sections(lines, ex.start, ex.end)
    attr_h3 = None
    for h in h3:
        if is_attribute_h3(h, lines):
            attr_h3 = h
            break

    if attr_h3 is None:
        insert_at = ex.start + 1
        while insert_at < ex.end and lines[insert_at].strip():
            insert_at += 1
        lines[insert_at:insert_at] = format_attribute_gain(attr_payload)
    else:
        lines[attr_h3.start] = "### Attribute Gain"

    # Re-parse h3 after potential insertion/rename.
    sections = parse_h2_sections(lines)
    ex = find_h2(sections, "extraordinary abilities")
    h3 = parse_h3_sections(lines, ex.start, ex.end)

    if expand_imputed:
        imputed_payloads = build_imputed_payloads(pathway, seq_name, seq_num)
        lines[ex.start:ex.end] = build_imputed_extraordinary_section(
            attr_payload=attr_payload,
            imputed_payloads=imputed_payloads,
        )

        final_lines = [*render_front_matter(fm), *lines]
        while final_lines and not final_lines[-1].strip():
            final_lines.pop()
        final_text = "\n".join(final_lines) + "\n"

        if final_text != text:
            path.write_text(final_text, encoding="utf-8", newline="\n")
            return True, rel
        return False, rel

    non_attr = [h for h in h3 if not is_attribute_h3(h, lines)]

    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    unmatched: List[Dict[str, Any]] = []
    for ability in abilities:
        if not isinstance(ability, dict):
            continue
        src = ability.get("_source") if isinstance(ability.get("_source"), dict) else {}
        key = norm_key(src.get("heading") or ability.get("name") or "")
        if key:
            buckets[key].append(ability)
        else:
            unmatched.append(ability)

    # Inject/replace YAML for existing headings from bottom to top.
    for h in sorted(non_attr, key=lambda x: x.start, reverse=True):
        key = norm_key(h.title)
        ability = buckets[key].pop(0) if buckets.get(key) else None
        if ability is None:
            ability = {}
        payload = ability_payload(ability, pathway, seq_num, fallback_name=h.title)

        src = ability.get("_source") if isinstance(ability, dict) and isinstance(ability.get("_source"), dict) else {}
        if src.get("imputed"):
            payload = impute_lore_for_sparse(pathway, seq_name, seq_num, payload)

        yaml_lines = render_yaml_ability(payload)
        lines = replace_or_insert_yaml(lines, h, yaml_lines)

    # Reparse after yaml insertion.
    sections = parse_h2_sections(lines)
    ex = find_h2(sections, "extraordinary abilities")
    h3 = parse_h3_sections(lines, ex.start, ex.end)
    non_attr = [h for h in h3 if not is_attribute_h3(h, lines)]

    # Add effect/limits bullets if missing.
    for h in sorted(non_attr, key=lambda x: x.start, reverse=True):
        key = norm_key(h.title)
        ability = None
        if buckets.get(key):
            ability = buckets[key][0]
        imputed = False
        text_hint = ""
        if isinstance(ability, dict):
            src = ability.get("_source") if isinstance(ability.get("_source"), dict) else {}
            imputed = bool(src.get("imputed"))
            text_hint = ascii_clean(ability.get("text") or "")
        if not text_hint:
            text_hint = f"{ascii_clean(h.title)} resolves using its yaml ability block and section prose."
        lines = ensure_effect_limits(lines, h, text_hint, imputed)

    # Append unmatched/imputed abilities when no heading exists.
    sections = parse_h2_sections(lines)
    ex = find_h2(sections, "extraordinary abilities")
    h3 = parse_h3_sections(lines, ex.start, ex.end)
    existing_keys = {norm_key(h.title) for h in h3}

    remaining = list(unmatched)
    for vals in buckets.values():
        remaining.extend(vals)

    append_at = ex.end
    while append_at > ex.start and not lines[append_at - 1].strip():
        append_at -= 1

    for ability in remaining:
        if not isinstance(ability, dict):
            continue
        src = ability.get("_source") if isinstance(ability.get("_source"), dict) else {}
        fallback_heading = ascii_clean(src.get("heading") or ability.get("name") or f"{seq_name} Authority")
        key = norm_key(fallback_heading)
        if key in existing_keys:
            continue

        payload = ability_payload(ability, pathway, seq_num, fallback_name=fallback_heading)
        if src.get("imputed") or rec.get("sections", {}).get("imputed_extraordinary_abilities"):
            payload = impute_lore_for_sparse(pathway, seq_name, seq_num, payload)

        block = [
            f"### {payload['name']}",
            "",
            *render_yaml_ability(payload),
            "",
            f"- **Effect:** {payload['text']}",
            f"- **Limits:** {IMPUTED_LIMIT_TEXT}",
            "",
        ]
        lines[append_at:append_at] = block
        append_at += len(block)
        existing_keys.add(key)

    final_lines = [*render_front_matter(fm), *lines]
    while final_lines and not final_lines[-1].strip():
        final_lines.pop()
    final_text = "\n".join(final_lines) + "\n"

    if final_text != text:
        path.write_text(final_text, encoding="utf-8", newline="\n")
        return True, rel
    return False, rel


def load_canon_pathways(path: Path) -> Dict[str, str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8", errors="replace"))
    out: Dict[str, str] = {}
    if isinstance(data, dict) and isinstance(data.get("pathways"), list):
        for item in data["pathways"]:
            if not isinstance(item, dict):
                continue
            slug = str(item.get("slug") or "").strip().lower()
            if slug:
                out[slug] = ascii_clean(item.get("canonical") or slug.title())
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Refactor sequence markdown files into schema-ready structure.")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument("--compendium", default=DEFAULT_COMPENDIUM, help=f"Compendium JSON path (default: {DEFAULT_COMPENDIUM})")
    parser.add_argument("--content-root", default=DEFAULT_CONTENT_ROOT, help=f"Sequence content root (default: {DEFAULT_CONTENT_ROOT})")
    parser.add_argument("--canon-pathways", default=DEFAULT_CANON_PATHWAYS, help=f"Canonical pathways file (default: {DEFAULT_CANON_PATHWAYS})")
    parser.add_argument("--canon-sequences", default=DEFAULT_CANON_SEQUENCES, help=f"Canonical sequences file (default: {DEFAULT_CANON_SEQUENCES})")
    parser.add_argument("--pathway", action="append", default=[], help="Optional pathway filter (repeatable)")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    compendium_path = repo / args.compendium
    canon_pathways_path = repo / args.canon_pathways

    if not compendium_path.exists():
        print(f"ERROR: missing compendium file: {compendium_path}")
        return 2
    if not canon_pathways_path.exists():
        print(f"ERROR: missing canonical pathways file: {canon_pathways_path}")
        return 2

    comp = json.loads(compendium_path.read_text(encoding="utf-8", errors="replace"))
    sequences = comp.get("sequences") if isinstance(comp, dict) else None
    if not isinstance(sequences, list):
        print("ERROR: compendium root missing sequences[]")
        return 2

    canon_pathways = load_canon_pathways(canon_pathways_path)
    filter_set = {p.strip().lower() for p in args.pathway if p.strip()}

    changed = 0
    scanned = 0
    failures: List[str] = []

    for rec in sequences:
        if not isinstance(rec, dict):
            continue
        pathway = str(rec.get("pathway") or "").strip().lower()
        if filter_set and pathway not in filter_set:
            continue
        scanned += 1
        try:
            did_change, msg = refactor_file(repo=repo, rec=rec, canon_pathways=canon_pathways)
            if did_change:
                changed += 1
        except Exception as exc:
            failures.append(f"{rec.get('file', '<unknown>')}: {exc}")

    print("Schema refactor complete")
    print(f"repo: {repo}")
    print(f"scanned: {scanned}")
    print(f"changed: {changed}")
    print(f"failures: {len(failures)}")
    for line in failures[:50]:
        print(f"  - {line}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
