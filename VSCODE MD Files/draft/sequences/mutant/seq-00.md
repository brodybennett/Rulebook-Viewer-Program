---
title: 'Sequence 0: Chained'
id: mutant-seq-00
tags:
- pathway:mutant
- sequence:0
---





# Chained Pathway: Sequence 0

## Chained

- See also: Prisoner Pathway

> **Lore:** The Bound is the **True God** of the Prisoner Pathway.
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

### Chained Authority

```yaml ability
id: mutant-seq-00-chained-authority
name: Chained Authority
pathway: mutant
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
- defense
- control
text: You channel chained curse authority, balancing madness suppression against violent
  transformation and spirit-flesh instability.
```

- **Effect:** You channel chained curse authority, balancing madness suppression against violent transformation and spirit-flesh instability.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Chain of Reason

```yaml ability
id: mutant-seq-00-chain-of-reason
name: Chain of Reason
pathway: mutant
sequence: 0
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: willpower_defense
range: line of sight
target: designated target(s)
duration: 1 encounter
scaling: []
tags:
- control
- debuff
- defense
text: You bind a target's mental state with suppressive chain marks, dampening frenzy
  spikes and limiting extreme actions.
```

- **Effect:** You bind a target's mental state with suppressive chain marks, dampening frenzy spikes and limiting extreme actions.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.

### Cursed Metamorphosis

```yaml ability
id: mutant-seq-00-cursed-metamorphosis
name: Cursed Metamorphosis
pathway: mutant
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
- offense
- defense
text: You assume a chained monstrous form, gaining physical threat at the cost of
  tighter sanity and control requirements.
```

- **Effect:** You assume a chained monstrous form, gaining physical threat at the cost of tighter sanity and control requirements.
- **Limits:** Imputed from LoTM Wiki pathway references; refine with table-specific mechanics if needed.
