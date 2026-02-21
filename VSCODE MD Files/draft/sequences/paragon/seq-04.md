---
title: 'Sequence 4: Mysticologist'
id: paragon-seq-04
tags:
- pathway:paragon
- sequence:4
---






# Paragon Pathway: Sequence 4

> **GM Note:** This section is marked “unfinished” in the source.

Alchemists can infuse souls into crafted items, grant them a measure of life, and further manipulate the nature, shape, and characteristics of matter.

## Mysticologist

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Extract all vitality in a certain area; the soil will be desertified and the lake will be dried up.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** inspiration +2
- Your craftsmanship, mechanical maintenance, engineering, and mysticism can be promoted to master.

### Life Drain

```yaml ability
id: paragon-seq-04-life-drain
name: Life Drain
pathway: paragon
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 6
roll: 1d20 + @attr.int + @skill.chemistry
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.chemistry
  damage_roll: 1d6
  heal_roll: null
  effect_roll: 2d6
  notes: Use any scientific skill (chemistry/physics/biology); damage is 1d6 per km of chosen diameter (1-5 km, or 1-5 km equivalent for a single target), and temporary hit points are 2d6 per km (min 2d6, max 10d6).
scaling: []
tags:
- ritual
- defense
- offense
text: 'Cost: 6 [[Spirituality]] Use: spellcasting action Targeting and range: Area
  centered on you with a diameter of about 15 kilometers, or An individual (see Effect).
  Effect: You use any of your scientific skills to attack the physical defenses of
  living creatures in the area. For each kilometer of diameter you choose, you deal
  1d6 damage to most creatures in the area (e.g., 5 km diameter deals 5d6).'
```





- **Cost:** 6 [[Spirituality]]
- **Use:** **spellcasting action**
- **Targeting and range:**
  - Area centered on you with a **diameter** of about 1–5 kilometers, or
  - An individual (see Effect).
- **Effect:**
  - You use any of your scientific skills to attack the physical defenses of living creatures in the area.
  - For each kilometer of diameter you choose, you deal **1d6** damage to most creatures in the area (e.g., 5 km diameter deals **5d6**).
  - Damage type depends on the skill used:
    - Chemical skills: acid and fire damage
    - Physical skills: physical damage
    - Biological skills: poison damage
  - This extraction turns soil into deserts, dries up lakes, and makes life unsuitable for survival.
  - Instead of an area, you can use this effect to attack an individual for **1d6–5d6** damage, at your choice.
- **Aftereffects:**
  - You gain [[Temporary Hit Points]] equal to **2d6–10d6**.
  - These hit points heal your wounds first; hit points beyond the damage quickly fade after a few minutes.

- **Limits:** As described in this section's prose.


### Forged Formation

```yaml ability
id: paragon-seq-04-forged-formation
name: Forged Formation
pathway: paragon
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.crafting
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.crafting
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Crafting check DV 20; time bonuses apply as listed (+5 identification/appraisal at each milestone).
scaling: []
tags:
- buff
text: 'Use: spellcasting action Check: Pass a [[Crafting Check]] with Difficulty Value
  20. Extra crafting time can improve your skill check, assuming you work 4 hours
  a day: Day 1: Identification +5 1 week: Identification +5 1 month: [[Appraisal]]
  +5 1 year: Appraisal +5 10 years: Appraisal +5'
```





- **Use:** **spellcasting action**
- **Check:** Pass a [[Crafting Check]] with Difficulty Value 20.
- Extra crafting time can improve your skill check, assuming you work 4 hours a day:
  - Day 1: Identification +5
  - 1 week: Identification +5
  - 1 month: [[Appraisal]] +5
  - 1 year: Appraisal +5
  - 10 years: Appraisal +5
  - 100 years: Identification +5; after that, Identification +5 every 100 years.
- Successful skill identification allows you to manufacture:
  - [[Alchemy Arm]]
  - [[Alchemy Eye]]
  - [[Alchemy Heart]]
  - [[Alchemy Brain]]
  - [[Alchemy Vehicle]]
  - Other alchemy machinery

#### Alchemy Arm

A mechanical arm that can automatically combine with the human body to replace or assist it. It can replace the limbs of living organisms, or be additionally attached to other humans or machines.

- Each arm beyond the creature’s natural number of arms can perform an additional Attack Action.
- A robotic arm deals **2d6** damage.
- Its [[Strength]] counts as 5 points.
- Each additional arm requires an additional use of a [[Special Fighting Skill]].
- For every 5 of your skill check above 20, you can make and fit an additional arm for a creature or machine (e.g., skill check 25 allows two alchemical arms for a human).

#### Alchemy Eye

A mechanical eye that can see everything around it. It can replace the eyeball of a living body, or be additionally installed on other people or machines.

- All alchemy eyes can transmit information to your body.
- You can use the [[Spot]] skill with the mechanical eye to find what is around you.
- For every 5 of your skill check higher than 20, you can manufacture and install an additional mechanical eye for a creature or machine.
- If your skill check is 25, you can get two alchemical eyes, which will always pass the signal to you.

#### Alchemy Heart

A second heart that replaces the normal heart. It can replace the heart of a living being, or be additionally installed on other people or machines, thereby completely changing their physique.

- The physique of a living being carrying an alchemical heart becomes 6.
- When making an alchemy heart, the **recipient** gains **+1 Constitution** for every 5 points your skill check exceeds 20 (while the heart remains installed).

- **Effect:** Forged Formation resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Animate Object

```yaml ability
id: paragon-seq-04-animate-object
name: Animate Object
pathway: paragon
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
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice; mode costs are 4/6/8 spirituality (double for living matter). Disintegration damage applies after Armor Damage Reduction x2.
scaling: []
tags:
- mobility
text: You create and animate an object. You imbue an object you create with all of
  your [[Temporary Hit Points]], giving it life and movement.
```





You create and animate an object.

- You imbue an object you create with all of your [[Temporary Hit Points]], giving it life and movement.

- **Effect:** Animate Object resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Animate a Puppet

```yaml ability
id: paragon-seq-04-animate-a-puppet
name: Animate a Puppet
pathway: paragon
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
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- detection
- mobility
text: You create and animate a puppet. You infuse all your temporary hit points into
  a mechanical puppet you made, so that it can gain life and can move, similar to
  an intelligent robot in the sense of mysticism.
```





You create and animate a puppet.

- You infuse all your **temporary hit points** into a mechanical puppet you made, so that it can gain “life” and can move, similar to an intelligent robot in the sense of mysticism.

- **Effect:** Animate a Puppet resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Object Refining

```yaml ability
id: paragon-seq-04-object-refining
name: Object Refining
pathway: paragon
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
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- utility
text: 'You practice an object. You use a craft to make an identification or to create
  an object you expect. This usually does not involve creatures. This is the field
  opposite to the [[Ancient Alchemist]] of the Earth Path: Ancient alchemist is life
  refining, and you make objects.'
```





You practice an object.

- You use a craft to make an identification or to create an object you expect. This usually does not involve creatures.
- This is the field opposite to the [[Ancient Alchemist]] of the Earth Path: “Ancient alchemist” is life refining, and you make objects.

- **Effect:** Object Refining resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Cycle of Life

```yaml ability
id: paragon-seq-04-cycle-of-life
name: Cycle of Life
pathway: paragon
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- control
text: 'Alchemists can give or strip life force from items. #### Empower Alchemists
  can grant life force by touching a target. If it is an [[Extraordinary Item]], an
  item composed of a single [[Characteristic]] will go out of control, and an item
  composed of multiple characteristics will explode. The explosion value and range
  depend on (extraordinary craft level number of characteristics that make up the
  item). If the characteristics are not from the same Pathway, calculate them separately;
  after summing, the range takes the highest Sequence Characteristic of the item.
  #### Stripping By consuming spirituality, the alchemist strips the target''s vitality
  from the surrounding environment into itself.'
```





Alchemists can give or strip life force from items.

#### Empower

- Alchemists can grant life force by touching a target.
- If it is an [[Extraordinary Item]], an item composed of a single [[Characteristic]] will go out of control, and an item composed of multiple characteristics will explode.
- The explosion value and range depend on (extraordinary craft level × number of characteristics that make up the item).
- If the characteristics are not from the same **Pathway**, calculate them separately; after summing, the range takes the highest Sequence Characteristic of the item.

#### Stripping

- By consuming spirituality, the alchemist strips the target's vitality from the surrounding environment into itself.
- Alchemists can draw life force from the surrounding environment at a ratio of **1:2** to supplement their own lost life points.
- Alchemists can also pay **20** points of spirituality at a time to completely suppress [[Out-of-Control Monsters]] whose highest level characteristics do not exceed those of alchemists.
- Using an Extraordinary item of its own Sequence temporarily suppresses its active ability.

- **Effect:** Cycle of Life resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Alchemy

```yaml ability
id: paragon-seq-04-alchemy
name: Alchemy
pathway: paragon
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
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- defense
- offense
text: 'Alchemists use a free-Casting Action that consumes spirituality to complete
  the manipulation of matter (manipulation of living matter will double the spiritual
  consumption): #### Disintegration Cost: 4 points of spirituality Effect: Decompose
  matter by manipulating the gap between materials. Can dismantle mechanical enemies
  (causing damage after deducting [[Armor Damage Reduction]] 2), or Non-living matter
  (such as some walls blocking the way). #### Qualitative Change Cost: 6 spiritual
  points'
```





Alchemists use a **free-Casting Action** that consumes spirituality to complete the manipulation of matter (manipulation of living matter will double the spiritual consumption):

#### Disintegration

- **Cost:** 4 points of spirituality
- **Effect:** Decompose matter by manipulating the gap between materials.
  - Can dismantle mechanical enemies (causing damage after deducting [[Armor Damage Reduction]] × 2), or
  - Non-living matter (such as some walls blocking the way).

#### Qualitative Change

- **Cost:** 6 spiritual points
- **Effect:** Change the physical properties of the target (e.g., change the clothes on your body into iron; change water into red wine).

#### Recasting

- **Cost:** 8 spiritual points
- **Effect:** Directly manipulate the form of matter (e.g., build a stone bridge on a certain broken stone bridge; stab the enemy behind you).

- **Limits:** As described in this section's prose.
