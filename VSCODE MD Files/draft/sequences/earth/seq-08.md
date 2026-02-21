---
title: 'Sequence 8: Doctor'
id: earth-seq-08
tags:
- pathway:earth
- sequence:8
---






# Mother Pathway: Sequence 8

> **Lore:** Known as "healing priest" in ancient times. Also called a doctor, able to cure diseases and stitch souls.

## Doctor

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +2, Agility (DEX) +1, Intuition (INT) +1.
- **Skill Gain:** Medical Guidance +1 level; Psychological Guidance +1 level.

### Rapid Growth

```yaml ability
id: earth-seq-08-rapid-growth
name: Rapid Growth
pathway: earth
sequence: 8
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
- buff
text: 'Your Medical Guidance / Psychological Guidance are included in the rapid growth
  category of Sequence 9. Each time you cure a disease/injury that: does not repeat
  the type, and has at least moderate injuries, it is also considered growth. Skill
  caps from this growth: Medical Guidance can be improved at most to Master. Psychological
  Guidance can be improved at most to Mastery.'
```





- Your Medical Guidance / Psychological Guidance are included in the rapid growth category of Sequence 9.
- Each time you cure a disease/injury that:
  - does **not** repeat the type, and
  - has at least moderate injuries,
  it is also considered growth.
- Skill caps from this growth:
  - Medical Guidance can be improved at most to **Master**.
  - Psychological Guidance can be improved at most to **Mastery**.

Use **Mastery** as the canonical tier name in this section; any "Master" mention here means **Mastery**.

- **Effect:** Rapid Growth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Heal Diseases

```yaml ability
id: earth-seq-08-heal-diseases
name: Heal Diseases
pathway: earth
sequence: 8
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.medicine
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: persistent
dice:
  check_roll: 1d20 + @attr.int + @skill.medicine
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Check roll maps the medical appraisal performed with a spellcasting action.
scaling: []
conditions:
- bleeding
tags:
- healing
text: 'Use: Passive. Effect: You have medical skills beyond reality. You can suture
  broken limbs, making them as flexible as before. Medical Appraisal: Whenever you
  use a spellcasting action to make a medical appraisal, your appraisal result is
  equal to the targetaTMs recovered health. Severed limbs: For severed limb injuries,
  you must take the severed limb and suture it; otherwise, you can only stop bleeding
  and cannot recover. Definition (Serious disease): All external wounds or injuries
  that can be treated by surgery, excluding terminal diseases. Medical supplies: Depending
  on the injury, in addition to using abilities, you also need different medical drugs/equipment
  for treatment. #### Treat...'
```





- **Use:** Passive.
- **Effect:** You have medical skills beyond reality. You can suture broken limbs, making them as flexible as before.
- **Medical Appraisal:** Whenever you use a **spellcasting action** to make a medical appraisal, your appraisal result is equal to the target's recovered health.
- **Severed limbs:** For severed limb injuries, you must take the severed limb and suture it; otherwise, you can only stop bleeding and cannot recover.

- **Definition (Serious disease):** All external wounds or injuries that can be treated by surgery, excluding terminal diseases.
- **Medical supplies:** Depending on the injury, in addition to using abilities, you also need different medical drugs/equipment for treatment.

#### Treatment Requirements by Injury Level

1. **Minor Injury:** If the patient's remaining blood volume is not less than half (rounded up), it is a minor injury.
   - **Consumes (each treatment):** 1 recovery herb **or** 3 medicinal plants.

2. **Slander:** If the patient's blood volume is less than half but not less than 3 points, it is regarded as slander.
   - **Consumes (each suturing):** 1 set of needle and thread (small volume items).
   - **Consumes (each treatment):** 1 restoration herb **or** 3 medicinal plants.

3. **Serious Injury:** Remaining blood volume is less than 3 points; dying and other states are serious injuries.
   - **Action change:** Treatment becomes **1 Full-Round Action**.
   - **Other requirements:** The rest is equal to moderate injury.
   - After blood volume returns to above the standard line of serious injury, it will be judged as moderate injury.

#### Treatment Case

A seriously injured patient needs to be treated once, turning the serious injury into a moderate injury, then judging according to the moderate injury, then turning the moderate injury into a minor injury, and then judging according to the minor injury, until fully recovered. (The extra recovery effect of the recovery herb still works.)

- **Limits:** As described in this section's prose.



### Healing

```yaml ability
id: earth-seq-08-healing
name: Healing
pathway: earth
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: Choose 1 target you touch.
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: 2d6
  effect_roll: null
  notes: Heal roll maps baseline vitality restoration; injury severity and sequence-tier adjustments are in scaling.
scaling:
- when: moderate_injury
  changes:
    heal_roll: 1d6
- when: serious_injury
  changes:
    heal_roll: 1d4
- when: sequence_7_or_higher
  changes:
    heal_roll: 3d6
    effect_note: Moderate injuries heal 2d6; serious injuries heal 1d6 at Sequence 7.
- when: sequence_6_or_higher
  changes:
    effect_note: Moderate injuries no longer suffer recovery reduction; toxin timing limits extend to 5 minutes for non-plague toxins.
- when: sequence_5_or_higher
  changes:
    heal_roll: 4d6
    effect_note: Serious injuries become treatable if not terminally ill.
tags:
- ritual
- healing
- mobility
- debuff
text: 'Cost: 3 spiritual points. Use: 1 Casting Action. Targeting and range: Choose
  1 target you touch. Effect: Restores 2d6 Vitality and removes the effect of poison
  that has not deteriorated on the body. Injury scaling: The Vitality restoration
  changes to: 1d6 for moderate injuries 1d4 for serious injuries Limits (toxins and
  timing):'
```





- **Cost:** 3 spiritual points.
- **Use:** 1 Casting Action.
- **Targeting and range:** Choose 1 target you touch.
- **Effect:** Restores 2d6 Vitality and removes the effect of poison that has not deteriorated on the body.
- **Injury scaling:** The Vitality restoration changes to:
  - 1d6 for moderate injuries
  - 1d4 for serious injuries

- **Limits (toxins and timing):**
  - The witch's plague is ineffective from infection level 3.
  - The rest of the toxins are ineffective from long-term medical treatment.

#### Scaling by Sequence (Future Improvements)

- Sequence 7: Recover 3d6 Vitality instead; 2d6 for moderate wounds; 1d6 for critical wounds.
- [[id:alias-sequence-6|Sequence 6]]:
  - Moderate injuries no longer suffer recovery reduction.
  - The witch's upper limit of healing is raised to infection level 3.
  - The rest of the toxins can still be cleared even if they miss the golden healing time, as long as it does not exceed 5 minutes.
- [[Sequence 5]]:
  - Restored Vitality changes to 4d6.
  - Serious injuries are also included in the scope of treatment; as long as it is not terminally ill, it can be treated.

#### Special

Diseases affecting more than one character, no matter how advanced they are, will suffer recovery reduction. Starting from infection level 3, they cannot be cleared by this type of spell, and they cannot be cleared even if they miss the golden healing time. The recovery effect of moderate wounds/serious wounds is reduced by 1d6.

- **Limits:** As described in this section's prose.


### Stitching the Soul

```yaml ability
id: earth-seq-08-stitching-the-soul
name: Stitching the Soul
pathway: earth
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.psychological_guidance
opposed_by: difficulty_value
range: Choose the target you touch.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychological_guidance
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Base check maps Psychological Guidance vs (10 + lost sanity); follow-up identification check uses the same skill at +2.
scaling:
- when: follow_up_identification_check
  changes:
    check_roll: 1d20 + @attr.int + @skill.psychological_guidance + 2
    opposed_by: difficulty_value
tags:
- ritual
- control
text: 'Cost: 3 spirituality points. Use: 1 spellcasting action. Targeting and range:
  Choose the target you touch. Effect: You sew up wounds suffered by other peopleaTMs
  or your own souls. Check: Psychological Guidance against a10 + lost sanity valuea.
  Identification: After a successful Psychological Guidance check, make an Identification
  check at (10 + lost sanity value + 2) to choose the symptom to end. If the identification
  is successful, you choose one symptom of madness/emotional state/mental disease
  and terminate it. This cannot stop the split personality that is semi-out of control
  / indeterminate madness / indeterminate madness, but it can end the symptoms of
  madness that are constantly b...'
```





- **Cost:** 3 spirituality points.
- **Use:** 1 spellcasting action.
- **Targeting and range:** Choose the target you touch.
- **Effect:** You sew up wounds suffered by other people's or your own souls.
- **Check:** Psychological Guidance against "10 + lost sanity value".
- **Identification:** After a successful Psychological Guidance check, make an Identification check at **(10 + lost sanity value + 2)** to choose the symptom to end.

1. If the identification is successful, you choose one symptom of madness/emotional state/mental disease and terminate it.
2. This cannot stop the split personality that is semi-out of control / indeterminate madness / indeterminate madness, but it can end the symptoms of madness that are constantly brought about by indeterminate madness, and treat the symptoms but not the root cause.

- **Note (what can/can't be terminated):** The former is a purely mental disease, while the latter is mixed with a tendency to lose control.

- **Limits:** As described in this section's prose.
