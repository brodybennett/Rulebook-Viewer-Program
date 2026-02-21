# Manual YAML Review - Round 15

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/mutant/seq-01.md`
- `draft/sequences/mutant/seq-03.md`
- `draft/sequences/mutant/seq-04.md`
- `draft/sequences/mutant/seq-05.md`
- `draft/sequences/mutant/seq-06.md`
- `draft/sequences/mutant/seq-07.md`
- `draft/sequences/mutant/seq-08.md`
- `draft/sequences/mutant/seq-09.md`

## Primary Goals
- Close all Mutant `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, passive traits).
- Add DV/scaling breakpoints where prose provides tiers.

## Manual Changes Applied
- Closed all queue-flagged Mutant dice mappings:
  - `mutant-seq-01-abominable-state`
  - `mutant-seq-01-curse-damage-bypasses-the-double`
  - `mutant-seq-01-the-body-is-the-cage-of-the-mind-and-the-world-is-the-cage-of-the-body`
  - `mutant-seq-03-extra-death-path-immunity-limits`
  - `mutant-seq-03-source-of-the-curse`
  - `mutant-seq-03-transformation-curse`
  - `mutant-seq-04-immortal-body`
  - `mutant-seq-04-object-activation-mind-control`
  - `mutant-seq-04-the-source-of-the-curse`
  - `mutant-seq-05-advanced-shadow-invisibility`
  - `mutant-seq-05-anti-divination`
  - `mutant-seq-05-devour-soul`
  - `mutant-seq-05-mind-manipulation`
  - `mutant-seq-05-shapeshifting-shadow`
  - `mutant-seq-05-spirit-world-divination`
  - `mutant-seq-05-wraith-scream`
  - `mutant-seq-06-blessing-of-cold`
  - `mutant-seq-06-blessing-of-rot`
  - `mutant-seq-06-full-moon-curse`
  - `mutant-seq-06-ice-crystal-arrow`
  - `mutant-seq-06-ice-wall-consolidation`
  - `mutant-seq-06-immortal-body`
  - `mutant-seq-06-manipulate-living-corpses`
  - `mutant-seq-06-rotten-finger`
  - `mutant-seq-06-steel-skin`
  - `mutant-seq-07-blade-swipe`
  - `mutant-seq-07-fast-healing`
  - `mutant-seq-07-full-moon-curse`
  - `mutant-seq-07-hair-armor`
  - `mutant-seq-07-spiritual-alienation`
  - `mutant-seq-07-transform-werewolf`
  - `mutant-seq-07-werewolf-transformation`
  - `mutant-seq-08-crazy-intuitive-action`
  - `mutant-seq-08-full-moon-curse`
  - `mutant-seq-09-sexual-behavior`
  - `mutant-seq-09-vision`

- Corrected explicit prose/YAML cost mismatches:
  - `mutant-seq-01-the-body-is-the-cage-of-the-mind-and-the-world-is-the-cage-of-the-body` -> `spirituality: 3`
  - `mutant-seq-04-object-activation-mind-control` -> `spirituality: 3`
  - `mutant-seq-04-the-source-of-the-curse` -> `spirituality: 4`
  - `mutant-seq-05-wraith-scream` -> `spirituality: 3`
  - `mutant-seq-06-blessing-of-cold` -> `spirituality: 1`
  - `mutant-seq-06-blessing-of-rot` -> `spirituality: 1`
  - `mutant-seq-06-rotten-finger` -> `spirituality: 2`
  - `mutant-seq-06-ice-wall-consolidation` -> `spirituality: 1`
  - `mutant-seq-06-manipulate-living-corpses` -> `spirituality: 3`
  - `mutant-seq-07-werewolf-transformation` -> `spirituality: 2`
  - `mutant-seq-08-crazy-intuitive-action` -> `spirituality: 2`
  - `mutant-seq-09-vision` -> `spirituality: 1` per round

- Added roll mappings and scaling notes:
  - Mysticism/Occultism vs defenses for curse and object-control attacks
  - Divination DV tiers for Spirit World Divination
  - Sanity check rolls for full-moon and transformation effects
  - Damage/heal dice for rot/cold blessings, blade swipe, devour soul, and fast healing
  - Sequence 6 fast healing upgrade (2d6 per round)
  - Rapid crafting option for `mutant-seq-03-source-of-the-curse`

- Normalized mechanics metadata:
  - `mutant-seq-01-curse-damage-bypasses-the-double` set to passive/persistent
  - DV-anchored checks documented for full moon curse and psychological guidance escape
  - Non-opposed creation effects set to `opposed_by: none` where appropriate

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Mutant pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 60`
  - `total_abilities: 131`
