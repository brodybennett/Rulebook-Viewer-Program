---
title: 'Sequence 6: Calamity Priest'
id: fate-seq-06
tags:
- pathway:fate
- sequence:6
---





# Wheel of Fortune Pathway: Sequence 6

> **Lore:** A Disaster Priest often encounters disasters passively, but can foresee them and prepare to eliminate or mitigate their impact. They leverage “luck” to avoid most dangers, attack amid chaos, and draw opponents into environments that favor them—sometimes even using passively encountered dangers as weapons.

## Calamity Priest

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +2.

### Disasters

```yaml ability
id: fate-seq-06-disasters
name: Disasters
pathway: fate
sequence: 6
type: active
action: cast
cost:
  spirituality: 6
roll: null
opposed_by: none
range: self
target: self
duration: The above disasters only last for **1 round**.
scaling: []
tags:
- ritual
text: 'Passive: At 0:00 every day, roll 1d3 to determine how many disasters you encounter
  today. For each disaster, roll 1d24 to determine the time of day when the disaster
  will occur. By default, you can foresee the time and location of the disaster. Note:
  In addition to 1d24, roll 1d59 for each disaster to determine how many minutes per
  hour. Active: Use: 1 Casting Action Cost: 3 spirituality points'
```




> **Lore:** You passively encounter disasters, but can prepare in advance and exploit them in combat.

- **Passive:**
  - At **0:00** every day, roll **1d3** to determine how many disasters you encounter today.
  - For each disaster, roll **1d24** to determine the time of day when the disaster will occur.
  - By default, you can foresee the time and location of the disaster.
  - Note: In addition to **1d24**, roll **1d59** for each disaster to determine how many minutes per hour.
- **Active:**
  - **Use:** 1 Casting Action
  - **Cost:** 3 spirituality points
  - **Effect:** You immediately cause a disaster centered on you.

- **List of disasters** (passive disasters only affect you alone):
  - **Restricted actions:**
    - All creatures within 20 meters need to make a **Luck** test (**Difficulty Value 20**), otherwise they will lose their balance.
    - They can change to a **Difficulty Value 30 Agility (DEX)** test to react forcefully.
    - > **GM Note:** Examples include the ground collapsing or creatures falling for no reason.
  - **Chaos out of control:**
    - Extreme chaos will appear within 20 meters (e.g., horses lose control and start to cause chaos; buildings collapse and cause damage; ground depressions cause landslides).
    - ① Creatures in the area need to make a **Luck** identification (**Difficulty Value 20**), otherwise they will suffer **1d6** physical damage due to chaos.
    - ② All skill and attribute appraisals against others are **-2 disadvantageous**, and the target cannot be accurately locked due to confusion; **Luck** appraisal will not be affected.
  - **Action failure:**
    - For all creatures within 20 meters, any spellcasting/Attack Action requires a **Luck** check (**Difficulty Value 20**), otherwise it will fail.
    - > **GM Note:** Examples include melee failures from loss of strength control, extraordinary abilities failing from abnormal states causing spiritual disorder, and firearms missing due to slipping—or even exploding.
  - **Omen magnification:**
    - For all creatures within 20 meters, **1–5** of their **rd20 base values** are considered a big failure.
    - When a big failure occurs, the resulting result can be avoided with **Luck (Difficulty Value 20)**.
  - **Negative enhancement:**
    - All creatures within 20 meters: the negative effects they originally suffered are **halved (rounded down)**. It may be half of the penalty, and it may be half of the resistance.
    - If it is in a thunderstorm, a big failure will suffer **1d10** lightning harm.
  - **Difficulty in action:**
    - For all creatures within 20 meters, normal behavior that does not require identification also requires a **Luck** identification (**Difficulty Value 20**) to perform.
    - Actions that have been identified will change the relevant attributes to **Luck**.
    - > **GM Note:** Examples include suddenly losing feeling in the legs while moving, or repeatedly dropping items / having pockets in a mess and being unable to find what you want.
  - Other reasonable disasters allowed by the **GM**.

- **Duration:** The above disasters only last for **1 round**.
- **Special:** For every target higher than you by 1+ Sequence, the difficulty of all **Luck** checks is **halved (rounded up)**.

- **Limits:** As described in this section's prose.


### Spiritual Storm

```yaml ability
id: fate-seq-06-spiritual-storm
name: Spiritual Storm
pathway: fate
sequence: 6
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: All targets within 20 meters from you as the center
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- buff
- defense
text: 'Use: 1 Casting Action Cost: 3 spiritual points Targeting and range: All targets
  within 20 meters from you as the center Effect: Make an Intuition (INT) check against
  physical defense. On success, it will cause a shock effect, and cause all affected
  targets to suffer a common disaster from the Disasters list (GM chooses). Special:
  For a creature suffering from a mental storm, within 1 round, the basic value of
  the big failure judgment is increased by 2 points (that is, 1, 2, and 3 are all
  big failures).'
```




> **Lore:** You create a “spiritual storm,” directly affecting the other party’s spiritual/mental body and causing dizziness or mental loss.

- **Use:** 1 Casting Action
- **Cost:** 3 spiritual points
- **Targeting and range:** All targets within 20 meters from you as the center
- **Effect:**
  - Make an **Intuition (INT)** check against **physical defense**.
  - On success, it will cause a shock effect, and cause all affected targets to suffer a common disaster from the **Disasters** list (GM chooses).

- **Special:**
  - For a creature suffering from a mental storm, within **1 round**, the basic value of the big failure judgment is increased by **2** points (that is, **1, 2, and 3** are all big failures).
  - The **Omen magnification** disaster is changed to **1–7** being regarded as a big failure.
  - It will lead to more and more disasters. “Mental storm” here refers to this **Spiritual Storm** ability.

- **Limits:** As described in this section's prose.
