---
title: 'Sequence 2: Life-Giver'
id: moon-seq-02
tags:
- pathway:moon
- sequence:2
---






# Moon Pathway: Sequence 2

## Life-Giver

> **Lore:** You master the “power of creation,” making the life around you feel the joy of growth and the arrival of new life.

- See also: Blood Duke Pathway

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Bring new life to a destroyed site or barren land; at the full moon, make spirit creatures active again; make wild animals or intelligent creatures willing to come here to reproduce and pass on from generation to generation; make this place re-possess the prerequisites and foundations that can become a civilization.

> **GM Note:** The source labels this as an “unofficial ceremony.”

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2; your **Pharmacy**, **Chemistry**, and **Biology** skills increase by one level each.

### Creation Authority

```yaml ability
id: moon-seq-02-creation-authority
name: Creation Authority
pathway: moon
sequence: 2
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.biology
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.biology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Creation requires a successful science check; biology is the default mapping.
scaling: []
tags:
- ritual
- buff
text: 'Creation of all things; creation of life; fundamentally possesses the power
  of incarnation and creation. Cost: 3 points of Spirituality Use: Casting Action
  Effect: On the basis of having seen or understood creatures, you can improve, create,
  or even create a unique species out of thin air. Limits: Requires a successful corresponding
  Science test.'
```





Creation of all things; creation of life; fundamentally possesses the power of incarnation and “creation.”

- **Cost:** 3 points of **Spirituality**
- **Use:** **Casting Action**
- **Effect:** On the basis of having seen or understood creatures, you can improve, create, or even create a unique species out of thin air.
- **Limits:** Requires a successful corresponding **Science test**.

### Life

```yaml ability
id: moon-seq-02-life
name: Life
pathway: moon
sequence: 2
status: canonical
type: active
action: cast
cost:
  spirituality: 15
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
  notes: No explicit dice; this restores the target to life and clears listed afflictions.
scaling: []
conditions:
- dead
tags:
- ritual
- healing
- mobility
- debuff
- offense
text: 'You can speed up the metabolism and recovery speed of creatures, and give all
  living beings the extraordinary resilience of blood races. Cost: 15 Spirituality
  points Use: Single Casting Action Effect: Bring anyone who is not completely dead
  back to life, allowing their damaged body and even their soul to instantly restore
  and grow life. Limits: Limited to two uses per encounter. Aftereffects / Additional
  Effects: Removes any presence of curses, toxins, and diseases. Insanity is terminated
  immediately, and all Sanity / Rationality points lost due to insanity are restored.'
```





You can speed up the metabolism and recovery speed of creatures, and give all living beings the extraordinary resilience of blood races.

- **Cost:** 15 **Spirituality** points
- **Use:** Single **Casting Action**
- **Effect:** Bring anyone who is not completely dead back to life, allowing their damaged body and even their soul to instantly restore and grow life.
- **Limits:** Limited to two uses per encounter.
- **Aftereffects / Additional Effects:**
  - Removes any presence of curses, toxins, and diseases.
  - Insanity is terminated immediately, and all **Sanity / Rationality** points lost due to insanity are restored.
  - Cannot reverse loss of control; for loss of control and extraordinary creatures, this only allows them to continue to have part reason.

### Additional

```yaml ability
id: moon-seq-02-additional
name: Additional
pathway: moon
sequence: 2
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: All dead objects within your line of sight
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
conditions:
- dead
tags:
- ritual
- control
text: 'Cost: 8 points of Spirituality Use: Casting Action Targeting and range: All
  dead objects within your line of sight Effect: You can animate all dead objects
  within your line of sight, including extraordinary items. You can make undead creatures
  have part of their essence, which is judged as an ordinary existence. Limits: If
  the target is a slave of the God of Death Pathway, it can still dominate these former
  undead creatures.'
```





- **Cost:** 8 points of **Spirituality**
- **Use:** **Casting Action**
- **Targeting and range:** All dead objects within your line of sight
- **Effect:**
  - You can animate all dead objects within your line of sight, including extraordinary items.
  - You can make undead creatures have part of their essence, which is judged as an ordinary existence.
- **Limits:**
  - If the target is a slave of the God of Death Pathway, it can still dominate these former undead creatures.
  - Undead creatures transformed into ordinary existence no longer enjoy physical immunity and can be hit by vital points.
- **Additional Effects:**
  - Allied members who are cast by you at the same time can enjoy your life regeneration effect every round together, but they will not have your **Heart Weakness**.
  - The ferryman of the death path will lose the direct-looking death effect in the round you use this, and it lasts until your next round of action under normal circumstances.
    - The ferryman retains the life drain of each round.
    - Maintaining this means you need to continue to pay **Spirituality**.
    - Suppression of undead creatures is incidental.
  - Full activation of an undead creature is limited to creatures less than a demigod in a round; creatures above a demigod follow the times below. GM decides how “life grants” map to full activation uses.

- **Life grants by target Sequence (for creatures above a demigod):**
  - **Sequence 4:** Three life grants; temporary transformation into normal creatures.
  - **Sequence 3:** Five life grants; temporary transformation into normal creatures (excluding ferrymen who have completely become dead).

- **Undead transformation constraints:**
  - An undead creature of the same tier as you cannot transform unless it volunteers and you are given enough time.
  - The life grant to an undead creature wears off over time.
  - This is not really equivalent to resurrection. To turn back to the living in this way:
    - You need to repair the deformed state of the spirit body so that it looks more biological when alive.
    - There will be memory loss after resurrection.
    - It will turn back into an undead creature after one year, and completely dissipate due to exhaustion of **Spirituality**.
  - People who have been dead for many years are usually unable to do this.
  - If the target is a soulless skeleton or zombie, it cannot be resurrected into a real original person.

- **Promotion:**
  - If you have promoted to **Sequence** 1, the number of life grants required is -1.
  - **Sequence** 0 is excluded.

### Bottom-Level Improvement

```yaml ability
id: moon-seq-02-bottom-level-improvement
name: Bottom-Level Improvement
pathway: moon
sequence: 2
status: canonical
type: active
action: free
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.biology
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.biology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Biology check determines modification tier; DV thresholds map the outcome.
scaling:
- when: check_result_is_big_failure
  changes:
    effect_note: Instantly spawns a horrible monster.
- when: check_result_meets_dv_10
  changes:
    effect_note: Swap limbs or swap a natural trait (e.g., grow gills).
- when: check_result_meets_dv_15
  changes:
    effect_note: Grow an extra limb; +1 limb per 5 points above DV 15.
- when: check_result_meets_dv_20
  changes:
    effect_note: Grant a trait that cannot exist in nature; permanent.
- when: check_result_meets_dv_25
  changes:
    effect_note: More incredible transformations.
- when: check_result_meets_dv_30
  changes:
    effect_note: Target becomes a new lifeform retaining consciousness.
- when: check_result_is_big_success
  changes:
    effect_note: Makeover nearly perfectly fulfills your intent.
tags:
- ritual
- buff
text: 'You can make incredible modifications to creatures, and this modification will
  be directly engraved into the genetic information inside the gene. Cost: 3 Spirituality
  points Use: Free action Effect: Make a Biology check and apply the outcome below.
  Outcome: Big Fail: Instantly randomly spawns a horrible monster. Difficulty Value
  10: You can swap the limbs of two creatures, or swap a certain trait (e.g., make
  a human grow fish gills). Difficulty Value 15: You can cause a creature to grow
  an extra limb like a normal creatures, at a rate of one limb for every 5 points
  above Difficulty Value 15.'
```





You can make incredible modifications to creatures, and this modification will be directly engraved into the genetic information inside the gene.

- **Cost:** 3 **Spirituality** points
- **Use:** Free action
- **Effect:** Make a **Biology check** and apply the outcome below.

- **Outcome:**
  - **Big Fail:** Instantly randomly spawns a horrible monster.
  - **Difficulty Value 10:** You can swap the limbs of two creatures, or swap a certain trait (e.g., make a human grow fish gills).
  - **Difficulty Value 15:** You can cause a creature to grow an extra limb like a normal creature’s, at a rate of one limb for every 5 points above **Difficulty Value 15**.
    - Using an additional physical attack always requires a new special fighting skill; otherwise it is considered untrained.
  - **Difficulty Value 20:** You give a creature a trait that cannot exist in nature, and that trait lasts forever.
  - **Difficulty Value 25:** Even more incredible transformations.
  - **Difficulty Value 30:** Beyond the scope of transformation itself, the opponent is directly regarded as a new life that retains its own consciousness.
  - **Big hit:** A makeover that almost perfectly fulfills your wishes.

- **Limits:** As described in this section's prose.
