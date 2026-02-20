---
title: 'Sequence 0: Red Priest'
id: red-priest-seq-00
tags:
- pathway:red-priest
- sequence:0
---





# Red Priest Pathway: Sequence 0

## Red Priest

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Start a war that sweeps the continent and win enough decisive battles to determine the war’s outcome.
## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Not explicitly specified in source (schema placeholder).

### Red Priest Authority

```yaml ability
id: red-priest-seq-00-red-priest-authority
name: Red Priest Authority
pathway: red-priest
sequence: 0
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
id: red-priest-seq-00-war-provocation
name: War Provocation
pathway: red-priest
sequence: 0
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: willpower_defense
range: 50m
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
id: red-priest-seq-00-flame-command
name: Flame Command
pathway: red-priest
sequence: 0
type: active
action: attack
cost:
  spirituality: 2
roll: null
opposed_by: physical_defense
range: 40m
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
