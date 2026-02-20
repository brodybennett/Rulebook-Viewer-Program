---
title: 'Sequence 2: Death Consul'
id: death-seq-02
tags:
- pathway:death
- sequence:2
---





# Death Pathway: Sequence 2

## Death Consul

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Get the approval of the underworld, change an order of the underworld, and let the law of death engrave your eternal name. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Constitution (CON) +1

### Death Consul Authority

```yaml ability
id: death-seq-02-death-consul-authority
name: Death Consul Authority
pathway: death
sequence: 2
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
id: death-seq-02-underworld-command
name: Underworld Command
pathway: death
sequence: 2
type: active
action: full-round
cost:
  spirituality: 3
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
id: death-seq-02-river-of-death
name: River of Death
pathway: death
sequence: 2
type: active
action: full-round
cost:
  spirituality: 4
roll: null
opposed_by: constitution_defense
range: 20m
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
