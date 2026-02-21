# Manual YAML Review - Round 23

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/visionary/seq-02.md`
- `draft/sequences/visionary/seq-03.md`
- `draft/sequences/visionary/seq-04.md`
- `draft/sequences/visionary/seq-06.md`
- `draft/sequences/visionary/seq-07.md`
- `draft/sequences/visionary/seq-09.md`

## Primary Goals
- Close all Visionary dice mapping entries listed in the queue.
- Align explicit spirituality costs with prose.
- Capture DV checks and embedded dice results in notes.

## Manual Changes Applied
- Closed all queue-flagged Visionary dice mappings:
  - `visionary-seq-02-insight`
  - `visionary-seq-03-dream-weaving`
  - `visionary-seq-03-psychic-phantom`
  - `visionary-seq-04-consciousness-walking`
  - `visionary-seq-04-multiple-minds`
  - `visionary-seq-04-psychic-breath`
  - `visionary-seq-04-psychic-plague`
  - `visionary-seq-04-psychic-stealth`
  - `visionary-seq-04-psychic-storm`
  - `visionary-seq-06-combat-hypnosis`
  - `visionary-seq-06-dragon-scale`
  - `visionary-seq-07-frenzy`
  - `visionary-seq-09-observe-others`
  - `visionary-seq-09-remove-emotional-effects`
  - `visionary-seq-09-spectator-state`
  - `visionary-seq-09-spiritual-vision`

- Added roll mappings and dice notes:
  - Target DV checks for Dream Weaving, Psychic Phantom, Multiple Minds.
  - Psychological attack check and damage dice for Psychic Breath.
  - Mode-specific dice details and guidance checks for Psychic Storm.
  - Sanity loss dice and DV checks for Psychic Plague and Frenzy.
  - Psychology DV checks for Observe Others and Remove Emotional Effects.

- Corrected explicit prose/YAML mismatches:
  - Added spirituality costs for Dream Weaving, Psychic Phantom, Psychic Breath, Psychic Storm, Psychic Plague, Combat Hypnosis, Frenzy, and Spiritual Vision.
  - Set `opposed_by: difficulty_value` for Observe Others and Remove Emotional Effects.
  - Set `opposed_by: willpower_defense` for Psychic Storm (mode 2).

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 18, warnings: 81); non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed Visionary pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 5`
  - `total_abilities: 14`
