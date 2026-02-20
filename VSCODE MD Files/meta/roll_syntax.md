# Roll Syntax Contract (Phase 2)

Date: 2026-02-20  
Scope: grammar and style contract for `roll` fields in `yaml ability` blocks.

This locks roll notation early so automation buttons stay deterministic.

## 1) Canonical Roll Shape

- A check expression is terms joined by `+` or `-`.
- A term is one of:
  - Dice (`NdM`, for example `1d20`, `2d6`)
  - Integer constant (`3`, `-1`)
  - Scoped reference (`@attr.dex`, `@skill.fighting`)
  - Parenthesized expression (`(@attr.int + 2)`)
- Optional opposition is modeled as a `vs` clause:
  - `1d20 + @attr.dex + @skill.fighting vs @def.physical`
- Optional labeled clauses are allowed in snippets:
  - `damage: 1d8 + @attr.str`
- In `ability_schema.yml`, keep `roll` and `opposed_by` separate whenever possible.

## 2) EBNF

```text
roll_snippet = clause , { ws , ";" , ws , clause } ;
clause       = labeled_clause | contest_clause | check_expr | vs_clause ;
labeled_clause = label , ":" , ws , check_expr ;
label        = "roll" | "check" | "damage" | "heal" ;
contest_clause = check_expr , ws , "vs" , ws , defense_ref ;
vs_clause    = "vs" , ws , defense_ref ;

check_expr   = term , { ws , ("+" | "-") , ws , term } ;
term         = dice | integer | ref | "(" , check_expr , ")" ;
dice         = integer_pos , "d" , integer_pos ;
ref          = attr_ref | skill_ref | defense_ref | resource_ref | mod_ref | "@bonus" ;

attr_ref     = "@attr." , attr_token ;
skill_ref    = "@skill." , skill_token ;
defense_ref  = "@def." , defense_token ;
resource_ref = "@res." , resource_token ;
mod_ref      = "@mod." , mod_token ;
```

Allowed tokens come from `meta/ability_schema.yml` under `roll_registry`.

## 3) Formatting Rules (Strict)

- Use lowercase namespaces and tokens only.
- Use snake_case for token names.
- Use exactly one space around `+` and `-`.
- Do not include spaces inside references (`@attr.dex`, not `@attr. dex`).
- Use lowercase `vs` keyword.
- Use lowercase labels (`damage:`, not `Damage:`).
- Use semicolon separators for multi-clause snippets.

## 4) Valid Examples

```text
1d20 + @attr.dex + @skill.fighting + @bonus
1d20 + @attr.int + @skill.occultism vs @def.dv
damage: 1d8 + @attr.str
1d20 + (@attr.int + 2) + @skill.investigation
roll: 1d20 + @attr.cha + @skill.persuade; vs @def.willpower
```

## 5) Invalid Examples

```text
1d20+@attr.dex+@skill.fighting
1d20 + @attr.agility + @skill.fighting
1d20 + Dex + Fighting
1d20 + @skills.fighting
Damage: 1d8+@attr.str
1d20 + @skill.occult
```

Why invalid:
- missing canonical spacing,
- alias token instead of canonical token,
- freeform references,
- unknown namespace,
- non-canonical label casing,
- alias skill token instead of canonical skill token.

## 6) Linting

Use:

```bash
python tools/lint_roll_syntax.py --repo .
python tools/lint_roll_syntax.py --repo . --expr "1d20 + @attr.int + @skill.occultism + @bonus"
python tools/lint_roll_syntax.py --repo . --expr "1d20+@attr.agility+@skill.fighting"
```

The linter enforces this file plus token registries from `meta/ability_schema.yml`.
