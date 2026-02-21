# Manual YAML Review - Round 17

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/night/seq-02.md`
- `draft/sequences/night/seq-04.md`
- `draft/sequences/night/seq-08.md`
- `draft/sequences/night/seq-09.md`

## Primary Goals
- Close all Night `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Add DV/scaling breakpoints where prose provides tiers.

## Manual Changes Applied
- Closed all queue-flagged Night dice mappings:
  - `night-seq-02-servant-of-concealment`
  - `night-seq-04-ethereal-mastery`
  - `night-seq-04-grasp-of-doom`
  - `night-seq-08-recite-poems`
  - `night-seq-09-premonition-of-danger`

- Corrected explicit prose/YAML mismatches:
  - `night-seq-04-grasp-of-doom` -> `spirituality: 5`
  - `night-seq-08-recite-poems` -> `spirituality: 3`, `action: cast`

- Added roll mappings and scaling notes:
  - Inspiration/Luck appraisal for Servant of Concealment (DV 20)
  - Grasp of Doom lucky check (DV 15, scaling to DV 20 at Sequence 2)
  - Ethereal Mastery +5d6 vs incorporeal targets
  - Recite Poems will-test and lucky-appraisal rolls with verse-specific DV notes
  - Premonition of Danger Intuition appraisal DV 15 with higher-sequence notes

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Night pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 48`
  - `total_abilities: 113`
