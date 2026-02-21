# Manual YAML Review - Round 8

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/death/seq-00.md`
- `draft/sequences/death/seq-01.md`
- `draft/sequences/death/seq-02.md`
- `draft/sequences/death/seq-03.md`
- `draft/sequences/death/seq-04.md`
- `draft/sequences/death/seq-05.md`
- `draft/sequences/death/seq-06.md`
- `draft/sequences/death/seq-07.md`
- `draft/sequences/death/seq-08.md`
- `draft/sequences/death/seq-09.md`

## Primary Goals
- Close all Death `dice_mapping_missing` findings.
- Correct explicit prose/YAML mismatches for costs and persistent/toggle packaging.
- Add prose-backed scaling for mode branches and tiered outcomes.

## Manual Changes Applied
- Closed all queue-flagged Death dice mappings:
  - `death-seq-03-ferryman`
  - `death-seq-03-river-of-eternal-darkness`
  - `death-seq-03-the-language-of-the-dead`
  - `death-seq-04-necrotic-seal`
  - `death-seq-04-underworld-executive-power`
  - `death-seq-05-gate-to-the-underworld`
  - `death-seq-06-language-of-the-dead`
  - `death-seq-07-communicating-with-the-dead`
  - `death-seq-07-psychic-communication-with-living-people`
  - `death-seq-08-eyes-of-death`
  - `death-seq-09-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `death-seq-01-withering` -> `spirituality: 10`
  - `death-seq-04-necrotic-seal` -> `spirituality: 8` baseline, with permanent mode total of 16
  - `death-seq-05-gate-to-the-underworld` -> `spirituality: 5`
  - `death-seq-06-language-of-the-dead` -> `spirituality: 1` upkeep
  - `death-seq-07-communicating-with-the-dead` -> `spirituality: 3`
  - `death-seq-08-eyes-of-death` -> `spirituality: 5`
  - `death-seq-09-vision` -> `spirituality: 1` upkeep

- Type/action/duration normalization where prose was explicit:
  - `death-seq-03-ferryman` -> passive persistent trait package
  - `death-seq-03-river-of-eternal-darkness` -> toggle sustained package
  - `death-seq-06-language-of-the-dead` -> toggle sustained package
  - `death-seq-09-vision` -> toggle sustained

- Added prose-backed scaling blocks for explicit mode/tier conditions:
  - once-per-encounter burst and extra cast mode (`river-of-eternal-darkness`)
  - temporary vs permanent sealing mode (`necrotic-seal`)
  - gate mode branch (`gate-to-the-underworld`)
  - target tier penalties and spirit-state damage tiers (`language-of-the-dead`)
  - voluntary setup mode (`psychic-communication-with-living-people`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Death pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals remain:
  - `total_sequences: 121`
  - `total_abilities: 277`
