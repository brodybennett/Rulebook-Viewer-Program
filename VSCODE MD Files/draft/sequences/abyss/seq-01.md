---
title: 'Sequence 1: Filthy Monarch'
id: abyss-seq-01
tags:
- pathway:abyss
- sequence:1
---





# Abyss Pathway: Sequence 1

## Filthy Monarch

## Filthy Monarch

> **Lore:** Wields the power to defile, corrode, pollute, and similar effects.
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

### Filthy Monarch Authority

```yaml ability
id: abyss-seq-01-filthy-monarch-authority
name: Filthy Monarch Authority
pathway: abyss
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
- debuff
- control
text: You embody abyssal depravity and corruption, turning malice, filth, and curse-laden
  intent into constant supernatural pressure.
```

- **Effect:** You embody abyssal depravity and corruption, turning malice, filth, and curse-laden intent into constant supernatural pressure.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Corruption Bloom

```yaml ability
id: abyss-seq-01-corruption-bloom
name: Corruption Bloom
pathway: abyss
sequence: 1
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: constitution_defense
range: line of sight
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- debuff
- offense
- control
text: You plant abyssal corruption in body and spirit, degrading resistance and making
  later curse effects harder to purge.
```

- **Effect:** You plant abyssal corruption in body and spirit, degrading resistance and making later curse effects harder to purge.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Profane Curse Weave

```yaml ability
id: abyss-seq-01-profane-curse-weave
name: Profane Curse Weave
pathway: abyss
sequence: 1
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: willpower_defense
range: 30m
target: designated target(s)
duration: sustained
scaling: []
tags:
- debuff
- control
- offense
text: You layer conditional curses that punish movement, betrayal, or reckless action
  until the target breaks the bind.
```

- **Effect:** You layer conditional curses that punish movement, betrayal, or reckless action until the target breaks the bind.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
