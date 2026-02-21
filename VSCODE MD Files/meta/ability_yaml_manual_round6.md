# Manual YAML Review - Round 6

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/arbiter/seq-00.md`
- `draft/sequences/arbiter/seq-01.md`
- `draft/sequences/arbiter/seq-02.md`
- `draft/sequences/arbiter/seq-03.md`
- `draft/sequences/arbiter/seq-04.md`
- `draft/sequences/arbiter/seq-05.md`
- `draft/sequences/arbiter/seq-06.md`
- `draft/sequences/arbiter/seq-07.md`
- `draft/sequences/arbiter/seq-08.md`
- `draft/sequences/arbiter/seq-09.md`

## Primary Goals
- Close all Arbiter `dice_mapping_missing` findings.
- Correct explicit prose/YAML mismatches for costs, persistent/toggle states, and check fields.
- Add prose-backed scaling for mode branches and sequence-tier upgrades.

## Manual Changes Applied
- Added/normalized structured dice mapping for all queue-flagged Arbiter abilities:
  - `arbiter-seq-03-chaos-hunter`
  - `arbiter-seq-04-law-of-truth`
  - `arbiter-seq-04-practitioners-of-order`
  - `arbiter-seq-05-punishment-target-biological-type`
  - `arbiter-seq-06-death`
  - `arbiter-seq-06-imprisoned`
  - `arbiter-seq-06-whip`
  - `arbiter-seq-07-spirit-piercing`
  - `arbiter-seq-09-fighting-skills`
  - `arbiter-seq-09-verdict`
  - `arbiter-seq-09-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `arbiter-seq-01-hand-of-order` -> `spirituality: 5`
  - `arbiter-seq-02-sage-s-balance` -> `spirituality: 5`
  - `arbiter-seq-04-law-of-truth` -> `spirituality: 5`
  - `arbiter-seq-04-make-a-contract` -> `spirituality: 3`
  - `arbiter-seq-05-the-violator-shall-be-punished` -> `spirituality: 2`
  - `arbiter-seq-05-punishment-target-biological-type` -> `spirituality: 3`
  - `arbiter-seq-05-the-guilty-shall-be-restrained` -> `spirituality: 3`
  - `arbiter-seq-06-imprisoned` -> `spirituality: 3`
  - `arbiter-seq-06-whip` -> `spirituality: 2`
  - `arbiter-seq-06-death` -> `spirituality: 8`
  - `arbiter-seq-09-verdict` -> `spirituality: 3`
  - `arbiter-seq-09-vision` -> `spirituality: 1` upkeep

- Type/action/duration normalization where prose was explicit:
  - `arbiter-seq-03-chaos-hunter` -> passive persistent tracking package
  - `arbiter-seq-04-law-of-truth` -> toggle sustained field law
  - `arbiter-seq-04-practitioners-of-order` -> toggle sustained aura
  - `arbiter-seq-06-authority` -> toggle sustained aura
  - `arbiter-seq-07-weapon-proficiency` -> passive persistent
  - `arbiter-seq-09-reputation-growth` -> passive persistent
  - `arbiter-seq-09-fighting-skills` -> passive persistent
  - `arbiter-seq-09-vision` -> toggle sustained

- Added scaling blocks for explicit sequence/mode conditions:
  - law-breaking penalties and dual-roll DV setup (`hand-of-order`)
  - sequence-upgrade range/context expansions (`balancer`, `chaos-hunter`, `law-of-truth`)
  - mode split costs/effects (`spirit-piercing`, `death`, `whip`, `verdict`, `vision`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: global balance findings remain; Arbiter `dice_mapping_missing` entries are now zero.

## Queue Outcome
- Removed Arbiter pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals updated:
  - `total_sequences: 121`
  - `total_abilities: 277`
