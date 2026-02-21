# Manual YAML Review - Round 22

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/tyrant/seq-00.md`
- `draft/sequences/tyrant/seq-01.md`
- `draft/sequences/tyrant/seq-02.md`
- `draft/sequences/tyrant/seq-03.md`
- `draft/sequences/tyrant/seq-04.md`
- `draft/sequences/tyrant/seq-05.md`
- `draft/sequences/tyrant/seq-06.md`
- `draft/sequences/tyrant/seq-07.md`
- `draft/sequences/tyrant/seq-08.md`
- `draft/sequences/tyrant/seq-09.md`

## Primary Goals
- Close all Tyrant `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (costs, opposition, action type).
- Map disaster checks, DV checks, and bonus damage dice into ability schema fields.

## Manual Changes Applied
- Closed all queue-flagged Tyrant dice mappings:
  - `tyrant-seq-00-celestial-thunder`
  - `tyrant-seq-00-sweeping-tides`
  - `tyrant-seq-00-tyrant`
  - `tyrant-seq-01-become-thunder`
  - `tyrant-seq-01-hundreds-of-millions-of-thunders-and-entanglements`
  - `tyrant-seq-02-humanoid-scourge`
  - `tyrant-seq-02-summon-meteor`
  - `tyrant-seq-03-dominate-sea-creatures`
  - `tyrant-seq-03-lightning-immunity`
  - `tyrant-seq-03-lightning-storm`
  - `tyrant-seq-04-rock-tide-stomp`
  - `tyrant-seq-05-lightning-mastery`
  - `tyrant-seq-06-create-a-gale`
  - `tyrant-seq-06-create-air-cushions`
  - `tyrant-seq-06-wind-attachment`
  - `tyrant-seq-06-wind-bind`
  - `tyrant-seq-06-wind-blade`
  - `tyrant-seq-06-wind-pressure-slap`
  - `tyrant-seq-07-fuzzy-probability-calculation`
  - `tyrant-seq-07-intuitive-grasp`
  - `tyrant-seq-08-furious-strike`
  - `tyrant-seq-09-high-rank-sensitivity`
  - `tyrant-seq-09-phantom-scale`
  - `tyrant-seq-09-spirit-vision`

- Corrected explicit prose/YAML mismatches:
  - `tyrant-seq-00-tyrant` -> opposed_by Willpower Defense
  - `tyrant-seq-06-wind-blade` -> action set to cast (base use is spellcasting action)
  - `tyrant-seq-08-furious-strike` -> action set to attack (base use is attack action)
  - `tyrant-seq-09-spirit-vision` -> `spirituality: 1`

- Added roll mappings and dice notes:
  - Disaster checks (+20/+25) for lightning/meteor/storm effects
  - Bonus damage dice for lightning/wind attachments and rage strikes
  - Navigation-mapped checks for wind blade/pressure slap and piloting substitutions
  - DV checks for wind bind, gale balance, and high-rank sensitivity

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 18, warnings: 82); global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Tyrant pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 11`
  - `total_abilities: 29`
