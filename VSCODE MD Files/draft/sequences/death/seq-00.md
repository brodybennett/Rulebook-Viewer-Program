---
title: 'Sequence 0: Death'
id: death-seq-00
tags:
- pathway:death
- sequence:0
---





# Death Pathway: Sequence 0

## Death

> **Lore:** Also known as "Eternal Sleeper".

- [[Deathmark]]
- Deathmark is the only mark in the Death Pathway.
## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Not explicitly specified in source (schema placeholder).

### Death Authority

```yaml ability
id: death-seq-00-death-authority
name: Death Authority
pathway: death
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
- summon
- control
- debuff
text: You embody death authority and river-like underworld law, granting natural command
  over spirits, corpses, and endings.
```

- **Effect:** You embody death authority and river-like underworld law, granting natural command over spirits, corpses, and endings.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Underworld Command

```yaml ability
id: death-seq-00-underworld-command
name: Underworld Command
pathway: death
sequence: 0
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: willpower_defense
range: line of sight
target: designated target(s)
duration: sustained
scaling: []
tags:
- summon
- control
- utility
text: You issue death-path commands to spirits and undead, suppressing rebellion and
  redirecting lower entities to your chosen task.
```

- **Effect:** You issue death-path commands to spirits and undead, suppressing rebellion and redirecting lower entities to your chosen task.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### River of Death

```yaml ability
id: death-seq-00-river-of-death
name: River of Death
pathway: death
sequence: 0
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: constitution_defense
range: 40m
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- offense
- debuff
- control
text: You invoke underworld chill and grave pressure, numbing vitality while inviting
  nearby dead spirits to converge on the target.
```

- **Effect:** You invoke underworld chill and grave pressure, numbing vitality while inviting nearby dead spirits to converge on the target.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
