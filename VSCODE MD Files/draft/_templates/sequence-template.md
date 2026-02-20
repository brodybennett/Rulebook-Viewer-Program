---
title: "Sequence <N>: <Canonical Sequence Name>"
id: "<pathway>-seq-<nn>"
tags: ["pathway:<pathway>", "sequence:<N>"]
---

# <Canonical Pathway> Pathway: Sequence <N> {#<pathway>-seq-<nn>}

## <Canonical Sequence Name> {#<pathway>-seq-<nn>-<sequence-slug>}

- See also: [[<Canonical Pathway> Pathway]]
- Source note: lore naming should align with `meta/canon_sequences.yml` and `meta/canon_pathways.yml`.

## Advancement {#<pathway>-seq-<nn>-advancement}

### Main Materials {#<pathway>-seq-<nn>-main-materials}

- **Main Materials:** <item> x<n>; <item> x<n>

### Auxiliary Materials {#<pathway>-seq-<nn>-auxiliary-materials}

- **Auxiliary Materials:** <item> x<n>; <item> x<n>

### Advancement Ritual {#<pathway>-seq-<nn>-advancement-ritual}

- **Advancement Ritual:** <ritual description>

### Acting Rules {#<pathway>-seq-<nn>-acting-rules}

- <rule 1>
- <rule 2>

## Extraordinary Abilities {#<pathway>-seq-<nn>-extraordinary-abilities}

### Attribute Gain {#<pathway>-seq-<nn>-attribute-gain}

- **Attribute Gain:** <Attribute (ABBR)> +<n>; <Attribute (ABBR)> +<n>
- **Skill Gain:** <Skill> +<n level>; <Skill> +<n level>
- **Passive Effect:** <always-on rules gained at this sequence>

### <Ability Name> {#<pathway>-seq-<nn>-<ability-slug>}

```yaml ability
id: "<pathway>-seq-<nn>-<ability-slug>"
name: "<Ability Name>"
pathway: "<pathway>"
sequence: <N>
type: "active"
action: "cast"
cost: {spirituality: 1}
roll: null
opposed_by: "none"
range: "self"
target: "designated target"
duration: "instant"
scaling: []
tags: ["utility"]
text: "Short mechanical summary in one sentence."
```

- **Use:** <action economy or trigger>
- **Cost:** <resource use and cadence>
- **Targeting and Range:** <who/what can be affected, and from where>
- **Effect:** <mechanical resolution in plain language>
- **Limits:** <caps, immunities, exclusions, and edge constraints>
- **Sequence Upgrades:** <optional: how this ability changes at higher sequence>

## Notes {#<pathway>-seq-<nn>-notes}

- Keep exactly one `yaml ability` block per ability heading.
- Keep IDs stable after publication.
- Keep roll syntax compliant with `meta/roll_syntax.md`.
- Keep naming canonical to `meta/canon_terms.yml`.
