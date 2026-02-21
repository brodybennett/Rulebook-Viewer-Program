---
title: 'Sequence 4: Devil Monarch'
id: abyss-seq-04
tags:
- pathway:abyss
- sequence:4
---






# Abyss Pathway: Sequence 4

## Devil Monarch

- See also: Abyss

Their own thinking becomes less error-prone, while nearby creatures become more error-prone (see **Stupid Aura**).

Their own thinking becomes less error-prone, while nearby creatures become more error-prone (see **Stupid Aura**).

## Advancement

### Advancement Ritual

- **Advancement Ritual (unofficial ceremony):** Make a demigod or a whole city-state a slave to their own desires, only act in accordance with their own heart, reveal their deepest malice without concealment, and you yourself become all of them the instigator, the devil in this depraved catastrophe; take the potion at the moment when everyone in the whole city fell into chaos or when the demigod caused serious disasters.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2, Charisma +3, Intuition (INT) +2.

### Stupid Aura

```yaml ability
id: abyss-seq-04-stupid-aura
name: Stupid Aura
pathway: abyss
sequence: 4
status: adapted
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: nearby creatures
target: creatures in aura range
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: Adapted roll token for the stated 0/1 sanity check after seed detonation on major failure.
scaling:
- when: target_rolls_major_failure_in_aura
  changes:
    effect_note: You may instantly detonate that target's desire seed.
tags:
- ritual
- control
- debuff
text: 'Use: Free Action to enable or disable. Effect: The thinking ability of all
  nearby creatures will be significantly reduced, making mistakes easily. Effect:
  See your creature Intuition (INT) and Education -4; this does not affect [[Spirituality
  cap]] and skill training. Effect: At the same time, as long as it is within the
  influence range of this ability, the points for [[Major Failure]] will increase
  to 1, 2, and 3. Trigger: Whenever there is a major failure, you can directly detonate
  the desire seeds in the target''s body, allowing the seeds to mature instantly.
  Aftereffects: An additional [[Sanity / Rationality Check]] of 0/1 is caused to the
  target.'
```





- **Use:** Free Action to enable or disable.
- **Effect:** The thinking ability of all nearby creatures will be significantly reduced, making mistakes easily.
- **Effect:** See your creature Intuition (INT) and Education -4; this does not affect [[Spirituality cap]] and skill training.
- **Effect:** At the same time, as long as it is within the influence range of this ability, the points for [[Major Failure]] will increase to 1, 2, and 3.
- **Trigger:** Whenever there is a major failure, you can directly detonate the desire seeds in the target's body, allowing the seeds to mature instantly.
- **Aftereffects:** An additional [[Sanity / Rationality Check]] of 0/1 is caused to the target.

- **Limits:** As described in this section's prose.


### Devil

```yaml ability
id: abyss-seq-04-devil
name: Devil
pathway: abyss
sequence: 4
status: adapted
type: active
action: free
cost: {}
roll: 1d20 + @attr.wil
opposed_by: difficulty_value
range: self
target: witnessing creatures
duration: sustained
dice:
  check_roll: 1d20 + @attr.wil
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted mapping for witness sanity-test resolution when exposed to mythical-creature runes.
scaling: []
tags:
- ritual
text: 'Effect: Choose a limb, allowing you to maintain the shape of a [[mythical creature]]
  on this limb for a long time. Use: You only need a Free Action to choose a Spellcasting
  Action. Limits: The free action can only be done once in a round, and cannot be
  changed within a day. Effect: Your [[Life Value]] extra +10; [[Spirituality]] +10.
  Effect: In addition to strengthening your physique, this can also allow you to display
  the strange runes unique to mythical creatures through this limb, which directly
  results in a sanity test equivalent to your Sequence promotion. Limits: Anyone who
  has witnessed this scene and is not in the same position as you (per your tables
  positioning rules) will dire...'
```





- **Effect:** Choose a limb, allowing you to maintain the shape of a [[mythical creature]] on this limb for a long time.
- **Use:** You only need a Free Action to choose a Spellcasting Action.
- **Limits:** The free action can only be done once in a round, and cannot be changed within a day.
- **Effect:** Your [[Life Value]] extra +10; [[Spirituality]] +10.
- **Effect:** In addition to strengthening your physique, this can also allow you to display the strange runes unique to mythical creatures through this limb, which directly results in a sanity test equivalent to your Sequence promotion.
- **Limits:** Anyone who has witnessed this scene and is not in the same position as you (per your tables positioning rules) will directly suffer the corresponding loss of sanity; each encounter is limited to one time.

- **Limits:** Anyone who has witnessed this scene and is not in the same position as you (per your tables positioning rules) will directly suffer the corresponding loss of sanity; each encounter is limited to one time.

### Cunning Man, Trickster

```yaml ability
id: abyss-seq-04-cunning-man-trickster
name: Cunning Man, Trickster
pathway: abyss
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.cha + @bonus
opposed_by: willpower_defense
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: '@bonus = chosen Social Skill modifier used for this contested social check.'
scaling: []
tags:
- defense
text: 'Effect: Your social skills that have not reached the [[Proficiency level]]
  are considered proficient. Effect: You get an additional Identification bonus of
  +4. Effect: A social skill against its Willpower Defense, you can force a person
  to act according to your will once a round, or make him unable to distinguish between
  illusion and reality. Limits: The latter presupposes the presentation of hallucinatory
  things.'
```





- **Effect:** Your social skills that have not reached the [[Proficiency level]] are considered proficient.
- **Effect:** You get an additional Identification bonus of +4.
- **Effect:** A social skill against its Willpower Defense, you can force a person to act according to your will once a round, or make him unable to distinguish between illusion and reality.
- **Limits:** The latter presupposes the presentation of hallucinatory things.

> **Lore:** This usually allows you to solve a series of things very flexibly and plan, and even directly use a man leads to fall; this is usually in your hands, and will manifest in a malicious direction according to your will.

### Volcanic Eruption

```yaml ability
id: abyss-seq-04-volcanic-eruption
name: Volcanic Eruption
pathway: abyss
sequence: 4
status: canonical
type: active
action: full-round
cost:
  spirituality: 10
roll: 1d20 + 15
opposed_by: physical_defense
range: at least 10km radius
target: creatures in disaster area
duration: sustained
dice:
  check_roll: 1d20 + 15
  damage_roll: 6d6
  heal_roll: null
  effect_roll: null
  notes: Damage composition is 2d6 physical plus 2d6 fire plus 2d6 poison at the beginning of each round.
scaling:
- when: start_of_each_round_in_disaster_area
  changes:
    check_roll: 1d20 + 15
    damage_roll: 6d6
damage_types:
- physical
- fire
- poison
tags:
- ritual
- debuff
- defense
- offense
text: 'Effect: From now on, you can cause a volcanic eruption disaster. Use: A [[Full-Round
  Action]]. Requirements: Qualified environment. Cost: 10 points of spiritual consumption.
  Effect: You directly trigger a volcanic eruption, causing disasters covering a radius
  of at least ten kilometers. Effect: The volcanic eruption will bring thick volcanic
  ash and earthquake rockfall. Effect (ongoing): People in the disaster range will
  suffer +15 disaster attack identification against [[Physical Defense]] at the beginning
  of each round, causing 2d6 physical damage, 2d6 fire damage, and 2d6 poison harm.
  Effect: You can act normally within the range of the eruption.'
```





- **Effect:** From now on, you can cause a volcanic eruption disaster.
- **Use:** A [[Full-Round Action]].
- **Requirements:** Qualified environment.
- **Cost:** 10 points of spiritual consumption.
- **Effect:** You directly trigger a volcanic eruption, causing disasters covering a radius of at least ten kilometers.
- **Effect:** The volcanic eruption will bring thick volcanic ash and earthquake rockfall.
- **Effect (ongoing):** People in the disaster range will suffer +15 disaster attack identification against [[Physical Defense]] at the beginning of each round, causing 2d6 physical damage, 2d6 fire damage, and 2d6 poison harm.
- **Effect:** You can act normally within the range of the eruption.
- **Limits:** The specific effect of this skill depends on the specific situation.
