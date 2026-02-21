---
title: 'Sequence 6: Biologist'
id: earth-seq-06
tags:
- pathway:earth
- sequence:6
---






# Mother Pathway: Sequence 6

## Biologist

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +1, Intuition (INT) +1
- [[Biology (skill)]] increased by 1 level.

### Rapid Growth Research

```yaml ability
id: earth-seq-06-rapid-growth-research
name: Rapid Growth Research
pathway: earth
sequence: 6
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
text: Your Biology has been included in the rapid growth category of Sequence 9 rapid
  growth category. Biology can be upgraded to [[Erudition]] at most, and [[Botany
  (skill)]] can also be upgraded to Erudition. Every time you complete a complete
  research without repeating the type, it is regarded as a growth.
```





- Your Biology has been included in the rapid growth category of Sequence 9 rapid growth category.
- Biology can be upgraded to [[Erudition]] at most, and [[Botany (skill)]] can also be upgraded to Erudition.
- Every time you complete a complete research without repeating the type, it is regarded as a growth.

- **Effect:** Rapid Growth Research resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Biological Hybridization

```yaml ability
id: earth-seq-06-biological-hybridization
name: Biological Hybridization
pathway: earth
sequence: 6
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
text: 'Biological Hybridization: You can hybridize various organisms to produce strange
  products, and you can hybridize down to the bacterial level. Biological Hybridization
  is not a short-term ability. Like scientific research, it must go through multiple
  stages such as theory, practice, and error correction. Through this ability, you
  can permanently transform a certain entry of one creature into another creature.
  Creature definition: A acreaturea includes intelligent creatures, plants, and animals;
  you can cross any type of them. #### Transformation Procedure To use Biological
  Hybridization, complete all stages below to finish one transformation: 1) Confirm
  the modified creature Choose: A crea...'
```





- **Biological Hybridization:** You can hybridize various organisms to produce strange products, and you can hybridize down to the bacterial level.

Biological Hybridization is not a short-term ability. Like scientific research, it must go through multiple stages such as theory, practice, and error correction. Through this ability, you can permanently transform a certain entry of one creature into another creature.

- **Creature definition:** A "creature" includes intelligent creatures, plants, and animals; you can cross any type of them.

#### Transformation Procedure

To use Biological Hybridization, complete all stages below to finish one transformation:

1) **Confirm the modified creature**
   - Choose:
     - A creature you mainly transform, and
     - A creature whose entry is the "transferred" sample.
   - Example: If you want to eat apples instead of medicine, prepare apples and medicinal materials, and transfer the "cough" entry to apples.
   - Sample requirement: Some samples must represent the corresponding entries. For example, when transferring internal organs of creatures, the samples must be internal organs rather than blood.

2) **Theoretical stage**
   - After obtaining samples of the two creatures, you need **1d2 weeks** to confirm the theoretical direction of transformation.
- If you have enough realistic inspiration, then as long as you have summarized the general content of the theory in reality, you can skip this step (GM approval based on your Intuition (INT) and prior research).

3) **Experiment phase**
   - You need **1d3 months** to carry out the experiment and conduct a biological identification with **Difficulty Value** 25.
   - If the identification fails, there is a problem with the experiment; you must conduct another **1d3 months** of experiments until the identification is successful.
   - **Special:**
     - You must have **2 hours** for experiments every **24 hours**.
     - For every additional hour, the experimental identification will be **+1 beneficial**.
      - You must maintain this schedule every day to gain additional-hour benefits.
      - Additional-hour bonuses are counted beyond the required **2 hours** per day.
      - If a day does not meet the 2-hour baseline, no additional-hour bonus is gained for that day.

4) **Analysis stage**
   - You need **1d3 months** to analyze experimental data and compare it with your theory to adjust the direction of the next experiment.
- This **1d3 months** also includes any repeat experiment after a failed attempt; you do not repeat the **Difficulty Value 25** identification during this analysis stage.

5) **Achievement stage**
   - The creature you mainly transform gets the transferred entry and becomes a special hybrid species.

#### Notes

- There is no upper limit to the number of times a creature can be transformed, but some effects may require multiple transformations to achieve.
- Example: To turn fish blood into wine, you need to combine the fish with some plant sugar entries, then combine microorganisms that convert sugar into wine with another fish, then combine the two fish to achieve the result.
- Your transformation base must be a creature.

> **GM Note:** When creating a Biologist who has not just been promoted, the **GM** can allow them to enter play with modifications equal to the attribute of Intuition (INT), because a modification needs to be researched several times to be considered complete, so the number of times each modification has been modified will not be counted.

#### Hybrid Extraordinary Creatures

- If Biologists transfer the entry of a certain [[Extraordinary creature]] / Extraordinary to another species, they need to obtain samples of the corresponding entry of the Extraordinary.
  - Example: If they want to transfer the cell proliferation of the [[Rose Bishop]], they must obtain the flesh and blood of the Rose Bishop.
- This is considered to have passed on the Rose Bishop's flesh and blood growth entry.
- The species after transformation is not regarded as Extraordinary items / [[Spiritual Materials]], and has become an independent species that does not contain [[Extraordinary characteristics]], but has corresponding properties.
- Whether the entry to be transferred is an extraordinary creature or a normal transformation, the content must be specific and cannot be broad.
  - Example: You can transfer the cell proliferation of the Rose Bishop, but you cannot transfer the entry of the Rose Bishop Sequence 6 (representing all abilities).
- After being transferred, the new species inherits the special type represented by the transferred entry (for example, a mushroom inheriting the Rose Bishop's cell proliferation ability).
  - Even if it does not have Extraordinary characteristics, it is still regarded as a [[fallen creature]] and belongs to [[evil]].

> **GM Note:** Because failure of the experiment can face serious consequences, organisms that fail the experiment may die or leave serious sequelae.

- **Effect:** Biological Hybridization resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Highly Toxic

```yaml ability
id: earth-seq-06-highly-toxic
name: Highly Toxic
pathway: earth
sequence: 6
status: adapted
type: active
action: attack
cost:
  spirituality: 3
roll: 1d20 + @attr.dex + @skill.throwing
opposed_by: physical_defense
range: The throw resists physical defense.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.dex + @skill.throwing
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Baseline roll maps the hair-throw attack; secondary symptom checks are in scaling.
scaling:
- when: severe_itching_effect
  changes:
    opposed_by: difficulty_value
    check_roll: 1d20 + @attr.wil
    damage_roll: 1d3
    effect_note: Failure on Difficulty Value 20 Will test forces scratching and self-damage.
- when: shortness_of_breath_effect
  changes:
    effect_note: Target suffers ongoing -2 penalties to skills/attributes.
- when: laughing_wildly_effect
  changes:
    opposed_by: difficulty_value
    check_roll: 1d20 + @attr.wil
    effect_note: Will test (DV 10) required to perform attack/cast/full-round actions.
- when: vomiting_effect
  changes:
    opposed_by: difficulty_value
    check_roll: 1d20 + @attr.con
    damage_roll: 1d6
    effect_note: Failure on DV 20 Constitution appraisal causes vomiting and vitality loss.
- when: cough_effect
  changes:
    opposed_by: difficulty_value
    check_roll: 1d20 + @attr.wil
    effect_note: Failure on DV 15 Will test causes action loss.
- when: detoxification_attempt_with_medicine
  changes:
    opposed_by: difficulty_value
    check_roll: 1d20 + @attr.int + @skill.medicine
    effect_note: Medicine check (DV 20) within 2 rounds can end the effect early.
tags:
- ritual
- debuff
- defense
- offense
text: 'Your hair can be highly toxic. Cost: 3 [[Spirituality]] Use: 1 Attack Action.
  Tear off a handful of your hair, designate one effect below, then throw it at the
  target. Targeting and range: The throw resists physical defense. Effect: Deals 2d6
  poison damage, and the designated effect takes effect. #### Effects 1) Severe Itching
  Every time a new round starts, the target must immediately make a Will Test (Difficulty
  Value 20), otherwise it is forced to use a Swift Action to scratch the skin, causing
  1d3 physical damage to itself.'
```





Your hair can be highly toxic.

- **Cost:** 3 [[Spirituality]]
- **Use:** 1 Attack Action. Tear off a handful of your hair, designate one effect below, then throw it at the target.
- **Targeting and range:** The throw resists physical defense.
- **Effect:** Deals **2d6** poison damage, and the designated effect takes effect.

#### Effects

1) **Severe Itching**
   - Every time a new round starts, the target must immediately make a Will Test (Difficulty Value **20**), otherwise it is forced to use a Swift Action to scratch the skin, causing **1d3** physical damage to itself.

2) **Shortness of Breath**
   - The target's breath begins to weaken, the eyes lose focus, and the skills and attribute appraisals continue to suffer **-2 disadvantages**.

3) **Laughing Wildly**
   - The target can't hold back laughter and can't breathe.
   - Attacking / casting / full-round actions require a Will Test (Difficulty Value **10**) to execute successfully.

4) **Vomiting**
   - Every time a new round starts, the target must make a Constitution appraisal (Difficulty Value **20**), otherwise it starts vomiting and loses **1d6 Vitality**.

5) **Cough**
   - Every time a new round starts, the target must make a Will Test (Difficulty Value **15**), otherwise it coughs violently and loses **1** attack/Casting Action, or **2** swift actions.

#### Detoxification

- **Use:** Use 1 Casting Action to perform any [[Medicine (skill)]] (Difficulty Value **20**) within **2 rounds**, or take a potion that can detoxify.
- **Effect:** The effect will continue after this time until **1 hour** passes, or until extraordinary medicine **Rescue** is used (whichever comes first).
- **Special:** If the same biological effect is applied by more than **1** character, it lasts only **1 round**; if applied by more than **2** characters, it has no effect.

- **Limits:** As described in this section's prose.
