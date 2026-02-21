# Manual YAML Review - Round 21

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/sun/seq-00.md`
- `draft/sequences/sun/seq-02.md`
- `draft/sequences/sun/seq-03.md`
- `draft/sequences/sun/seq-04.md`
- `draft/sequences/sun/seq-05.md`
- `draft/sequences/sun/seq-07.md`
- `draft/sequences/sun/seq-08.md`
- `draft/sequences/sun/seq-09.md`

## Primary Goals
- Close all Sun `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Map damage dice, DV checks, and passive bonuses into ability schema fields.

## Manual Changes Applied
- Closed all queue-flagged Sun dice mappings:
  - `sun-seq-00-ultra-high-temperature-flames`
  - `sun-seq-02-incarnate-sun`
  - `sun-seq-03-symmetra`
  - `sun-seq-03-zhengyao-wings`
  - `sun-seq-04-darkness-endless-light`
  - `sun-seq-04-pure-white-ray`
  - `sun-seq-04-sacred-armor`
  - `sun-seq-04-spear-of-darkness`
  - `sun-seq-04-yang-yan`
  - `sun-seq-05-divine-light`
  - `sun-seq-05-holy-baptism`
  - `sun-seq-05-holy-rain`
  - `sun-seq-07-body-of-the-sun`
  - `sun-seq-07-cleansing-slash`
  - `sun-seq-07-fire-of-light`
  - `sun-seq-07-sacred-oath`
  - `sun-seq-07-sun-halo`
  - `sun-seq-08-brightness`
  - `sun-seq-08-call-the-holy-light`
  - `sun-seq-08-purification`
  - `sun-seq-08-sun-path-restraint`
  - `sun-seq-09-sing-piety`
  - `sun-seq-09-song-of-courage`
  - `sun-seq-09-spirit-vision`

- Corrected explicit prose/YAML mismatches (costs):
  - `sun-seq-02-incarnate-sun` -> `spirituality: 10`
  - `sun-seq-04-pure-white-ray` -> `spirituality: 3`
  - `sun-seq-04-sacred-armor` -> `spirituality: 4`
  - `sun-seq-04-spear-of-darkness` -> `spirituality: 5`
  - `sun-seq-04-yang-yan` -> `spirituality: 6`
  - `sun-seq-05-divine-light` -> `spirituality: 4`
  - `sun-seq-05-holy-baptism` -> `spirituality: 4`
  - `sun-seq-07-fire-of-light` -> `spirituality: 2`
  - `sun-seq-07-cleansing-slash` -> `spirituality: 1`
  - `sun-seq-07-sacred-oath` -> `spirituality: 2`
  - `sun-seq-07-sun-halo` -> `spirituality: 2`
  - `sun-seq-08-brightness` -> `spirituality: 2`
  - `sun-seq-08-call-the-holy-light` -> `spirituality: 3`
  - `sun-seq-08-purification` -> `spirituality: 2`
  - `sun-seq-09-song-of-courage` -> `spirituality: 2`
  - `sun-seq-09-sing-piety` -> `spirituality: 2`
  - `sun-seq-09-spirit-vision` -> `spirituality: 1`

- Added roll mappings and dice notes:
  - Occult vs Physical Defense for Sun-domain attacks
  - Damage dice for spear/ray/yang-yan/divine light/call holy light
  - Incarnate Sun per-round damage with scaling notes
  - Cleansing slash/sacred oath bonus damage dice
  - Sun restraint bonus dice and temp sanity armor dice
  - Singing identification checks for Bard songs

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 20, warnings: 83); global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Sun pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 21`
  - `total_abilities: 53`
