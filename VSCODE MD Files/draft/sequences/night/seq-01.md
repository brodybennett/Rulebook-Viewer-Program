---
title: 'Sequence 1: Knight of Misfortune'
id: night-seq-01
tags:
- pathway:night
- sequence:1
---





# Darkness Pathway: Sequence 1

## Knight of Misfortune

- See also: Dark Path Pathway

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

### Knight of Misfortune Authority

```yaml ability
id: night-seq-01-knight-of-misfortune-authority
name: Knight of Misfortune Authority
pathway: night
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
- stealth
- control
- debuff
text: You embody darkness and dream authority, masking presence while letting fear,
  slumber, and concealment spread naturally.
```

- **Effect:** You embody darkness and dream authority, masking presence while letting fear, slumber, and concealment spread naturally.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Dream Infiltration

```yaml ability
id: night-seq-01-dream-infiltration
name: Dream Infiltration
pathway: night
sequence: 1
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: willpower_defense
range: line of sight
target: designated target(s)
duration: sustained
scaling: []
tags:
- control
- debuff
- stealth
text: You drag a target's awareness toward a dreamlike state, disrupting judgment
  and opening them to nightmare suggestion.
```

- **Effect:** You drag a target's awareness toward a dreamlike state, disrupting judgment and opening them to nightmare suggestion.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Night Veil

```yaml ability
id: night-seq-01-night-veil
name: Night Veil
pathway: night
sequence: 1
type: toggle
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: 30m
target: designated target(s)
duration: sustained
scaling: []
tags:
- stealth
- defense
- control
text: You spread layered darkness that obscures movement and weakens hostile perception
  while allies operate under your concealment.
```

- **Effect:** You spread layered darkness that obscures movement and weakens hostile perception while allies operate under your concealment.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
