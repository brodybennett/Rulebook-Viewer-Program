---
title: 'Sequence 0: Demoness'
id: demoness-seq-00
tags:
- pathway:demoness
- sequence:0
---





# Demoness Pathway: Sequence 0

## Demoness

- Also known as:
  - "primordial witch"
  - "chaos witch"
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

### Demoness Authority

```yaml ability
id: demoness-seq-00-demoness-authority
name: Demoness Authority
pathway: demoness
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
- debuff
- control
- social
text: You embody calamity-tinted charm and cursecraft, blending seduction, deceit,
  and misfortune into a single supernatural style.
```

- **Effect:** You embody calamity-tinted charm and cursecraft, blending seduction, deceit, and misfortune into a single supernatural style.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Mirror Transit

```yaml ability
id: demoness-seq-00-mirror-transit
name: Mirror Transit
pathway: demoness
sequence: 0
type: active
action: move
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- mobility
- stealth
- utility
text: You traverse adjacent reflections to reposition and evade pursuit, using mirror
  pathways as short-range movement channels.
```

- **Effect:** You traverse adjacent reflections to reposition and evade pursuit, using mirror pathways as short-range movement channels.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Calamity Hex

```yaml ability
id: demoness-seq-00-calamity-hex
name: Calamity Hex
pathway: demoness
sequence: 0
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: willpower_defense
range: 50m
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- debuff
- control
- offense
text: You stamp a target with Demoness misfortune, biasing outcomes toward errors,
  social collapse, and escalating disaster.
```

- **Effect:** You stamp a target with Demoness misfortune, biasing outcomes toward errors, social collapse, and escalating disaster.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
