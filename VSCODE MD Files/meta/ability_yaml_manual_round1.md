# Manual YAML Review - Round 1

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/fool/seq-07.md`
- `draft/sequences/fool/seq-08.md`
- `draft/sequences/fool/seq-01.md`

## Issues Found
- Missing `cost` values despite explicit prose costs.
- `roll`/`dice.*_roll` left null for abilities with explicit checks/damage.
- Empty `scaling` despite explicit multi-shot penalties or sequence progression breakpoints.
- Overly generic `dice.notes`.
- Action/type mismatches for passive/reactive abilities.

## Changes Applied
- Added/normalized explicit costs for:
  - `fool-seq-07-injury-transfer`
  - `fool-seq-07-flame-jump`
  - `fool-seq-07-manipulate-flames`
  - `fool-seq-07-air-bomb`
  - `fool-seq-07-paper-doll-substitute`
  - `fool-seq-07-illusion`
  - `fool-seq-07-false-breathing-underwater`
  - `fool-seq-07-turn-paper-into-soldiers`

- Added explicit rolls/dice mapping for:
  - `fool-seq-07-injury-transfer` (adapted conditional check)
  - `fool-seq-07-manipulate-flames`
  - `fool-seq-07-air-bomb`
  - `fool-seq-07-paper-doll-substitute` (anti-divination mode check)
  - `fool-seq-07-illusion` (contest-mapped check)
  - `fool-seq-07-bone-softening` (`effect_roll: 1d6`)
  - `fool-seq-08-premonition-of-danger`
  - `fool-seq-08-turn-paper-into-flying-knives` (adapted half-strength handling note)

- Added scaling rules for:
  - `fool-seq-07-injury-transfer`
  - `fool-seq-07-manipulate-flames`
  - `fool-seq-07-air-bomb`
  - `fool-seq-07-paper-doll-substitute`
  - `fool-seq-07-illusion`
  - `fool-seq-08-premonition-of-danger`
  - `fool-seq-08-turn-paper-into-flying-knives`

- Corrected reactive/passive modeling:
  - `fool-seq-08-premonition-of-danger` -> `type: reaction`, `action: none`
  - `fool-seq-08-muscle-mastery` -> `type: passive`, `action: none`
  - `fool-seq-07-magicianatms-performance-props` -> `type: passive`, `action: none`

- Improved non-roll `dice.notes` clarity in `fool-seq-01` abilities and updated `fool-seq-01-mysterious-realm` duration to sustained.

## Next Manual Batch Proposal
- Continue Fool Pathway in descending sequence order:
  1. `draft/sequences/fool/seq-06.md`
  2. `draft/sequences/fool/seq-05.md`
  3. `draft/sequences/fool/seq-04.md`

- Then repeat the same methodology pathway-by-pathway using `meta/dice_authoring_queue.md` ordering.
