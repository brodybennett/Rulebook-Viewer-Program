---
title: 'Sequence 8: Lunatic'
id: mutant-seq-08
tags:
- pathway:mutant
- sequence:8
---






# Chained Pathway: Sequence 8

## Lunatic

- You can voluntarily and actively sacrifice your **Sanity / Rationality** and burst out your desires in exchange for strength, gaining improvements in all aspects.
  - During this time, your mind becomes less clear; this is usually not a big problem, and you may even gain some insight.
- You have strong resistance to extraordinary abilities that interfere with thoughts and affect the spirit.
- From this **Sequence** onwards, the curse emerges gradually, and you are easily out of control.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength +1, constitution +1, inspiration +2.
- **Upgrade:** Your Sequence 9 potion skills can be upgraded to advanced.

### Crazy Intuitive Action

```yaml ability
id: mutant-seq-08-crazy-intuitive-action
name: Crazy Intuitive Action
pathway: mutant
sequence: 8
status: canonical
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: 1d3
  notes: Sanity check loss is 1/1d3; bonus damage applies while insanity or sanity loss persists.
scaling: []
tags:
- ritual
- healing
- offense
text: 'Use: 1 Swift Action. Cost: 2 [[Spirituality]]. Effect: Choose 1 of the following:
  You reroll a roll you are currently making, but must initiate an SC (1/1d3). [[SC]]
  Whenever you fail, you immediately get an Attack Action or Spellcasting Action of
  your choice. Limits: The whenever you fail option can only be used once per round
  and cannot be superimposed by similar abilities. Aftereffects: If you lose Sanity
  / Rationality, or are in a state of insanity, you gain +1 to all stats and your
  attack actions deal an extra 1d6 physical damage until Sanity / Rationality is restored,
  24 hours have elapsed, or a [[long rest]] has elapsed. Special: While insane, thoughts-disturbing
  and mind-affecting...'
```





- **Use:** 1 Swift Action.
- **Cost:** 2 [[Spirituality]].
- **Effect:** Choose 1 of the following:
  - You reroll a roll you are currently making, but must initiate an **SC** (1/1d3). [[SC]]
  - Whenever you fail, you immediately get an Attack Action or Spellcasting Action of your choice.
- **Limits:** The “whenever you fail” option can only be used once per round and cannot be superimposed by similar abilities.
- **Aftereffects:** If you lose **Sanity / Rationality**, or are in a state of **insanity**, you gain +1 to all stats and your attack actions deal an extra 1d6 physical damage until Sanity / Rationality is restored, 24 hours have elapsed, or a [[long rest]] has elapsed.
- **Special:** While insane, **thoughts-disturbing** and **mind-affecting** abilities, good or bad, take a -4 penalty on you.
  - This only includes disturbing auxiliary types of psychic abilities, such as [[dragon power]], [[id:alias-frenzy|frenzy]], and [[Dreaming]] (awakening +4 is beneficial), but does not include effects that directly cause [[psychic damage]], such as [[psychic piercing]].

> **GM Note:** For a sensible reply, see [[Chapter Three: Attributes]] and [[Attributes]].

### Full Moon Curse

```yaml ability
id: mutant-seq-08-full-moon-curse
name: Full Moon Curse
pathway: mutant
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
  effect_roll: 1d3
  notes: Sanity check loss is 1/1d3; sanity/rationality checks gain +2 but rolls of 18-20 are catastrophic failures.
scaling: []
tags:
- control
- debuff
text: 'Effect: The Curse of the Full Moon is an inherent effect once possessing the
  ability of a madman and cannot be recorded or stolen. [[madman]] Trigger: When you
  are illuminated by a full moon, you immediately take an SC (1/1d3) that does not
  retrigger, and you become vulnerable to [[loss of control]]. Easy to Lose Control:
  You gain a +2 bonus on Sanity / Rationality checks. [[Sanity / Rationality checks]]
  d20 rolls on Sanity / Rationality checks of 18, 19, or 20 are considered catastrophic
  failures. Special: When acquiring a new full moon curse, the original full moon
  curse will be overwritten.'
```





- **Effect:** The Curse of the Full Moon is an inherent effect once possessing the ability of a madman and cannot be recorded or stolen. [[madman]]
- **Trigger:** When you are illuminated by a full moon, you immediately take an **SC** (1/1d3) that does not retrigger, and you become vulnerable to [[loss of control]].
- **Easy to Lose Control:**
  - You gain a +2 bonus on **Sanity / Rationality checks**. [[Sanity / Rationality checks]]
  - d20 rolls on Sanity / Rationality checks of 18, 19, or 20 are considered catastrophic failures.
- **Special:** When acquiring a new full moon curse, the original full moon curse will be overwritten.

- **Limits:** As described in this section's prose.
