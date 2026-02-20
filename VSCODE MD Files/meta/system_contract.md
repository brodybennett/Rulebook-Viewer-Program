# Core System Contract (Phase 1)

Date: 2026-02-20  
Scope: core gameplay logic in `draft/core-rules/` (checks, attributes, combat, conditions, skills, and core resource flow)

This contract is the mechanical baseline for Phase 1. It is intentionally strict and minimal so future sequence/item tuning can rely on stable math.

## 1) Resolution Engine (Non-Negotiable)

- Standard check: `1d20 + relevant Attribute + relevant Skill modifier + situational modifiers`.
- Success condition: final total must **exceed** the Difficulty Value (or relevant Defense).
- Natural 20: automatic success.
- Natural 1: automatic failure.
- Attack critical rule: roll damage normally, then set damage to at least `ceil(theoretical max / 2)` if the rolled value is lower.

## 2) Vocabulary Lock

- Core positional mechanic terms are **Advantage** and **Disadvantage**.
- Numeric modifier language is **favorable** / **unfavorable**.
- `beneficial` is not a separate rules keyword in core adjudication.

## 3) Action Economy

- One combat round is approximately 6 seconds.
- Regular round budget:
  - 1 Attack/Casting Action
  - 3 Swift Actions
  - 1 Move Action
  - Unlimited Free Actions
- Surprise Round (legacy term: Ambush Round): ambushing side gets `1 Attack/Casting/Move Action` or `2 Swift Actions`; ambushed side takes no actions.
- Full-Round Action consumes the full regular round budget and resolves at the start of the actor's next turn.
- Action conversion is one-way only: `1 Attack/Casting Action -> 2 Swift Actions`.
- No action banking between rounds.

## 4) Defense Mapping

- Physical Defense: `10 + Armor + Agility (DEX) + Dodge`.
- Firearm exception:
  - Without Quick Dodge: firearms oppose `10 + Armor`.
  - With Quick Dodge: firearms oppose full Physical Defense.
- Willpower Defense: `10 + Willpower (WIL)`.
- Constitution Defense: `10 + Constitution (CON)`.
- Ability text must state which defense is opposed.

## 5) Resource Economy

- Vitality is the primary durability pool.
  - At `Vitality <= 0`, target is Dying.
  - **Dying Threshold** is `-Constitution (CON)`.
- Spirituality is the core supernatural spend resource.
  - If Spirituality is empty and abilities are still forced, costs spill into Sanity / Rationality.
- Sanity / Rationality is the core mental stability resource.
  - Base loss roll is `1d20` vs current Sanity / Rationality.
- Luck does not passively add to normal checks.
  - Burn Luck is a once-per-24h Free Action and recovers at 1 point per 24h.

## 6) Core Condition Contract

- Caught Off Guard and Restrained remove Agility (DEX) and Dodge contributions from Physical Defense.
- Advantage gives +2 favorable to applicable checks against enemies.
- Disadvantage gives -2 unfavorable to Agility (DEX) and Dodge contributions in Physical Defense.
- Advantage/Disadvantage do not stack with themselves.

## 7) Conflict Resolution Rule

If wording conflicts, use this order until an explicit revision is published:

1. `meta/system_contract.md`
2. `draft/core-rules/checks.md`
3. `draft/core-rules/attributes.md`
4. `draft/core-rules/combat/combat-procedure.md`
5. `draft/core-rules/combat/special-conditions.md`
6. `draft/core-rules/combat/special-actions.md`

Any deliberate exception must be documented in `meta/balance_targets.yml` (or a release log) before use.
