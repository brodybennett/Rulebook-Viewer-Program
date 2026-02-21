---
title: 'Sequence 7: Cryptologist'
id: error-seq-07
tags:
- pathway:error
- sequence:7
---






# Error Pathway: Sequence 7

A Cryptologist can analyze many mysteries (such as dreams and illusions) and can also determine an enemy's location through analysis.

## Cryptologist

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Agility (DEX) +1, Constitution +1, Intuition (INT) +2.
- Your **Occult** and **Detection** skills increase by 1 level.
- Whenever you complete a decryption of extraordinary events, your **Occult** increases by 1 level.
- If no extraordinary events are involved, your **Investigation** increases by 1 level.
- These two types of events must be more complicated and challenging.
  - The standard is whether the event may bring danger to you.
  - Events that are too monotonous and ordinary are not included in the corresponding category.
- This kind of improvement can at most reach proficiency.

### Premonition of Danger

```yaml ability
id: error-seq-07-premonition-of-danger
name: Premonition of Danger
pathway: error
sequence: 7
status: adapted
type: reaction
action: none
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
  notes: Triggered Intuition appraisal against DV 15; defensive benefits apply on success as described.
scaling:
- when: check_result_meets_dv_15
  changes:
    effect_note: Success prevents raids/ambushes and grants +4 temporary Physical Defense unless light/lightning.
- when: incoming_attack_is_firearm_or_lightning_or_light
  changes:
    effect_note: Resolve defense using normal Agility/Dodge instead of the +4 bonus.
- when: sequence_6_or_higher
  changes:
    effect_note: Intuition appraisal succeeds by default and provides clearer imagery.
- when: sequence_5_or_higher
  changes:
    effect_note: Can perceive danger higher than Sequence 1.
tags:
- divination
- healing
- offense
text: 'Also known as intuitive premonition. You can predict othersaTM actions at critical
  moments and perceive danger. Use: Triggered whenever you are raided, sneak attacked,
  or there is something on the scene that is about to put the raid or sneak attack
  into action. Use: If 1 damage exceeds half of your maximum health (rounded up),
  this ability can also be triggered. Effect: 1) Make an Intuition (INT) appraisal
  (Difficulty Value 15). If you succeed, an idea flashes in your mind immediately,
  telling you the form of danger. After you succeed, you will not be able to be raided
  or ambushed. Threats that you mistakenly think are asafea will not trigger this
  ability. 2) Under the above premise, as l...'
```





Also known as intuitive premonition. You can predict others' actions at critical moments and perceive danger.

- **Use:** Triggered whenever you are raided, sneak attacked, or there is something on the scene that is about to put the raid or sneak attack into action.
- **Use:** If 1 damage exceeds half of your maximum health (rounded up), this ability can also be triggered.
- **Effect:**
  1) Make an Intuition (INT) appraisal (**Difficulty Value** 15). If you succeed, an idea flashes in your mind immediately, telling you the form of danger.
     - After you succeed, you will not be able to be raided or ambushed.
     - Threats that you mistakenly think are "safe" will not trigger this ability.
  2) Under the above premise, as long as you are not restrained or affected by other reasons, your **physical defense** gains a +4 **temporary bonus**.
     - In the face of light and lightning, use normal Agility (DEX) and Dodge in Physical Defense instead of the +4 bonus.
  3) If the danger range is large enough (for example, a gas explosion in the entire area in an instant), even if you are alarmed by the danger, you will not be able to gain benefits.

- **Special:**
  - Dangers higher than 1 level cannot be foreseen.
  - Hazards dependent on luck are foreseeable but gain no benefit.
  - Danger premonition is a kind of spiritual intuition, so it is invalidated by [[id:alias-anti-divination|Anti-Divination]] and [[Anti-Prophecy]].

- **Sequence scaling:**
  - **Sequence 6:** Your Intuition (INT) appraisal is successful by default, and the flashing thought becomes a flashing picture, letting you know the manifestation of danger. [[id:alias-sequence-6|Sequence 6]]
  - **Sequence 5:** You can perceive danger higher than Sequence 1. [[Sequence 5]] [[Personality]]

- **Limits:** As described in this section's prose.


### Decryption

```yaml ability
id: error-seq-07-decryption
name: Decryption
pathway: error
sequence: 7
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Base decryption uses Occultism; Investigation-based decryption is captured in scaling.
scaling:
- when: mundane_or_non_extraordinary_case
  changes:
    check_roll: 1d20 + @attr.int + @skill.investigation
    effect_note: Use Investigation for non-extraordinary cases.
- when: dv_20_detection_appraisal
  changes:
    effect_note: Detection/appraisal uses Difficulty Value 20, improved by +2 per clue.
- when: dv_30_identity_detection
  changes:
    effect_note: Identity detection uses Difficulty Value 30 with clue-based bonuses.
- when: dv_35_truth_reconstruction
  changes:
    effect_note: Truth reconstruction uses Difficulty Value 35 with clue-based bonuses.
tags:
- ritual
- detection
text: 'You can analyze many mysteries (such as dreams and illusions), and you can
  also find out an enemyaTMs location through analysis. Use: 1 Casting Action Cost:
  3 spirituality points Effect: Choose 1 of the following effects: a Detection and
  appraisal (Difficulty Value 20): Choose a clue. You learn: The information represented
  by the clue. Whether it involves an extraordinary event. A rough answer at Difficulty
  Value 20.'
```





You can analyze many mysteries (such as dreams and illusions), and you can also find out an enemy's location through analysis.

- **Use:** 1 **Casting Action**
- **Cost:** 3 **spirituality points**
- **Effect:** Choose 1 of the following effects:

  1. **Detection and appraisal** (**Difficulty Value** 20): Choose a clue. You learn:
  - The information represented by the clue.
  - Whether it involves an extraordinary event.
  - A rough answer at Difficulty Value 20.
  - Each time the appraisal exceeds 5 points of appraisal difficulty, the content you get becomes clearer.

  2. **Detection test** (**Difficulty Value** 30): Choose a creature. You reveal its full name, identity, and other people's nickname or nickname for it.
  - This test must obtain any of the following clues to proceed:
    - Know what other people call it / nickname / first name / surname.
    - Know its general experience, past, or identity information, or important things.
    - Witness 1 full episode of its actions in any event, or any 1 occasion where (based on its personality) it is emotional, uttered, or overly calm.
    - Other possible clues.
  - Once there are 3 clues above, the identification is successful by default.
  - For every 1 clue, your detection identification gains a +2 favorable bonus.
  - The content of obtained clues must be true. If it is contrary to the truth, it is a disguise, and what you get will also be false information.

  3. **Detection appraisal** (**Difficulty Value** 35): You restore the complete truth of a matter and calculate the next development and result of this matter.
  - Each time you have a clue whose meaning you already know, your detection appraisal gains a +2 beneficial bonus.
  - Clues include the real names, identities, and general past of the people involved in the incident (each clue in 2. is calculated independently).
  - If you do not truly grasp all the clues, the restored truth is also incomplete truth, and there will be some false content.

- **Special:** The truth that can be restored includes:
  - The extraordinary path of a creature,
  - The specific effect of an extraordinary ability,
  - The type of extraordinary ability,
  - The map of an area,
  - The principle of a maze,
  - Etc.
  - Restored truth can only cover information contained in your available clues; it does not infer facts outside that clue scope.

- **Other uses of 1.:**
  - Distinguish between hallucinations and falsehoods.
  - Reveal the meaning of hallucinations or dream content.
  - Reveal the type of extraordinary ability that a clue may represent (such as illusion, flame, ability strength, etc.).
  - Judge whether the caster is far stronger or weaker than your own.

- **About Decryption:**
  - Decryption is not a kind of [[id:alias-divination|Divination]]. It is pure deduction in the mind.
  - Therefore, Decryption ignores [[id:alias-anti-divination|Anti-Divination]] and [[Anti-Prophecy]], and generally does not arouse spiritual responses. [[Spiritual Responses]]

- **About Anti-Divination:**
  - You can use one Decryption skill and choose one item of specific mystical information related to you (for example: you plan to attack someone next) to realize anti-divination.
  - Conduct detection and appraisal; the check result becomes the difficulty of anti-divination.
  - When successful, this information is excluded in related divination, spiritual intuition, and prophecy unless it exceeds the corresponding difficulty.

- **Limits:** As described in this section's prose.
