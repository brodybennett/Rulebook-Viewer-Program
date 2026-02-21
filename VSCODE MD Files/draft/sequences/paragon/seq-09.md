---
title: 'Sequence 9: Savant'
id: paragon-seq-09
tags:
- pathway:paragon
- sequence:9
---






# Paragon Pathway: Sequence 9

## Savant

> **Lore:** Believing that knowledge is power, Savants have a cursory grasp of the occult and a stronger proficiency in chemicals and intricate mechanisms-seeming to "know it all." Their core talent is awakening memory: recalling everything they have read while improving comprehension and learning speed.

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
- **Rapid Learning (skills):** Process manufacturing, physics, engineering, mechanical maintenance, and chemistry can be quickly learned.
- **Course-Based Skill Increase:** Each time you receive at least 2 hours of non-repetitive and effective corresponding guidance, choose one skill that matches the course; that skill increases by 1 grade.
  1. Unlike other methods, learning takes effect immediately after each 2-hour course ends. Skill-rank progression follows the normal ladder (training -> proficient -> advanced -> mastery), and you can improve at most 2 skills per day.
  2. This course-based increase is **separate** from rapid learning; you do not apply both to the same 2-hour course.

- **Character Creation (not newly promoted):** When creating a character above Sequence 9 (not newly promoted), use the Intuition (INT) from the [[Triple Potion]] as a pool to buy [[Growth Skills]].

### Wake Up Memory

```yaml ability
id: paragon-seq-09-wake-up-memory
name: Wake Up Memory
pathway: paragon
sequence: 9
status: canonical
type: active
action: swift
cost:
  spirituality: 3
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
  notes: No roll; the next skill check gains a one-tier boost (up to advanced).
scaling: []
tags:
- ritual
- buff
text: 'Cost: 3 Spirituality. Use: 1 Swift Action. Effect: On your next skill check,
  one of your skills improves by one tier for that check: Untrained acts as trained.
  Trained acts as proficient. Proficient acts as advanced. Limits: This ability can
  reach advanced level at most.'
```





- **Cost:** 3 **Spirituality**.
- **Use:** 1 **Swift Action**.
- **Effect:** On your next skill check, one of your skills improves by one tier for that check:
  - Untrained acts as trained.
  - Trained acts as proficient.
  - Proficient acts as advanced.
- **Limits:** This ability can reach advanced level at most.

### Fast Learning

```yaml ability
id: paragon-seq-09-fast-learning
name: Fast Learning
pathway: paragon
sequence: 9
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
text: 'Effect (training time): You can use one day to train a skill to be trained,
  and one week to train to be proficient. It takes two weeks from proficient to advanced,
  four weeks from advanced to erudite, two months from erudite to master. The GM can
  limit the stacking skills. For example, investigators can only learn a few skills
  at most, and several skills can be advanced. Usually, except for potions, the group
  canaTMt learn more than 3 kinds, and canaTMt exceed advanced level.'
```





- **Effect (training time):**
  1. You can use one day to train a skill to be trained, and one week to train to be proficient. It takes two weeks from proficient to advanced, four weeks from advanced to erudite, two months from erudite to master.
  2. The **GM** can limit the stacking skills. For example, investigators can only learn a few skills at most, and several skills can be advanced.
     - Usually, except for potions, the group can't learn more than 3 kinds, and can't exceed advanced level.

- **Effect:** Fast Learning resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Practical Assemblies

```yaml ability
id: paragon-seq-09-practical-assemblies
name: Practical Assemblies
pathway: paragon
sequence: 9
status: canonical
type: active
action: full-round
cost: {}
roll: 1d20 + @attr.int + @skill.crafting
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.crafting
  damage_roll: 2d6 + 1d6
  heal_roll: null
  effect_roll: null
  notes: Use the relevant skill for the task (craft manufacturing, chemistry, pharmacy, deception); DV 15/20+ as listed. Chemical identification explosions deal 2d6 poison + 1d6 fire and ignore 2 armor; big failures can injure you.
scaling: []
tags:
- utility
text: 'Special: Strictly speaking, this is not a transcendent ability, but an introduction
  to applying awakened memory. Therefore, this ability cannot be stolen or recorded.
  Having awakened memory means possessing this ability. Requirements: Prepare enough
  materials, usually obtained in the [[Black Market]], [[Steam Church]], or from informal
  vendors. Use (assembly time): Perform 1 Full-Round Action to assemble items such
  as firearms, rifles, nitroglycerin. Large devices (such as textile machines) require
  10 minute. Examples (checks and results): Difficulty Value 15 craft manufacturing
  appraisal: Assemble a pocket watch, or a pistol (appearance fully customizable depending
  on whether it is steam...'
```





- **Special:** Strictly speaking, this is not a transcendent ability, but an introduction to applying awakened memory. Therefore, this ability cannot be stolen or recorded. Having awakened memory means possessing this ability.
- **Requirements:** Prepare enough materials, usually obtained in the [[Black Market]], [[Steam Church]], or from informal vendors.
- **Use (assembly time):**
  - Perform 1 **Full-Round Action** to assemble items such as firearms, rifles, nitroglycerin.
  - Large devices (such as textile machines) require 10 minute.

- **Examples (checks and results):**
  - **Difficulty Value 15** craft manufacturing appraisal: Assemble a pocket watch, or a pistol (appearance fully customizable depending on whether it is steam style or not). Weapon-related damage is taken from [[Weapon Paradigm]].
  - **Difficulty Value 20** chemical identification: Produce aqua regia and nitroglycerin.
    1. If you want to use them in battle, you need to roll identification; you produce an explosion. Damage is 2d6 poison and 1d6 fire, ignoring 2 points of armor. Two people standing together are regarded as the same target.
    2. Because they are inherently dangerous, your throws will definitely have a -4 disadvantage, and a big failure will hurt yourself. These are more suitable for non-combat or exploration.
  - **Difficulty Value 15** pharmaceutical identification: You need to make distillation equipment and other equipment first; you can make ordinary medicines (cold medicines, painkillers). They have no supernatural effect, but are slightly better than some ordinary pharmacists.
  - **Difficulty Value 15** craftsmanship and Deception check: Create an imitation of an object, similar only in appearance.
  - **Difficulty Value 20** craft manufacturing and corresponding scientific appraisal: Manufacture tools/devices for academic or manufacturing research (e.g., stills, telescopes).
  - **Difficulty Value 15** craft manufacturing identification: You need to manufacture a device such as a spinning machine first; you have manufactured high-quality clothing with customizable appearance.
  - **Difficulty Value 20+** crafting check: Make crossbows and rifles. A steam rifle would involve breaking the law.

- **Heavy weapons:**
  - For heavy weapons, **GM** should restrict. To manufacture heavy weapons, you need the consent of **GM** and relevant materials; they are not easy to find.
  - During battle, heavy weapons generally cannot be temporarily assembled because 1 set of materials is difficult to carry. If the Extraordinary brings almost nothing else, or brings a large backpack, they are allowed to carry at most 1 set.

- **Feasibility and research time:**
  - The identification of the feasibility of other theories should be in line with this era. Even if you know more advanced knowledge, it usually takes a month of research and trial and error because no one explores-unless you are a time traveler.

- **Combat timing note:**
  - If you temporarily create during combat, you cannot take any other actions, including free actions, until the creation is complete. The "1 full round" time usually refers to your next turn.

- **Effect:** Practical Assemblies resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spirit Vision
```yaml ability
id: paragon-seq-09-spirit-vision
name: Spirit Vision
pathway: paragon
sequence: 9
status: canonical
type: active
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: No roll; while active, Spiritual Intuition tests gain +1.
scaling: []
tags:
- ritual
- detection
text: 'Use: 1 Free Action to activate. Cost: 1 Spirituality per round. Effect: While
  Spirit Vision is active, you gain the following benefits: Etheric body: You can
  roughly tell whether the other partyaTMs body is good or bad through aura color,
  but you canaTMt get detailed information. Spiritual body: You can confirm whether
  an object/creature has spirituality; this cannot identify extraordinary people.
  Mental body: You can see whether the other party is thinking, but only that; you
  cannot get more detailed information. Astral body: You cannot see the astral body.
  While in the state of spiritual vision, your Spiritual Intuition test gains +1 (beneficial).'
```





- **Use:** 1 **Free Action** to activate.
- **Cost:** 1 **Spirituality** per round.
- **Effect:** While Spirit Vision is active, you gain the following benefits:


  1. **Etheric body:** You can roughly tell whether the other party's body is good or bad through aura color, but you can't get detailed information.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality; this cannot identify extraordinary people.
  3. **Mental body:** You can see whether the other party is thinking, but only that; you cannot get more detailed information.
  4. **Astral body:** You cannot see the astral body.
  5. While in the state of spiritual vision, your **Spiritual Intuition** test gains **+1** (beneficial).

- **Notes:**
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding path.
  - The colors seen by Spirit Vision allow you to see each other in the dark, but you can only see the existence of colors; it is still possible to get lost in the dark because the colors you can see are limited. You cannot use them to distinguish the undead biology.
  - **Sequence 7:** You can determine the path corresponding to extraordinary objects; see [[Spiritual Perception]] for details.
  - Spirit Vision can see some ordinary spirit bodies by default if they have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
