# Manual YAML Review - Round 14

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/moon/seq-02.md`
- `draft/sequences/moon/seq-04.md`
- `draft/sequences/moon/seq-05.md`
- `draft/sequences/moon/seq-07.md`
- `draft/sequences/moon/seq-08.md`
- `draft/sequences/moon/seq-09.md`

## Primary Goals
- Close all Moon `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, passive traits).
- Add DV/table scaling where prose provides breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Moon dice mappings:
  - `moon-seq-02-bottom-level-improvement`
  - `moon-seq-02-creation-authority`
  - `moon-seq-02-life`
  - `moon-seq-04-illusionary-bat-swarm`
  - `moon-seq-04-moon-paper-man`
  - `moon-seq-05-moonlight`
  - `moon-seq-05-potion-effect-enhancement`
  - `moon-seq-05-summon-full-moon`
  - `moon-seq-07-extraordinary-regeneration`
  - `moon-seq-07-extraordinary-sense-of-smell`
  - `moon-seq-07-high-speed-movement`
  - `moon-seq-08-animal-senses`
  - `moon-seq-08-domesticated-animal-examples`
  - `moon-seq-09-chemicals`
  - `moon-seq-09-pharmaceutical-agents`
  - `moon-seq-09-pharmacy-preparation`

- Corrected explicit prose/YAML cost mismatches:
  - `moon-seq-02-creation-authority` -> `spirituality: 3`
  - `moon-seq-02-life` -> `spirituality: 15`
  - `moon-seq-02-bottom-level-improvement` -> `spirituality: 3`
  - `moon-seq-04-moon-paper-man` -> `spirituality: 1`
  - `moon-seq-05-summon-full-moon` -> `spirituality: 3`
  - `moon-seq-05-moonlight` -> `spirituality: 3` per round
  - `moon-seq-08-animal-senses` -> `spirituality: 3`

- Added roll mappings and scaling notes:
  - Biology checks and DV tiers for creature modification
  - Bat swarm attack/heal/recovery dice and spirituality scaling
  - Full moon temporary spirituality roll (1d6/2d6) and moon-knowledge bonuses
  - Moonlight reorganization heal roll (2d6)
  - Regeneration heal roll (1d6 -> 2d6 at Sequence 4)
  - Animal senses taming checks
  - Domesticated animal vitality tables
  - Pharmacy preparation time and restock rolls
  - Chemical throw checks and damage tables

- Normalized passive traits or reference tables:
  - `moon-seq-07-extraordinary-regeneration` -> passive package
  - `moon-seq-08-domesticated-animal-examples` -> passive reference table

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Moon pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 68`
  - `total_abilities: 167`
