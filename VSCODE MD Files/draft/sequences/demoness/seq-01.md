---
title: 'Sequence 1: Apocalypse'
id: demoness-seq-01
tags:
- pathway:demoness
- sequence:1
---






# Demoness Pathway: Sequence 1

## Apocalypse

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Proactively cause an [[Apocalypse]] that brings civilization to the brink of extinction, and take the [[Potion]] just as the disaster is officially beginning.
  - This is described as an unofficial ceremony.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Agility (DEX) +2, Constitution +1, Strength +1, Charisma (CHA) +1.

### Doomsday

```yaml ability
id: demoness-seq-01-doomsday
name: Doomsday
pathway: demoness
sequence: 1
status: adapted
type: active
action: cast
cost:
  spirituality: 15
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "3"
  notes: Effect roll encodes the explicit three-instance/triple-damage disaster multiplier mode.
scaling:
- when: superimpose_three_disasters
  changes:
    effect_note: Combine three disaster effects in one encounter.
- when: repeat_one_disaster_three_times
  changes:
    effect_roll: "3"
    effect_note: Resolve one disaster three times in one encounter (triple damage handling).
tags:
- offense
text: 'Effect: Your [[Disaster Ability]] spans the entire continent. You can combine
  your original abilities to create new disasters. In one Encounter, you can: Mix
  and superimpose three disasters, or Make one disaster appear three times in the
  same encounter (resolve as three instances; for damage, treat it as triple damage).
  Example: Meteorites become a meteor shower, dealing triple damage. Cost:'
```





- **Effect:**
  - Your [[Disaster Ability]] spans the entire continent.
  - You can combine your original abilities to create new disasters.
  - In one Encounter, you can:
    - Mix and superimpose three disasters, **or**
    - Make one disaster appear three times in the same encounter (resolve as three instances; for damage, treat it as triple damage).
      - Example: Meteorites become a meteor shower, dealing triple damage.
- **Cost:**
  - Each Casting Action consumes 15 points of [[Spirituality]].

> **GM Note:** If the target is the entire continent, do not focus on a single instance of damage. This disaster appears across the entire continent, and almost everyone will be affected; people may be devastated, which may cause a [[Divine Drop]].

- **Limits:** As described in this section's prose.
