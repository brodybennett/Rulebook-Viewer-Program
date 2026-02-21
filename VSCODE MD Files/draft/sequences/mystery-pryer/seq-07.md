---
title: 'Sequence 7: Warlock'
id: mystery-pryer-seq-07
tags:
- pathway:mystery-pryer
- sequence:7
---






# Hermit Pathway: Sequence 7

## Warlock

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2.
- Your occult/occult language can be quickly raised to proficiency.

### Speed Word

```yaml ability
id: mystery-pryer-seq-07-speed-word
name: Speed Word
pathway: mystery-pryer
sequence: 7
status: canonical
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No roll; counteracting uses compared damage rolls from relevant abilities.
scaling: []
damage_types:
- fire
tags:
- offense
text: 'Use: Once per turn, you can use 1 Casting Action as 1 free action (non-stackable).
  Effect: Your channeling is very fast. Counteracting: The ability cast by the high-speed
  oracle allows you to use it to counteract the abilities of others. Example: If a
  storm-path water spell deals 2d10 damage, and a [[Red Priest]] fire ability deals
  2d10 damage, you can reduce the damage by subtracting the Red Priests damage result
  from your damage result. This does not mean fire abilities can only be counteracted
  with water; you can also split them with lightning. Limits: The high-speed divine
  words of the Mystic Pathway can only be used in the abilities of the Mystic Pathway
  itself.'
```





- **Use:** Once per turn, you can use **1 Casting Action** as **1 free action** (non-stackable).
- **Effect:** Your channeling is very fast.
- **Counteracting:** The ability cast by the high-speed oracle allows you to use it to counteract the abilities of others.
  - Example: If a storm-path water spell deals 2d10 damage, and a [[Red Priest]] fire ability deals 2d10 damage, you can reduce the damage by subtracting the Red Priest’s damage result from your damage result.
  - This does not mean fire abilities can only be counteracted with water; you can also split them with lightning.
- **Limits:** The high-speed divine words of the Mystic Pathway can only be used in the abilities of the Mystic Pathway itself.

### Knowledge Enhancement

```yaml ability
id: mystery-pryer-seq-07-knowledge-enhancement
name: Knowledge Enhancement
pathway: mystery-pryer
sequence: 7
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit roll; enhancement adds a layer of spell tuning and is applied by the caster.
scaling: []
tags:
- ritual
- buff
- offense
text: 'Trigger: When you cast a damage-type spell. Cost: If you expend an extra Casting
  Action, you can apply Knowledge Enhancement to that spell. Effect: You spend more
  time tuning the spell with occult knowledge to increase its damage output. Limits:
  Generally, Knowledge Enhancement can strengthen one layer at most, and cannot be
  stacked infinitely. Cumulative casting is more in line with high-level ritual magic.
  Knowledge Enhancement is only an explanation of the spell cast and cannot be stolen
  or recorded. Recording/stealing captures only the base ability; Knowledge Enhancement
  must be applied by the user. Scrolls can store enhanced effects.'
```





- **Trigger:** When you cast a damage-type spell.
- **Cost:** If you expend an extra Casting Action, you can apply **Knowledge Enhancement** to that spell.
- **Effect:** You spend more time tuning the spell with occult knowledge to increase its damage output.
- **Limits:**
  - Generally, Knowledge Enhancement can strengthen one layer at most, and cannot be stacked infinitely.
  - Cumulative casting is more in line with high-level ritual magic.
  - Knowledge Enhancement is only an explanation of the spell cast and cannot be stolen or recorded.
  - Recording/stealing captures only the base ability; Knowledge Enhancement must be applied by the user. Scrolls can store enhanced effects.
  - [[Voyeur ability]]
  - [[Recorder]]
  - [[Scroll casting]]

### Spellcaster

```yaml ability
id: mystery-pryer-seq-07-spellcaster
name: Spellcaster
pathway: mystery-pryer
sequence: 7
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 1d10
  heal_roll: null
  effect_roll: null
  notes: Fireball and Frost each have their own spirituality costs; Frost also applies movement halving and -2 on the next check unless resisted.
scaling:
- when: knowledge_enhancement_fireball
  changes:
    effect_note: +1 spirituality cost; fireballs increase to ceil(Intuition/2) and may hit multiple targets (once each).
- when: knowledge_enhancement_frost
  changes:
    damage_roll: 3d6
    effect_note: +3 spirituality cost; Frost becomes a 10m ice storm affecting all targets.
damage_types:
- fire
tags:
- buff
- defense
- offense
text: 'You have learned to manipulate supernatural forces, and you gain the following
  spells. Fireball Cost: Consumes 2 spirit points, 1 Casting Action. Use: Choose a
  target. Effect: Unleash a ball of fire that counters the targets [[Physical Defense]]
  with [[Occultism]] and deals 1d10 fire damage. Benefits of Knowledge Enhancement:
  Spirit consumption +1; the number of fireballs changes from one to (Intuition (INT)/2,
  rounded up); you can attack multiple targets, but each target can only be hit once.
  Frost Cost: Consumes 3 Spirit points, 1 Casting Action.'
```





You have learned to manipulate supernatural forces, and you gain the following spells.

- **Fireball**
  - **Cost:** Consumes **2 spirit points**, **1 Casting Action**.
  - **Use:** Choose a target.
  - **Effect:** Unleash a ball of fire that counters the target’s [[Physical Defense]] with [[Occultism]] and deals **1d10 fire damage**.
  - **Benefits of Knowledge Enhancement:** Spirit consumption +1; the number of fireballs changes from one to (**Intuition (INT)/2**, rounded up); you can attack multiple targets, but each target can only be hit once.

- **Frost**
  - **Cost:** Consumes **3 Spirit points**, **1 Casting Action**.
  - **Use:** Choose a target within your **field of vision**.
  - **Effect:** Cause a burst of cold air around the target, using [[Occultism]] to counter the target’s [[Physical Defense]], dealing **1d10 cold damage**. Inorganic objects will be frozen, and the physical and fire damage received is halved.
  - **Aftereffects:**
    - A creature that takes cold damage has half its movement on its next move.
    - The creature takes a -2 penalty on its next check.
    - Negate the effect on targets with [[Cold Resistance]].
  - **Benefits of Knowledge Enhancement:** spirituality consumption +3; Frost changes to ice storm:
    - Choose an area with a radius of **10 meters**.
    - The area bursts into snow and becomes extremely cold.
    - [[Mysticism]] resists the [[Physical Defense]] of all creatures in the area, causing **3d6 cold damage**.
    - The area is immediately recognized as an **extremely cold environment**.
    - **Extremely cold environment:** Creatures without cold resistance suffer:
      - Continuous -2 disadvantage in skill and attribute checks.
      - A total of -2 in

- **Limits:** As described in this section's prose.
