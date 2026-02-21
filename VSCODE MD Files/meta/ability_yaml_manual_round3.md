# Manual YAML Review - Round 3

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/fool/seq-00.md`
- `draft/sequences/fool/seq-02.md`
- `draft/sequences/fool/seq-03.md`
- `draft/sequences/fool/seq-07.md`
- `draft/sequences/fool/seq-09.md`

## Focus
- Close all remaining Fool pathway dice-mapping gaps found by power audit.
- Correct explicit prose/YAML mismatches (cost, type/action, targeting, duration).
- Add scaling breakpoints when prose includes concrete thresholds.

## Manual Changes Applied
- Added adapted check mapping for:
  - `fool-seq-00-fooling`
  - `fool-seq-02-wish`
  - `fool-seq-03-summon-historical-images`
  - `fool-seq-03-paper-doll-stand`
  - `fool-seq-03-restoring-your-self`
  - `fool-seq-07-flame-jump`
  - `fool-seq-07-turn-paper-into-soldiers`
  - `fool-seq-09-divination`
  - `fool-seq-09-spiritual-vision`

- Corrected structural/type modeling:
  - `fool-seq-00-divine-gaze` -> reaction trigger model
  - `fool-seq-00-god-of-blindness-and-foolishness` -> passive/none
  - `fool-seq-00-aura-of-foolishness` -> toggle/free
  - `fool-seq-09-ritual-mastery` -> passive/none

- Fixed explicit prose mismatches:
  - `fool-seq-03-restoring-your-self` spirituality cost corrected to 15.
  - `fool-seq-03-paper-doll-stand` spirituality cost corrected to 8.
  - `fool-seq-02-influence-the-future` spirituality cost set to 5.
  - `fool-seq-09-divination` spirituality cost set to 2.
  - `fool-seq-09-spiritual-vision` upkeep spirituality cost set to 1.

- Added prose-driven scaling notes:
  - DV/result tiers and clue modifiers for divination.
  - Familiarity/cost/summon-limit breakpoints for historical summoning.
  - Sequence-upgrade behavior for Flame Jump and paper weapons.
  - Wish gating and per-target cadence constraints.

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: global legacy balance findings remain, but Fool dice-mapping misses are now zero.

## Outcome
- Fool pathway removed from `meta/dice_authoring_queue.md`.
- Remaining queue now starts from other pathways for next manual batch.
