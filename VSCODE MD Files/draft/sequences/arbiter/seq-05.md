---
title: 'Sequence 5: Disciplinary Paladin'
id: arbiter-seq-05
tags:
- pathway:arbiter
- sequence:5
---






# Justiciar Pathway: Sequence 5

> **Lore:** Violators should be punished.

## Disciplinary Paladin

## Advancement

### Advancement Ritual

- **Advancement Ritual (unofficial):**
  - Face up to the crimes you have committed.
  - Assume responsibility to make up for your mistakes.
  - Tolerate no injustice, even the slightest.
  - Make yourself a completely innocent person.
  - Promote only after confirming you will no longer bear any sins.

### Promotion Effects

- At the moment of promotion, a Beyonder may appear loyal to the law, but may not be innocent enough; this is a major taboo for promotion to disciplinary knights.
- For every fault in the life of a Beyonder that has not been made up for, the Beyonder must accept the corresponding punishment; at the moment of promotion, the Beyonder suffers **one injury** per such fault. [[Injury]]
- The more mistakes, the more the Beyonder is torn apart, and may eventually:
  - Die on the spot, **or**
  - Collapse into a monster because the law enforcers violated the order. [[Law Enforcers]]
- Even minor crimes (e.g., crossing the road) require self-punishment.
- Only when all crimes are punished as they should be punished can the Beyonder be promoted safely.
- Generally speaking, anyone will break the law inadvertently in their life, so it is dangerous to assume one’s ordinary life is just and straightforward.
- The fewer sins left unpaid, the easier it is to succeed in promotion.
- What counts as a "safe" number of unpaid sins is GM-defined based on severity.
- Because it is generally impossible to completely count unconscious violations, it is normal to feel at least intense torture during promotion.
- Once the promotion is completely completed, the Beyonder will feel a new life.

> **Lore:** “Those who try to hold a sword must first stab the sword at themselves, and make a corresponding awareness.”

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +1.
- All your attack skills can be learned as **Knowledge** skills at **Proficient**.

- **Retribution:** You gain the following laws related to punishment. [[Laws]]

### The Violator Shall Be Punished!

```yaml ability
id: arbiter-seq-05-the-violator-shall-be-punished
name: The Violator Shall Be Punished!
pathway: arbiter
sequence: 5
status: canonical
type: active
action: attack
cost:
  spirituality: 2
roll: null
opposed_by: none
range: Choose 1 target within 50 meters that violates your **Forbidden Law**. [[Forbidden
  Law]]
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- offense
text: 'Use: 1 Attack Action. Attack Action Cost: Consume 2 Spirituality. [[Spirituality]]
  Targeting and range: Choose 1 target within 50 meters that violates your Forbidden
  Law. [[Forbidden Law]] Effect: Make 1 Melee Attack. [[id:alias-melee-attack|Melee
  Attack]] This attack must hit (guaranteed hit). Limits: This cannot be used with
  [[id:alias-death|Death]] / [[Whiplash]] and other laws.'
```





- **Use:** 1 **Attack Action**. Attack Action
- **Cost:** Consume 2 **Spirituality**. [[Spirituality]]
- **Targeting and range:** Choose 1 target within 50 meters that violates your **Forbidden Law**. [[Forbidden Law]]
- **Effect:** Make 1 **Melee Attack**. [[id:alias-melee-attack|Melee Attack]] This attack must hit (guaranteed hit).
- **Limits:** This cannot be used with [[id:alias-death|Death]] / [[Whiplash]] and other laws.

> **GM Note:** Example: even if a giant dragon is flying in the air, you can bounce up at once, jump higher than the dragon can fly, and achieve the inevitable-hit effect in an unreasonable form.

### Punishment Target: Biological Type

```yaml ability
id: arbiter-seq-05-punishment-target-biological-type
name: 'Punishment Target: Biological Type'
pathway: arbiter
sequence: 5
status: adapted
type: active
action: attack
cost:
  spirituality: 3
roll: 1d20 + @attr.str + @skill.fighting
opposed_by: physical_defense
range: Designate 1 target within 50 meters, then name the corresponding **creature
  type**. [[Creature Type]]
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.str + @skill.fighting
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Adapted as a melee-attack rider; damage_roll represents additional damage on top of the underlying melee weapon strike.
scaling:
- when: target_is_undead_and_holy_conversion_applies
  changes:
    damage_roll: 2d6
- when: cold_conversion_applies
  changes:
    effect_note: Target suffers -2 on next identification within 1 round and movement is halved (round up).
damage_types:
- psychic
tags:
- ritual
- buff
- offense
text: 'Use: 1 Attack Action. Attack Action Cost: Consume 3 Spirituality. [[Spirituality]]
  Targeting and range: Designate 1 target within 50 meters, then name the corresponding
  creature type. [[Creature Type]] Effect: Perform 1 Melee Attack. [[id:alias-melee-attack|Melee
  Attack]] Increase damage by 1d6. Change the damage type to the type that can traumatize
  the enemy to the greatest extent (see below). [[Damage Type]] Limits: This change
  excludes psychic damage. [[psychic damage]] #### Damage Type Conversion'
```





- **Use:** 1 **Attack Action**. Attack Action
- **Cost:** Consume 3 **Spirituality**. [[Spirituality]]
- **Targeting and range:** Designate 1 target within 50 meters, then name the corresponding **creature type**. [[Creature Type]]
- **Effect:** Perform 1 **Melee Attack**. [[id:alias-melee-attack|Melee Attack]]
  - Increase damage by **1d6**.
  - Change the **damage type** to the type that can traumatize the enemy to the greatest extent (see below). [[Damage Type]]
- **Limits:** This change excludes **psychic damage**. [[psychic damage]]

> **GM Note:** Example: “Punishment objects: resentful souls and ghosts!” While gaining extra damage, your attack is changed to **holy damage**.

#### Damage Type Conversion

1. **Holy damage:** [[Holy Damage]]
   - When the punishment target is ghost/wraith/living corpse/skeleton/Rose bishop/vampire/demon, the attack changes to holy damage.
   - It gains an additional **1d6** damage restraint effect only when facing **undead creatures**. [[Undead]]
2. **Curse damage:** [[Curse Damage]]
   - Change when the punishment target is human/other living creatures/any creature with the lowest curse resistance.
3. **Cold damage:** [[Cold Damage]]
   - Change when the punishment target is gargoyle/golem/any creature with the lowest cold resistance.
   - The hit creature suffers **-2 disadvantage** on the next identification within **1 round**, and its movement power is halved (round up). Disadvantage Identification [[Movement Power]]
   - Sexual creatures are exempt at the GM's discretion.
4. **Fire damage:** [[Fire Damage]]
   - Change when the punishment target is a frozen creature/spider silk/plant/any creature with the lowest fire resistance.
5. **Poison damage:** [[Poison Damage]]
   - Change when the punishment target is plant/spider silk/poisoned creature/any creature with the lowest poison resistance.

- **Special:** Punishment abilities can also shift if there are more valid damage types, but excluding psychic damage. [[Damage Type]]
- When multiple resistances of a certain creature are the same, the GM chooses one of the most effective damage types to change. [[Resistance]]

### The Guilty Shall Be Restrained!

```yaml ability
id: arbiter-seq-05-the-guilty-shall-be-restrained
name: The Guilty Shall Be Restrained!
pathway: arbiter
sequence: 5
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: Choose 1 target within 50 meters.
target: designated target(s)
duration: The restriction effect lasts for **1 round**.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
conditions:
- restrained
tags:
- ritual
- control
- defense
text: 'Use: 1 Spellcasting Action. Spellcasting Action Cost: Consume 3 Spirituality.
  [[Spirituality]] Targeting and range: Choose 1 target within 50 meters. Effect:
  Choose the crime of the target and announce the crime (e.g., illegal trespassing
  into another persons house is a crime), then connect with the guilty shall be restricted!
  Different crimes can be handled in one use, with separate sentences for each. Restraint
  (choose by crime severity): Minor crime: Agility (DEX) and evasion in mobility/physical
  defense -2 disadvantage. Agility (DEX) [[Evasion]] [[Mobility]] [[Physical Defense]]
  Disadvantage'
```





- **Use:** 1 **Spellcasting Action**. Spellcasting Action
- **Cost:** Consume 3 **Spirituality**. [[Spirituality]]
- **Targeting and range:** Choose 1 target within 50 meters.
- **Effect:**
  - Choose the crime of the target and announce the crime (e.g., “illegal trespassing into another person’s house is a crime”), then connect with “the guilty shall be restricted!”
  - Different crimes can be handled in **one use**, with separate sentences for each.
- **Restraint (choose by crime severity):**
  - **Minor crime:** Agility (DEX) and evasion in mobility/physical defense **-2 disadvantage**. Agility (DEX) [[Evasion]] [[Mobility]] [[Physical Defense]] Disadvantage
  - **Moderate crime:** Agility (DEX) and evasion in mobility/physical defense **-4 disadvantage**. Disadvantage
  - **Serious crime:** Agility (DEX) and evasion in mobility/physical defense **-6 disadvantage**. Disadvantage
- **Duration:** The restriction effect lasts for **1 round**.
- **Limits:** After 1 round, the same crime cannot be sentenced again, and the corresponding crime is deemed to have disappeared. [[Sentencing]]
