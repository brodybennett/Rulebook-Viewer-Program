# Manual YAML Review - Round 5

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/apprentice/seq-00.md`
- `draft/sequences/apprentice/seq-01.md`
- `draft/sequences/apprentice/seq-02.md`
- `draft/sequences/apprentice/seq-03.md`
- `draft/sequences/apprentice/seq-04.md`
- `draft/sequences/apprentice/seq-05.md`
- `draft/sequences/apprentice/seq-06.md`
- `draft/sequences/apprentice/seq-07.md`
- `draft/sequences/apprentice/seq-08.md`
- `draft/sequences/apprentice/seq-09.md`

## Primary Goals
- Close all Apprentice `dice_mapping_missing` findings.
- Correct explicit prose/YAML mismatches (cost/type/action/duration) where the prose is clear.
- Add explicit scaling breakpoints where the prose defines mode or tier changes.

## Manual Changes Applied
- Added/normalized structured dice mapping for all Apprentice queue-flagged abilities:
  - `apprentice-seq-00-conceptualization`
  - `apprentice-seq-01-gate`
  - `apprentice-seq-03-tolerate-the-environment`
  - `apprentice-seq-05-invisible-hand`
  - `apprentice-seq-06-record`
  - `apprentice-seq-07-premonition-of-danger`
  - `apprentice-seq-08-spells`
  - `apprentice-seq-09-open-the-door`
  - `apprentice-seq-09-spiritual-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `apprentice-seq-00-void-collapse` -> `spirituality: 50`
  - `apprentice-seq-01-authority-locating` -> `spirituality: 3`
  - `apprentice-seq-01-gate` -> `spirituality: 5`
  - `apprentice-seq-01-spoon` -> `spirituality: 3`
  - `apprentice-seq-02-space-swap` -> `spirituality: 10`
  - `apprentice-seq-04-illusion` -> `spirituality: 10`
  - `apprentice-seq-04-space-hiding` -> `spirituality: 5`
  - `apprentice-seq-07-astrology` -> `spirituality: 2`
  - `apprentice-seq-09-open-the-door` -> `spirituality: 2` baseline, with peephole mode override in scaling
  - `apprentice-seq-09-spiritual-vision` -> `spirituality: 1` upkeep

- Type/action/duration normalization where prose indicated persistent, passive, reaction, or toggle behavior:
  - Passive conversions: `apprentice-seq-03-freedom-of-action`, `apprentice-seq-03-tolerate-the-environment`, `apprentice-seq-05-records`, `apprentice-seq-07-astrology-study-and-advancement`, `apprentice-seq-08-performance-recognition`, `apprentice-seq-09-ritual-mastery`
  - Reaction mapping: `apprentice-seq-07-premonition-of-danger`
  - Toggle/state mapping: `apprentice-seq-00-conceptualization`, `apprentice-seq-09-spiritual-vision`
  - Duration normalization for persistent doors/hidden-space effects and multi-round seals where explicitly stated.

- Added prose-backed scaling blocks for mode switches and level breakpoints:
  - `apprentice-seq-01-gate` (longer seals/lower-sequence conditions/Sequence 0 scope)
  - `apprentice-seq-02-concept-travel` (action economy by higher sequence)
  - `apprentice-seq-02-to-reproduce` (DV25/DV35 and half-effect conditions)
  - `apprentice-seq-05-traveler-s-gate` (long-distance travel vs short-distance flash mode)
  - `apprentice-seq-05-records` (capacity tiers)
  - `apprentice-seq-06-record` (DV adjustments by sequence difference)
  - `apprentice-seq-07-astrology` (divination DV tiers and anti-divination mode)
  - `apprentice-seq-07-premonition-of-danger` (DV gate, sequence improvements)
  - `apprentice-seq-08-spells` (mode-by-mode costs/effects)
  - `apprentice-seq-09-open-the-door` and `apprentice-seq-09-spiritual-vision` (mode/tier notes)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: global balance findings remain; Apprentice `dice_mapping_missing` entries are now zero.

## Queue Outcome
- Removed Apprentice pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals updated:
  - `total_sequences: 127`
  - `total_abilities: 288`
