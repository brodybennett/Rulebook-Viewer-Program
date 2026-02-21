---
title: 'Sequence 4: Knight of Misfortune'
id: arbiter-seq-04
tags:
- pathway:arbiter
- sequence:4
---






# Justiciar Pathway: Sequence 4

## Knight of Misfortune

A Law Mage can **prohibit** specific behaviors within a defined range, and can also **deprive** a target of a specific **Beyonder** ability. Its core principle is: **"mystery is weakened, reality is strengthened."**

> **Lore:** In the mundane world, this is considered a powerful tool for militaries to counter extraordinary individuals.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** For a country with far-reaching and long-standing problems, formulate a system that can solve its fundamental problems, then secure implementation and effective feedback with the approval of national leaders. (Unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +1, Agility (DEX) +1, Strength +1, Constitution +1
- Legal skills increase by 1 skill level. [[Legal Skills]]

### Law of Truth

```yaml ability
id: arbiter-seq-04-law-of-truth
name: Law of Truth
pathway: arbiter
sequence: 4
status: adapted
type: toggle
action: free
cost:
  spirituality: 5
roll: null
opposed_by: none
range: 1 kilometer radius (centered on caster)
target: all creatures in area
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d5
  notes: Adapted from the explicit law outcome where extraordinary damage in-band is normalized to 1d5 under the decree.
scaling:
- when: extraordinary_effect_exceeds_your_personality
  changes:
    effect_note: Extraordinary effects resolve at half effect (including duration/range where applicable).
- when: sequence_2_upgrade
  changes:
    range: city
    effect_note: Reality-side benefits double and weak undead or basic summons die on the spot.
tags:
- ritual
- debuff
- offense
- control
- defense
text: '*Law of Truth: aMystery is weakened here, and reality is strengthened.a Cost:
  5 points of Spirituality [[Spirituality]] Use: 1 free action; treated as a spoken
  law [[Spoken Law]] Timing: Takes 1 round to gradually take effect. Area: Within
  a radius of 1 kilometer. *Mystery is weakened (extraordinary effects): You are also
  affected by this ability (aincluding oneaTMs owna). Damage from extraordinary powers:'
```





**Law of Truth:** "Mystery is weakened here, and reality is strengthened."

- **Cost:** 5 points of **Spirituality** [[Spirituality]]
- **Use:** 1 **free action**; treated as a **spoken law** [[Spoken Law]]
- **Timing:** Takes 1 **round** to gradually take effect.
- **Area:** Within a radius of 1 kilometer.

**Mystery is weakened (extraordinary effects):**
- You are also affected by this ability ("including one's own").
- **Damage from extraordinary powers:**
  - If the extraordinary power does **not exceed your Personality**, all **final damage dice** are treated as **1d5**. [[Personality]]
  - If it **exceeds your Personality**, the full effect is **halved**. (Damage and/or duration.)
  - Teleportation assisted by the **Spirit World** requires **two rounds**; the activation is still treated as a **free action**, but the teleportation takes two rounds to complete. [[Spirit World]]
- **Other extraordinary abilities:** Suffer the same "half effect."
- **Non-damaging extraordinary abilities** (e.g., nightmares and illusions):
  - Targets can clearly distinguish illusion from reality.
- **Control-check requirements** caused by extraordinary abilities are **halved**.
  - Example: If the Difficulty Value to identify/break free is 20, it becomes 10. Difficulty Value
- **Extraordinary self-strengthening abilities:** Are halved; their **range** is halved and their **duration** is halved.
  - This does **not** affect Constitution that was already enhanced by the potion.
- Example (range-halving): An extraordinary ability that normally works on others only by being next to them must instead be applied by **physical touch**.

**Reality is strengthened (mundane effects):**
1. The damage dice of all weapons increase by **2d6**.  
   When the maximum possible roll total exceeds **40**, the final weapon damage is increased by **half**.
2. All attributes of ordinary people **+3**; all skill identification **+4**.
3. Add **5 points of temporary armor** to all ordinary people in response to extraordinary abilities.
4. The benefits of **Personality Suppression** are all **halved**. [[Personality Suppression]]
   - Because angels essentially have two levels of Personality Suppression improvement for ordinary people and middle/low Sequences, the halving only returns it to one level, so there is no special calculation.
5. The incomplete form of **mythical creatures** can no longer affect the sanity of ordinary people, unless the creature has fallen to the brink of madness; the sanity test against complete mythical creatures is **halved**. [[Mythical Creatures]]
6. For weak undead creatures and various activated summons (e.g., activated flesh and blood, plants that attack by themselves instead of manual operation):
   - Total damage die becomes **1**.
   - Movement range is **halved**.
   - Only **one action** can be performed each round.
   - Their "due death" is thus re-enhanced.
   - If an undead creature or summoned object has extraordinary characteristics, it counts as an extraordinary person; if it is still "one bit lower" than the Law Mage while being extraordinary, its damage dice is no longer 1 but **1d5**, but it still suffers halved movement range and only one action per round.  

**Sequence 2 note (for this decree):**
- The scope extends to a **city**.
- Undead creatures and summons that are not extraordinary **die on the spot**.
- All benefits on the reality side are **doubled**.
- The complete mythical form can no longer affect the sanity of ordinary people.
- All Personality Suppression must be reduced by **one level** and then **halved**; it cannot become a negative number.  
  Sequence 2 Upgrade

- **Effect:** Law of Truth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Make a Contract

```yaml ability
id: arbiter-seq-04-make-a-contract
name: Make a Contract
pathway: arbiter
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: touch
target: consenting signatories
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- detection
text: 'You make a contract that cannot be broken. Cost: 3 points of Spirituality [[Spirituality]]
  Use: A Casting Action. Casting Action Requirement: Mutual consent. Effect: You create
  a sacred contract that cannot be violated. The contractaTMs terms prevent prohibited
  content from occurring in an objective sense. Example: If buying an item is prohibited,
  then when faced with that item, the signatory fundamentally has no desire or ability
  to buy it. This is an objective limitation shared by both parties, so it cannot
  be violated.'
```





You make a contract that cannot be broken.

- **Cost:** 3 points of **Spirituality** [[Spirituality]]
- **Use:** A **Casting Action**. Casting Action
- **Requirement:** Mutual consent.
- **Effect:** You create a sacred contract that cannot be violated.
  - The contract's terms prevent prohibited content from occurring in an **objective** sense.
    - Example: If buying an item is prohibited, then when faced with that item, the signatory fundamentally has no desire or ability to buy it.
  - This is an objective limitation shared by both parties, so it cannot be violated.
- If there is a situation that could be violated under special circumstances, the **GM** must impose a serious punishment that matches **Party A's Personality**. [[Party A]]

- **Limits:** As described in this section's prose.


### Practitioners of Order

```yaml ability
id: arbiter-seq-04-practitioners-of-order
name: Practitioners of Order
pathway: arbiter
sequence: 4
status: adapted
type: toggle
action: free
cost: {}
roll: 1d20 + @attr.wil
opposed_by: difficulty_value
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.wil
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted will-test token for targets attempting to launch attacks under the active aura.
scaling:
- when: aura_active
  changes:
    effect_note: Enemy identification and damage checks suffer -4 while aura pressure persists.
- when: enemy_attempts_active_attack
  changes:
    difficulty_value: 20
- when: sequence_2_upgrade
  changes:
    difficulty_value: 30
    effect_note: Targets below demigod are strongly pressured toward surrender and avoidance behaviors.
tags:
- ritual
- offense
- control
- defense
- detection
text: 'Effect: You can distinguish ordinary people from extraordinary people by their
  different apositions,a and judge the level of extraordinary people based on this.
  This is limited to Sequence level only, not the Pathway they belong to. Sequence
  Level Pathway Aura: You can actively release a solemn and majestic aura so that
  enemies below demigods do not dare raise their heads or launch attacks, including
  some extraordinary creatures. Cost: No obvious Spirituality consumption. While this
  aura is active: Enemy identification and damage are -4. An enemyaTMs active attack
  requires at least a Difficulty Value 20 will identification. [[Will Identification]]
  *Sequence 2 note (aura):'
```





- **Effect:** You can distinguish ordinary people from extraordinary people by their different "positions," and judge the level of extraordinary people based on this.
  - This is limited to **Sequence** level only, not the **Pathway** they belong to. Sequence Level Pathway
- **Aura:** You can actively release a solemn and majestic aura so that enemies below demigods do not dare raise their heads or launch attacks, including some extraordinary creatures.
  - **Cost:** No obvious Spirituality consumption.
  - **While this aura is active:**
    - Enemy identification and damage are **-4**.
    - An enemy's active attack requires at least a **Difficulty Value 20** will identification. [[Will Identification]]

**Sequence 2 note (aura):**
- Below the angel level: those below the demigod level must pass a **Difficulty Value 30** will test before they can attack you.
- It is difficult for them to curb their desire to surrender, and they do not dare raise their heads.
[[Demigod]] [[Angel]]

- **Limits:** As described in this section's prose.
