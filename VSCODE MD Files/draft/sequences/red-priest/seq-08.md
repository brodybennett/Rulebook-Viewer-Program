---
title: 'Sequence 8: Provoker'
id: red-priest-seq-08
tags:
- pathway:red-priest
- sequence:8
---






# Red Priest Pathway: Sequence 8

> **Lore:** Good at provoking others with casual words and actions.

## Provoker

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
- Deception / Speaking / Persuasion are included in the growth range of your Sequence 9 skills Sequence 9, up to proficiency.
- Each time you successfully provoke an intelligent creature stronger than you for the first time, you may lose 1 [[Sanity / Rationality]] to count it as 1 growth.

### Provoke

```yaml ability
id: red-priest-seq-08-provoke
name: Provoke
pathway: red-priest
sequence: 8
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int - 4
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int - 4
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Situation 1 uses Intuition -4 vs Willpower Defense; Situation 2 uses Intuition vs Willpower Defense; Situation 3 is automatic success.
scaling: []
tags:
- ritual
- control
- defense
- offense
text: 'Use: You provoke a creature. You must use verbal roleplay (to provoke or taunt),
  except where the rules explicitly say words are not required. This ability is divided
  into three situations. #### Situation 1: Complete Strangers / Newly Met Friends
  Action: 1 Casting Action. Casting Action Cost: 2 spirituality points. [[Spirituality]]
  Check: Intuition (INT) -4 vs the targets Willpower Defense. Intuition Willpower
  Defense Effect: The targets next action involving attacks and negative effects (e.g.,
  shooting, fighting, using extraordinary abilities) must target you, unless you have
  fallen into a state of death, fainting, or helplessness. [[id:alias-death|Death]]
  [[Fainting]] [[Helplessness]]'
```





- **Use:** You provoke a creature. You must use verbal roleplay (to provoke or taunt), except where the rules explicitly say words are not required.

This ability is divided into three situations.

#### Situation 1: Complete Strangers / Newly Met Friends

1. **Action:** 1 Casting Action. Casting Action
2. **Cost:** 2 spirituality points. [[Spirituality]]
3. **Check:** Intuition (INT) -4 vs the target’s Willpower Defense. Intuition Willpower Defense
4. **Effect:**
   1. The target’s next action involving attacks and negative effects (e.g., shooting, fighting, using extraordinary abilities) must target you, unless you have fallen into a state of death, fainting, or helplessness. [[id:alias-death|Death]] [[Fainting]] [[Helplessness]]
5. **Special Targets (beasts/monsters/out-of-control persons):**
   1. You can only use the first level of provocation against them.
   2. No words are required; more in-depth provocations are invalid for these targets (this is the use of actively exuding disgusting feelings).
   3. For intelligent beings, this unspoken feeling of disgust is not provocative, but it does make you more conspicuous.
   4. For beasts and insane targets only: if you have already dealt two critical blows to it, the provocation automatically counts as a second tier of provocation, not a first tier. [[Critical Blow]]

#### Situation 2: Target Has Some Understanding of the Provocateur

1. **Action:** 1 Casting Action.
2. **Cost:** 2 spirituality points.
3. **Check:** Intuition (INT) vs the target’s Willpower Defense.
4. **Effect:** In addition to the Situation 1 effect, the target also falls into a state of anger (Rage state).

- If the provoked object successfully causes an effective damage to the source of anger, the anger state will end.

**Rage state:**
- You suffer a -4 penalty on skill checks.
- Move actions can only move toward the source of rage. Move Action
- You must attack the source of rage or blockers first, until you regain your composure or the source of rage dies, faints, or falls into a helpless state.

1. If the remaining Vitality of the recipient of the anger state ≤ the total Vitality divided by 4 (rounded up), the subject will only suffer from the anger state, and the anger state does not have the effect of restricting actions. [[Vitality]]
2. Different from normal anger: Rage can be relieved only if (a) the provocateur has dealt at least 1 damage to the target since the last round, or (b) the target succeeds on a Will/Psychological Guidance appraisal at the beginning of each round. [[Will (Attribute/Check)]] [[id:alias-psychological-guidance|Psychological Guidance]]
3. Half meditation suppresses the action-restricting portion of Rage for 1 round. Full meditation halves the remaining Rage duration (round up). [[Meditation]]
4. Others can also use 1 Psychological Guidance / Social Identification to help resolve the provocation, against the result of the inspirational identification when the provocateur provokes. [[Social Identification]]
5. For 1 round, a target that has made a successful Mental Channel check cannot be provoked. [[Mental Channel]]

#### Defining “Some Understanding” vs “Full Knowledge”

1. **Some understanding** is satisfied if the provocateur meets **either** condition:
   1. Know one of the titles of the provocateur (by name or pronoun), and know the general life experience of the provocation target (roughly what kind of person they are). This information can be obtained through inquiring. (Experience must be real; mere speculation is not accurate unless it is correct.)
   2. Know the weakness of the object being provoked. This must be accurate, true, and still valid, including shady personal hobbies that make people laugh, as long as the target really cares about these.
2. If **both** conditions are met, the provocateur is considered to have **full knowledge** of the target.

#### Situation 3: Target Fully Known to the Provocateur

- **Action:** 1 Swift Action. Swift Action
- **Cost:** 2 spirituality points.
- **Check:** The provocation is successful by default.
- **Roleplay:** You use the other party’s name or weakness in roleplay words.
- **Effect:**
  1. All actions involving attacks and negative effects must take you as the top priority, unless you fall into a state of death, fainting, or helplessness, or the remaining Vitality of the provoked object ≤ the total Vitality divided by 4 (rounded up).
  2. The provoked person continues to be in a state of anger. If the provoked creature is provoked when the remaining Vitality ≤ total Vitality divided by 4 (rounded up), it will only suffer the effect of anger, but this state of anger does not contain any restrictions on actions.
  3. If someone obstructs the person being provoked, then only when the obstruction is being executed, the obstructer is also included in the attackable range.
  4. At the beginning of each round, the provoked person can still use the Will/Psychological Guidance appraisal to try to remove the provocation (anger) effect independently, but the difficulty becomes **Willpower Defense + the provocateur’s Intuition (INT)**. If the confrontation succeeds once, the effect is only halved (no forced movement), and it can be removed after two successes.
  5. Half-meditation is no longer effective. Full meditation is regarded as (4), but you must meditate twice in a row, and the provocateur in the middle can provoke again.

- This rage state doesn't end just by doing damage to you simply successfully.

#### Removal of Anger by Others

- **Action:** 1 Psychological Guidance / Social Identification.
- **Effect:** In this state, provocation (including anger state) can still be lifted, but the identification difficulty of Psychological Guidance must exceed “the Willpower Defense of the provoked object + the Intuition (INT) of the provocateur.”
- If the Mental Guidance check succeeds, the provocateur cannot provoke the target again for 1 round. [[Mental Guidance]]

- **Limits:** As described in this section's prose.
