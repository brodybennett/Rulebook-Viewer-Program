---
title: 'Sequence 9: Bard'
id: sun-seq-09
tags:
- pathway:sun
- sequence:9
---






# Sun Pathway: Sequence 9

## Bard

> **Lore:** A mythical creature in the form of the sun, corresponding to [[Tarot Card — Sun]].

- Core theme: praise the sun; bolster courage, strength, piety, and obedience through song.

## Advancement

### Auxiliary Materials

- **Auxiliary Materials:** [[Midsummer Grass]], [[July Wine Juice]], [[Fairy Dark Leaf]]

### Advancement Ritual

- **Main Materials:** [[Crystallized Sunflower]] **or** [[Flintbird Tail Feather]] **or** [[Arsonbird Tail Feather]], plus [[Siren’s Stone]] **or** [[Singing Sunflower]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** [[Attributes]] — +1 [[Strength]], +1 Agility (DEX), +1 Intuition, +1 [[Constitution]]
- You can begin learning [[Singing]] quickly.

### Singing Training

```yaml ability
id: sun-seq-09-singing-training
name: Singing Training
pathway: sun
sequence: 9
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
text: Each time you receive 2 hours of effective guidance (no repetition), your Singing
  level increases by 1. It takes 2, 3, and 4 training sessions to become proficient,
  advanced, and mastery respectively; the maximum is mastery.
```





- Each time you receive 2 hours of effective guidance (no repetition), your Singing level increases by 1.
  It takes 2, 3, and 4 training sessions to become proficient, advanced, and mastery respectively; the maximum is mastery.

- **Effect:** Singing Training resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Potion-Assisted Growth

```yaml ability
id: sun-seq-09-potion-assisted-growth
name: Potion-Assisted Growth
pathway: sun
sequence: 9
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
- utility
text: When creating a character that is not "just promoted," you can use the [[Bard
  Potion]] to apply double the potion's Intuition (INT) bonus to add growth skills.
```





- When creating a character that is not "just promoted," you can use the [[Bard Potion]] to apply **double the potion's Intuition (INT) bonus** to add growth skills.

- **Effect:** Potion-Assisted Growth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Song of Courage

```yaml ability
id: sun-seq-09-song-of-courage
name: Song of Courage
pathway: sun
sequence: 9
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.cha + @skill.singing_identification
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.singing_identification
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Singing Identification DV 15; on success grants +1 Strength/+1 Agility and clears listed conditions.
scaling: []
conditions:
- fear
tags:
- ritual
- debuff
text: 'Cost: 2 [[Spirituality]]. Use: 1 Casting Action; perform a [[Singing Identification]]
  ( Difficulty Value 15 ); roleplay the corresponding chant. The chant must be themed
  around praising the sun. Effect: On a success, you and any friendly unit that heard
  the singing gain +1 Strength and +1 Agility (DEX) for 1 Encounter. Effect: Also
  clears the physical effects of [[Fear]], [[Poisoning]], [[Curse]], [[Darkness]],
  [[Corruption]], and [[Undeath]] from affected targets. These effects can be applied
  again later. Limits: Fears, poisons, and curses from sources 2+ Sequences higher
  than you are unaffected.'
```





- **Cost:** 2 **[[Spirituality]]**.
- **Use:** 1 **Casting Action**; perform a **[[Singing Identification]]** ( **Difficulty Value** 15 ); roleplay the corresponding chant. The chant must be themed around praising the sun.
- **Effect:** On a success, you and any friendly unit that heard the singing gain +1 Strength and +1 Agility (DEX) for 1 **Encounter**.
- **Effect:** Also clears the physical effects of [[Fear]], [[Poisoning]], [[Curse]], [[Darkness]], [[Corruption]], and [[Undeath]] from affected targets. These effects can be applied again later.
- **Limits:** Fears, poisons, and curses from sources 2+ Sequences higher than you are unaffected.

### Sing Piety

```yaml ability
id: sun-seq-09-sing-piety
name: Sing Piety
pathway: sun
sequence: 9
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.cha + @skill.singing_identification
opposed_by: willpower_defense
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.singing_identification
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: Singing Identification DV 15; Benefit B uses the Singing result vs Willpower Defense.
scaling: []
damage_types:
- sanity
- rationality
tags:
- ritual
- defense
text: 'Cost: 2 Spirituality. Use: 1 Casting Action; perform a Singing Identification
  ( Difficulty Value 15 ); roleplay the corresponding chant. The chant must be themed
  around praising the sun. Effect: Choose one of the following benefits: Benefit A
  (Allies): You and friendly units gain 1d2 [[Temporary Sanity / Rationality]] for
  1 Encounter. During the Encounter, Sanity / Rationality loss is first applied to
  Temporary Sanity / Rationality. Temporary Sanity / Rationality does not count toward
  the [[Madness]] caused by Sanity / Rationality loss. Benefit B (Opposition): Use
  your Singing Identification result against the Willpower Defense of an enemy who
  heard the singing; this benefit takes effect...'
```





- **Cost:** 2 **Spirituality**.
- **Use:** 1 **Casting Action**; perform a **Singing Identification** ( **Difficulty Value** 15 ); roleplay the corresponding chant. The chant must be themed around praising the sun.
- **Effect:** Choose one of the following benefits:

  - **Benefit A (Allies):** You and friendly units gain 1d2 **[[Temporary Sanity / Rationality]]** for 1 Encounter. During the Encounter, Sanity / Rationality loss is first applied to Temporary Sanity / Rationality. Temporary Sanity / Rationality does not count toward the [[Madness]] caused by Sanity / Rationality loss.
  - **Benefit B (Opposition):** Use your Singing Identification result against the **Willpower Defense** of an enemy who heard the singing; this benefit takes effect only if it succeeds.  
    Dark, corrupt, and undead beings who hear the singing become hard to fight against you: you and friendly units gain **[[Advantage]]** against enemies affected by the singing (i.e., +2 to [[Skill Check]] and [[Attribute Check]]). The enemy does not gain disadvantage. Duration: 1 Encounter.

- **Limits:** The effect is ineffective for corresponding creatures that are 1 Sequence higher than you; they only feel uncomfortable.

### Spirit Vision
```yaml ability
id: sun-seq-09-spirit-vision
name: Spirit Vision
pathway: sun
sequence: 9
status: canonical
type: active
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: No roll; while active, Spiritual Intuition tests gain +1.
scaling: []
tags:
- ritual
- detection
text: 'Use: 1 Free Action to activate. Cost: 1 Spirituality per round. Effect: While
  Spirit Vision is active, you gain the following benefits: Etheric Body: You can
  roughly tell whether a creatures physical condition is good or bad from aura color,
  but you cannot get detailed information. Spiritual Body: You can confirm whether
  an object/creature has spirituality; you cannot identify Beyonders. Mental Body:
  You can see whether the other party is thinking, but you cannot get more detailed
  information. Astral Body: You cannot see the astral body. While Spirit Vision is
  active, your [[Spiritual Intuition]] tests gain +1.'
```





- **Use:** 1 **Free Action** to activate.
- **Cost:** 1 **Spirituality** per round.
- **Effect:** While Spirit Vision is active, you gain the following benefits:


  1. **Etheric Body:** You can roughly tell whether a creature’s physical condition is good or bad from aura color, but you cannot get detailed information.
  2. **Spiritual Body:** You can confirm whether an object/creature has spirituality; you cannot identify Beyonders.
  3. **Mental Body:** You can see whether the other party is thinking, but you cannot get more detailed information.
  4. **Astral Body:** You cannot see the astral body.
  5. While Spirit Vision is active, your **[[Spiritual Intuition]]** tests gain +1.

- **Notes:**
  - Dead creatures are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding Pathway.
  - Spirit Vision lets you perceive colors in darkness; you can see the existence of colors, but can still get lost (your visible color range is limited). You cannot use these colors to distinguish undead creatures.
  - Spirit Vision can, by default, see some ordinary spirit bodies that have not dissipated for 24 hours; they cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
