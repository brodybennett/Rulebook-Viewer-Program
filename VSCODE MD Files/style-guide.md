# --- Suggested style-guide.md ---
# Style Guide (LOTM RPG Rulebook)

This file is the *single source of truth* for formatting decisions.

## Goals
- Keep mechanics correct.
- Keep structure predictable so links, search, and UI all work.
- Minimize registry bloat by using stable anchors and (when needed) id-based links.

## File Frontmatter
Every file starts with:

```yaml
---
title: "<Title>"
id: "<top-level-id>"
tags: ["..."]
---
```

## Heading + Anchor Rules
- Every heading that should be linkable MUST include an anchor: `{#lowercase-hyphen-id}`.
- Anchor IDs are stable. If you rename a heading title, keep the same `{#id}`.

## Sequence File Template
Use the template in `draft/_templates/sequence-template.md` as your starting point.

### Standard Section Order (Sequences)
1) `# <Pathway> Pathway: Sequence <N> {#<pathway>-seq-<nn>}`
2) `## <Sequence Name> {#<pathway>-seq-<nn>-<sequence-name>}`
3) `## Advancement {#<pathway>-seq-<nn>-advancement}`
   - `### Auxiliary Materials {#...-auxiliary-materials}`
   - `### Advancement Ritual {#...-advancement-ritual}`
4) `## Extraordinary Abilities {#<pathway>-seq-<nn>-extraordinary-abilities}`
   - `### Attribute Gain {#...-attribute-gain}`
   - One `### <Ability Name> {#...}` per ability

## Ability Block Formatting
For each ability subsection, prefer a consistent bullet schema:
- **Cost:** ...
- **Use:** ...
- **Effect:** ...
- **Targeting and range:** ...
- **Limits:** ...
- **Duration:** ...
- **Aftereffects:** ...

Only include fields that actually exist in the rules text.

## Wiki-links
- Preferred for stable, unambiguous targets: `[[id:<anchor-id>|Display Text]]`.
- Allowed (title-based): `[[Exact Section Title]]`, but avoid for generic titles ("Advancement", "Ritual", "Abilities").        

## Flags
- Use `[[UNCLEAR: ...]]` only when the source is ambiguous and cannot be resolved faithfully.


# --- Suggested draft/_templates/sequence-template.md ---
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

- **Cost:**
- **Use:**
- **Effect:**
- **Limits:**
