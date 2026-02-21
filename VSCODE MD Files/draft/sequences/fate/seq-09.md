---
title: 'Sequence 9: Monster'
id: fate-seq-09
tags:
- pathway:fate
- sequence:9
---






# Wheel of Fortune Pathway: Sequence 9

- **Non-interchangeable:** This Pathway is the only one that is not interchangeable.

> **Lore:** “Uniqueness” is solidified into [[Dice of Probability]], and its mythical creature is a mercury snake corresponding to the Tarot card [[Wheel of Fortune]].

## Monster

> **Lore:** You are a “super-inspired” type—often hearing voices others cannot hear, seeing things others cannot see, occasionally glimpsing the future, and sensing danger with sharp intuition. You may fall into trances, whispering words others cannot understand, and be regarded as a “monster.”

You gain the following extraordinary abilities.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +3.
- **Effect:** You can occasionally glimpse the future.

### Glimpse of the Future

```yaml ability
id: fate-seq-09-glimpse-of-the-future
name: Glimpse of the Future
pathway: fate
sequence: 9
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
text: 'Use: Triggered when you conduct an Intuition (INT)/Spiritual Intuition identification
  and the identification is a big success or big failure. Effect: When triggered,
  you see a future screen; the content is determined by the GM. If the Intuition (INT)
  identification exceeds 30, you can see ordinary future events, with results that
  are good for you. A big success usually represents a picture beneficial to you.
  A big failure represents a picture that is not good for you (it may be a crisis
  that does not tell you the solution). Whenever you take at least 3 hours of sufficient
  rest, this also triggers in your dream (the same effect as above). Limits:'
```





- **Use:** Triggered when you conduct an **Intuition (INT)**/**Spiritual Intuition** identification and the identification is a big success or big failure.
- **Effect:**
  1. When triggered, you see a “future screen”; the content is determined by the **GM**.
  2. If the Intuition (INT) identification exceeds 30, you can see ordinary future events, with results that are good for you.
  3. A big success usually represents a picture beneficial to you.
  4. A big failure represents a picture that is not good for you (it may be a crisis that does not tell you the solution).
  5. Whenever you take at least 3 hours of sufficient rest, this also triggers in your dream (the same effect as above).
- **Limits:**
  - The picture you see does not necessarily mean it will happen; the crisis can be prevented or stopped.

### Very High Intuition (INT)

```yaml ability
id: fate-seq-09-very-high-intuition-int
name: Very High Intuition (INT)
pathway: fate
sequence: 9
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
damage_types:
- sanity
- rationality
tags:
- debuff
text: 'Effect: You can often hear voices others cannot hear and see things others
  cannot see. Effect (choose/apply as triggered): Peeping: You can see the specialness
  of others and determine whether the other party belongs to the realm of immortality/corruption/darkness/sacred/cursed,
  but the information is not specific enough (for example, you can find a person who
  died a few days ago, but you dont know the specific reason). Special: If the witnessed
  special is higher than your Sequence by 1+, or has pollution, you immediately suffer
  the corresponding Sanity / Rationality loss. Listening: Whenever you carry out an
  Intuition (INT)-related skill appraisal and the result is 20, if there is a spiri...'
```





- **Effect:** You can often hear voices others cannot hear and see things others cannot see.
- **Effect (choose/apply as triggered):**
  1. **Peeping:** You can see the “specialness” of others and determine whether the other party belongs to the realm of immortality/corruption/darkness/sacred/cursed, but the information is not specific enough (for example, you can find a person who died a few days ago, but you don’t know the specific reason).
    - **Special:** If the witnessed special is higher than your Sequence by 1+, or has pollution, you immediately suffer the corresponding **Sanity / Rationality** loss.
  2. **Listening:** Whenever you carry out an Intuition (INT)-related skill appraisal and the result is ≥20, if there is a spirit within a 20-meter area, you can discover its existence through normally inaudible sound, or hear normally inaudible sound due to extraordinary factors.
     - **Special:** This often only takes effect for a moment; its existence can only be found within 1 second, or a small amount of sound can be heard.
  3. **Trance:** Whenever you see a future picture or listen to extraordinary content, you fall into a short **Semi-Trance** state: you whisper the information you got and enter a round of **Surprised**. You wake up when you receive any stimulus or hear a reminder.
     - **Limits:** This is passive, bound to potion benefits, and cannot be stolen or recorded.

### Premonition of Danger

```yaml ability
id: fate-seq-09-premonition-of-danger
name: Premonition of Danger
pathway: fate
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Intuition test determines danger warnings; DV 20 success grants immediate guidance.
scaling:
- when: check_result_meets_dv_20
  changes:
    effect_note: You are told what to do next to avoid the surprise or sneak attack.
- when: danger_attack_half_vitality_or_sanity
  changes:
    effect_note: Physical Defense gains +4 correction against the incoming danger.
- when: light_or_lightning_threat
  changes:
    effect_note: Full Physical Defense is retained against light/lightning threats.
- when: sequence_5_or_higher
  changes:
    effect_note: Danger premonition and undisturbed Spiritual Intuition succeed by default.
damage_types:
- sanity
- rationality
tags:
- divination
- defense
- offense
text: 'Effect: You have a keen intuition for danger and can foresee danger beyond
  your personality. Effect: Whenever you suffer any Surprised/Sneak Attack, you must
  perform a Difficulty Value 20 Intuition (INT) test. On a success, you are immediately
  told what you should do next to avoid the surprised/sneak attack. You usually dont
  know why you do this. Any attack that can cause half of your Vitality loss (rounded
  up) in one instance, or half of your Sanity / Rationality loss, is also included
  in the effect of (1). When this applies, your Physical Defense gains an additional
  +4 correction (affecting your Constitution Defense/Willpower Defense). When the
  effect of (2) is used against light/lightn...'
```





- **Effect:** You have a keen intuition for danger and can foresee danger beyond your personality.
- **Effect:**
  1. Whenever you suffer any **Surprised**/**Sneak Attack**, you must perform a **Difficulty Value** 20 **Intuition (INT)** test. On a success, you are immediately told what you should do next to avoid the surprised/sneak attack. You usually don’t know why you do this.
  2. Any attack that can cause half of your **Vitality** loss (rounded up) in one instance, or half of your **Sanity / Rationality** loss, is also included in the effect of (1). When this applies, your **Physical Defense** gains an additional +4 correction (affecting your **Constitution Defense**/**Willpower Defense**).
  3. When the effect of (2) is used against light/lightning, the full Physical Defense is retained instead.
  4. If the danger range is large enough (for example, a gas explosion across the entire area in an instant), then even if you are alerted to the danger, you do not gain benefits.
- **At Sequence 5:**
  - Your danger premonition test is successful by default.
  - Your Spiritual Intuition test is also successful by default when it is not disturbed.
  - Even if you are blind/deaf, you can start maintaining normal actions through Spiritual Intuition.
- **Limits:**
  - In the Semi-Trance state, this ability does not take effect.
  - The Intuition (INT) test for danger premonition does not cause the Semi-Trance state.

### Spiritual Vision
```yaml ability
id: fate-seq-09-spiritual-vision
name: Spiritual Vision
pathway: fate
sequence: 9
status: canonical
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Spiritual Vision is a sustained toggle; check_roll maps Spiritual Intuition checks while active.
scaling:
- when: spiritual_vision_active
  changes:
    check_bonus: 2
    effect_note: Spiritual Intuition tests gain +2 while the mode is maintained.
tags:
- ritual
- detection
- healing
- mobility
text: 'Use: 1 free action to activate. Cost: 1 spirituality point per round while
  active. Effect: While active, your vision gains the following benefits: Etheric
  body: You can directly see the health status of the target through aura color; directly
  find where the other partys body is uncomfortable/has a problem; and, through thin
  doors, confirm the number of people inside. Spiritual body: You can confirm whether
  an object/creature has spirituality. This cannot identify extraordinary people.
  It can also penetrate a door to see inside, identify whether there is ritual magic
  power in it, and penetrate the spiritual wall. Mental Body: You can see the color
  represented by the other persons emotions,...'
```





- **Use:** 1 **free action** to activate.
- **Cost:** 1 **spirituality point per round** while active.
- **Effect:** While active, your vision gains the following benefits:


  1. **Etheric body:** You can directly see the health status of the target through aura color; directly find where the other party’s body is uncomfortable/has a problem; and, through thin doors, confirm the number of people inside.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality. This cannot identify extraordinary people. It can also penetrate a door to see inside, identify whether there is ritual magic power in it, and penetrate the spiritual wall.
  3. **Mental Body:** You can see the color represented by the other person’s emotions, but only general content (for example, whether the other person is depressed or uneasy). This kind of negative emotion is usually a dark tone.
  4. **Astral body:** You cannot see the astral body.
  5. While in Spiritual Vision, your Spiritual Intuition test gains a +2 beneficial modifier.
- **Notes:**
  - Dead creatures are usually only dull in color and cannot be identified.
  - Spiritual materials usually have spirituality; the color of a material in Spiritual Vision usually represents its corresponding Pathway. This does not mean you can see the power of a **Beyonder** Pathway.
  - The colors seen in Spiritual Vision allow you to see each other in the dark, but you can only see the existence of color; it is still possible to get lost in the dark.
  - Unlike dead creatures, undead creatures have a deep black spirituality color instead of none.
- **Special:**
  - Spiritual Vision can see some ordinary spirit bodies by default (those that have not dissipated for 24 hours).
  - This cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
