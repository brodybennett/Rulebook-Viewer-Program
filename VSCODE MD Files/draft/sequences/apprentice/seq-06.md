---
title: 'Sequence 6: Scribe'
id: apprentice-seq-06
tags:
- pathway:apprentice
- sequence:6
---





# Door Pathway: Sequence 6

## Scribe

> **Lore:** The mutated “brain” reproduces the extraordinary ability used by the target, and then drives the activated part of the cells to form the corresponding symbols, patterns, and logos to complete the storage. Let the spirit be the pen and the spirit body be the paper: “I come, I see, I record.”

- You can record extraordinary abilities **with divine influence**.
- The higher the Sequence, the higher the probability of failure. Even at Sequence 4, it may not succeed once in a dozen attempts.
- Recorded ability effectiveness (vs. the original):
  - Recorded extraordinary abilities of Sequence 6 and Sequence 5 are **half** of the original.
  - Recorded extraordinary abilities of Sequence 9 are **close** to the original.

## Advancement

### Main Materials

- A complete [[Asman]]
- [[Cursed Object]] of the [[Ancient Wraith]]

## Acting Rules

- Record various extraordinary abilities and the scenery and folk customs of various places.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition +2
- Your [[Occult]] can be quickly upgraded to Proficient.

### Record

```yaml ability
id: apprentice-seq-06-record
name: Record
pathway: apprentice
sequence: 6
type: active
action: free
cost: {}
roll: null
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- buff
text: 'Your mutated brain reproduces an extraordinary ability used by a target and
  constructs a corresponding pattern for storage. Use: 1 free action, whenever you
  witness an active extraordinary ability, you can immediately record it. Check: Recording
  an Extraordinary Ability is an Intuition Appraisal with an initial difficulty of
  20. 1 Every time your recording ability increases by 1 Sequence: identification
  difficulty +5. Limits: "Character" refers to Sequence level in this section. 4 The
  ability to record is reduced by 1 Sequence: identification difficulty -5. 5 Every
  time your record ability is lowered by 1 character: the difficulty of identification
  -5, until the Difficulty Value is 10 or...'
```




Your mutated “brain” reproduces an extraordinary ability used by a target and constructs a corresponding pattern for storage.

- **Use:** 1 **free action**, whenever you witness an active extraordinary ability, you can immediately record it.
- **Check:** Recording an Extraordinary Ability is an Intuition Appraisal with an initial difficulty of **20**.
  - ① Every time your recording ability increases by 1 Sequence: identification difficulty **+5**.
- **Limits:** "Character" refers to **Sequence level** in this section.

  - ④ The ability to record is reduced by 1 Sequence: identification difficulty **-5**.
  - ⑤ Every time your record ability is lowered by 1 character: the difficulty of identification **-5**, until the Difficulty Value is **10** or lower, at which point it succeeds by default.
- **Special:** Ability records higher than two of yours (comparison method determined by the GM) fail by default, or the probability is extremely low to almost none.
- **On success:** This extraordinary ability is considered owned by you as a **one-time ability**; it disappears after being used.

#### Casting a Recorded Extraordinary Ability

The following rules must be followed to cast a Recorded Extraordinary Ability:

1. ① Summon an illusory book in front of you. Each extraordinary ability corresponds to one page. Read: “I came, I saw, I recorded.”
2. ② When using the ability, you must use the action the ability originally required. You must also pay **1 additional Swift Action** to cast it; flipping through pages is a **free action**.
3. ③ If you roleplay in advance, inform your **GM** of the ability you plan to use next and prepare in advance; as long as it is within your prediction range, the ability you prepared in advance does not need to pay extra free actions.
4. ④ You can only cast recorded abilities with [[Mystical Identification]]. If it involves strength damage dice, your Intuition value should be treated as strength.
5. ⑤ The recorded ability is definitely not as good as the original version, but even if the ability below your level is not as good as the original version, this gap is negligible. For **24 hours** after promotion, your recorded Sequence 6-5 ability and Sequence 4-3 ability will be cut in half.

#### Record Capacity

- The number of abilities you can record is as follows:
  - [[Potion Undigested]]: 1 Sequence 4–3 ability, 8 Sequence 6–5 abilities, 20 Sequence 9–7 abilities.
  - [[Potion digestion progress]] 15: 2 Sequence 4–3 abilities, 9 Sequence 6–5 abilities, 22 Sequence 9–7 abilities.
  - [[Complete Potion Digestion]]: 3 Sequence 4–3 abilities, 10 Sequence 6–5 abilities, 25 Sequence 9–7 abilities.
- **Special:** When the potion is fully digested, the recorded Sequence 6–5 abilities will no longer be halved.

- **Effect:** Record resolves using its yaml ability block and section prose.
