---
title: 'Sequence 8: Gravedigger'
id: death-seq-08
tags:
- pathway:death
- sequence:8
---






# Death Pathway: Sequence 8

## Gravedigger

- Your body is stronger, your spirit vision is stronger, your skills are more agile, and you can initially communicate with a small number of nearby spirits.
- **Eyes of Death** lets you overlook an enemy “from a higher level” to find key weaknesses, especially against unfamiliar undead and spirit creatures.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +2, Agility (DEX) +1, Intuition (INT) +1
- Your knowledge of the dead can be learned to be erudite.

### Training and Learning Benefits

```yaml ability
id: death-seq-08-training-and-learning-benefits
name: Training and Learning Benefits
pathway: death
sequence: 8
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
- buff
text: Fighting, shooting, throwing, and their subdivision skills are included in your
  quick learning scope. You need to receive at least 2 hours of real and effective
  related guidance to improve a level. You can only learn once a day to digest Knowledge.
  From training to proficiency, you must learn 2 times; the maximum remains Proficient.
  Character cards that have not just been promoted can use twice the Intuition (INT)
  brought by potions to add growth skills.
```





1. Fighting, shooting, throwing, and their subdivision skills are included in your quick learning scope. You need to receive at least 2 hours of real and effective related guidance to improve a level. You can only learn once a day to digest Knowledge.
2. From training to proficiency, you must learn **2 times**; the maximum remains **Proficient**.
3. Character cards that have not just been promoted can use twice the Intuition (INT) brought by potions to add growth skills.

- **Effect:** Training and Learning Benefits resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Eyes of Death

```yaml ability
id: death-seq-08-eyes-of-death
name: Eyes of Death
pathway: death
sequence: 8
status: adapted
type: active
action: full-round
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.knowledge
opposed_by: physical_defense
range: self
target: designated target(s)
duration: 1 encounter
dice:
  check_roll: 1d20 + @attr.int + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: check_roll maps the scrutiny-assisted attack package; effect_roll encodes that successful hits gain guaranteed-damage floor behavior from Great Success handling.
scaling:
- when: successful_attack_damage_is_below_half_theoretical_max
  changes:
    effect_note: Raise damage to half of the maximum theoretical value, rounded up.
conditions:
- dead
tags:
- ritual
- offense
text: 'Cost: 5 [[Spirituality]] Use: As a Full-Round Action [[Full-Round Action]],
  choose 1 undead creature in front of you. If the execution completes and is not
  interrupted, the effect applies. Effect: You personally benefit from a Great Success
  on all attacks against the chosen undead creature. Regardless of whether the undead
  creature you choose has ever been known to you, as long as the Eyes of Death scrutiny
  is complete, your attacks against it gain the bonus of [[Knowledge of the Dead]].
  Great Success (damage rule): Your damage is guaranteed, and it must cause more than
  half of the maximum theoretical damage, rounded up.'
```





- **Cost:** 5 [[Spirituality]]
- **Use:** As a **Full-Round Action** [[Full-Round Action]], choose 1 **undead creature** in front of you.
  - If the execution completes and is not interrupted, the effect applies.
- **Effect:**
  - You personally benefit from a **Great Success** on all attacks against the chosen undead creature.
  - Regardless of whether the undead creature you choose has ever been known to you, as long as the Eyes of Death scrutiny is complete, your attacks against it gain the bonus of [[Knowledge of the Dead]].
- **Great Success (damage rule):**
  - Your damage is guaranteed, and it must cause more than half of the maximum theoretical damage, rounded up.
  - If the value of the rolled damage is lower than half of the maximum theoretical damage, it will be changed to half of the damage regardless of the [[Attack Identification]] result.
- **Valid targets (what counts as undead):**
  - The out-of-control is also regarded as a kind of undead creature (its essence has died) and can be examined with Eyes of Death. [[Out-of-Control]]
  - This includes products considered to have “died of essence,” such as secret puppets. [[Secret Puppets]]
- **Special:**
  - Enjoying the benefits of Great Success does **not** mean your attack must hit. You still need to conduct attack identification; only when you hit the target can you enjoy the guaranteed-damage benefit.

> **Lore:** Eyes of Death seems able to “enter the spiritual world and the kingdom of the dead,” overlooking enemies to find an important node.

- **Limits:** As described in this section's prose.


### Communicating with the Dead

```yaml ability
id: death-seq-08-communicating-with-the-dead
name: Communicating with the Dead
pathway: death
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
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
conditions:
- dead
tags:
- ritual
- defense
text: 'Cost: 3 [[Spirituality]] Use: 1 Casting Action Casting Action Effect: You summon
  a spirit body and let it perform 1 action instead of you. Limits: For the time being,
  you can only summon the following spirits: Shadow 15 Vitality 15 [[Physical Defense]]
  (Agility (DEX) and Dodge 5)'
```





- **Cost:** 3 [[Spirituality]]
- **Use:** 1 **Casting Action** Casting Action
- **Effect:** You summon a **spirit body** and let it perform 1 action instead of you.
- **Limits:**
  - For the time being, you can only summon the following spirits:
    - **Shadow**
      - 15 Vitality
      - 15 [[Physical Defense]] (Agility (DEX) and Dodge 5)
      - 10 Willpower Defense
      - 5 points of [[Cold Resistance]]
      - Attack actions cause 1d6 cold damage
      - No more abilities, but can perform special actions such as grapple [[Grapple]]
      - For ease of calculation, Shadow’s skill and ability bonuses depend on your Intuition (INT), or use a +5 check value for processing.
  - Each Casting Action can summon a spirit body. However, your current ability cannot summon them in advance; you can only temporarily issue preliminary instructions to surrounding spirits.
  - After each spirit performs an action, it will disappear.
- **Special:**
  - For continuous actions such as grapple, the spirit will continue to execute until the target breaks free.
  - You and the spirit do not have any deeper communication and sensory sharing.
  - Generally speaking, any area can call this preliminary spirit body.

### Quick Dodge

```yaml ability
id: death-seq-08-quick-dodge
name: Quick Dodge
pathway: death
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
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
- debuff
- defense
- offense
text: 'Effect: You can dodge firearms. When facing guns, you fully retain the agility
  and dodge in [[Physical Defense]], which does not include light and lightning. [[light
  and lightning]] When you face an attack that is slower than a gun, you can dodge
  more quickly, and you get an extra level of dodge. [[Dodge level]] Special: This
  is the effect brought by 1 potion and cannot be stolen or recorded. [[Potions]]'
```





- **Effect:** You can dodge firearms.
1. When facing guns, you fully retain the agility and dodge in [[Physical Defense]], which does not include light and lightning. [[light and lightning]]
2. When you face an attack that is slower than a gun, you can dodge more quickly, and you get an extra level of dodge. [[Dodge level]]
- **Special:** This is the effect brought by 1 potion and cannot be stolen or recorded. [[Potions]]

- **Limits:** As described in this section's prose.
