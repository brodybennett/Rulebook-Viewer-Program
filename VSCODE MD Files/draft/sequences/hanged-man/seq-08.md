---
title: 'Sequence 8: Listener'
id: hanged-man-seq-08
tags:
- pathway:hanged-man
- sequence:8
---






# Hanged Man Pathway: Sequence 8

> **Lore:** In ancient times they were called “whisperers.” They can directly hear the whispers of the corresponding hidden existence, gaining many powerful, twisted, and unique abilities. However, if they cannot be promoted, it is difficult to survive for more than five years. “Listeners” are all lunatics—even if they usually behave normally, they must be hidden lunatics.

## Listener

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2; **Will** +1.
- **Skill Gain:** **Listen** +2 skill levels.  
  - Your **Listen** skill can hear the unique sounds from extraordinary creatures.
  - Your **Listen** skill is added to the rapid improvement of Sequence 9 and can be improved at most to the master.

### Listening Perception

```yaml ability
id: hanged-man-seq-08-listening-perception
name: Listening Perception
pathway: hanged-man
sequence: 8
status: canonical
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.listen
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.listen
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: Effect roll maps sanity loss from extraordinary sounds; DV 20 listening check applies when targets are silent.
scaling:
- when: target_is_silent
  changes:
    effect_note: Listening detection uses DV 20; distance reduces DV by 1 per meter until success is automatic.
- when: detect_higher_sequence_or_tainted
  changes:
    effect_note: Triggers 1 or 1d2 Sanity/Rationality loss on extraordinary sound detection.
conditions:
- dead
damage_types:
- sanity
- rationality
tags:
- detection
text: 'Effect: With the extraordinary ability of listening, you will hear more sounds
  and get more dangers in a normal environment. Trigger (extraordinary sounds): Whenever
  there are sounds of extraordinary significance around you, from beings 1 higher
  than you or tainted beings [[Tainted Being]], you suffer an immediate 1/1d2 Sanity
  / Rationality [[Sanity / Rationality]] loss. On Sanity / Rationality check: Whenever
  you make a Sanity / Rationality check [[Sanity / Rationality Check]] because of
  this, you immediately determine what the source of the sound is (usually only known
  by the type of creature, dead or alive, adult or child, and so on). Spotting spirits:
  You can use Listen instead of Ste...'
```





- **Effect:** With the extraordinary ability of listening, you will hear more sounds and get more dangers in a normal environment.
- **Trigger (extraordinary sounds):** Whenever there are sounds of extraordinary significance around you, from beings 1 higher than you or tainted beings [[Tainted Being]], you suffer an immediate 1/1d2 **Sanity / Rationality** [[Sanity / Rationality]] loss.
- **On Sanity / Rationality check:** Whenever you make a **Sanity / Rationality check** [[Sanity / Rationality Check]] because of this, you immediately determine what the source of the sound is (usually only known by the type of creature, dead or alive, adult or child, and so on).
- **Spotting spirits:** You can use **Listen** instead of **Stealth** [[Stealth]] to spot spirits [[Spirit]].
- **Blind hearing:** While blind, you can locate others without checks.
- **If the target does not actively make a sound:** If the being 1 higher than you, or possessing pollution [[Pollution]], does not actively make a sound:
  - You can perform a listening detection with **Difficulty Value** Difficulty Value 20.
  - The **Difficulty Value** is -1 for every 1 meter closer, until the default is successful; it will also cause **Sanity / Rationality** loss.

- At a Detection result of 4+, if the target 1 higher than you does not release pollution and mythical runes [[Mythical Rune]], then only when the target with pollution is detected will cause **Sanity / Rationality** loss.

> **GM Note:** (This is an explanation, ancillary to the ability of listening, which disappears when the latter disappears.)

- **Limits:** As described in this section's prose.


### Latent Madness

```yaml ability
id: hanged-man-seq-08-latent-madness
name: Latent Madness
pathway: hanged-man
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
- utility
text: 'Requirement: Can only be obtained when potion digestion reaches 10. [[Potion
  Digestion]] Effect: Your temporary madness [[Temporary Madness]] will not affect
  your actions, but the madness still exists. Does not include: extraordinary madness
  [[Extraordinary Madness]], indeterminate madness [[Indeterminate Madness]], and
  permanent madness [[Permanent Madness]]. Special: (This is an explanation and cannot
  be recorded or stolen.)'
```





> **Lore:** All “Listeners” are madmen. Even if they behave normally, they must be hidden madmen.

- **Requirement:** Can only be obtained when potion digestion reaches 10. [[Potion Digestion]]
- **Effect:** Your temporary madness [[Temporary Madness]] will not affect your actions, but the madness still exists.
- **Does not include:** extraordinary madness [[Extraordinary Madness]], indeterminate madness [[Indeterminate Madness]], and permanent madness [[Permanent Madness]].
- **Special:** (This is an explanation and cannot be recorded or stolen.)

- **Limits:** As described in this section's prose.


### LISTEN

```yaml ability
id: hanged-man-seq-08-listen
name: LISTEN
pathway: hanged-man
sequence: 8
status: canonical
type: active
action: swift
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.listen
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.listen
  damage_roll: null
  heal_roll: null
  effect_roll: 1d8
  notes: Effect roll maps the success table; failure uses a separate 1d5 table and always risks sanity loss.
scaling:
- when: listen_check_fails
  changes:
    effect_roll: 1d5
    effect_note: Failure table applies; failed luck checks trigger the rd5 outcomes.
- when: listen_check_succeeds
  changes:
    effect_note: Success table applies; each use also triggers 0 or 1d2 Sanity/Rationality loss.
damage_types:
- sanity
- rationality
tags:
- ritual
- debuff
- buff
text: 'Use: 1 Swift Action Swift Action; once a round. Cost: Consumes 2 spirituality
  points. [[Spirituality]] Check: Perform a 30-Difficulty Value listening appraisal.
  Special: When holding this extraordinary ability, your Listen skill will increase
  by another 2 levels; when this ability disappears, that increase disappears. Narrative
  truth: Regardless of the results of your listening, you have actually heard the
  words of the Creator [[Creator]]; it is only possible to interpret the curse from
  them. #### Listening appraisal success Roll rd8 to determine the effect. [[rd8]]
  Each time (regardless of outcome), take a 0/1d2 Sanity / Rationality loss.'
```





- **Use:** 1 **Swift Action** Swift Action; once a round.
- **Cost:** Consumes 2 spirituality points. [[Spirituality]]
- **Check:** Perform a 30-**Difficulty Value** listening appraisal.
- **Special:** When holding this extraordinary ability, your **Listen** skill will increase by another 2 levels; when this ability disappears, that increase disappears.
- **Narrative truth:** Regardless of the results of your listening, you have actually heard the words of the Creator [[Creator]]; it is only possible to interpret the curse from them.

#### Listening appraisal success

- Roll rd8 to determine the effect. [[rd8]]
- Each time (regardless of outcome), take a 0/1d2 **Sanity / Rationality** loss.
- For 24 hours, you can use the obtained effect as a **Swift Action**, but only once per round.
  - 1 ability use opportunity can be stacked.

Effects (rd8):
- ① Choose a target within your field of vision [[Field of Vision]]; they are flooded with filthy and depraved ravings, and suffer a 1d2/1d4 loss of **Sanity / Rationality**.
- ② The hostile extraordinary ability that targets you once, and no more than 1 character, will fail strangely. This is a kind of substitute: your shadow helps you resist this attack, and the damage to the area ability can only be reduced by half. [[Area Ability]]
- ③ Your body suddenly squirms, and a small circle grows out of thin air, gaining 3d6 extra life (which can be replaced by a stack of flesh and blood).
- ④ Lasts for 1 hour: you lose your vitals, and you are regarded as a corrupt (flesh and blood) creature [[Corrupt Creature (Flesh and Blood)]]. Regular vital strikes [[Vital Strike]] are invalid for you.
- ⑤ You can use 1 **Swift Action** to choose one of your own limbs to explode, causing 3d6 physical and 1d6 poison damage [[Poison Damage]] (fighting against physical defense [[Physical Defense]]). On failure, the damage is halved, and you will take full damage.  
  (Blown-up limbs cannot be restored by conventional means.)
- ⑥ Select a target within the field of vision; their shadow suddenly activates and restrains them, and uses movement and attack actions to fight against their own strength attribute until they escape.  
  (Shadow rolls are made by you or the GM.)
- ⑦ Lasts 1 hour: you can use 1 round of freedom to become a shadow or escape, and lose the ability after 1 round.
- ⑧ You can shoot flesh and blood bullets at 1 or more targets, up to 3 rounds; identify the corresponding number of times. Each round, lose 1d2 Vitality [[Vitality]]. Intuition (INT) + shooting (against physical defense); there is no disadvantage and it is regarded as a firearm [[Firearm]]. Each round causes 1d6 physical damage. If you hear the ravings of other existences of the real Creator, the effect obtained will be determined by the GM, generally not including the Seven Gods. [[Seven Gods]]


#### Listening appraisal failure

- Make an rd5 [[rd5]] to determine what happens if you fail your luck check. [[Luck Check]]

Outcomes:
- ① You immediately suffer 2d6 curse damage [[Curse Damage]] and suffer 1/1d2 **Sanity / Rationality** loss.
- ② If you have not deciphered anything, make a **Will** test with **Difficulty Value** 15; otherwise you will lose 1/1d2 **Sanity / Rationality**.
- ③ You immediately fall into a temporary madness and suffer 1/1d2 **Sanity / Rationality** loss.
- ④ You immediately fall into an extraordinary madness and suffer a **Sanity / Rationality** loss of 1/1d3.
- ⑤ You heard ravings from other than the real Creator, and the effect is determined by the GM, generally not including the Seven Gods.

- **Effect:** LISTEN resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
