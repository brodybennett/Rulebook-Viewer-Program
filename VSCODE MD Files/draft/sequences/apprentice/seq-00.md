---
title: 'Sequence 0: Door'
id: apprentice-seq-00
tags:
- pathway:apprentice
- sequence:0
---






# Door Pathway: Sequence 0

## Door

- You can open or close all things related to the concept of “door” in the whole world, allowing a seal to be broken or strengthened within a certain period of time.
- You can create a space cage out of thin air.
- You can degenerate and destroy space, causing the target to collapse and be destroyed with the surrounding void, then be swallowed by darkness.

- **Uniqueness:** A pair of eyeballs that seem to be composed of pure starlight, containing layers of illusory doors.

## Advancement

### Advancement Ritual

- **Advancement Ritual (unofficial ceremony):** Allow yourself to break through the god level, the seal of **Sequence 0** level, and open the door of the seal belonging to **Sequence 0**.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** inspiration +2; pilot skill increased by 2 skill levels.

### Conceptualization

```yaml ability
id: apprentice-seq-00-conceptualization
name: Conceptualization
pathway: apprentice
sequence: 0
status: adapted
type: toggle
action: free
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
  effect_roll: "1"
  notes: Deterministic transformation-state token for automation; while active, Conceptualization ignores physical damage.
scaling:
- when: conceptualization_active
  changes:
    effect_note: Ignore all physical damage until the conceptual state ends.
damage_types:
- physical
tags:
- defense
- utility
text: 'Use: Free Action Effect: The Planeswalker ability of Sequence 0 undergoes a
  qualitative change. You can become a conceptual creature: your figure becomes distorted,
  instantly stained with bright starlight, and extremely illusoryas if turning into
  a star gateno longer like a physical creature, but closer to an aggregate of symbols
  such as roaming, star passage, key, and gate. Limits: In the conceptual creature
  state, you completely ignore any physical damage.'
```





- **Use:** **Free Action**
- **Effect:** The **Planeswalker** ability of **Sequence 0** undergoes a qualitative change. You can become a **conceptual creature**: your figure becomes distorted, instantly stained with bright starlight, and extremely illusory—as if turning into a star gate—no longer like a physical creature, but closer to an aggregate of symbols such as “roaming,” “star passage,” “key,” and “gate.”
- **Limits:** In the conceptual creature state, you completely ignore any physical damage.

### Void Collapse

```yaml ability
id: apprentice-seq-00-void-collapse
name: Void Collapse
pathway: apprentice
sequence: 0
status: canonical
type: active
action: cast
cost:
  spirituality: 50
roll: null
opposed_by: none
range: Select an area.
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
text: 'Cost: 50 points of Spirituality Use: Spellcasting Action Targeting and range:
  Select an area. Limits: You can use this ability at most 2 times per Encounter.
  Effect: You make space collapse and annihilate into nothingness. This is almost
  a death-level ability; even if the target is Sequence 0 of the Fool pathway, they
  must lose all their [[substitutes]] and, at the cost of being unable to maintain
  further survival, can barely avoid this blow.'
```





- **Cost:** 50 points of **Spirituality**
- **Use:** **Spellcasting Action**
- **Targeting and range:** Select an area.
- **Limits:** You can use this ability at most **2 times per Encounter**.
- **Effect:** You make space collapse and annihilate into nothingness. This is almost a death-level ability; even if the target is **Sequence 0** of the Fool pathway, they must lose all their [[substitutes]] and, at the cost of being unable to maintain further survival, can barely avoid this blow.

### Divine Gaze
```yaml ability
id: apprentice-seq-00-divine-gaze
name: Divine Gaze
pathway: apprentice
sequence: 0
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
- utility
text: 'Use: When any creature recites your True Name. Effect: You can gaze at the
  surroundings of that creature, and use your extraordinary abilities to target the
  area at will.'
```





- **Use:** When any creature recites your **True Name**.
- **Effect:** You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.

- **Limits:** As described in this section's prose.
