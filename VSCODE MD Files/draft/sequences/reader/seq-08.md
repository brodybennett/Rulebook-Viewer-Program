---
title: 'Sequence 8: Detective'
id: reader-seq-08
tags:
- pathway:reader
- sequence:8
---






# White Tower Pathway: Sequence 8

## Detective

> **Lore:** This Sequence focuses on sharper observation, stronger logical reasoning, and deep competence in ritual magic.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition +2.
- **Skill Increases:** [[Investigation]] +1 level; [[Psychology]] +1 level.
- **Rapid Skill Growth:** [[Mysticism]], Investigation, and Psychology can grow rapidly. Each time you receive **2 hours** of non-repetitive, effective guidance relevant to one of these skills, choose one guided skill; it increases by **1 level** (grade).  

- **Training Thresholds:** It takes **2**, **3**, and **4** trainings to become **proficient**, **advanced**, and **mastery** respectively. At most, you can quickly reach **proficiency** temporarily.  

- **Deduction-Based Improvement:** Each time you fully deduce almost all of a person’s experiences **and** at least one important secret—and the experience/secret *types* are not repeated—this also counts as a skill improvement (as above).
- **Spending Intuition (INT):** If you are creating a character above Sequence 9 (not just promoted), you can use **twice** the Intuition (INT) to add growth skills.  

### Basic Deduction

```yaml ability
id: reader-seq-08-basic-deduction
name: Basic Deduction
pathway: reader
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.investigation
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.investigation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Detection check; portrait deductions cap at DV 25. DV tiers 20/25/30/35 apply as listed.
scaling: []
tags:
- detection
- healing
text: '*Basic Deduction reversely restores a persons characteristics through details.
  Cost: 1 Spellcasting Action. Use: Make a [[Detection Check]] and choose 1 target.
  If deducing from a portrait, the maximum Difficulty Value is 25. Effect: You know
  people by details, gaining information based on the Difficulty Value achieved. Limits:
  Repeated deductions do not grant new clues until the result is the same; you only
  obtain new clues once circumstances/clues change enough to alter the result. Basic
  Deduction (and Action Deduction) are benefits brought by potions; they cannot be
  recorded or stolen. *Difficulty Value Results (repeat deductions until the result
  is the same before obtaining new clues):'
```





**Basic Deduction** reversely restores a person’s characteristics through details.

- **Cost:** 1 Spellcasting Action.
- **Use:** Make a [[Detection Check]] and choose 1 target. If deducing from a portrait, the maximum Difficulty Value is 25.
- **Effect:** You “know people by details,” gaining information based on the Difficulty Value achieved.
- **Limits:**
  - Repeated deductions do not grant new clues until the result is the same; you only obtain new clues once circumstances/clues change enough to alter the result.
  - **Basic Deduction** (and **Action Deduction**) are benefits brought by potions; they **cannot be recorded or stolen**.

**Difficulty Value Results** (repeat deductions until the result is the same before obtaining new clues):

1. **Difficulty Value 20:** Determine the target’s current occupation, previous occupation, and potential physical diseases.
2. **Difficulty Value 25:** In addition to the above, determine living habits, whether the target’s family is complete, and whether the target has experienced grief.
3. **Difficulty Value 30:** In addition to the above, deduce a very vague interpersonal network (who the target may be in contact with ordinarily).
4. **Difficulty Value 35:** In addition to the above, guess the target’s itinerary **6 hours ago**—where they went (information is vague).

- **Great Success:** In addition to the above, obtain detailed information on the 6-hour itinerary (including what the target ate and what kind of men or women they met). If important information is deliberately concealed, it is still impossible to obtain.
- **Big Failure:** Your reasoning goes in a badly wrong direction, and you must believe it until you get new clues.

**More Reasoning (Difficulty Value 30):** This may involve passwords, places where important items are hidden, etc. There must be clues to deduce.

- **Warning:** This is not considered [[id:alias-divination|Divination]] and is not affected by [[id:alias-anti-divination|Anti-Divination]]. However, if false clues are obtained or the target deliberately disguises themselves, your reasoning may still lead in a false direction even without a Big Failure.

> **Lore:** Example ways to describe your reasoning to others include pointing to concrete details (hands, smells, habits, living spaces) and explaining how each detail supports your conclusion.

### Action Deduction

```yaml ability
id: reader-seq-08-action-deduction
name: Action Deduction
pathway: reader
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.psychology
opposed_by: difficulty_value
range: Choose a target you have performed **Basic Deduction** on within the last **12
  hours** (in your mind).
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Psychology appraisal DV tiers 15/20/25/30/35; capped by the DV reached with Basic Deduction.
scaling: []
tags:
- utility
text: '*Action Deduction imagines a creatures next actions. Cost: 1 Spellcasting Action.
  Use: Conduct a [[Psychology Appraisal]]. Targeting and range: Choose a target you
  have performed Basic Deduction on within the last 12 hours (in your mind). Effect:
  Predict what the target will do, based on the Difficulty Value achieved. Limits:
  If the Basic Deduction information is wrong, the Action Deduction information is
  also wrong. Repeated deductions yield the same result until new clues are obtained.'
```





**Action Deduction** imagines a creature’s next actions.

- **Cost:** 1 Spellcasting Action.
- **Use:** Conduct a [[Psychology Appraisal]].
- **Targeting and range:** Choose a target you have performed **Basic Deduction** on within the last **12 hours** (in your mind).
- **Effect:** Predict what the target will do, based on the Difficulty Value achieved.
- **Limits:**
  - If the Basic Deduction information is wrong, the Action Deduction information is also wrong.
  - Repeated deductions yield the same result until new clues are obtained.
  - If your Basic Deduction of the target only reaches Difficulty Value **15**, then Action Deduction can also reach Difficulty Value **15** at most.  

**Difficulty Value Results:**

1. **Difficulty Value 15:** Deduce the target's immediate intent within **1 minute** (very vague).
2. **Difficulty Value 20:** Deduce what the target will do within **5 minutes** from the moment you separate.
3. **Difficulty Value 25:** Deduce what the target will do within **half an hour** of separation.
4. **Difficulty Value 30:** Deduce what the target will do within **2 hours** of separation (information is vague).
5. **Difficulty Value 35:** Deduce what the target will do within **6 hours** of separation (there is a big gap with the actual situation).

- **Great Success:** You directly obtain the complete and detailed action process of the target within **half an hour**, and the approximate process of the final result of your appraisal after half an hour. Your maximum time horizon is still limited by your appraisal result (example given: even on Great Success, if your total appraisal result is only 25, then the information can only be up to 2 hours).
- **Big Failure:** The content is completely wrong and very different from reality, but you must believe it until you get new clues.

- **Note:** The deduction results cannot involve things you don’t know. For example, if you don’t know the target is conducting a hidden sacrifice, you cannot obtain content related to the sacrifice. False information can cause most of your deduction to go wrong.

### Thinking Intuition

```yaml ability
id: reader-seq-08-thinking-intuition
name: Thinking Intuition
pathway: reader
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Intuition appraisal DV 25 to detect incongruity; DV 30 or Great Success reveals the source.
scaling: []
tags:
- ritual
- detection
text: '*Thinking Intuition gives you unique revelations through spirituality. Trigger:
  Whenever you make a Difficulty Value 25 Intuition Appraisal, you can detect whether
  something you have experienced before has a sense of incongruity and whether you
  have missed something. Great Success / Higher Difficulty: If the Intuition (INT)
  Appraisal is a Great Success or the Difficulty Value exceeds 30, you can judge the
  source of the incongruity, but you do not know more specific information.'
```





**Thinking Intuition** gives you unique revelations through spirituality.

- **Trigger:** Whenever you make a **Difficulty Value 25** Intuition Appraisal, you can detect whether something you have experienced before has a sense of incongruity and whether you have missed something.
- **Great Success / Higher Difficulty:** If the Intuition (INT) Appraisal is a Great Success **or** the Difficulty Value exceeds **30**, you can judge the source of the incongruity, but you do not know more specific information.

> **Lore:** Ordinary people occasionally have a weaker version of this; it reflects the brain producing a correct result without a conscious reasoning chain. This extraordinary version still relies on valid facts.

> **GM Note:** The GM may not be able to remind you to use this passive ability in time. If necessary, actively request that the trigger be checked.

- **Effect:** Thinking Intuition resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
