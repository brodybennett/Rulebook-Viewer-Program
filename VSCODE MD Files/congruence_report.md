# Congruence Audit Report

- Generated (UTC): `2026-02-16T15:43:57+00:00`
- Repo: `C:\Users\dan\Desktop\Personal\Projects\LoTM Rulebook\VSCODE MD Files`
- Content root: `draft`
- Markdown files scanned: **263**

## Summary

- High: **3**
- Medium: **1**
- Low: **93**

- High details:
  - Definition drift terms: **1**
  - Mechanic field drift blocks: **2**
- Medium details:
  - Heading collisions: **1**
- Low details:
  - `[[UNCLEAR: ...]]` markers: **0**
  - `[[LINK LATER: ...]]` markers: **0**
  - Unreferenced heading collisions: **93**

## High Severity

### Definition Drift (`**Term:** ...`)

#### Term: `Pathway` (6 occurrences, 4 variants)

- Variant (x3): `Earth Pathway.` (sample: `draft/sequences/earth/seq-02.md:11`)
- Variant (x1): `[[Red Priest Pathway]].` (sample: `draft/sequences/red-priest/seq-01.md:9`)
- Variant (x1): `[[Secret-Seeker Pathway]]` (sample: `draft/sequences/mystery-pryer/seq-05.md:11`)
- Variant (x1): `[[Visionary Pathway]].` (sample: `draft/sequences/visionary/seq-03.md:11`)
- Locations:
  - `draft/sequences/earth/seq-02.md:11` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/earth/seq-03.md:9` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/earth/seq-07.md:9` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/mystery-pryer/seq-05.md:11` - `- **Pathway:** [[Secret-Seeker Pathway]]`
  - `draft/sequences/red-priest/seq-01.md:9` - `**Pathway:** [[Red Priest Pathway]].`
  - `draft/sequences/visionary/seq-03.md:11` - `**Pathway:** [[Visionary Pathway]].`

### Mechanic Field Drift (repeated heading blocks)

#### Block Title: `Spiritual Vision` (10 occurrences)

- Field `**Cost:**` -> conflicting values (10/10 blocks have this field)
  - Variant (x9): `1 **spirituality point per round** while active.` (sample: `draft/sequences/apprentice/seq-09.md:60`)
  - Variant (x1): `Consuming 1 **spirituality point** per round.` (sample: `draft/sequences/red-priest/seq-09.md:188`)
- Field `**Use:**` -> conflicting values (10/10 blocks have this field)
  - Variant (x9): `1 **free action** to activate.` (sample: `draft/sequences/apprentice/seq-09.md:60`)
  - Variant (x1): `1 free action.` (sample: `draft/sequences/red-priest/seq-09.md:188`)
- Field `**Effect:**` -> conflicting values (10/10 blocks have this field)
  - Variant (x9): `While active, your vision gains the following benefits:` (sample: `draft/sequences/apprentice/seq-09.md:60`)
  - Variant (x1): `You activate Spiritual Vision, and your vision gains the following benefits:` (sample: `draft/sequences/red-priest/seq-09.md:188`)
- Locations:
  - `draft/sequences/apprentice/seq-09.md:60` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/earth/seq-09.md:137` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/error/seq-09.md:95` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/fate/seq-09.md:65` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/fool/seq-09.md:124` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/hanged-man/seq-09.md:40` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/mystery-pryer/seq-09.md:32` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/reader/seq-09.md:166` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/red-priest/seq-09.md:188` - `### Spiritual Vision` | Cost=Consuming 1 **spirituality point** per round., Use=1 free action., Effect=You activate Spiritual Vision, and your vision gains the following benefits:
  - `draft/sequences/visionary/seq-09.md:139` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:

#### Block Title: `Divine Gaze` (5 occurrences)

- Field `**Effect:**` -> conflicting values (5/5 blocks have this field)
  - Variant (x4): `You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.` (sample: `draft/sequences/apprentice/seq-00.md:43`)
  - Variant (x1): `You can gaze at the surroundings of that creature, and use extraordinary abilities that normally target an area to target that area (normal range limits still apply).` (sample: `draft/sequences/arbiter/seq-00.md:24`)
- Locations:
  - `draft/sequences/apprentice/seq-00.md:43` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/arbiter/seq-00.md:24` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use extraordinary abilities that normally target an area to target that area (normal range limits still apply).
  - `draft/sequences/fool/seq-00.md:32` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/moon/seq-00.md:15` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/visionary/seq-00.md:26` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.

## Medium Severity

### Heading Collisions

#### Heading: `Luck` (x2, linked 1x)

- Link references:
  - `draft/sequences/tyrant/seq-04.md:97` - `[[Luck]]`
- Heading locations:
- `draft/sequences/fate/seq-05.md:24` (h3, `# luck`) `### Luck`
- `draft/sequences/fate/seq-07.md:20` (h3, `# luck`) `### Luck`

## Low Severity

### `[[UNCLEAR: ...]]` Markers

- None found.

### `[[LINK LATER: ...]]` Markers

- None found.

### Unreferenced Heading Collisions

- These collisions currently have no plain `[[Title]]` references, so they are lower-priority unless you plan to link to them by title.
- `Extraordinary Abilities` (x198)
- `Attribute Gain` (x191)
- `Advancement` (x135)
- `Advancement Ritual` (x104)
- `Auxiliary Materials` (x38)
- `Main Materials` (x12)
- `Overview` (x12)
- `Spiritual Vision` (x11)
- `Description` (x10)
- `Acting Rules` (x7)
- `Ritual Mastery` (x7)
- `Spirit Vision` (x7)
- `Vision` (x6)
- `Divine Gaze` (x5)
- `Premonition of Danger` (x5)
- `Sequence 4` (x5)
- `Sequence abilities` (x5)
- `Sequence abilities (overview)` (x5)
- `Breeding Environment` (x4)
- `Common Items` (x4)
- `Full Moon Curse` (x4)
- `Sequence 2` (x4)
- `Abyss` (x3)
- `Acting` (x3)
- `Additional` (x3)
- `Basic Data` (x3)
- `Combat` (x3)
- `Divination` (x3)
- `Habits` (x3)
- `Insight` (x3)
- `Living Environment` (x3)
- `Quick Dodge` (x3)
- `Roleplay` (x3)
- `Sequence 1` (x3)
- `Sequence 3` (x3)
- `Sequence 6` (x3)
- `Taste` (x3)
- `Tyrant` (x3)
- `Visionary` (x3)
- `Anti-Divination` (x2)
- ... +53 more
