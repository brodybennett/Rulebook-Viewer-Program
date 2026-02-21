# Manual YAML Review - Round 4

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/abyss/seq-03.md`
- `draft/sequences/abyss/seq-04.md`
- `draft/sequences/abyss/seq-05.md`
- `draft/sequences/abyss/seq-06.md`
- `draft/sequences/abyss/seq-07.md`
- `draft/sequences/abyss/seq-08.md`
- `draft/sequences/abyss/seq-09.md`

## Primary Goals
- Close all Abyss `dice_mapping_missing` findings.
- Correct explicit prose/YAML mismatches (cost/action/duration/type) where clear.
- Add explicit scaling breakpoints from prose.

## Manual Changes Applied
- Added explicit/ adapted roll mappings for queue-flagged abilities:
  - `abyss-seq-03-babbling`
  - `abyss-seq-03-danger-countermeasure`
  - `abyss-seq-04-stupid-aura`
  - `abyss-seq-04-devil`
  - `abyss-seq-04-volcanic-eruption`
  - `abyss-seq-05-incarnation-of-desire`
  - `abyss-seq-06-arrogance-flaming-horns`
  - `abyss-seq-06-dehumanization`
  - `abyss-seq-06-demonic-spells`
  - `abyss-seq-06-demonization`
  - `abyss-seq-06-fallen-wings`
  - `abyss-seq-06-magic-scale-armor`
  - `abyss-seq-07-nether-disturbance`
  - `abyss-seq-08-broken-wings`
  - `abyss-seq-08-inhuman-body`
  - `abyss-seq-09-intoxicated`
  - `abyss-seq-09-perception-of-depravity`
  - `abyss-seq-09-spirit-vision`

- Corrected prose/YAML mismatches with explicit values:
  - `abyss-seq-04-volcanic-eruption` spirituality cost set to 10.
  - `abyss-seq-05-incarnation-of-desire` spirituality cost set to 2.
  - `abyss-seq-05-control-desires` normalized to cast-mode with 2 spirituality baseline.
  - `abyss-seq-06-arrogance-flaming-horns` spirituality cost set to 2 (branch detail in prose).
  - `abyss-seq-06-fallen-wings` mapped as 1 spirituality per fireball branch.
  - `abyss-seq-09-spirit-vision` upkeep spirituality set to 1.

- Type/action normalization for passive/toggle framing:
  - `abyss-seq-04-stupid-aura` -> `type: toggle`
  - `abyss-seq-08-inhuman-body` -> `type: passive`
  - `abyss-seq-09-spirit-vision` -> `type: toggle`
  - `abyss-seq-09-perception-of-depravity` -> `type: passive`
  - `abyss-seq-09-intoxicated` -> `type: reaction`

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: global balance/cost findings remain, but Abyss `dice_mapping_missing` entries are now zero.

## Queue Outcome
- Removed Abyss pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals updated:
  - `total_sequences: 135`
  - `total_abilities: 297`
