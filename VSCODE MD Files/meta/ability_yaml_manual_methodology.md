# Manual Ability YAML Methodology

Date: 2026-02-20
Scope: Human-only review and correction of ability YAML blocks.

## Core Rule
- Do not bulk-generate mechanics.
- For each ability, read prose first, then set YAML manually.

## Per-Ability Checklist
1. Confirm structural fields:
- `id`, `name`, `pathway`, `sequence`, `status`, `type`, `action`.

2. Normalize economy and gate data:
- `cost` from explicit prose only.
- `opposed_by` from explicit defense/check wording.

3. Fill roll fields:
- `roll` should be non-null only when prose defines a check or attack test.
- `dice.check_roll`, `dice.damage_roll`, `dice.heal_roll`, `dice.effect_roll` must be populated when explicitly supported.
- If a roll exists but is context-conditional, explain in `dice.notes`.

4. Validate effect geometry/state:
- `range`, `target`, `duration` should reflect actual usage conditions (not defaults).

5. Add meaningful `scaling`:
- Use only explicit breakpoints from prose:
  - repeat-shot penalties
  - mode switches (for same ability)
  - sequence-tier improvements stated in text

6. Reconcile tags:
- Keep tags capability-focused (`offense`, `defense`, `control`, `utility`, etc).
- Remove tags that are not evidenced by the ability description.

7. Set status confidence:
- `canonical`: YAML directly supported by prose.
- `adapted`: YAML requires light interpretation/mapping (for example, mapping freeform prose into roll token format).
- `stub`: placeholder only.

## Validation Gate (after each manual batch)
1. `python tools/extract_compendium.py --repo "VSCODE MD Files"`
2. `python tools/lint_compendium.py --repo "VSCODE MD Files" --compendium dist/compendium.json`
3. `python tools/lint_roll_syntax.py --repo "VSCODE MD Files" --content-root draft`
4. `python tools/power_audit.py --repo "VSCODE MD Files" --compendium dist/compendium.json --power-scale meta/power_scale.yml --out meta/power_audit_report.md --json-out meta/power_audit_report.json`
