---
title: 'Sequence 1: White Angel'
id: sun-seq-01
tags:
- pathway:sun
- sequence:1
---





# Sun Pathway: Sequence 1

## White Angel

> **Lore:** An [[Archangel]] on the [[Sun]].
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

### White Angel Authority

```yaml ability
id: sun-seq-01-white-angel-authority
name: White Angel Authority
pathway: sun
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
- healing
- buff
text: You channel solar holiness and purification authority, burning corruption while
  stabilizing allies under radiant order.
```

- **Effect:** You channel solar holiness and purification authority, burning corruption while stabilizing allies under radiant order.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Purifying Radiance

```yaml ability
id: sun-seq-01-purifying-radiance
name: Purifying Radiance
pathway: sun
sequence: 1
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: constitution_defense
range: 40m
target: designated target(s)
duration: instant
scaling: []
tags:
- offense
- healing
- buff
text: You release concentrated sunlight that harms tainted entities and strips hostile
  curse residue from protected allies.
```

- **Effect:** You release concentrated sunlight that harms tainted entities and strips hostile curse residue from protected allies.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Holy Covenant

```yaml ability
id: sun-seq-01-holy-covenant
name: Holy Covenant
pathway: sun
sequence: 1
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: none
range: touch
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- buff
- defense
- utility
text: You establish a sacred contract that strengthens resolve and punishes clear
  oath-breaking under your witnessed light.
```

- **Effect:** You establish a sacred contract that strengthens resolve and punishes clear oath-breaking under your witnessed light.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
