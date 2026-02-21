# Manual YAML Review - Round 12

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/fate/seq-02.md`
- `draft/sequences/fate/seq-03.md`
- `draft/sequences/fate/seq-04.md`
- `draft/sequences/fate/seq-05.md`
- `draft/sequences/fate/seq-06.md`
- `draft/sequences/fate/seq-07.md`
- `draft/sequences/fate/seq-08.md`
- `draft/sequences/fate/seq-09.md`

## Primary Goals
- Close all Fate `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition).
- Add DV and table scaling where prose provides breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Fate dice mappings:
  - `fate-seq-02-prophet`
  - `fate-seq-03-chaos-walker`
  - `fate-seq-03-destiny-disturb-the-torrent-of-fate`
  - `fate-seq-04-disaster-field`
  - `fate-seq-04-misfortune`
  - `fate-seq-05-accumulate-luck`
  - `fate-seq-05-luck`
  - `fate-seq-05-luck-grant`
  - `fate-seq-06-disasters`
  - `fate-seq-06-spiritual-storm`
  - `fate-seq-07-luck`
  - `fate-seq-08-anti-divination`
  - `fate-seq-08-calculation`
  - `fate-seq-08-divination`
  - `fate-seq-09-premonition-of-danger`
  - `fate-seq-09-spiritual-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `fate-seq-03-chaos-walker` -> `spirituality: 5`
  - `fate-seq-03-destiny-disturb-the-torrent-of-fate` -> `spirituality: 10`
  - `fate-seq-04-misfortune` -> `spirituality: 8` (variable luck spend noted)
  - `fate-seq-04-disaster-field` -> `spirituality: 4`
  - `fate-seq-05-luck-grant` -> `spirituality: 3`
  - `fate-seq-06-disasters` -> `spirituality: 3` (active cost)
  - `fate-seq-06-spiritual-storm` -> `spirituality: 3`
  - `fate-seq-08-divination` -> `spirituality: 3`
  - `fate-seq-08-anti-divination` -> `spirituality: 3`
  - `fate-seq-09-spiritual-vision` -> `spirituality: 1` upkeep

- Resolved roll/opposition mismatches:
  - `fate-seq-09-premonition-of-danger` -> `opposed_by: difficulty_value` (DV 20 Intuition test)

- Added scaling for DV tiers and table rolls:
  - Prophet DV tiers and critical outcomes
  - Fate divination DV tiers, clue bonus, and higher-sequence default failure
  - Luck tables and special good luck triggers
  - Disasters timing and damage branches
  - Spiritual Vision bonus while active

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Fate pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 81`
  - `total_abilities: 199`
