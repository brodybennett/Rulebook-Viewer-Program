---
title: 'Sequence 8: Barbarian'
id: black-emperor-seq-08
tags:
- pathway:black-emperor
- sequence:8
---






# Black Emperor Pathway: Sequence 8

> **Lore:** Problems that cannot be solved by law must be dealt with force; force is also a kind of rule.

## Barbarian

## Advancement

### Auxiliary Materials

- **Main Materials:** a stalk of crazy grass; solid unicorn crystal of the earth rhinoceros
- **Auxiliary Materials:** one deep-grained walnut; one lemon balm; 10ml of pure dew soaked from poplar bark; 100ml of spirits

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2; Constitution +1; Agility (DEX) +1; Willpower (WIL) +2
- **Skill Gain:** Fighting +1 level; Climbing +1 level; Survival +1 level

### Skill Growth Through Violence

```yaml ability
id: black-emperor-seq-08-skill-growth-through-violence
name: Skill Growth Through Violence
pathway: black-emperor
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
text: 'When you face a problem that is: non-repetitive, and challenging, and cannot
  be resolved by law, and you begin to resort to violence and successfully solve the
  matter (regardless of the outcome), choose one: Fighting a Fighting subdivision
  Climbing'
```





- When you face a problem that is:
  - non-repetitive, and
  - challenging, and
  - cannot be resolved by law,
  and you begin to resort to violence and **successfully solve** the matter (regardless of the outcome), choose one:
  - Fighting
  - a Fighting subdivision
  - Climbing
  - Survival  
  Increase the chosen skill by 1 level.
- This does not include bullying.
- “Challenging” means you tried to rely on the law, but the matter was beyond what the law can handle.
- Each skill can be quickly upgraded to **Proficient** at most.
- The number of growths (not just promotions) follows Sequence 9’s reputation growth rules.

- **Effect:** Skill Growth Through Violence resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Law of Wildness

```yaml ability
id: black-emperor-seq-08-law-of-wildness
name: Law of Wildness
pathway: black-emperor
sequence: 8
status: adapted
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
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Mapped from the explicit plus-1d6 Fighting damage rider; other bonuses are static modifiers.
scaling: []
tags:
- buff
- defense
- offense
text: For Barbarians, power is also a kind of ruleanother rule besides law. Gain a
  beneficial +2 to Strength-related skills and [[Attribute Identification]]; Fighting
  damage increases by +1d6. This is described as being enough to blow the wall out
  of spider web traces with one punch and make the building tremble. [[Spider Web]]
  Gain [[id:alias-fast-dodge|Fast Dodge]]; against firearms, retain full Physical
  Defense; light and lightning are unaffected; and gain +1 Dodge level. Dodge [[Firearms]]
  Whenever you look for water, food, or other survival resources in a primitive or
  social environment, gain a beneficial +2 to [[Survival Identification]].
```





- For Barbarians, power is also a kind of rule—another rule besides law.

1. Gain a beneficial +2 to Strength-related skills and [[Attribute Identification]]; Fighting damage increases by +1d6. This is described as being enough to blow the wall out of “spider web” traces with one punch and make the building tremble. [[Spider Web]]
2. Gain [[id:alias-fast-dodge|Fast Dodge]]; against firearms, retain full Physical Defense; light and lightning are unaffected; and gain +1 **Dodge** level. Dodge [[Firearms]]
3. Whenever you look for water, food, or other survival resources in a primitive or social environment, gain a beneficial +2 to [[Survival Identification]].

> **GM Note:** “Survival resources” must be direct materials (excluding written materials) and may include various animals and creatures. The definition is broad: you may search for a species (including humans) and identify whether food is edible.

> **GM Note:** This effect is brought by the potion and cannot be stolen or recorded.

- **Effect:** Law of Wildness resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Mental Resistance

```yaml ability
id: black-emperor-seq-08-mental-resistance
name: Mental Resistance
pathway: black-emperor
sequence: 8
status: adapted
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
  effect_roll: 1d3
  notes: Mapped from the explicit sanity-loss example of 1d3 on failed Sanity and Rationality loss tests.
scaling: []
tags:
- defense
text: 'You have fairly high resistance to mental influences. Whenever your Sanity
  / Rationality is deducted [[Sanity / Rationality]]: Reduce the deducted Sanity /
  Rationality value by 1 (treat it as -1). The deduction cannot be reduced below 0.
  Example: If you suffer a Sanity / Rationality loss of 1/1d3, you lose 1 Sanity /
  Rationality on a successful [[Sanity / Rationality Loss Test]] and 1d3 Sanity /
  Rationality on a failure. With this ability: On a success: 1 1 = 0 (no Sanity /
  Rationality loss). On a failure: 1d3 1 Sanity / Rationality.'
```





- You have fairly high resistance to mental influences.
- Whenever your **Sanity / Rationality** is deducted [[Sanity / Rationality]]:
  - Reduce the deducted Sanity / Rationality value by 1 (treat it as “-1”).
  - The deduction cannot be reduced below 0.
- Example: If you suffer a Sanity / Rationality loss of **1/1d3**, you lose 1 Sanity / Rationality on a successful [[Sanity / Rationality Loss Test]] and 1d3 Sanity / Rationality on a failure. With this ability:
  - On a success: 1 − 1 = 0 (no Sanity / Rationality loss).
  - On a failure: 1d3 − 1 Sanity / Rationality.

> **GM Note:** This effect is brought by the potion and cannot be stolen or recorded. See [[Madness and Loss of Control]] for details on Sanity / Rationality loss.

- **Effect:** Mental Resistance resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
