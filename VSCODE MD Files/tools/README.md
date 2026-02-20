# LoTM Rulebook Automation Pack

Scripts to keep prompting fast, links stable, and your `tag-registry.yml` from exploding while `draft/` is your active content root.

All scripts are **read-only by default**. Anything that writes requires an explicit `--write` flag.

Command examples below assume your working directory is `VSCODE MD Files/`.
If you run from repo root, either `cd "VSCODE MD Files"` first or prefix script/repo paths accordingly.

## Install deps

```bash
pip install pyyaml
```

## 1) Prompt bundle (use constantly)

Generate a small YAML bundle (glossary + registry slice) for a raw chunk or a specific markdown file:

```bash
python tools/prompt_bundle.py --repo . --raw chunk.txt > prompt_bundle.yml
python tools/prompt_bundle.py --repo . --md draft/sequences/apprentice/seq-02.md > prompt_bundle.yml
```

Paste `prompt_bundle.yml` into your editing prompt as the "GLOSSARY + TAG REGISTRY".

## 2) Find heading title collisions

```bash
python tools/find_heading_collisions.py --repo .
python tools/find_heading_collisions.py --repo . --content-root draft
```

## 3) Find ambiguous wiki-links in your markdown

```bash
python tools/find_ambiguous_wikilinks.py --repo .
python tools/find_ambiguous_wikilinks.py --repo . --content-root draft
```

These links are risky with the current viewer (title-based resolution). Convert them to id-links:
`[[id:<anchor-id>|Text]]`.

## 4) Congruence audit (cross-file consistency risks)

Generate a severity-grouped report (High/Medium/Low) for:
- `[[UNCLEAR: ...]]` and `[[LINK LATER: ...]]` counts + locations
- heading collisions
- bold-term definition drift (`**Term:** ...`)
- repeated block title field drift (`**Cost:**`, `**Use:**`, `**Effect:**`)

```bash
python tools/congruence_audit.py --repo .
python tools/congruence_audit.py --repo . --content-root draft --out congruence_report.md
python tools/congruence_audit.py --repo . --out reports/congruence_report.md --json
python tools/congruence_audit.py --repo . --out -   # print markdown report to stdout
```

`--json` accepts an optional path. If omitted, JSON is written next to `--out` with a `.json` suffix.

## 5) Merge TAG DELTA into the main registry

Dry run:

```bash
python tools/merge_tag_delta.py --repo . --delta tag-delta.yml
```

Apply:

```bash
python tools/merge_tag_delta.py --repo . --delta tag-delta.yml --write
```

## 6) Prune alias bloat

Dry run:

```bash
python tools/prune_registry_aliases.py --repo .
```

Apply:

```bash
python tools/prune_registry_aliases.py --repo . --write
```

## 7) Bootstrap style guide + template

```bash
python tools/bootstrap_style_guide.py --repo . --write --write-template
```

## 8) Canon term lint (Phase 0 naming lock)

Scan markdown for non-canonical terms from `meta/canon_terms.yml` and print a replacement report:

```bash
python tools/lint_canon_terms.py --repo . --content-root draft
```

Use a deliberate-deviation allowlist (default file is `meta/canon_allowlist.yml`):

```bash
python tools/lint_canon_terms.py --repo . --allowlist meta/canon_allowlist.yml
```

Write JSON output:

```bash
python tools/lint_canon_terms.py --repo . --json-out reports/canon_term_lint.json
```

## 9) Core combat simulator (Phase 1 balance lock)

Run Monte Carlo checks against `meta/balance_targets.yml` and output markdown/json reports:

```bash
python tools/sim_core_combat.py --repo .
python tools/sim_core_combat.py --repo . --targets meta/balance_targets.yml --out meta/balance_report.md --json
python tools/sim_core_combat.py --repo . --trials 50000 --seed 20260220
```


