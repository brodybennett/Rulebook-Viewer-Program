---
title: 'Sequence 0: Abyss'
id: abyss-seq-00
tags:
- pathway:abyss
- sequence:0
---





# Abyss Pathway: Sequence 0

## Abyss

> **Lore:** Master the authority of [[Corruption]] and [[Curse]], [[Alien]], and so on.
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

### Abyss Authority

```yaml ability
id: abyss-seq-00-abyss-authority
name: Abyss Authority
pathway: abyss
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
- debuff
- control
text: You embody abyssal depravity and corruption, turning malice, filth, and curse-laden
  intent into constant supernatural pressure.
```

- **Effect:** You embody abyssal depravity and corruption, turning malice, filth, and curse-laden intent into constant supernatural pressure.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Corruption Bloom

```yaml ability
id: abyss-seq-00-corruption-bloom
name: Corruption Bloom
pathway: abyss
sequence: 0
type: active
action: swift
cost:
  spirituality: 1
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
id: abyss-seq-00-profane-curse-weave
name: Profane Curse Weave
pathway: abyss
sequence: 0
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: willpower_defense
range: 40m
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
