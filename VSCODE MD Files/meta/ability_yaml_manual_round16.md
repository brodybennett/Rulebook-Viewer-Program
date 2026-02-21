# Manual YAML Review - Round 16

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/mystery-pryer/seq-02.md`
- `draft/sequences/mystery-pryer/seq-03.md`
- `draft/sequences/mystery-pryer/seq-04.md`
- `draft/sequences/mystery-pryer/seq-06.md`
- `draft/sequences/mystery-pryer/seq-07.md`
- `draft/sequences/mystery-pryer/seq-08.md`
- `draft/sequences/mystery-pryer/seq-09.md`

## Primary Goals
- Close all Mystery Pryer `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, passive traits).
- Add DV/scaling breakpoints where prose provides tiers.

## Manual Changes Applied
- Closed all queue-flagged Mystery Pryer dice mappings:
  - `mystery-pryer-seq-02-information-storm`
  - `mystery-pryer-seq-02-tampering`
  - `mystery-pryer-seq-03-prophecy`
  - `mystery-pryer-seq-04-mystery-peeping-eyes`
  - `mystery-pryer-seq-04-mythical-blood`
  - `mystery-pryer-seq-06-scroll-improvement`
  - `mystery-pryer-seq-07-knowledge-enhancement`
  - `mystery-pryer-seq-07-speed-word`
  - `mystery-pryer-seq-07-spellcaster`
  - `mystery-pryer-seq-08-fist-of-fighting`
  - `mystery-pryer-seq-09-curtain-peeping`
  - `mystery-pryer-seq-09-divination`
  - `mystery-pryer-seq-09-spiritual-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `mystery-pryer-seq-02-information-storm` -> `spirituality: 3`
  - `mystery-pryer-seq-04-mythical-blood` -> `spirituality: 3`
  - `mystery-pryer-seq-08-fist-of-fighting` -> `spirituality: 2`
  - `mystery-pryer-seq-09-divination` -> `spirituality: 2`
  - `mystery-pryer-seq-09-spiritual-vision` -> `spirituality: 1` per round

- Added roll mappings and scaling notes:
  - Knowledge/Occultism vs defense checks for Information Storm and Tampering
  - Prophecy DV tiers (15/20/25/30) with intuition appraisal
  - Mystery-Peeping Eyes detection check (DV 25) for qualified observers
  - Scroll Improvement occult check vs Willpower Defense; 1d2 maintenance duration; +1d10 option
  - Spellcaster baseline occult vs Physical Defense with 1d10 damage; Knowledge Enhancement variants for fireball/frost
  - Fist of Fighting uses Intuition for attack/strength bonus
  - Divination DV tiers and spiritual-vision bonus mapping

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Mystery Pryer pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 53`
  - `total_abilities: 118`
