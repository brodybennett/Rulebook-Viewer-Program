# Manual YAML Review - Round 24

Date: 2026-02-20
Reviewer: Codex (manual pass)

## Batch Scope
- `draft/sequences/war-god/seq-03.md`
- `draft/sequences/war-god/seq-04.md`
- `draft/sequences/war-god/seq-05.md`
- `draft/sequences/war-god/seq-06.md`
- `draft/sequences/war-god/seq-08.md`
- `draft/sequences/war-god/seq-09.md`

## Primary Goals
- Close all War-God dice mapping entries listed in the queue.
- Align explicit spirituality costs with prose.
- Capture DV checks and embedded dice results in notes.

## Manual Changes Applied
- Closed all queue-flagged War-God dice mappings:
  - `war-god-seq-03-mercury`
  - `war-god-seq-03-silver-rapier`
  - `war-god-seq-04-demon-hunt-ritual`
  - `war-god-seq-04-detect-evil`
  - `war-god-seq-04-material-identification`
  - `war-god-seq-04-spiritual-disturbance`
  - `war-god-seq-05-wall-of-protection`
  - `war-god-seq-06-armor-of-dawn`
  - `war-god-seq-06-gather-dawn`
  - `war-god-seq-06-storm-of-light`
  - `war-god-seq-08-extraordinary-fighting`
  - `war-god-seq-08-extraordinary-physical-abilities`
  - `war-god-seq-09-spirit-vision`

- Added roll mappings and dice notes:
  - Attack check and damage for Silver Rapier.
  - DV checks and time rolls for Detect Evil and Material Identification.
  - Weapon damage dice and restraint bonuses for Gather Dawn.
  - Occultism check and mixed holy/fire damage for Storm of Light.

- Corrected explicit prose/YAML mismatches:
  - Added spirituality costs where specified (Silver Rapier, Demon Hunt Ritual, Wall of Protection, Gather Dawn, Storm of Light, Spirit Vision).
  - Adjusted Armor of Dawn cost to 3 spirituality.

## Validation Results
- `extract_compendium.py`: pass (warnings: 0)
- `lint_compendium.py`: pass (0 errors, 0 warnings)
- `lint_roll_syntax.py`: pass (0 findings)
- `power_audit.py`: completed (errors: 18, warnings: 81); non-zero findings remain expected in current draft state.

## Queue Outcome
- Removed War-God pathway entries from `meta/dice_authoring_queue.md`.
- Queue totals now:
  - `total_sequences: 0`
  - `total_abilities: 0`
