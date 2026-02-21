---
title: 'Sequence 1: Hand of Order'
id: arbiter-seq-01
tags:
- pathway:arbiter
- sequence:1
---






# Justiciar Pathway: Sequence 1

> **Lore:** This Sequence can stop chaos by separating combatants into distinct battlefields, standing in an independent position to control influence. It can sense changes in order.

## Hand of Order

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Become the leader of a country's order; make the system you formulate a moral and legal benchmark that subjects will not violate (even in their hearts); and make the system you formulate part of the social norm. *(Unofficial ceremony.)*

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Charisma +3, Intuition (INT) +1, Agility (DEX) +1, Strength +1, Constitution +1
- **Skill Gain:** [[Law skill]] increased by 1 skill level

### Hand of Order

```yaml ability
id: arbiter-seq-01-hand-of-order
name: Hand of Order
pathway: arbiter
sequence: 1
status: adapted
type: active
action: free
cost:
  spirituality: 5
roll: 1d20 + @attr.cha + @skill.law
opposed_by: willpower_defense
range: designated area in law scope
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.cha + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: 2d20
  notes: Adapted from explicit law-setting procedure where two Law plus Charisma rolls are made and one is chosen as the violation Difficulty Value.
scaling:
- when: law_is_first_imposed
  changes:
    effect_note: Roll two Law plus Charisma checks and choose one result as the violation Difficulty Value.
- when: target_attempts_to_break_order
  changes:
    check_penalty: -4
    effect_note: Violator resolves Law versus Willpower Defense with at least a -4 penalty.
- when: target_sequence_lower_than_you
  changes:
    effect_note: Each sequence gap adds another -4 penalty when trying to violate the law.
tags:
- ritual
- control
- defense
text: 'You can make the rules of the world to a certain extentrules that cannot usually
  be violatedand cause them to become reality. Cost: 5 [[Spirituality]] (total) Use:
  Free action Free Action Effect: You formulate a world law that is regarded as a
  law and becomes real. Common types include: Divide the battlefield: Formulate a
  chaotic area as a rule where combatants cannot interact with each other under world
  laws. Example: You divide a lobby into different small worlds. Physically it still
  seems whole, but mystically it is separated into different small rooms. Use case:
  Divide a chaotic battle so enemies become one-on-one with each other. Restriction:
  Extraordinary powers cannot be remotely a...'
```





You can make the rules of the world to a certain extent—rules that cannot usually be violated—and cause them to become reality.

- **Cost:** **5** [[Spirituality]] (total)
- **Use:** **Free action** Free Action
- **Effect:** You formulate a **world law** that is regarded as a law and becomes real. Common types include:

1. **Divide the battlefield:** Formulate a chaotic area as a rule where combatants cannot interact with each other under world laws.
   - Example: You divide a lobby into different small worlds. Physically it still seems whole, but mystically it is separated into different small rooms.
   - Use case: Divide a chaotic battle so enemies become one-on-one with each other.
   - **Restriction:** Extraordinary powers cannot be remotely applied to each other, except for enhanced attributes that were applied in advance.

2. **Prevent related forces from being generated (by rule):** A related force cannot be generated (e.g., sacred, light, flame, corruption, shadow).
   - You can specify up to **two** powers.
   - This does not affect corresponding creatures that have already appeared, but it can prevent them from using related abilities.
   - If the corresponding creatures that appear are not half-god, they will most likely die on the spot due to the loss of these powers.
   - [[Half-God]]

3. **Create an independent space (based on battlefield division):**
   - This space can be regarded as having a partial concealment effect, making it difficult to be discovered by establishing a corresponding order.
   - Or use this to make a certain [[Sealed Item]] completely independent—or even a kind of thing—so as to complete the effect of the seal.

#### Setting the Difficulty Value to Violate the Law

- When specifying any of the above rules, roll **two** of your **Law + Charisma** values, then choose **one** roll as the **Difficulty Value** (**Difficulty Value**) for someone trying to violate this rule. Difficulty Value
- Breaking through this Difficulty Value allows the violator to achieve the desired effect. This requires the corresponding [[Skill Test]] or Will Test to fight.
- A breaker is immediately regarded as a **criminal**, so they will be allowed to be judged. [[Criminal]] [[Judgment]]

#### Penalties to Break Through

- Breaking through this order requires a **-4** penalty.
- The violator makes a **Law** check vs the target's **Willpower Defense**. For each **Sequence** level the enemy is lower than you, that check suffers another **-4** penalty.

- **Limits:** As described in this section's prose.
