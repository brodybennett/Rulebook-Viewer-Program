# Manual YAML Review - Round 7

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/black-emperor/seq-00.md`
- `draft/sequences/black-emperor/seq-01.md`
- `draft/sequences/black-emperor/seq-02.md`
- `draft/sequences/black-emperor/seq-03.md`
- `draft/sequences/black-emperor/seq-04.md`
- `draft/sequences/black-emperor/seq-05.md`
- `draft/sequences/black-emperor/seq-06.md`
- `draft/sequences/black-emperor/seq-07.md`
- `draft/sequences/black-emperor/seq-08.md`
- `draft/sequences/black-emperor/seq-09.md`

## Primary Goals
- Close all Black Emperor `dice_mapping_missing` findings.
- Correct explicit prose and YAML mismatches (costs, passive and toggle state, duration).
- Add prose-backed scaling where explicit sequence or mode breakpoints are stated.

## Manual Changes Applied
- Corrected explicit prose and YAML costs:
  - `black-emperor-seq-04-chaotic-order` -> `spirituality: 5` (already adjusted in this pathway pass)
  - `black-emperor-seq-05-chaos` -> `spirituality: 2`
  - `black-emperor-seq-06-distortion` -> `spirituality: 3`
  - `black-emperor-seq-06-corrosion` -> `spirituality: 1` upkeep
  - `black-emperor-seq-07-bribe` -> `spirituality: 3`
  - `black-emperor-seq-09-vision` -> `spirituality: 1` upkeep

- Closed all queue-flagged dice mappings:
  - `black-emperor-seq-06-multiple-targets`
  - `black-emperor-seq-07-bribe`
  - `black-emperor-seq-08-law-of-wildness`
  - `black-emperor-seq-08-mental-resistance`
  - `black-emperor-seq-09-conversational-and-eloquent`
  - `black-emperor-seq-09-spotting-loopholes`
  - `black-emperor-seq-09-vision`

- Type/action/duration normalization where prose was explicit:
  - `black-emperor-seq-04-chaotic-order` -> casting baseline with conditional free-action follow-up
  - `black-emperor-seq-05-majesty` -> toggle sustained aura
  - `black-emperor-seq-06-corrosion` -> toggle sustained field
  - `black-emperor-seq-06-multiple-targets` -> passive persistent upgrade package
  - `black-emperor-seq-08-law-of-wildness` -> passive persistent package
  - `black-emperor-seq-08-mental-resistance` -> passive persistent package
  - `black-emperor-seq-09-conversational-and-eloquent` -> passive persistent package
  - `black-emperor-seq-09-vision` -> toggle sustained

- Added explicit scaling breakpoints from prose:
  - cast/free mode split (`chaotic-order`)
  - target sequence penalties and exemptions (`chaos`, `majesty`)
  - mode and sequence-conditional behavior (`multiple-targets`, `bribe`)
  - difficulty tier outcomes (`spotting-loopholes`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; report regenerated (non-zero global findings remain as expected in current draft state).

## Queue Outcome
- Removed Black Emperor entries from `meta/dice_authoring_queue.md`.
- Queue totals remain:
  - `total_sequences: 121`
  - `total_abilities: 277`
