# Manual YAML Review - Round 11

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/error/seq-02.md`
- `draft/sequences/error/seq-03.md`
- `draft/sequences/error/seq-04.md`
- `draft/sequences/error/seq-05.md`
- `draft/sequences/error/seq-06.md`
- `draft/sequences/error/seq-07.md`
- `draft/sequences/error/seq-08.md`
- `draft/sequences/error/seq-09.md`

## Primary Goals
- Close all Error `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (especially missing or incorrect costs).
- Add explicit mode and tier scaling where prose provides breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Error dice mappings:
  - `error-seq-02-destiny-trojan-horse`
  - `error-seq-02-detached-worm-of-time`
  - `error-seq-02-insight-of-destiny`
  - `error-seq-03-rules-of-deceit`
  - `error-seq-04-steal-flesh`
  - `error-seq-04-steal-sight`
  - `error-seq-04-steal-storage`
  - `error-seq-05-steal-memories`
  - `error-seq-06-stealing-tinder`
  - `error-seq-07-decryption`
  - `error-seq-07-premonition-of-danger`
  - `error-seq-08-charisma`
  - `error-seq-08-extraordinary-eloquence`
  - `error-seq-08-misleading-thinking`
  - `error-seq-09-spiritual-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `error-seq-02-destiny-trojan-horse` -> `spirituality: 3`
  - `error-seq-02-detached-worm-of-time` -> `spirituality: 1`
  - `error-seq-03-rules-of-deceit` -> `spirituality: 3`
  - `error-seq-05-steal-memories` -> `spirituality: 3`
  - `error-seq-06-stealing-tinder` -> `spirituality: 3`
  - `error-seq-07-decryption` -> `spirituality: 3`
  - `error-seq-08-extraordinary-eloquence` -> `spirituality: 2`
  - `error-seq-08-misleading-thinking` -> `spirituality: 2`
  - `error-seq-09-spiritual-vision` -> `spirituality: 1` upkeep

- Type/action/duration normalization where prose was explicit:
  - `error-seq-04-steal-storage` -> passive persistent package
  - `error-seq-07-premonition-of-danger` -> reaction trigger
  - `error-seq-08-charisma` -> passive persistent package
  - `error-seq-09-spiritual-vision` -> toggle sustained upkeep package

- Added prose-backed scaling blocks for explicit mode/tier conditions:
  - Trojan-horse option branches and fate grafting (`destiny-trojan-horse`)
  - worm evasion window notes (`detached-worm-of-time`)
  - Library-based appraisal option (`insight-of-destiny`)
  - encounter-to-hours duration roll (`rules-of-deceit`)
  - target recall DV (`steal-memories`)
  - range increase and clue bonuses (`stealing-tinder`)
  - DV tiers and investigation alternative (`decryption`)
  - social-skill variants (`extraordinary-eloquence`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Error pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 89`
  - `total_abilities: 215`
