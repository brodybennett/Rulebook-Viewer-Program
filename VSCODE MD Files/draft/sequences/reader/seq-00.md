---
title: 'Sequence 0: White Tower'
id: reader-seq-00
tags:
- pathway:reader
- sequence:0
---





# White Tower Pathway: Sequence 0

## White Tower

> **Lore:** The [[True God]] of the [[White Tower]].
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

### White Tower Authority

```yaml ability
id: reader-seq-00-white-tower-authority
name: White Tower Authority
pathway: reader
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
- utility
- divination
- buff
text: You hold White Tower style cognitive authority, reconstructing truth from fragments
  and rapidly assimilating hidden knowledge.
```

- **Effect:** You hold White Tower style cognitive authority, reconstructing truth from fragments and rapidly assimilating hidden knowledge.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Thought Reconstruction

```yaml ability
id: reader-seq-00-thought-reconstruction
name: Thought Reconstruction
pathway: reader
sequence: 0
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: willpower_defense
range: line of sight
target: designated target(s)
duration: instant
scaling: []
tags:
- divination
- utility
- detection
text: You rebuild a target's likely intent chain from micro-signals, exposing lies,
  hesitation points, and exploitable reasoning gaps.
```

- **Effect:** You rebuild a target's likely intent chain from micro-signals, exposing lies, hesitation points, and exploitable reasoning gaps.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Knowledge Cascade

```yaml ability
id: reader-seq-00-knowledge-cascade
name: Knowledge Cascade
pathway: reader
sequence: 0
type: toggle
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: sustained
scaling: []
tags:
- buff
- utility
- divination
text: You enter a high-load calculation state that boosts analysis and ritual interpretation
  while steadily consuming mental resources.
```

- **Effect:** You enter a high-load calculation state that boosts analysis and ritual interpretation while steadily consuming mental resources.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
