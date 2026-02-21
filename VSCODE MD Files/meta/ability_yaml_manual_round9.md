# Manual YAML Review - Round 9

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/demoness/seq-01.md`
- `draft/sequences/demoness/seq-02.md`
- `draft/sequences/demoness/seq-03.md`
- `draft/sequences/demoness/seq-04.md`
- `draft/sequences/demoness/seq-05.md`
- `draft/sequences/demoness/seq-06.md`
- `draft/sequences/demoness/seq-07.md`
- `draft/sequences/demoness/seq-08.md`
- `draft/sequences/demoness/seq-09.md`

## Primary Goals
- Close all Demoness `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (especially missing or incorrect costs).
- Add explicit mode and sequence-tier scaling where prose provides hard breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Demoness dice mappings:
  - `demoness-seq-01-doomsday`
  - `demoness-seq-02-cataclysm-wreaks`
  - `demoness-seq-03-extraordinary-lifespan`
  - `demoness-seq-06-primordial-cocoon`
  - `demoness-seq-06-touch-of-pleasure`
  - `demoness-seq-06-web-creation`
  - `demoness-seq-07-black-flame`
  - `demoness-seq-07-frost-mastery`
  - `demoness-seq-08-charisma-cha`
  - `demoness-seq-08-cognitive-misleading`
  - `demoness-seq-08-intensification-of-persuasion`
  - `demoness-seq-09-assassination-action`
  - `demoness-seq-09-poised-burst`
  - `demoness-seq-09-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `demoness-seq-01-doomsday` -> `spirituality: 15`
  - `demoness-seq-02-cataclysm-wreaks` -> `spirituality: 6`
  - `demoness-seq-03-extraordinary-lifespan` -> removed unsupported `vitality: 10`
  - `demoness-seq-04-mirror-illusion` -> `spirituality: 3`
  - `demoness-seq-05-frost-control` -> `spirituality: 4`
  - `demoness-seq-06-web-creation` -> `spirituality: 3`
  - `demoness-seq-06-primordial-cocoon` -> `spirituality: 6`
  - `demoness-seq-07-curse` -> `spirituality: 3`
  - `demoness-seq-07-black-flame` -> `spirituality: 2` baseline remote mode
  - `demoness-seq-07-frost-mastery` -> `spirituality: 2` baseline long-range mode
  - `demoness-seq-07-invisibility` -> `spirituality: 1`
  - `demoness-seq-09-poised-burst` -> `spirituality: 2`
  - `demoness-seq-09-vision` -> `spirituality: 1` upkeep

- Type/action/duration normalization where prose was explicit:
  - `demoness-seq-03-extraordinary-lifespan` -> passive persistent trait
  - `demoness-seq-06-primordial-cocoon` -> toggle sustained package
  - `demoness-seq-09-assassination-action` -> passive persistent package
  - `demoness-seq-09-vision` -> toggle sustained upkeep package

- Added prose-backed scaling blocks for explicit mode/tier conditions:
  - disaster mode branches (`cataclysm-wreaks`)
  - rebirth penalties (`extraordinary-lifespan`)
  - web burn/repair branches (`web-creation`)
  - joy/bind/deflect/long-duration branches (`touch-of-pleasure`)
  - cocoon layer and repair branches (`primordial-cocoon`)
  - ranged/melee/split combo + sequence upgrades (`black-flame`)
  - ranged/melee/area + sequence upgrades (`frost-mastery`)
  - social branch and loophole release conditions (`seq-08` social suite)
  - assassin burst and recovery windows (`poised-burst`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Demoness pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 103`
  - `total_abilities: 245`
