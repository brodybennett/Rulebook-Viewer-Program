---
title: 'Sequence 0: The Fool'
id: fool-seq-00
tags:
- pathway:fool
- sequence:0
---






# Fool Pathway: Sequence 0

## The Fool

- See also: [[Fool]]

> **Lore:** The essence of this promotion is to make the promoted feel slightly uncoordinated, unnatural, and abnormal—so that a bit of the spirit transformed from everything resurfaces and regains some self-awareness, preventing them from losing themselves.

## Advancement

### Advancement Ritual

- **Ritual of Ascension:** Fool time, history, or fate once. [[Ritual of Ascension]] [[Fooling]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +1. Intuition
- If you fooled time or history when promoted, **Intuition (INT)** +1.
- If you fooled history when promoted, **Education** +1. [[Education]]
- Regardless of what you fooled to promote, your **History** skill increases by 1 skill level. [[History (Skill)]]

> **Lore:** Because you have become the incarnation representing the Fool and mastered the three powers of fooling (with only differences in which is stronger or weaker), the **History** skill increase applies no matter what you fooled to promote.

### Divine Gaze
```yaml ability
id: fool-seq-00-divine-gaze
name: Divine Gaze
pathway: fool
sequence: 0
status: canonical
type: reaction
action: none
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
  notes: Triggered by True Name recitation; no explicit random roll in source text.
scaling: []
tags:
- utility
text: 'Use: When any creature recites your True Name. Effect: You can gaze at the
  surroundings of that creature, and use your extraordinary abilities to target the
  area at will.'
```





- **Use:** When any creature recites your **True Name**.
- **Effect:** You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.

- **Limits:** As described in this section's prose.



### God of Blindness and Foolishness

```yaml ability
id: fool-seq-00-god-of-blindness-and-foolishness
name: God of Blindness and Foolishness
pathway: fool
sequence: 0
status: canonical
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- utility
text: 'Effect: You gain the following abilities: Aura of Foolishness Fooling'
```





- **Effect:** You gain the following abilities:
  - **Aura of Foolishness**
  - **Fooling**

- **Limits:** As described in this section's prose.


### Aura of Foolishness

```yaml ability
id: fool-seq-00-aura-of-foolishness
name: Aura of Foolishness
pathway: fool
sequence: 0
status: canonical
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: field of vision
target: creatures in sight
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Aura-state effect with deterministic caps and insanity rider; no explicit contested roll in source text.
scaling: []
tags:
- detection
- control
text: 'Effect: All creatures within your field of vision have their Intuition (INT)
  capped at 1 (cannot exceed 1). [[Field of Vision]] If a creature becomes insane
  due to a Sanity / Rationality roll, it is immediately incapacitated and cannot take
  any actions until the insanity ends. [[Sanity / Rationality Roll]] [[Incapacitated]]
  [[Insanity]]'
```





- **Effect:** All creatures within your **field of vision** have their **Intuition (INT)** capped at 1 (cannot exceed 1). [[Field of Vision]]
- If a creature becomes insane due to a **Sanity / Rationality roll**, it is immediately **incapacitated** and cannot take any actions until the insanity ends. [[Sanity / Rationality Roll]] [[Incapacitated]] [[Insanity]]

- **Limits:** As described in this section's prose.


### Fooling

```yaml ability
id: fool-seq-00-fooling
name: Fooling
pathway: fool
sequence: 0
status: adapted
type: active
action: free
cost: {}
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: difficulty_value
range: self
target: one creature or one resolved action instance
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted check model for uncertainty-heavy uses; baseline effect remains immediate cancellation of one resolved action and its consequences.
scaling:
- when: same_target_again_in_same_round
  changes:
    effect_note: Cannot be used on the same creature more than once per round.
tags:
- ritual
- offense
- control
text: 'Use: Free action. Free Action Limits: Can be used only once on the same creature
  in a round. Round Effect: You declare that what has happened does not exist. When
  you declare that a thing that happened does not exist, 1 action and all consequences
  of that action disappear; you cancel the damage it caused, the ability used, and
  its result. Aftereffects: This ability does not return spirituality lost through
  using the ability. [[Spirituality]]'
```





- **Use:** **Free action**. Free Action
- **Limits:** Can be used only once on the same creature in a **round**. Round
- **Effect:** You declare that what has happened does not exist. When you declare that a thing that happened does not exist, 1 action and all consequences of that action disappear; you cancel the damage it caused, the ability used, and its result.
- **Aftereffects:** This ability does not return **spirituality** lost through using the ability. [[Spirituality]]
