---
title: "Sequence <N>: <Sequence Name>"
id: "<pathway>-seq-<nn>"
tags: ["pathway:<pathway>", "sequence:<N>"]
---

# <Pathway> Pathway: Sequence <N> {#<pathway>-seq-<nn>}

## <Sequence Name> {#<pathway>-seq-<nn>-<sequence-name>}

- See also: [[<Pathway> Pathway]]

## Advancement {#<pathway>-seq-<nn>-advancement}

### Auxiliary Materials {#<pathway>-seq-<nn>-auxiliary-materials}

- **Auxiliary Materials:** <item> ×<n>, <item> ×<n>

### Advancement Ritual {#<pathway>-seq-<nn>-advancement-ritual}

- **Advancement Ritual:** <ritual description>

## Extraordinary Abilities {#<pathway>-seq-<nn>-extraordinary-abilities}

### Attribute Gain {#<pathway>-seq-<nn>-attribute-gain}

- **Attribute Gain:** <attribute> +<n>, <attribute> +<n>

### <Ability Name> {#<pathway>-seq-<nn>-<ability-slug>}

```yaml ability
id: "<pathway>-seq-<nn>-<ability-slug>"
name: "<Ability Name>"
pathway: "<pathway>"
sequence: <N>
type: "active"
action: "cast"
cost: {spirituality: 1}
roll: "1d20 + @attr.int + @skill.occultism + @bonus"
opposed_by: "difficulty_value"
range: "self"
target: "self"
duration: "instant"
scaling: []
tags: ["utility"]
text: "Describe mechanical effect and constraints in prose below."
```

- **Effect:**
- **Limits:**
