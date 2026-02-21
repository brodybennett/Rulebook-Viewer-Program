# Manual YAML Review - Round 18

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/paragon/seq-04.md`
- `draft/sequences/paragon/seq-05.md`
- `draft/sequences/paragon/seq-06.md`
- `draft/sequences/paragon/seq-07.md`
- `draft/sequences/paragon/seq-08.md`
- `draft/sequences/paragon/seq-09.md`

## Primary Goals
- Close all Paragon `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Map DV checks and dice tables for crafting/astronomy kits.

## Manual Changes Applied
- Closed all queue-flagged Paragon dice mappings:
  - `paragon-seq-04-alchemy`
  - `paragon-seq-04-forged-formation`
  - `paragon-seq-04-life-drain`
  - `paragon-seq-05-astrological-reproduction`
  - `paragon-seq-05-astronomical-prediction`
  - `paragon-seq-06-extraordinary-crafting`
  - `paragon-seq-06-wondercrafting`
  - `paragon-seq-07-spiritual-identification`
  - `paragon-seq-08-lore-practice`
  - `paragon-seq-09-practical-assemblies`
  - `paragon-seq-09-spirit-vision`
  - `paragon-seq-09-wake-up-memory`

- Corrected explicit prose/YAML mismatches:
  - `paragon-seq-04-life-drain` -> `spirituality: 6`
  - `paragon-seq-05-astrological-reproduction` -> removed incorrect base cost and clarified mixed defenses
  - `paragon-seq-05-astronomical-prediction` -> `spirituality: 2`
  - `paragon-seq-09-spirit-vision` -> `spirituality: 1` (per round)
  - `paragon-seq-09-wake-up-memory` -> `spirituality: 3`

- Added roll mappings and dice notes:
  - Scientific checks and per-km damage/THP on Life Drain
  - Crafting checks for Forged Formation, Wondercrafting, and Extraordinary Crafting
  - Astronomy checks with per-effect damage lists for Astrological Reproduction
  - 1d24 timing, 1d7 effect selection, and 1d2 healing for Astronomical Prediction
  - Occult DV 15 identification with 1d2/2d3 info tiers for Spiritual Identification
  - DV 15 knowledge checks for Lore Practice
  - Crafting checks and explosion damage for Practical Assemblies
  - Static +1 Spiritual Intuition and +1 tier boosts captured as effect rolls

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 23, warnings: 82); global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Paragon pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 42`
  - `total_abilities: 101`
