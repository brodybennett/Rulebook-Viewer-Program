---
title: 'Sequence 1: Thunder God'
id: tyrant-seq-01
tags:
- pathway:tyrant
- sequence:1
---






# Tyrant Pathway: Sequence 1

## Thunder God

## Advancement

### Advancement Ritual

> **Lore:** A ceremony of standing before the overwhelming force of nature and accepting one’s insignificance before thunder.

- **Advancement Ritual:**  
  Create or find a location capable of resisting thunderstorms approaching [[Sequence 0]] intensity. Attract a vast number of thunder-attributed phenomena (described as “thunder forests”).  
  As the location’s layered defenses are destroyed one layer at a time, the participant must:
  - Experience fear and surrender.
  - Recognize their own insignificance before nature.  
  Consume the potion when only the final defensive layer remains. After consumption, the user merges with the thunder that breaks the final defense, releasing a dazzling thunderburst that can reach back toward those thunder phenomena.  
  - **Clarification:** “Thunder forests” refers to a dense field of thunder phenomena across at least a 1 km radius. The defensive structure should have multiple layered defenses (at least 3 layers) that are destroyed one by one.

---

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2

---

### Become Thunder

```yaml ability
id: tyrant-seq-01-become-thunder
name: Become Thunder
pathway: tyrant
sequence: 1
status: canonical
type: active
action: full-round
cost:
  spirituality: 5
roll: null
opposed_by: none
range: self
target: self
duration: 2 rounds (3 rounds at [[Sequence 0]])
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: On exit, you may deal double Lightning Control damage or trigger Lightning Storm after sufficient acceleration; lightning-form charge uses Strength damage dice via a fighting test.
scaling: []
damage_types:
- lightning
tags:
- ritual
- mobility
- control
- offense
text: 'Cost: 5 Spirituality Use: Full-Round Action Duration: 2 rounds (3 rounds at
  [[Sequence 0]]) Effect: You transform into a thunderbolt and move at light speed.
  Your movement rate becomes the speed of light (described as ~300,000 kilometers
  of movement power), allowing you to reach any intended destination at light speed.
  This movement can be used to initiate a surprise attack. Upon ending movement: You
  may deal double the damage of [[Lightning Control]] or Directly trigger a lightning
  storm, which requires prior acceleration to a sufficient degree before use.'
```





- **Cost:** 5 Spirituality  
- **Use:** Full-Round Action  
- **Duration:** 2 rounds (3 rounds at [[Sequence 0]])  
- **Effect:**  
  You transform into a thunderbolt and move at light speed. Your movement rate becomes the speed of light (described as ~300,000 kilometers of movement power), allowing you to reach any intended destination at light speed. This movement can be used to initiate a surprise attack.

  Upon ending movement:
  - You may deal double the damage of [[Lightning Control]] **or**
  - Directly trigger a lightning storm, which requires prior acceleration to a sufficient degree before use.  
  - **Requirement:** You must have moved in lightning form for at least 1 full round (or an equivalent long-distance surge) before triggering the lightning storm.

- **Limits:**
  - While in lightning form, you cannot use other extraordinary abilities.
  - You may still enter a rage state.
  - You may charge in lightning form as an Attack Action, dealing lightning damage equal to your Strength damage dice via a fighting test.
  - Your quick dodge skill remains effective even against light-speed strikes.
  - Your dodge skill level increases by +1 while in this state.

---

### Hundreds of Millions of Thunders and Entanglements

```yaml ability
id: tyrant-seq-01-hundreds-of-millions-of-thunders-and-entanglements
name: Hundreds of Millions of Thunders and Entanglements
pathway: tyrant
sequence: 1
status: canonical
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + 25
opposed_by: physical_defense
range: Choose a target
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + 25
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Each bolt deals 1d6 lightning damage per point of Strength; combo adds +1d6 per round until combo value is spent.
scaling: []
damage_types:
- lightning
tags:
- ritual
- defense
- offense
text: 'Use: Casting Action (can be repeated each round) Targeting and Range: Choose
  a target Effect: You create vast, entangled lightning phenomena (described as forest-like
  lightning and extended electric arcs) and unleash continuous lightning combinations.
  Make a +25 disaster check against the targets physical defense. Ignores physical
  defense derived from Agility (DEX) and dodge. Each lightning bolt costs 1 Spirituality.
  Dark clouds gather and innumerable lightning strikes descend. *Base Damage Scaling:'
```





- **Use:** Casting Action (can be repeated each round)  
- **Targeting and Range:** Choose a target  
- **Effect:**  
  You create vast, entangled lightning phenomena (described as forest-like lightning and extended electric arcs) and unleash continuous lightning combinations.

  - Make a +25 disaster check against the target’s physical defense.
  - Ignores physical defense derived from Agility (DEX) and dodge.

  Each lightning bolt costs 1 Spirituality. Dark clouds gather and innumerable lightning strikes descend.

  **Base Damage Scaling:**
  - Damage depends on your Strength value (not Strength damage dice).
  - Each point of Strength = 1 lightning bolt.
  - Each bolt deals 1d6 lightning damage.  
  Example: Strength 20 → 20d6 lightning damage.

- **Sustained Casting:**  
  You may spend a Casting Action each round to maintain continuous strikes.

- **Combo Mechanic:**
  - Gain a combo value equal to your Agility (DEX).
  - Each consecutive round of using this ability counts as a combo:
    - Combo value −1.
    - Damage +1d6.
  - Example: Strength 20, Combo 15  
    - First round: 20d6  
    - Second: 21d6 (combo −1)  
    - Third: 22d6 (combo −1)

  When combo value reaches 0:
  - You may continue casting.
  - Damage no longer increases.

  If there is any interruption between combos:
  - Combo value resets.
  - Bonus damage from combos resets.

---

#### Interaction with Damage Reduction

- Normally a single-target ability, relying on repeated lightning strikes on the same target.
- If the target has damage reduction, reduction may apply to each lightning bolt individually, greatly lowering total damage.

- **Option:** You may expend all remaining combo value:
  - Lightning damage reduction applies only once per use instead of per bolt.
  - You cannot use combo value to increase damage further.
  - You may still maintain continuous casting, but without additional combo damage benefits.

- **Limits:** As described in this section's prose.
