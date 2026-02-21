---
title: 'Sequence 8: Clown'
id: fool-seq-08
tags:
- pathway:fool
- sequence:8
---






# Fool Pathway: Sequence 8

> **Lore:** A Clown buries sorrow behind a smile—reading people, defying balance, and trusting intuition even when fate feels unchangeable.

## Clown

- Skilled in deft combat with exceptional physical coordination, agility, and speed, and decent Strength.
- Can rely on intuition to predict a target’s next move.
- Can use ordinary paper as a weapon.
- Can effectively read facial expressions and body language, making lies easier to believe.

## Advancement

### Main Materials

- Adult Honakis gray goat horn crystal ×1 [[Honakis gray goat]]
- Rose with a complete human face ×1 [[Rose with a complete human face]]

### Auxiliary Materials

- Pure water 80ml
- Datura juice 5 drops [[Datura juice]]
- Black edge sun flower powder 7 grams [[Black edge sun flower powder]]
- Golden mantle grass powder 10 grams [[Golden mantle grass powder]]
- Poison violet juice 3 drops [[Poison violet juice]]

## Acting Rules

- Can slightly predict fate, but feel helpless about fate.
- Cover all sadness, pain, confusion, and frustration with a smiling face.

## Extraordinary Abilities

### Attribute Gain

- Strength +1
- Constitution +2
- Agility (DEX) +2
- Intuition (INT) +1 Intuition
- Performance and Deceit increase by 1 level [[Performance]] [[Deceit]]

In addition, from now on you will not lose your balance. If you fall, one of your limbs will land firmly. As long as there are still limbs touching the ground, you can stabilize your center of gravity. Even if you fall from a train, as long as you still have a support point, you can still perform acrobatic bounces.

### Premonition of Danger

```yaml ability
id: fool-seq-08-premonition-of-danger
name: Premonition of Danger
pathway: fool
sequence: 8
status: canonical
type: reaction
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Triggered appraisal check against DV 15 to identify incoming danger profile.
scaling:
- when: sequence <= 7
  changes:
    effect_note: Premonition output upgrades from thought flashes to image flashes.
- when: sequence <= 6
  changes:
    check_note: Intuition identification auto-succeeds.
- when: sequence <= 5
  changes:
    target: multiple attackers
tags:
- divination
- detection
- defense
text: 'Also known as intuitive premonition: you can predict the actions of others
  at critical moments and perceive danger. Use: Triggered whenever you are raided,
  sneak attacked, or something on the scene is about to put a raid or sneak attack
  into action. [[Raid]] [[Sneak Attack]] Use (additional trigger): If a single instance
  of damage exceeds half of your maximum health (rounded up), this ability can also
  be triggered. [[Maximum health]] [[Damage instance]] When triggered, resolve the
  following: Make an Intuition (INT) appraisal (Difficulty Value 15). [[Appraisal]]
  Difficulty Value On success, an idea flashes in your mind immediately, telling you
  the form the danger will take. After you succe...'
```





Also known as intuitive premonition: you can predict the actions of others at critical moments and perceive danger.

- **Use:** Triggered whenever you are raided, sneak attacked, or something on the scene is about to put a raid or sneak attack into action. [[Raid]] [[Sneak Attack]]
- **Use (additional trigger):** If a single instance of damage exceeds half of your maximum health (rounded up), this ability can also be triggered. [[Maximum health]] [[Damage instance]]

When triggered, resolve the following:

1. Make an Intuition (INT) appraisal (**Difficulty Value** 15). [[Appraisal]] Difficulty Value
   - On success, an idea flashes in your mind immediately, telling you the form the danger will take.
   - After you succeed, you cannot be raided or ambushed.
   - Threats you mistakenly think are “safe” do not trigger this ability.
2. Under the above premise, as long as you are not restrained or otherwise prevented, your **physical defense** gains a +4 temporary bonus. [[Physical Defense]] [[Restrained]]
   - Against light and lightning, you retain the agility and dodge in physical defense instead of applying the +4 value. [[Light]] [[Lightning]] Dodge
3. If the danger’s area is large enough (e.g., a gas explosion across the entire area instantly), even if you are alerted to the danger, you do not gain these benefits. [[Area effect]]

- **Special:**
  - Dangers higher than 1 level cannot be foreseen. [[Danger level]]
  - Hazards dependent on luck are foreseeable, but you gain no benefit.
- **Limits:**
  - As a kind of spiritual intuition, danger premonition is invalidated by anti-divination and anti-prophecy. [[Spiritual intuition]] [[id:alias-anti-divination|Anti-divination]] [[Anti-Prophecy]]

**Sequence progression (future improvements):**
- Sequence 7: The mind changes from flashing thoughts to flashing images, directly showing the manifestation of danger if not avoided.
- Sequence 6: Your Intuition (INT) identification succeeds by default. Identification
- Sequence 5: You can foresee danger from multiple persons (more than one attacker).

- **Effect:** Premonition of Danger resolves using its yaml ability block and section prose.


### Turn Paper into Flying Knives

```yaml ability
id: fool-seq-08-turn-paper-into-flying-knives
name: Turn Paper into Flying Knives
pathway: fool
sequence: 8
status: adapted
type: active
action: attack
cost: {}
roll: 1d20 + @attr.dex + @skill.throwing
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.dex + @skill.throwing
  damage_roll: 1d4 + @attr.str
  heal_roll: null
  effect_roll: null
  notes: Strength contribution is halved per prose rule; parser stores full attribute token and applies half-strength at resolution layer.
scaling:
- when: second_card_same_attack_action
  changes:
    check_penalty: -2
- when: third_card_same_attack_action
  changes:
    check_penalty: -4
tags:
- offense
text: 'The soft paper in your hand can turn into flying knives and fly out; this belongs
  to the magic class. [[Magic class]] Use: 1 Attack Action. Attack Action Effect:
  Turn paper and tarot cards into flying blades and throw them, dealing 1d4 + half
  Strength damage die. [[Strength Damage Die]] [[Tarot Cards]] Additional rules: Strength
  damage dice are rounded up to cause physical damage, and are rolled against physical
  defense. [[Physical Damage]] You can hit consecutively with flying blades and choose
  multiple targets. You can shoot 3 cards in a row with one Attack Action. Starting
  from the second card, you take 2 Disadvantages when making the identification throw;
  you take 4 Disadvantages for...'
```





The soft paper in your hand can turn into flying knives and fly out; this belongs to the magic class. [[Magic class]]

- **Use:** 1 Attack Action. Attack Action
- **Effect:** Turn paper and tarot cards into flying blades and throw them, dealing 1d4 + half Strength damage die. [[Strength Damage Die]] [[Tarot Cards]]

Additional rules:

1. Strength damage dice are rounded up to cause physical damage, and are rolled against physical defense. [[Physical Damage]]
2. You can hit consecutively with flying blades and choose multiple targets.
   - You can shoot 3 cards in a row with one Attack Action.
   - Starting from the second card, you take 2 **Disadvantages** when making the identification throw; you take 4 **Disadvantages** for the third card, and so on, increasing. [[Disadvantages]]

- **Limits:** As described in this section's prose.


### Muscle Mastery

```yaml ability
id: fool-seq-08-muscle-mastery
name: Muscle Mastery
pathway: fool
sequence: 8
status: canonical
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Passive package; includes auto-success clauses for specific skill contexts instead of direct rolled activation.
scaling: []
tags:
- buff
- stealth
- mobility
- defense
- utility
text: 'Your precise mastery of muscles gives you an advantage in learning and fighting.
  Your muscle-related identification is +2 beneficial, including: fighting, throwing,
  shooting, performing, deceiving, stealth, etc. [[Beneficial]] Your stealth makes
  no sound. When listening against stealth, listening without extraordinary factors
  fails against you by default. [[Listening]] [[Extraordinary Factors]] You get fast
  dodge, keep complete physical defense against firearms (excluding light and lightning),
  and gain an extra level of dodge. [[id:alias-fast-dodge|Fast dodge]] [[Firearms]]
  [[Dodge level]] 1 quick action; does not consume Spirituality: your Performance/Climbing/Jumping
  identification succ...'
```





Your precise mastery of muscles gives you an advantage in learning and fighting.

1. Your muscle-related identification is +2 beneficial, including: fighting, throwing, shooting, performing, deceiving, stealth, etc. [[Beneficial]]
   - Your stealth makes no sound.
   - When listening against stealth, listening without extraordinary factors fails against you by default. [[Listening]] [[Extraordinary Factors]]
2. You get fast dodge, keep complete physical defense against firearms (excluding light and lightning), and gain an extra level of dodge. [[id:alias-fast-dodge|Fast dodge]] [[Firearms]] [[Dodge level]]
3. 1 quick action; does not consume **Spirituality**: your Performance/Climbing/Jumping identification succeeds by default, and in confrontations the result is treated as +4 favorable. [[Quick Action]] [[Spirituality]] [[Climbing]] [[Jumping]] [[Confrontation]]
4. The Extraordinary of the Visionary pathway cannot read your thoughts through body language by default. [[Read thoughts through body language]]
5. You learn muscle-related skills faster, once every 24 hours:
   - If you receive relevant courses and guidance, and the content is effective, authentic, non-repetitive, and lasts more than 2 hours, your related skills increase by 1 level. [[Skill level]]
  - To reach **Proficient**, you must complete 2 + 3 + 4 learnings in order; you cannot advance beyond **Proficient**.
   - (This is a potion benefit that cannot be recorded or stolen.) [[Potion benefit]]

- **Effect:** Muscle Mastery resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
