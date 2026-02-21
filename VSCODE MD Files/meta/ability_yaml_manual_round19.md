# Manual YAML Review - Round 19

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/reader/seq-02.md`
- `draft/sequences/reader/seq-03.md`
- `draft/sequences/reader/seq-06.md`
- `draft/sequences/reader/seq-07.md`
- `draft/sequences/reader/seq-08.md`
- `draft/sequences/reader/seq-09.md`

## Primary Goals
- Close all Reader `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Map DV checks and passive bonuses into dice fields.

## Manual Changes Applied
- Closed all queue-flagged Reader dice mappings:
  - `reader-seq-02-wisdom-use`
  - `reader-seq-03-master-the-mysteries`
  - `reader-seq-06-analysis`
  - `reader-seq-06-simulation`
  - `reader-seq-07-fighting-skills`
  - `reader-seq-07-on-site-restoration`
  - `reader-seq-08-action-deduction`
  - `reader-seq-08-basic-deduction`
  - `reader-seq-08-thinking-intuition`
  - `reader-seq-09-spiritual-vision`

- Corrected explicit prose/YAML mismatches:
  - `reader-seq-02-wisdom-use` -> `spirituality: 5`
  - `reader-seq-09-spiritual-vision` -> `spirituality: 1` (per round)

- Added roll mappings and dice notes:
  - Education-based Knowledge checks for Analysis/Simulation with DV scaling notes
  - Investigation and Psychology appraisals for Basic/Action Deduction
  - Intuition appraisal DV thresholds for Thinking Intuition
  - +1d6 bonus damage for Fighting Skills and passive clue restoration notes
  - Passive effects captured as effect rolls where no base roll exists

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 23, warnings: 82); global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Reader pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 36`
  - `total_abilities: 91`
