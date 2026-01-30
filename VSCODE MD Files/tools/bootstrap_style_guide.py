#!/usr/bin/env python3
"""bootstrap_style_guide.py

Creates a starter style-guide.md and (optionally) a sequence template file.

Why:
- You already have a viewer + sanity checker. What you *don’t* have yet is a locked template.
- A short, enforceable template prevents formatting drift over hundreds of sequence entries.

Safe defaults:
- Prints the suggested content to stdout.
- Does NOT write anything unless you pass --write or --write-template.

Examples
  python tools/bootstrap_style_guide.py --repo .
  python tools/bootstrap_style_guide.py --repo . --write
  python tools/bootstrap_style_guide.py --repo . --write-template
  python tools/bootstrap_style_guide.py --repo . --write --write-template
"""

from __future__ import annotations

import argparse
from pathlib import Path

STYLE_GUIDE_CONTENT = """# Style Guide (LOTM RPG Rulebook)

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
Use the template in `build/_templates/sequence-template.md` as your starting point.

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
""".strip() + "\n"

TEMPLATE_MD = """---
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
""".strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".", help="Repo root (contains tag-registry.yml)")
    ap.add_argument("--write", action="store_true", help="Write style-guide.md only if empty")
    ap.add_argument("--write-template", action="store_true", help="Write build/_templates/sequence-template.md")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    style_path = repo / "style-guide.md"

    # Always print suggested content
    print("\n".join([
        "# --- Suggested style-guide.md ---",
        STYLE_GUIDE_CONTENT,
        "\n# --- Suggested build/_templates/sequence-template.md ---",
        TEMPLATE_MD,
    ]))

    if args.write:
        if style_path.exists() and style_path.read_text(encoding="utf-8", errors="replace").strip():
            print(f"\n[skip] {style_path} is not empty; not overwriting.")
        else:
            style_path.write_text(STYLE_GUIDE_CONTENT, encoding="utf-8")
            print(f"\n[wrote] {style_path}")

    if args.write_template:
        tpl_dir = repo / "build" / "_templates"
        tpl_dir.mkdir(parents=True, exist_ok=True)
        tpl_path = tpl_dir / "sequence-template.md"
        if tpl_path.exists() and tpl_path.read_text(encoding="utf-8", errors="replace").strip():
            print(f"\n[skip] {tpl_path} already exists and is not empty.")
        else:
            tpl_path.write_text(TEMPLATE_MD, encoding="utf-8")
            print(f"\n[wrote] {tpl_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
