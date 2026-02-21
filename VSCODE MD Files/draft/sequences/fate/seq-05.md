---
title: 'Sequence 5: Winner'
id: fate-seq-05
tags:
- pathway:fate
- sequence:5
---






# Wheel of Fortune Pathway: Sequence 5

> **Lore:** You can restrain yourself to accumulate large amounts of “luck,” resolve fatal crises dramatically at critical moments, and occasionally encounter extremely low-probability good fortune in everyday life. Your intuition is extremely strong, and you are an expert in mysticism—whether in divination or anti-divination. You can also inflict bad luck on enemies, making targets increasingly unlucky.

## Winner

## Advancement

### Advancement Ritual

- **Ritual:** Experience more than one loser experience. (unofficial ceremony)
- **Note:** Must be a complete loser, a loser in life.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** inspiration +2, luck +3, your occultism rises by 1 level.

### Luck

```yaml ability
id: fate-seq-05-luck
name: Luck
pathway: fate
sequence: 5
status: canonical
type: active
action: cast
cost:
  luck: 7
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 2d3
  notes: Effect roll maps extreme luck bonus/penalty; other luck tiers and special list rolls are noted in scaling.
scaling:
- when: better_luck
  changes:
    effect_roll: 2d2
    effect_note: Better luck bonus/penalty uses 2d2 instead of 2d3.
- when: ordinary_good_luck
  changes:
    effect_note: Ordinary good luck is a flat +2/-2 (no dice).
- when: special_lucky_money_pickup
  changes:
    effect_roll: 1d20
    effect_note: Roll 1d3 to determine currency type for the money found.
- when: special_lucky_bank_windfall
  changes:
    effect_roll: 3d10
    effect_note: Roll 1d3 to determine currency type for the banked windfall.
tags:
- buff
text: 'Your Luck ability during Sequence 7 Luck has been improved. *Luck level increased:
  1) Extreme luck: changed to 2d3 bonus/penalty. 2) Better luck: change to 2d2 bonus/deduction
  3) Ordinary good luck: changed to a bonus/deduction of 2 *Special lucky list promotion:
  You picked up 1d20 money, roll 1d3 to decide whether it is a penny, a soli, or a
  gold pound (banknote) You just met someone or something you wanted to see, just
  passed by, but you found out'
```





Your **Luck** ability during Sequence 7 Luck has been improved.

**Luck level increased:**
1) **Extreme luck:** changed to 2d3 bonus/penalty.
2) **Better luck:** change to 2d2 bonus/deduction
3) **Ordinary good luck:** changed to a bonus/deduction of 2

**Special lucky list promotion:**
- You picked up 1d20 money, roll 1d3 to decide whether it is a penny, a soli, or a gold pound (banknote)
- You just met someone or something you wanted to see, just passed by, but you found out
- You meet someone who will help you in the future, even if you don't know the person
- You overheard a piece of information of value to you
- Your bank has been banked with 3d10 money, or you have picked up the corresponding property. Roll 1d3 to decide whether it is a penny, a sole, or a gold pound (banknote). If the GM allows, you may inherit a batch of inheritance due to operational errors
- You've gotten the favor of one or more creatures who happened to be watching you for weird reasons you probably didn't even think about
- In one of the following events, the person chasing you will be stupidly lost, misjudged, and it will take 5 minutes to find the correct bearing
- Other benefits that the GM has prepared for you can directly replace the above content without being random

- **Effect:** Luck resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Accumulate luck

```yaml ability
id: fate-seq-05-accumulate-luck
name: Accumulate luck
pathway: fate
sequence: 5
status: canonical
type: active
action: free
cost:
  luck: 5
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 2d3
  notes: Effect roll maps extreme luck accumulation; other luck tiers adjust the stored value.
scaling:
- when: moderate_luck_accumulation
  changes:
    effect_roll: 2d2
    effect_note: Moderate luck accumulation stores 2d2 luck.
- when: normal_luck_accumulation
  changes:
    effect_note: Normal luck accumulation stores 2 luck (no dice).
tags:
- ritual
- buff
text: 'You can rely on moderation to accumulate a lot of luck to resolve crises in
  a dramatic way. 1) Accumulation: Whenever you decide the luck level of the next
  6 hours in the luck ability, you can choose to accumulate the continuous luck within
  these 6 hours so that it will not happen again, thus increasing the luck value corresponding
  to the bonus of luck level Example: extreme luck will increase 2d3 luck, moderate
  luck will increase 2d2 luck, normal luck will increase 2 points of luck 2) Storage:
  The luck accumulated by you will be stored by you. The storage limit is equal to
  half of the spiritual limit, rounded up 3) Release: 1 free action, release any value
  of luck you stored, they have t...'
```





You can rely on moderation to accumulate a lot of “luck” to resolve crises in a dramatic way.

1) **Accumulation:** Whenever you decide the luck level of the next 6 hours in the luck ability, you can choose to accumulate the continuous luck within these 6 hours so that it will not happen again, thus increasing the luck value corresponding to the bonus of luck level  
   - **Example:** extreme luck will increase 2d3 luck, moderate luck will increase 2d2 luck, normal luck will increase 2 points of luck
2) **Storage:** The luck accumulated by you will be stored by you. The storage limit is equal to half of the spiritual limit, rounded up
3) **Release:** 1 free action, release any value of luck you stored, they have the following uses

#### Resolve fatal crisis

If a certain attack against your Three Defenses is successfully identified, and can cause damage equal to or greater than half of the upper limit of your [[Vitality]] within 1 round, rounded up, the luck released will be automatically added to the defense value.

1) **Example:** 30 attack identification > 25 physical defense, and can cause fatal damage to you, then the luck you release will automatically consume 5 points to make up the difference
2) This ability can be triggered passively, in other words, this ability will passively release luck when suffering fatal damage
3) The lucky number consumed by area damage will be doubled, and the damage will be doubled for each higher level of damage. For multiple identifications of consecutive attacks, each identification will consume luck separately.
4) Luck will not provide protection for sanity loss identification that does not require confrontation and defense and succeeds directly

#### Increase skill bonus

As long as there is luck you have released, then whenever your skill appraisal fails, the corresponding difficulty is not exceeded or the confrontation fails, the released luck will be added to the skill result to ensure success.  
(Only good luck released to yourself, you can store it back)

Release Luck and special action [[id:alias-burn-luck|Burn Luck]] are independent. The released Luck is not an effect that you actively choose. As long as any of the above two conditions are met, Luck will be consumed automatically. Refer to Sequence 7 Luck for the expression form.

- **Effect:** Accumulate luck resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Luck Grant

```yaml ability
id: fate-seq-05-luck-grant
name: Luck Grant
pathway: fate
sequence: 5
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: 20m
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 2d3
  notes: Effect roll maps the bad luck disadvantage applied to each appraisal when granting bad luck.
scaling:
- when: bad_luck_event_trigger
  changes:
    effect_note: Target may be asked to make a DV 20 Luck check; on failure the narrated bad luck event occurs.
tags:
- ritual
text: 'You bestow luck or bad luck on the target. Use: 1 Casting Action, consume 3
  spiritual points, choose 1 target within 20 meters, you give him good luck/bad luck
  Effect: 1) Give good luck: You can give the target any amount of good luck. You
  can only choose the luck that you have accumulated. The target that you have given
  good luck enjoys the release effect of the accumulated luck. The good luck cannot
  exceed half of his spiritual limit. 2) Give bad luck: You give the target any amount
  of bad luck, and the luck you have accumulated is still used as the judgment. The
  target you give bad luck enjoys the following effects: All skills and attribute
  appraisals last for -2d3 disadvantages, and c...'
```





You bestow luck or bad luck on the target.

- **Use:** 1 Casting Action, consume 3 spiritual points, choose 1 target within 20 meters, you give him good luck/bad luck
- **Effect:**
  1) **Give good luck:** You can give the target any amount of good luck. You can only choose the luck that you have accumulated. The target that you have given good luck enjoys the release effect of the accumulated luck. The good luck cannot exceed half of his spiritual limit.
  2) **Give bad luck:** You give the target any amount of bad luck, and the luck you have accumulated is still used as the judgment. The target you give bad luck enjoys the following effects:
     - All skills and attribute appraisals last for -2d3 disadvantages, and consume the corresponding bad luck value until the consumption is exhausted
     - As long as bad luck exists, the GM should try his best to develop in a direction that is unfavorable to him for any events he encounters in the future, such as the psychic can't find the spirit body, encounter things that shouldn't be encountered, and different enemies It happened to appear at the same time, and suddenly my friends were unwilling to provide power
     - (When reaching the plot node where such things may happen, you can ask the creature suffering from bad luck to make a 20-difficulty lucky appraisal, and suffer the disadvantage of the first effect, and the event corresponding to the appraisal failure will actually happen)

- **Limits:** As described in this section's prose.
