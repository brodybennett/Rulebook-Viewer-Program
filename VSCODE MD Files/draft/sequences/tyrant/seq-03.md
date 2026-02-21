---
title: 'Sequence 3: Sea King'
id: tyrant-seq-03
tags:
- pathway:tyrant
- sequence:3
---






# Tyrant Pathway: Sequence 3

## Sea King

## Advancement

### Advancement Ritual

- **Advancement Ritual:**  
  Make at least one city or a significant population of creatures within a complete sea area:
  - Remember your name  
  - Agree with your jurisdiction and control over that sea area  
  - Recognize you as king  
  - Share a common and clear impression of you  
  > **Lore:** This is described as an unofficial ceremony.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2

### Dominate Sea Creatures

```yaml ability
id: tyrant-seq-03-dominate-sea-creatures
name: Dominate Sea Creatures
pathway: tyrant
sequence: 3
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 2d6
  heal_roll: null
  effect_roll: 2d6
  notes: Summons 2d6 sea creatures; each deals 2d6 melee damage.
scaling: []
tags:
- control
- offense
text: 'Use: Swift Action Effect: You enslave and control sea creatures. You summon
  and control 2d6 sea creatures. Statistics of Summoned Sea Creatures: To hit: +8
  Hit Points: 30 Damage: 2d6 (melee) Attacks: 2 attacks per turn'
```





- **Use:** Swift Action  
- **Effect:**  
  You enslave and control sea creatures. You summon and control **2d6 sea creatures**.
- **Statistics of Summoned Sea Creatures:**  
  - To hit: +8  
  - Hit Points: 30  
  - Damage: 2d6 (melee)  
  - Attacks: 2 attacks per turn  
- **Limits:**  
  - These creatures usually cannot leave the sea.  
  - Applies only to sea creatures.  
  [[Sea Creatures]]

### Lightning Immunity

```yaml ability
id: tyrant-seq-03-lightning-immunity
name: Lightning Immunity
pathway: tyrant
sequence: 3
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
  effect_roll: "1"
  notes: Lightning damage immunity.
scaling: []
damage_types:
- lightning
tags:
- offense
text: 'Effect: You are immune to lightning damage. [[Damage Types]]'
```





- **Effect:** You are immune to lightning damage.  
  [[Damage Types]]

- **Limits:** As described in this section's prose.


### Lightning Storm

```yaml ability
id: tyrant-seq-03-lightning-storm
name: Lightning Storm
pathway: tyrant
sequence: 3
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + 20
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + 20
  damage_roll: 3d10
  heal_roll: null
  effect_roll: null
  notes: Ignores Agility (DEX) and evasion; airborne/undead targets take +2d10 and lightning-state targets take +1d10; paralysis requires a DV 15 Constitution test (DV 20 if Wet).
scaling: []
damage_types:
- lightning
tags:
- ritual
- defense
- offense
text: 'Cost: 6 [[Spirituality]] Use: Casting Action Effect: You create a storm of
  lightning over an area: Damage: 3d10 + your Strength damage bonus as area lightning
  damage. Attack Roll: +20 [[Disaster Attack Roll]] vs targets [[Physical Defense]]
  This attack ignores Agility (DEX) and evasion. [[Evasion]]'
```





- **Cost:** 6 [[Spirituality]]  
- **Use:** Casting Action  
- **Effect:**  
  You create a storm of lightning over an area:
  - Damage: 3d10 + your Strength damage bonus as area lightning damage.
  - Attack Roll: +20 [[Disaster Attack Roll]] vs target’s [[Physical Defense]]  
  - This attack ignores Agility (DEX) and evasion.  
    [[Evasion]]

- **Multi-Attack Interaction:**  
  - Lightning Storm is treated as making **at least 5 attacks** for the purpose of substitute-type defenses.  
  - To fully avoid it using substitute skills, at least **3 substitutes** are required, but the confrontation test is performed only once.  
    [[Substitute Skills]]  
    [[Confrontation Test]]  
  - If the target is one Sequence lower than you, the number of substitutes required increases by +1.

- **Split Resolution:**  
  You may divide the effect into three separate instances of lightning damage; roll damage separately for each instance (and apply damage reduction separately).

  This also interacts with luck consumption by a Wheel of Fortune pathway Sequence 5 ability used to avoid a demigod domain ability, doubling the luck consumption.  
  [[Demigod Domain]]

- **Weather Interaction:**  
  - In heavy rain, Lightning Storm counts as 5 attacks.  

- **Sequence 2 Upgrade (Future):**  
  > **Lore:** At Sequence 2, the lightning storm becomes a “sea of thunder.”  
  - Damage increases by +1d10.  
  - Base number of attacks becomes 5 (6 in rainy weather).  
  [[id:alias-sequence-2|Sequence 2]]

- **Special Targets:**  
  - Airborne or undead targets take an additional **2d10 lightning damage**.  
    [[Undead]]  
  - Targets in a lightning state take an additional **1d10 lightning damage**.  
    [[Lightning State]]

- **Damage Reduction Interaction:**  
  - Damage reduction is applied separately to each lightning damage instance.  
  - Each 1d10 component is reduced individually, including extra damage and Strength-based damage.  
    [[Damage Reduction]]

- **Aftereffects (Paralysis):**  
  - Lightning inflicts a paralyzing effect.  
  - Targets with lightning resistance are unaffected by this paralysis.  
    [[Lightning Resistance]]  
  - To remove paralysis, the target must use an action (not a free action) to pass a Constitution test with Difficulty 15.  
    [[Constitution Test]]  
    Difficulty Value  
  - On failure, the target cannot perform attack or movement actions and does not return to normal until after the opponent’s next round of actions.  
  - If the target is in a wet state, the Difficulty increases to 20.  
    [[Wet State]]

- **Limits:** As described in this section's prose.


### Ocean Perception

```yaml ability
id: tyrant-seq-03-ocean-perception
name: Ocean Perception
pathway: tyrant
sequence: 3
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
- divination
- detection
text: 'Effect: While in contact with sea water, you can: Perceive events occurring
  on the waters connected to you. Observe any location on the sea. Use your extraordinary
  abilities anywhere on the sea. Limits: This perception can be affected by anti-divination.
  [[id:alias-anti-divination|Anti-Divination]]'
```





- **Effect:**  
  While in contact with sea water, you can:
  - Perceive events occurring on the waters connected to you.  
  - Observe any location on the sea.  
  - Use your extraordinary abilities anywhere on the sea.  

- **Limits:**  
  - This perception can be affected by anti-divination.  
    [[id:alias-anti-divination|Anti-Divination]]  
- The effective range is approximately the size of a city.  
  - **Clarification:** Treat this as roughly a 5 km radius of connected sea.
