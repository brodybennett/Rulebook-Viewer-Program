---
title: 'Sequence 5: Guardian'
id: war-god-seq-05
tags:
- pathway:war-god
- sequence:5
---






# Twilight Giant Pathway: Sequence 5

## Guardian

> **Lore:** It is rare for a Guardian to be hurt.

- When you enter a **Guardian State** and give up attacking, few beings below High Sequence can break your defense; your defense applies the same against all types of damage.
- When you attack, the corresponding defense is greatly reduced (still stronger than [[Refined Full-Body Armor]]).

You possess extraordinary abilities including [[Sword of Dawn]] and [[Storm of Light]], enabling you to:

- Deal damage to any type of monster.
- Avoid being confused by [[Illusions]].
- Help companions within a certain range bear damage and protect them.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Continue to endure extreme pain from being slapped shoulder-to-shoulder. Ensure the pain is close to death but not fatal. Persevere, and drink the potion at the moment you can regain your ability to move by your own will.

> **GM Note:** Labeled “unofficial ceremony” in the source text.

### Promotion Effects

- Advancing to Guardian causes your senses to be “guarded” indiscriminately, causing you to lose pain, smell, touch, and eventually all awareness of the outside world.
- The loss progresses in this order:
  1. Pain
  2. Smell
  3. Touch
  4. Complete external perception (you become “like a stone”)
- Continuous pain is required to maintain this anchor point; otherwise you become fully “protected” as above.

## Extraordinary Characteristics

- **Appearance:** Fist-sized, heart-like, covered with holes, shining like the morning sun.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +1, Willpower (WIL) +1.

### Wall of Protection

```yaml ability
id: war-god-seq-05-wall-of-protection
name: Wall of Protection
pathway: war-god
sequence: 5
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: physical_defense
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: "No roll; wall attacks resolve against your Physical Defense and share your Vitality."
scaling: []
tags:
- ritual
- stealth
- defense
- offense
text: 'Cost: 3 [[Spirituality]]. Use: 1 Casting Action. Effect: Insert a giant sword
  in front of your body. Morning light emerges, erecting an unbreakable invisible
  wall to your left and right. The wall shares [[Vitality]] with you: damage to the
  wall damages you. Attacks against the wall are resolved as attacks against your
  Physical Defense (including Armor/DR), and the damage is applied to you. The wall
  is used in one of the following ways: Guard Your Companions You place the giant
  sword in front of your body as a symbol. While your companions are behind the sword,
  a 50-meter-long invisible wall blocks attacks that try to hit them.'
```





- **Cost:** 3 [[Spirituality]].
- **Use:** 1 Casting Action.
- **Effect:** Insert a giant sword in front of your body. Morning light emerges, erecting an unbreakable invisible wall to your left and right.
- The wall shares [[Vitality]] with you: damage to the wall damages you. Attacks against the wall are resolved as attacks against your Physical Defense (including Armor/DR), and the damage is applied to you.

The wall is used in one of the following ways:

1. **Guard Your Companions**
   - You place the giant sword in front of your body as a symbol.
   - While your companions are behind the sword, a 50-meter-long invisible wall blocks attacks that try to hit them.
   - **Special:**
     - Your companions cannot cross this wall.
     - You can move freely inside and outside the wall.

2. **Guardian Status**
   - If you protect yourself instead of companions, you can no longer perform any actions.
   - You gain:
     - +8 [[External Damage Reduction]].
     - +5 [[Armor]].
   - A **Guardian Wall** isolates you from the inside and outside of the surrounding area.
   - **Special:** In **Guardian State**, even if [[Armor of Dawn]] is broken through the defense, it is not damaged.

- **Limits:** As described in this section's prose.


### Ignore Hallucinations

```yaml ability
id: war-god-seq-05-ignore-hallucinations
name: Ignore Hallucinations
pathway: war-god
sequence: 5
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- utility
text: 'Effect: As long as the source is no more than 1 Sequence higher than you, their
  [[Hallucination Abilities]] are invalid against you by default. This also applies
  to: Extraordinary abilities of pleasing/deceiving. The distortion of thinking by
  the [[Black Emperor]]. It does not include low-mystery conspiracies; those effects
  can still apply.'
```





- **Effect:** As long as the source is no more than 1 Sequence higher than you, their [[Hallucination Abilities]] are invalid against you by default.
- This also applies to:
  - Extraordinary abilities of pleasing/deceiving.
  - The distortion of thinking by the [[Black Emperor]].
- It does **not** include low-mystery conspiracies; those effects can still apply.

- **Limits:** As described in this section's prose.
