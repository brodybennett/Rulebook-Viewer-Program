---
title: 'Sequence 3: Chaoswalker'
id: fate-seq-03
tags:
- pathway:fate
- sequence:3
---






# Wheel of Fortune Pathway: Sequence 3

## Chaoswalker

- You are a **Sequence** 3 **Saint** of the [[Wheel of Fortune]].

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Disturb the torrent of fate related to yourself, make the fate orientation of this “river” no longer logical, find at least three ways of survival from this chaotic development within a day, and put them into practice at the same time.

> **GM Note:** The RAW notes this is an “unofficial ceremony,” and warns that causing chaotic fate around yourself can spill onto the city and anyone who might interact with you that day, potentially leading to sudden deaths, drawing attention from nearby forces, or being wiped out in the chaos.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Luck** +3, **Intuition (INT)** +3, **Constitution** +1.

### Chaos Walker

```yaml ability
id: fate-seq-03-chaos-walker
name: Chaos Walker
pathway: fate
sequence: 3
status: canonical
type: active
action: free
cost:
  spirituality: 5
roll: null
opposed_by: none
range: self
target: self
duration: Until you end it.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No roll required; reverses big success/failure outcomes and consumes stored luck/bad luck.
scaling: []
tags:
- ritual
text: 'Cost: 5 Spirituality. Use: Free Action. Effect: In your environment, you reverse
  the course of events around you. Within a maximum of 1 kilometer of you, a Big Success
  is considered a Big Failure, and a Big Failure is considered a Big Success. Limits:
  If a check has already been made and you use this ability at that time, rolls that
  have already been checked before that time are not affected by this ability, except
  for uses from other abilities that refer to this check. Each inversion reduces your
  stored Bad Luck by 5 points or your stored Luck by 5 points. When only one of these
  values is insufficient, Bad Luck points will be used as Luck points, and Luck points
  will also be used as Bad...'
```





- **Cost:** 5 **Spirituality**.
- **Use:** **Free Action**.
- **Effect:** In your environment, you reverse the course of events around you. Within a maximum of 1 kilometer of you, a **Big Success** is considered a **Big Failure**, and a **Big Failure** is considered a **Big Success**.
- **Limits:**
  - If a check has already been made and you use this ability at that time, rolls that have already been checked before that time are not affected by this ability, except for uses from other abilities that refer to this check.
  - Each inversion reduces your stored **Bad Luck** by 5 points or your stored **Luck** by 5 points. When only one of these values is insufficient, **Bad Luck** points will be used as **Luck** points, and **Luck** points will also be used as **Bad Luck** points.
  - When your stored **Luck** or **Bad Luck** reaches 0 (you cannot pay the cost), this ability becomes invalid.
- **Duration:** Until you end it.
- **Aftereffects:** You can end the **Big Failure**/**Big Success** reversal as a **Casting Action**.

### Chaos Walker (Additional)

```yaml ability
id: fate-seq-03-chaos-walker-additional
name: Chaos Walker (Additional)
pathway: fate
sequence: 3
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
text: 'Cost: 5 Spirituality (the same cost as Chaos Walker). Use: Once per Round.
  Effect: This can be used on a Big Success or a Big Failure of an Appraisal without
  opening it. A targets Big Success is regarded as a Big Failure, and a targets Big
  Failure is regarded as a Big Success, but it doubles the amount of Doom or Luck
  you have stored. Limits: If Chaos Walker is already activated, this additional ability
  is considered assimilated with the area ability and cannot be applied again.'
```





- **Cost:** 5 **Spirituality** (the same cost as Chaos Walker).
- **Use:** Once per **Round**.
- **Effect:** This can be used on a **Big Success** or a **Big Failure** of an **Appraisal** without opening it. A target’s **Big Success** is regarded as a **Big Failure**, and a target’s **Big Failure** is regarded as a **Big Success**, but it doubles the amount of **Doom** or **Luck** you have stored.
- **Limits:** If Chaos Walker is already activated, this additional ability is considered assimilated with the area ability and cannot be applied again.

### Destiny: Disturb the Torrent of Fate

```yaml ability
id: fate-seq-03-destiny-disturb-the-torrent-of-fate
name: 'Destiny: Disturb the Torrent of Fate'
pathway: fate
sequence: 3
status: canonical
type: active
action: cast
cost:
  spirituality: 10
roll: 1d20 + @attr.luk
opposed_by: difficulty_value
range: Everyone within 1 kilometer of you, excluding yourself.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.luk
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Targets make a Luck check against DV 20; outcomes apply immediately.
scaling:
- when: check_result_meets_dv_20
  changes:
    effect_note: Target takes an immediate action that is treated as a big success.
- when: check_result_fails_dv_20
  changes:
    effect_note: Target suffers a calamity and their next appraisal fails automatically.
tags:
- ritual
- divination
text: 'Cost: 10 Spirituality. Use: 1 Spellcasting Action; once per Encounter. Targeting
  and range: Everyone within 1 kilometer of you, excluding yourself. Effect: Each
  affected target immediately conducts a Luck Test. Those who pass the Luck Appraisal
  at Difficulty Value 20 immediately take an action; that action is directly regarded
  as a Big Success. Those who fail the Luck Appraisal immediately suffer a calamity,
  and their next Appraisal will definitely fail. Limits: This ability cannot be reversed
  between Big Failure and Big Success.'
```





- **Cost:** 10 **Spirituality**.
- **Use:** 1 **Spellcasting Action**; once per **Encounter**.
- **Targeting and range:** Everyone within 1 kilometer of you, excluding yourself.
- **Effect:**
  - Each affected target immediately conducts a **Luck Test**.
  - Those who pass the **Luck Appraisal** at **Difficulty Value** 20 immediately take an action; that action is directly regarded as a **Big Success**.
  - Those who fail the **Luck Appraisal** immediately suffer a calamity, and their next **Appraisal** will definitely fail.
- **Limits:** This ability cannot be reversed between **Big Failure** and **Big Success**.
