---
title: 'Sequence 1: Conqueror'
id: red-priest-seq-01
tags:
- pathway:red-priest
- sequence:1
---





# Red Priest Pathway: Sequence 1

**Pathway:** [[Red Priest]].

This entry describes **Sequence** 1: Conqueror.

## Conqueror

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Conquer a hostile nation of considerable power. [[Advancement Rituals]]

> **GM Note:** The source labels this ritual as an “unofficial ceremony.”

## Descriptive Notes

> **Lore:** Extraordinary characteristic appearance (see [[Beyonder Characteristic]]): a strange crown full of rust and blood.
## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Not explicitly specified in source (schema placeholder).

### Conqueror Authority

```yaml ability
id: red-priest-seq-01-conqueror-authority
name: Conqueror Authority
pathway: red-priest
sequence: 1
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- offense
- control
- buff
text: You embody war authority, converting conflict momentum into personal strength,
  command pressure, and battlefield initiative.
```

- **Effect:** You embody war authority, converting conflict momentum into personal strength, command pressure, and battlefield initiative.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### War Provocation

```yaml ability
id: red-priest-seq-01-war-provocation
name: War Provocation
pathway: red-priest
sequence: 1
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: willpower_defense
range: 40m
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- control
- debuff
- social
text: You ignite hostility and tunnel vision in enemies, forcing poor tactical choices
  and destabilizing coordinated formations.
```

- **Effect:** You ignite hostility and tunnel vision in enemies, forcing poor tactical choices and destabilizing coordinated formations.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Flame Command

```yaml ability
id: red-priest-seq-01-flame-command
name: Flame Command
pathway: red-priest
sequence: 1
type: active
action: attack
cost:
  spirituality: 3
roll: null
opposed_by: physical_defense
range: 30m
target: designated target(s)
duration: instant
scaling: []
tags:
- offense
- control
- buff
text: You direct battlefield fire like a general's blade, striking priority targets
  and shaping movement through heat and fear.
```

- **Effect:** You direct battlefield fire like a general's blade, striking priority targets and shaping movement through heat and fear.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
