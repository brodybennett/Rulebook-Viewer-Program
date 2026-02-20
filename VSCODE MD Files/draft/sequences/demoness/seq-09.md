---
title: 'Sequence 9: Assassin'
id: demoness-seq-09
tags:
- pathway:demoness
- sequence:9
---





# Demoness Pathway: Sequence 9

## Assassin

> **Lore:** The form of mythical creatures is female sexuality, thick hair like a snake, and spider silk coiled around the body, corresponding to the Tarot card as "Queen".

Assassins can briefly alter their body, move with feather-like lightness, harden sharp sight and dark vision, excel at fighting and dodging, and hide in shadows with dexterous stepsâ€”bursting with full power in a single blow.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute gain:** Strength +2, Constitution +1, Agility (DEX) +2.
- You can better learn:
  - [[Fighting (Hand-to-Hand Combat)]]
  - Detection
  - [[Stealth]]
  - Dodge
  - [[Throwing]]
  - [[Jumping]]
  - [[Swimming]]
- Every 2 hours, you receive non-repetitive, effective related guidance; gain 1 growth point for the corresponding skill.
  1. To reach **Proficient**, you must complete 2 + 3 + 4 learnings in order; you cannot advance beyond **Proficient**.
  2. Every time you assassinate a target that is stronger than you, it is also considered as a growth. Selecting any of the above skills is regarded as a learning. The learning is limited to one time per day, but the growth brought by the assassination is not counted.
- When creating a character that has not just been promoted, you can use the corresponding skill-related attributes brought by the [[Potion]] to add growth skills; treat **Intuition (INT)** as growth points.

### Body Change

```yaml ability
id: demoness-seq-09-body-change
name: Body Change
pathway: demoness
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- stealth
- mobility
- control
- debuff
text: 'Use: 1 Casting Action. Effect: You adjust your physiology to gain the properties
  of feathers, hawk-like lightness. Within 1 round (6 seconds), your body can be as
  light as a feather walking on the moon. In this state, your climbing, jumping, swimming,
  and stealth identifications are all successful by default. When confronting, it
  will be changed to +4 favorable. Because the body is light and easy to control,
  at the height of about the fifth and sixth floors of modern times (18a28 meters),
  you will not be hurt by falling. You will fall slowly like a feather, and you will
  not lose your balance or suffer impact injury (e.g., carriage/car). Even at a higher
  height, you only need to find a few...'
```




- **Use:** 1 **Casting Action**.
- **Effect:** You adjust your physiology to gain the properties of feathers, hawk-like lightness.
  1. Within 1 round (6 seconds), your body can be as light as a feather walking on the moon. In this state, your climbing, jumping, swimming, and stealth identifications are all successful by default. When confronting, it will be changed to +4 favorable.
  2. Because the body is light and easy to control, at the height of about the fifth and sixth floors of modern times (18â€“28 meters), you will not be hurt by falling. You will fall slowly like a feather, and you will not lose your balance or suffer impact injury (e.g., carriage/car).
  3. Even at a higher height, you only need to find a few support points as a transfer during the fall, and you will not be hurt by the fall.
- While in an altered state, you can make a [[Stealth]] check as a **Move Action**, even if you are being watched.
- At Sequence 7: Body Change requires only 1 **Swift Action**.

- **Limits:** As described in this section's prose.


### Sharp Sight

```yaml ability
id: demoness-seq-09-sharp-sight
name: Sharp Sight
pathway: demoness
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- detection
- mobility
text: 'Effect: Owl''s vision and darkvision are hardened on you, allowing you to see
  through darkness. You get dark vision; you can move in places without a ray of light.
  Your eyesight is like that of an eagle; you can see things within 1 km without occlusion.
  You can act normally at night and in the dark without any penalty.'
```




- **Effect:** Owl's vision and darkvision are hardened on you, allowing you to see through darkness.
  - You get dark vision; you can move in places without a ray of light.
  - Your eyesight is like that of an eagle; you can see things within 1 km without occlusion.
  - You can act normally at night and in the dark without any penalty.

- **Limits:** As described in this section's prose.


### Assassination Action

```yaml ability
id: demoness-seq-09-assassination-action
name: Assassination Action
pathway: demoness
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: self
duration: instant
scaling: []
tags:
- stealth
- defense
- offense
text: 'Effect: You can dexterously fight and dodge attacks in battle, grasp vital
  points in observation, and kill with one blow. As long as you are in the shadow/darkness,
  your stealth test is successful by default, and it is beneficial to +4 when confronting;
  this can be superimposed. It is beneficial to +2 special action appraisals such
  as [[Critical Strike]], [[Double Strike]], and [[Close Shot]], excluding first aid/surprise
  attack, and does not affect special actions that simply gain benefits. For example,
  gaining momentum and aiming will not change from +2 to +4. Only affects identification.
  Quick dodge: You use skills to retain complete physical defense against guns instead
  of light/light...'
```




- **Effect:** You can dexterously fight and dodge attacks in battle, grasp vital points in observation, and kill with one blow.
  1. As long as you are in the shadow/darkness, your stealth test is successful by default, and it is beneficial to +4 when confronting; this can be superimposed.
  2. It is beneficial to +2 special action appraisals such as [[Critical Strike]], [[Double Strike]], and [[Close Shot]], excluding first aid/surprise attack, and does not affect special actions that simply gain benefits. For example, gaining momentum and aiming will not change from +2 to +4. Only affects identification.
  3. **Quick dodge:** You use skills to retain complete physical defense against guns instead of light/lightning, and get an extra level of dodge.
- This is the effect brought by a [[Potion]]; it cannot be stolen or recorded.
  > **GM Note:** You should try more raids/sneak attacks. For details, see the benefits this can bring you in [[Special Actions]], and the invisibility starting from Sequence 7 (more favorable conditions for raids).

- **Limits:** As described in this section's prose.


### Poised Burst

```yaml ability
id: demoness-seq-09-poised-burst
name: Poised Burst
pathway: demoness
sequence: 9
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- mobility
- offense
text: 'Use: Accompanied by 1 attack/move/Swift Action. Cost: Consume 2 spiritual points.
  Limits: Only once every 5 minutes. Effect: You burst all your strength in 1 hit.
  Choose 1 of the following effects: The strength damage dice are counted twice (effective
  for double hits). For example, an assassin with 8 strength points has strength damage
  dice of 1d12, then it is counted as 2d12 in the burst hit. The strength attribute
  is counted twice: 8 points of the strength attribute are counted twice in a strength
  or combat appraisal, and it is regarded as 16. Skills related to strength, such
  as climbing and jumping, also enjoy this benefit. (Moving actions can also enjoy
  this benefit, because the dista...'
```




- **Use:** Accompanied by 1 attack/move/Swift Action.
- **Cost:** Consume 2 **spiritual points**.
- **Limits:** Only once every 5 minutes.
- **Effect:** You burst all your strength in 1 hit. Choose 1 of the following effects:
  1. The strength damage dice are counted twice (effective for double hits). For example, an assassin with 8 strength points has strength damage dice of 1d12, then it is counted as 2d12 in the burst hit.
  2. The strength attribute is counted twice: 8 points of the strength attribute are counted twice in a strength or combat appraisal, and it is regarded as 16. Skills related to strength, such as climbing and jumping, also enjoy this benefit.  
     (Moving actions can also enjoy this benefit, because the distance that can be moved by one moving action is "strength + agility", so the repeated calculation of strength will lead to an increase in moving speed.)
- **Aftereffects (Negative effects):**
  1. After using this blow, regardless of whether the blow succeeds or fails, the strength attribute and strength damage dice within 2 rounds will be temporarily cleared, regardless of whether you choose the strength attribute benefit or the strength damage benefit.
  2. Therefore, assuming that this blow is used in the first round, then until the third round of the assassin's action, the assassin's strength attribute and strength damage dice are regarded as 0.

### Vision
```yaml ability
id: demoness-seq-09-vision
name: Vision
pathway: demoness
sequence: 9
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
scaling: []
tags:
- ritual
- detection
text: 'Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect:
  You activate vision, and your vision gains the following benefits: Etheric body:
  You can roughly tell whether the other partyaTMs body is good or bad through the
  color of the aura, but you canaTMt get detailed information. Spiritual body: You
  can confirm whether an object/creature has spirituality, which cannot identify extraordinary
  people. Mental body: You can see whether the other party is thinking, but only so,
  and you cannot get more detailed information. Astral body: You cannot see the astral
  body. When in the state of spiritual vision, your spiritual intuition test +1 is
  beneficial.'
```




- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate vision, and your vision gains the following benefits:


  1. **Etheric body:** You can roughly tell whether the other partyâ€™s body is good or bad through the color of the aura, but you canâ€™t get detailed information.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality, which cannot identify extraordinary people.
  3. **Mental body:** You can see whether the other party is thinking, but only so, and you cannot get more detailed information.
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your spiritual intuition test +1 is beneficial.
- Notes:
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding path.
  - The colors seen by the spirit vision allow you to see each other in the dark, but you can only see the existence of colors. It is still possible to get lost in the dark because the colors you can see are limited, so you cannot use them to distinguish the undead biology.
- Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.  
  - In this section, "Vision," "spiritual vision," and "Spirit Vision" all refer to [[id:alias-spirit-vision|Spirit Vision]].

- **Limits:** As described in this section's prose.
