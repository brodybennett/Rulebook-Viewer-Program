# Manual YAML Review - Round 2

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/fool/seq-04.md`
- `draft/sequences/fool/seq-05.md`
- `draft/sequences/fool/seq-06.md`

## Method Applied
- Read prose first, then edited YAML fields manually.
- Added roll mappings only when a check is explicitly present or strongly implied by the same ability line.
- Added `scaling` entries for explicit range/tolerance/progression breakpoints.
- Corrected type/action for passive rule bundles that were previously modeled as active casts.

## Changes Applied
- Added/adapted contested roll mapping:
  - `fool-seq-05-manipulate-ethereal-threads`
  - `fool-seq-04-spirit-body-thread-control`

- Corrected passive/toggle modeling:
  - `fool-seq-06-instant-recognition-and-recall` -> `type: passive`, `action: none`
  - `fool-seq-06-other-extraordinary-ability-improvements` -> `type: passive`, `action: none`
  - `fool-seq-04-psychic-connection` -> `type: passive`, `action: none`
  - `fool-seq-04-spirit-worm-principles-and-loss` -> `type: passive`, `action: none`
  - `fool-seq-05-spiritual-thread-vision` -> `type: toggle`, `action: free`

- Added progression/scaling entries from prose:
  - `fool-seq-05-spiritual-thread-vision` (100m -> 120m -> 200m -> 300m by digestion)
  - `fool-seq-05-manipulate-ethereal-threads` (tiered success thresholds, bloodbath reduction, digestion reductions)
  - `fool-seq-06-metamorphosis` (height limit increase after full digestion/promotion)
  - `fool-seq-06-other-extraordinary-ability-improvements` (cross-ability upgrades)
  - `fool-seq-04-exchange-positions` (1km -> 5km at Sequence 3)
  - `fool-seq-04-spirit-worm-principles-and-loss` (loss thresholds/tolerance breakpoints)

- Normalized targeting/range/duration where prose was explicit:
  - `fool-seq-04-endow-marionette-with-extraordinary-abilities`
  - `fool-seq-04-psychic-connection`
  - `fool-seq-06-metamorphosis`

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: global report still contains legacy balance findings; Fool-specific dice-mapping misses reduced.

## Remaining Fool Dice-Mapping Flags (from power audit)
- `fool-seq-07-flame-jump`
- `fool-seq-07-turn-paper-into-soldiers`
- `fool-seq-09-divination`
- `fool-seq-09-spiritual-vision`
