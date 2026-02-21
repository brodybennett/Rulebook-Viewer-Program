# Manual YAML Review - Round 20

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/red-priest/seq-02.md`
- `draft/sequences/red-priest/seq-04.md`
- `draft/sequences/red-priest/seq-05.md`
- `draft/sequences/red-priest/seq-06.md`
- `draft/sequences/red-priest/seq-07.md`
- `draft/sequences/red-priest/seq-08.md`
- `draft/sequences/red-priest/seq-09.md`

## Primary Goals
- Close all Red Priest `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Map DV checks and bonus-damage dice into ability schema fields.

## Manual Changes Applied
- Closed all queue-flagged Red Priest dice mappings:
  - `red-priest-seq-02-celestial-alteration`
  - `red-priest-seq-02-freezing-ice`
  - `red-priest-seq-02-frost`
  - `red-priest-seq-04-steel`
  - `red-priest-seq-04-flame`
  - `red-priest-seq-04-iron-blooded-army`
  - `red-priest-seq-05-spot-weaknesses`
  - `red-priest-seq-05-harvest`
  - `red-priest-seq-06-insight`
  - `red-priest-seq-07-manipulation-of-fire`
  - `red-priest-seq-07-incarnation-of-blazing-spear`
  - `red-priest-seq-08-provoke`
  - `red-priest-seq-09-law-of-the-jungle`
  - `red-priest-seq-09-trap-making`

- Corrected explicit prose/YAML mismatches:
  - `red-priest-seq-02-celestial-alteration` -> `spirituality: 10`
  - `red-priest-seq-02-freezing-ice` -> `spirituality: 5`
  - `red-priest-seq-02-frost` -> `spirituality: 3`
  - `red-priest-seq-08-provoke` -> `spirituality: 2`

- Added roll mappings and dice notes:
  - Throwing vs Physical Defense for Frost (8d6 + STR bonus)
  - Target Dexterity tests for Freezing Ice
  - Bonus damage dice for Flame and Harvest
  - Detection appraisals for Spot Weaknesses and Insight
  - Mysticism vs Physical Defense for fire control suite; Fighting/Throwing for blazing spear
  - Trap crafting checks and typical damage payloads
  - Law of the Jungle DV skill checks captured in notes

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 23, warnings: 84); global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Red Priest pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 29`
  - `total_abilities: 77`
