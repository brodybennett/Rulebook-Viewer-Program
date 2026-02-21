---
title: 'Sequence 2: Justiciar'
id: arbiter-seq-02
tags:
- pathway:arbiter
- sequence:2
---






# Justiciar Pathway: Sequence 2

## Justiciar

- You can sense imbalances in the surrounding area and detect hidden targets.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Let the chaotic things that have been out of order for hundreds of years become a part of harmony and balance with today’s social order. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Charisma +3; Intuition (INT) +1; Agility (DEX) +1; Strength +1; Constitution +1.
- **Skill Gain:** [[Law skill]] +1 skill level.

### Sage's Balance

```yaml ability
id: arbiter-seq-02-sage-s-balance
name: Sage's Balance
pathway: arbiter
sequence: 2
status: canonical
type: active
action: free
cost:
  spirituality: 5
roll: null
opposed_by: none
range: Choose a designated area within 1 kilometer of you as the center (includes
  you and everyone in the area).
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling:
- when: ordinary_people_included_in_area
  changes:
    effect_note: Ordinary people count as sequence value 10 for balancing calculations.
tags:
- ritual
text: 'Use: Free Action Free Action. Cost: 5 spiritual points [[Spirituality]] (total).
  Targeting and range: Choose a designated area within 1 kilometer of you as the center
  (includes you and everyone in the area). Effect: You balance the designated area
  by speaking the corresponding law (decree). [[law (decree)]] Determine the strongest
  and weakest Sequence levels present in the area and use them as the benchmark. Set
  everyone in the area (including you) to the same intensity Sequence level: Add the
  strongest and weakest Sequence levels, divide by 2, and round up to a whole Sequence
  level.'
```





- **Use:** **Free Action** Free Action.
- **Cost:** 5 **spiritual points** [[Spirituality]] (total).
- **Targeting and range:** Choose a designated area within 1 kilometer of you as the center (includes you and everyone in the area).
- **Effect:**
  - You “balance” the designated area by speaking the corresponding **law** (decree). [[law (decree)]]
  - Determine the **strongest** and **weakest** Sequence levels present in the area and use them as the benchmark.
  - Set everyone in the area (including you) to the same “intensity” Sequence level:
    - Add the strongest and weakest Sequence levels, divide by 2, and **round up** to a whole Sequence level.
    - Example: if the strongest is Sequence 1 and the weakest is Sequence 9, then (1 + 9) ÷ 2 = 5, so everyone becomes Sequence 5.
  - Existing higher-Sequence abilities do not disappear, but their **strength** is reduced to match the balanced Sequence level.
  - Any Beyonder weaker than the balanced Sequence level is promoted to that level immediately in **personality** and strength, but does **not** gain higher-Sequence abilities.
  - Within the affected area, there is no more **personality suppression**. [[Personality Suppression]]
  - Additional adjustment for targets above your Sequence:
    - For each Sequence level an affected person is higher than you, their resulting balanced Sequence level is **-1**.
    - Example (using the Sequence 1 vs Sequence 9 case above): even if others become Sequence 5, if you are Sequence 2 and apply this to a Sequence 1, that target’s resulting level becomes Sequence 4 (not Sequence 5).
  - Special case—**King of Angels**:
    - A King of Angels is treated as a separate personality improvement. If the enemy is a King of Angels, their personality is raised by another level on the basis of Sequence 1. [[King of Angels]]
  - This does not change the outcome for other low-Sequence Beyonders in the area: all low-Sequence Beyonders are still promoted to the corresponding Sequence 5 level, regardless of whether the strongest exceeds your Sequence level.
  - Leader adjustment when an existence “breaks through the limit”:
    - If an existence successfully breaks through your restriction via high-level status, then **only for you**, your Sequence level in this law is **+1**; otherwise, calculate as usual.

- **Limits and calculation notes:**
  - All resulting Sequence levels are **rounded up**.
  - Example: if the weakest is Sequence 4 and the strongest is Sequence 1, then (4 + 1) ÷ 2 = 2.5, which rounds up to Sequence 3 (not Sequence 2).
  - Ordinary people affect the calculation and are treated as a value of **10**.
    - For convenience, unless Beyonders intentionally do so, only count those who join the battlefield when calculating.
    > **GM Note:** Plan the law’s effective scope to avoid including ordinary people unintentionally, since they can change the result.

- **Effect on ordinary people:**
  - Ordinary people do not gain any supernatural powers.
  - They avoid the personality coercion brought by supernatural powers, but whether they still suffer suppression depends on the final promoted personality present.
  - Example: if an ordinary person becomes a “transcendent” at Sequence 5, but someone breaks through the limit and reaches Sequence 4, they will still suffer suppression of Sequence 4 against Sequence 5, but they will be suppressed by the “substitute person.”> **GM Note:** This decree can take effect in any city, but if you are a “wild” Beyonder, it may cause the city’s forces to chase you. [[wild Beyonder]]

- **Limits:** As described in this section's prose.


### Balancer

```yaml ability
id: arbiter-seq-02-balancer
name: Balancer
pathway: arbiter
sequence: 2
status: adapted
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.law
opposed_by: willpower_defense
range: 1 kilometer radius.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted from explicit Legal Appraisal versus Willpower Defense detection gate.
scaling:
- when: sequence_1_or_higher
  changes:
    range: city
    effect_note: Also reveals how the imbalance appeared and major subsequent context.
conditions:
- invisible
tags:
- detection
- stealth
- defense
text: 'Effect: You sense imbalances in the order around you. Use: When hidden, invisible,
  corrupted, dark, undead, or other forces that violate the order are present, you
  may immediately make a legal appraisal against the enemys will defense and locate
  the corresponding target. [[Legal Appraisal]] Willpower Defense Targeting and range:
  1 kilometer radius. At Sequence 1: Expands to a city, and you can know how the corresponding
  imbalance appeared and the general ins and outs of the subsequent whole thing. [[id:alias-sequence-1|Sequence
  1]]'
```





- **Effect:** You sense imbalances in the order around you.
- **Use:** When hidden, invisible, corrupted, dark, undead, or other forces that violate the order are present, you may immediately make a **legal appraisal** against the enemy’s **will defense** and locate the corresponding target.
  - [[Legal Appraisal]]
  - Willpower Defense
- **Targeting and range:** 1 kilometer radius.

- **At Sequence 1:** Expands to a city, and you can know how the corresponding imbalance appeared and the general ins and outs of the subsequent whole thing. [[id:alias-sequence-1|Sequence 1]]

- **Limits:** As described in this section's prose.
