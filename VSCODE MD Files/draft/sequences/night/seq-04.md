---
title: 'Sequence 4: Soul Assurer'
id: night-seq-04
tags:
- pathway:night
- sequence:4
---






# Darkness Pathway: Sequence 4

> **Lore:** Brings misfortune to others and excels at dealing with spirit creatures.

## Soul Assurer

## Advancement

### Advancement Ritual

- **Advancement Ritual:** To resist a disaster that covers the entire night; in the course of fulfilling one’s duty, stand firm under strong pressure for a night, until dawn is approaching. (unofficial ceremony)

### Substitution

- **Substitution:** Through the power of the sleeping or undead domain, integrate into your own blood the corresponding main body parts of descendants of high-level beings or undead connected with that power. Only the corresponding main body parts are required.
  - Example: After such a descendant dies, spiritual skulls or other important parts may remain; skulls that have been dead for a long time may still possess spirituality. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +1, Constitution +1, Strength +1, Agility (DEX) +1.
- Choose two skills to increase by 1 level.

### Grasp of Doom

```yaml ability
id: night-seq-04-grasp-of-doom
name: Grasp of Doom
pathway: night
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 5
roll: null
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d20 + @attr.luk
  notes: Each skill check forces an extra luck check (DV 15) or reduces success level; DV increases to 20 at Sequence 2.
scaling:
- when: sequence_2
  changes:
    effect_note: Lucky check Difficulty Value becomes 20.
- when: sequence_1
  changes:
    effect_note: Can be cast synchronously with an attack; target suffers -4 to identification-related checks.
tags:
- ritual
- debuff
- offense
text: 'Cost: 5 [[Spirituality]]. Use: 1 Casting Action; curse one creature. Effect:
  Each time the cursed creature makes a [[Skill Check]], it must also make an additional
  Lucky Check with Difficulty Value 15. On a failure, the triggering skill check drops
  by 1 Success Level. Sequence Scaling: Sequence 2: Lucky check Difficulty Value becomes
  20. Sequence 1: It can be cast synchronously by attacking, and additionally applies
  -4 to all identification-related checks made by the target.'
```





- **Cost:** 5 [[Spirituality]].
- **Use:** 1 Casting Action; curse one creature.
- **Effect:** Each time the cursed creature makes a [[Skill Check]], it must also make an additional **Lucky Check** with **Difficulty Value** 15. On a failure, the triggering skill check drops by 1 **Success Level**.

- **Sequence Scaling:**
  - **Sequence 2:** Lucky check **Difficulty Value** becomes 20.
  - **Sequence 1:** It can be cast synchronously by attacking, and additionally applies **-4** to all identification-related checks made by the target.

- **Limits:** As described in this section's prose.


### Ethereal Mastery

```yaml ability
id: night-seq-04-ethereal-mastery
name: Ethereal Mastery
pathway: night
sequence: 4
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
  damage_roll: 5d6
  heal_roll: null
  effect_roll: null
  notes: Bonus damage applies against incorporeal creatures; attacks ignore incorporeality.
scaling:
- when: sequence_3
  changes:
    effect_note: At close range, may pull out a helpless target's spirit body for channeling.
tags:
- offense
text: 'Effect: You are proficient at dealing with ethereal creatures. Your attacks
  ignore [[Incorporeality]]. You deal 5d6 more damage against creatures with the [[Incorporeal
  Quality]]. Sequence Scaling: Sequence 3: At [[Close Range]], you can pull out the
  [[Spirit Body]] of a [[Helpless]] creature to [[Channeling]] directly, then stuff
  the spirit body back into its body after channeling; this is considered an [[Injury]].'
```





- **Effect:** You are proficient at dealing with ethereal creatures.
  - Your attacks ignore [[Incorporeality]].
  - You deal 5d6 more damage against creatures with the [[Incorporeal Quality]].

- **Sequence Scaling:**
  - **Sequence 3:** At [[Close Range]], you can pull out the [[Spirit Body]] of a [[Helpless]] creature to [[Channeling]] directly, then stuff the spirit body back into its body after channeling; this is considered an [[Injury]].

- **Limits:** As described in this section's prose.
