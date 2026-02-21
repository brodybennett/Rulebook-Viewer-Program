---
title: 'Sequence 3: Wanderer'
id: apprentice-seq-03
tags:
- pathway:apprentice
- sequence:3
---






# Door Pathway: Sequence 3

> **Lore:** You can roam the starry sky.  
> **Lore:** “So far, your journey has set foot on the stars”

## Wanderer

## Advancement

### Advancement Ritual

- **Requirement:** The ritual must be completed in at least **75%** of relevant places.

> **GM Note:** The source labels this as an “unofficial ceremony.”

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** inspiration +2, charisma +2, education +1, pilot skill increased by 2 skill levels.

### Freedom of Action

```yaml ability
id: apprentice-seq-03-freedom-of-action
name: Freedom of Action
pathway: apprentice
sequence: 3
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
- ritual
- mobility
- control
text: 'Effect: No effect can imprison the Wanderer. Effect: You are immune to bondage,
  binding, and all adverse effects of the environment on you. Limits: The [[Spiritual
  Body Thread]] has no effect on reducing your movements, but it can still turn you
  into a [[Secret Puppet]]. Limits: The [[Judge]] and the [[Black Emperor]] cannot
  restrain your actions.'
```





- **Effect:** No effect can imprison the Wanderer.
- **Effect:** You are immune to bondage, binding, and all adverse effects of the environment on you.
- **Limits:** The [[Spiritual Body Thread]] has no effect on reducing your movements, but it can still turn you into a [[Secret Puppet]].
- **Limits:** The [[Judge]] and the [[Black Emperor]] cannot restrain your actions.

### Tolerate the Environment

```yaml ability
id: apprentice-seq-03-tolerate-the-environment
name: Tolerate the Environment
pathway: apprentice
sequence: 3
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.con
opposed_by: difficulty_value
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.con
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted resilience roll token for edge-case environmental adjudication; base immunity to environmental damage is deterministic.
scaling:
- when: damage_source_is_environmental_hazard
  changes:
    effect_note: Environmental damage is ignored.
tags:
- defense
- utility
text: 'Effect: There is no environment that you cannot adapt to. Effect: You are immune
  to any damage caused by the environment, which can make the harsh environment of
  various planets no longer have a significant impact on you.'
```





- **Effect:** There is no environment that you cannot adapt to.
- **Effect:** You are immune to any damage caused by the environment, which can make the harsh environment of various planets no longer have a significant impact on you.

- **Limits:** As described in this section's prose.


### Symbol Positioning

```yaml ability
id: apprentice-seq-03-symbol-positioning
name: Symbol Positioning
pathway: apprentice
sequence: 3
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
  notes: No explicit dice expression in source text.
scaling: []
tags:
- detection
- stealth
- control
text: 'Effect: You obtain an extraordinary symbol. Whoever outlines this symbol or
  writes it on the ground, you can use a free action to observe, detect, or perceive
  everything around this symbol. Use: This is actively triggered and cannot be passively
  sensed. Limits: You can only sense the change at the moment when the symbol appears
  or the symbol is destroyed: you notice that someone has drawn the corresponding
  symbol, or the corresponding symbol disappearsnothing else. Limits: If you put the
  symbol in a territory that is not under your control, it may cause detection of
  you by an equal or higher level without concealment. Effect: As long as the symbol
  exists in a certain location, the locatio...'
```





- **Effect:** You obtain an extraordinary symbol. Whoever outlines this symbol or writes it on the ground, you can use a **free action** to observe, detect, or perceive everything around this symbol.
- **Use:** This is actively triggered and cannot be passively sensed.
- **Limits:** You can only sense the change at the moment when the symbol appears or the symbol is destroyed: you notice that someone has drawn the corresponding symbol, or the corresponding symbol disappears—nothing else.
- **Limits:** If you put the symbol in a territory that is not under your control, it may cause detection of you by an equal or higher level without concealment.
- **Effect:** As long as the symbol exists in a certain location, the location of the symbol is considered to be a coordinate in the [[spirit world]] or [[astral world]]. You can sense the specific location and travel long distances to get there as a **Casting Action**.
- **Limits:** The initial isolation of the spirit world may lead to the invalidation of this symbol. But because the spirit world cannot be completely isolated, its vague connection with you still exists.

### Fly

```yaml ability
id: apprentice-seq-03-fly
name: Fly
pathway: apprentice
sequence: 3
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
- mobility
text: 'Effect: You gain the ability to fly, allowing you to perform supersonic flawless
  flight.'
```





- **Effect:** You gain the ability to fly, allowing you to perform supersonic flawless flight.

- **Limits:** As described in this section's prose.


### Teleportation (Astral Shuttle)

```yaml ability
id: apprentice-seq-03-teleportation-astral-shuttle
name: Teleportation (Astral Shuttle)
pathway: apprentice
sequence: 3
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
- mobility
- buff
text: 'Effect: Your teleportation ability is greatly enhanced, and you can even use
  [[astral teleportation]] to travel to other starry skies and planets. See also:
  For details about the [[Star Realm]], see [[Chapter Twelve: Special Regions]].'
```





- **Effect:** Your teleportation ability is greatly enhanced, and you can even use [[astral teleportation]] to travel to other starry skies and planets.
- **See also:** For details about the [[Star Realm]], see [[Chapter Twelve: Special Regions]].

- **Limits:** As described in this section's prose.
