# Manual YAML Review - Round 10

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/earth/seq-03.md`
- `draft/sequences/earth/seq-04.md`
- `draft/sequences/earth/seq-05.md`
- `draft/sequences/earth/seq-06.md`
- `draft/sequences/earth/seq-08.md`
- `draft/sequences/earth/seq-09.md`

## Primary Goals
- Close all Earth `dice_mapping_missing` findings listed in the queue.
- Reconcile explicit prose/YAML mismatches (especially missing or incorrect costs).
- Add explicit mode and tier scaling where prose provides breakpoints.

## Manual Changes Applied
- Closed all queue-flagged Earth dice mappings:
  - `earth-seq-03-earth`
  - `earth-seq-03-pallbearer`
  - `earth-seq-03-soul-to-earth`
  - `earth-seq-04-alchemy-of-life`
  - `earth-seq-04-crazy-induction`
  - `earth-seq-05-create-vines`
  - `earth-seq-05-subterranean-sneaking`
  - `earth-seq-05-toxic-fog`
  - `earth-seq-06-highly-toxic`
  - `earth-seq-08-heal-diseases`
  - `earth-seq-08-healing`
  - `earth-seq-08-stitching-the-soul`
  - `earth-seq-09-identify-seeds`
  - `earth-seq-09-severe-cold-and-hot-effect`
  - `earth-seq-09-telling-the-time-of-day`

- Corrected explicit prose/YAML cost mismatches:
  - `earth-seq-03-soul-to-earth` -> `spirituality: 5`
  - `earth-seq-04-alchemy-of-life` -> `spirituality: 4`
  - `earth-seq-05-drain-the-earth` -> `spirituality: 3`
  - `earth-seq-05-subterranean-sneaking` -> `spirituality: 3`
  - `earth-seq-05-create-vines` -> `spirituality: 3`
  - `earth-seq-05-toxic-fog` -> `spirituality: 3`
  - `earth-seq-06-highly-toxic` -> `spirituality: 3`
  - `earth-seq-08-healing` -> `spirituality: 3`
  - `earth-seq-08-stitching-the-soul` -> `spirituality: 3`
  - `earth-seq-09-telling-the-time-of-day` -> `spirituality: 1` (base day)

- Type/action/duration normalization where prose was explicit:
  - `earth-seq-03-pallbearer` -> passive persistent bonus package
  - `earth-seq-03-soul-to-earth` -> sustained control package
  - `earth-seq-05-subterranean-sneaking` -> move action with sustained upkeep
  - `earth-seq-08-heal-diseases` -> passive persistent medical appraisal package
  - `earth-seq-09-severe-cold-and-hot-effect` -> passive persistent environmental package

- Added prose-backed scaling blocks for explicit mode/tier conditions:
  - undead tier burial pacing (`soul-to-earth`)
  - multi-hit and ground-piercing modes (`create-vines`)
  - fog persistence re-checks (`toxic-fog`)
  - symptom-specific secondary checks (`highly-toxic`)
  - injury severity and sequence-tier healing upgrades (`healing`)
  - crop growth/harvest dice tables (`identify-seeds`)
  - multi-day forecast rolls (`telling-the-time-of-day`)

## Validation Results
- `extract_compendium.py`: pass
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed; global non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Earth pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 97`
  - `total_abilities: 230`
