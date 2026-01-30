# LoTM Rulebook Automation Pack

Scripts to keep prompting fast, links stable, and your `tag-registry.yml` from exploding.

All scripts are **read-only by default**. Anything that writes requires an explicit `--write` flag.

## Install deps

```bash
pip install pyyaml
```

## 1) Prompt bundle (use constantly)

Generate a small YAML bundle (glossary + registry slice) for a raw chunk or a specific markdown file:

```bash
python tools/prompt_bundle.py --repo . --raw chunk.txt > prompt_bundle.yml
python tools/prompt_bundle.py --repo . --md build/sequences/apprentice/seq-02.md > prompt_bundle.yml
```

Paste `prompt_bundle.yml` into your editing prompt as the “GLOSSARY + TAG REGISTRY”.

## 2) Find heading title collisions

```bash
python tools/find_heading_collisions.py --repo .
```

## 3) Find ambiguous wiki-links in your markdown

```bash
python tools/find_ambiguous_wikilinks.py --repo .
```

These links are risky with the current viewer (title-based resolution). Convert them to id-links:
`[[id:<anchor-id>|Text]]`.

## 4) Merge TAG DELTA into the main registry

Dry run:

```bash
python tools/merge_tag_delta.py --repo . --delta tag-delta.yml
```

Apply:

```bash
python tools/merge_tag_delta.py --repo . --delta tag-delta.yml --write
```

## 5) Prune alias bloat

Dry run:

```bash
python tools/prune_registry_aliases.py --repo .
```

Apply:

```bash
python tools/prune_registry_aliases.py --repo . --write
```

## 6) Bootstrap style guide + template

```bash
python tools/bootstrap_style_guide.py --repo . --write --write-template
```
