# Manual YAML Review - Round 13

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/hanged-man/seq-01.md`
- `draft/sequences/hanged-man/seq-02.md`
- `draft/sequences/hanged-man/seq-04.md`
- `draft/sequences/hanged-man/seq-06.md`
- `draft/sequences/hanged-man/seq-07.md`
- `draft/sequences/hanged-man/seq-08.md`
- `draft/sequences/hanged-man/seq-09.md`

## Primary Goals
- Close all Hanged Man `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, passive traits).
- Add DV/table scaling where prose provides breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Hanged Man dice mappings:
  - `hanged-man-seq-01-corruption`
  - `hanged-man-seq-01-dark-angel`
  - `hanged-man-seq-02-evil-words`
  - `hanged-man-seq-04-blade-of-flesh`
  - `hanged-man-seq-04-shadow-armor`
  - `hanged-man-seq-06-bishop-rose-traits`
  - `hanged-man-seq-06-flesh-alteration`
  - `hanged-man-seq-06-flesh-bomb`
  - `hanged-man-seq-06-flesh-bullet`
  - `hanged-man-seq-06-flesh-cloak`
  - `hanged-man-seq-06-flesh-healing`
  - `hanged-man-seq-07-shadow-hide`
  - `hanged-man-seq-08-listen`
  - `hanged-man-seq-08-listening-perception`
  - `hanged-man-seq-09-filth-perception`
  - `hanged-man-seq-09-spiritual-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `hanged-man-seq-02-evil-words` -> `spirituality: 1` (self-blessing) with interception scaling to 5
  - `hanged-man-seq-06-flesh-cloak` -> `spirituality: 3`, `flesh_stack: 20`
  - `hanged-man-seq-06-flesh-bomb` -> `blood: 5` (thrown), planted scaling notes
  - `hanged-man-seq-06-flesh-bullet` -> `flesh_stack: 2`
  - `hanged-man-seq-06-flesh-healing` -> `spirituality: 3`, `flesh_stack: 20`
  - `hanged-man-seq-07-shadow-hide` -> `sanity: 2`
  - `hanged-man-seq-08-listen` -> `spirituality: 2`
  - `hanged-man-seq-09-spiritual-vision` -> `spirituality: 1` upkeep

- Added roll mappings and scaling notes:
  - Corruption mysticism check (Intuition + Occultism) vs Willpower Defense with -8 penalty
  - Dark Angel wing recovery d20 roll
  - Flesh Bomb throw check and damage rolls
  - Flesh Bullet attack roll and burst penalties
  - LISTEN DV 30 check with success/failure tables
  - Listening Perception DV 20 detection checks and sanity loss roll
  - Filth Perception sanity loss roll variants

- Normalized passive traits where prose is clearly always-on:
  - `hanged-man-seq-06-bishop-rose-traits`
  - `hanged-man-seq-08-listening-perception`
  - `hanged-man-seq-09-filth-perception`

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Hanged Man pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 74`
  - `total_abilities: 183`
