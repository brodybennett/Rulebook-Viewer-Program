---
title: 'Sequence 3: Ferryman'
id: death-seq-03
tags:
- pathway:death
- sequence:3
---






# Death Pathway: Sequence 3

> **GM Note:** This section is marked “for reference only” and includes “unofficial” ritual text. Treat it accordingly.

## Ferryman

- Creatures that look at you die directly; even creatures with divinity suffer heavy damage.
- Even without direct line-of-sight contact, a target included in your eyes slowly withers, as if crossing the river of death inch by inch.
- Most attacks are ineffective against you.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Guide wandering spirits to the underworld; bury tens of thousands of corpses and souls; after fulfilling an angel’s last wish, lead the angel’s remaining spirits to the underworld to rest in peace.
  - (Marked “unofficial ceremony” in RAW.)

- **Substitute Ritual:** Create an upside-down mausoleum at the location of the [[River of Eternal Darkness]]. After entering the mausoleum:
  - Connect yourself with the [[River of Eternal Darkness]].
  - Step into the [[River of Eternal Darkness]] to become part of the [[River Styx]].
  - Flow up to the end of the river.
  - Leave an immediate imprint on the [[River of Darkness]].
  - (Marked “unofficial ritual” and “reference to some of the original incomplete rituals” in RAW.)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Constitution +1, Strength +1, Agility (DEX) +1, Intuition (INT) +1; choose 1 skill to increase 1 level.

### Ferryman

```yaml ability
id: death-seq-03-ferryman
name: Ferryman
pathway: death
sequence: 3
status: adapted
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: Deterministic package; mapped constant captures the explicit maximum sanity-pressure cap of 1.
scaling:
- when: attacker_is_1_sequence_higher
  changes:
    effect_note: Damage immunities are bypassed except where the prose explicitly keeps immunity.
tags:
- detection
- defense
- offense
text: 'Effect: You have become the real dead. Your malice, thoughts, and behavior
  tendencies are hidden; you become a dead person without thoughts. No one can read
  your thoughts except a Beyonder of the Visionary at the same Sequence as you. The
  malicious perception of the Abyss is no longer effective against you. Defenses and
  damage interactions: Most attacks except holy attacks are no longer effective against
  you. You have no physical vitals.'
```





- **Effect:**
  - You have become the real dead.
  - Your malice, thoughts, and behavior tendencies are hidden; you become a dead person without thoughts.
  - No one can read your thoughts except a Beyonder of the Visionary at the same Sequence as you.
  - The malicious perception of the Abyss is no longer effective against you.

- **Defenses and damage interactions:**
  - Most attacks except **holy attacks** are no longer effective against you.
  - You have no physical vitals.
  - **Physical damage:** invalid.
  - **Fire damage:** halved.
  - **Mind and spirit strike damage:** halved.
  - **Cold damage:** invalid.
  - **Lightning damage:** normal.
  - **Curses:** no effect.
  - **Curse damage:** no effect.
  - **Sanity / Rationality damage:** halved.
    - Maximum pressure is 1.
    - Promotion sanity loss cannot be saved.

- **Higher-Sequence attacker rule:**
  - If the attacker is 1 Sequence higher than you: except for damage types you are immune to, their attacks can have normal effects.

- **Special (damage sharing):**
  - Damage sharing from the [[Secret Puppet]] with the same personality and different Pathways is still valid for you.
  - However, damage applied to you via damage sharing is unilaterally halved; the puppet still receives the full damage.
  - This is not limited to curse damage from sharing; all types of shared damage are unilaterally halved.
  - If the [[xenomorph]] is 1 level higher than you, you take full shared damage.

- **Limits:** As described in this section's prose.


### River of Eternal Darkness

```yaml ability
id: death-seq-03-river-of-eternal-darkness
name: River of Eternal Darkness
pathway: death
sequence: 3
status: adapted
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: 6d10 + 10
  heal_roll: null
  effect_roll: 1d10
  notes: damage_roll is the direct-gaze burst; effect_roll is the per-round peripheral-vision damage.
scaling:
- when: direct_gaze_burst_already_triggered_this_encounter
  changes:
    damage_roll: null
    effect_note: The 6d10 plus 10 burst can only trigger once per encounter.
- when: target_is_higher_sequence
  changes:
    effect_note: Direct-gaze burst damage is reduced by 10 for each sequence the target is above you.
- when: extra_mode_endow_ferryman_trait
  changes:
    action: cast
    cost:
      spirituality: 3
    effect_note: Applies Ferryman-like undead traits to designated targets as described in prose.
tags:
- detection
- debuff
- offense
text: 'Effect: A target you put into your eyes slowly withers, like crossing the river
  of death inch by inch. Use: As a free action, open this effect. Targeting and range:
  Direct gaze: Non-undead creatures that meet your gaze. Peripheral vision: If the
  target is not looking at you, but is only seen out of your peripheral vision, and
  remains within your sight. Damage (direct gaze): The target immediately suffers
  6d10+10 damage. This 6d10+10 damage can only be triggered once per encounter.'
```





- **Effect:** A target you put into your eyes slowly withers, like crossing the river of death inch by inch.

- **Use:** As a **free action**, open this effect.

- **Targeting and range:**
  - **Direct gaze:** Non-undead creatures that meet your gaze.
  - **Peripheral vision:** If the target is not looking at you, but is only seen out of your peripheral vision, and remains within your sight.

- **Damage (direct gaze):**
  - The target immediately suffers 6d10+10 damage.
  - This 6d10+10 damage can only be triggered once per encounter.
  - The damage is reduced by 10 for each Sequence higher than you.

- **Damage (peripheral vision):**
  - The target suffers 1d10 damage each round while within your sight.
  - GM decides how many times this damage can apply within a single round.

- **Damage type and resistance:**
  - This is **curse damage**, but it ignores the effects of [[Curse Resistance]] and [[Curse Reduction]].

- **Clones and indirect viewing:**
  - Even through a clone like [[Secret Puppet]], if the Secret Puppet owner dares to look directly at you, they suffer half of the damage of looking at you.
  - The clone of the Error pathway and the Visionary will not affect the main body because they are very independent.

- **Sequence 2 reference (RAW text):**
  - **Sequence 2:** There is no need to look at each other. Except for the target of the same personality, all creatures you see suffer the damage of the river of death and die almost immediately.
  - After death, they are directly converted into undead creatures controlled by you, and slaves at all your command.
  - Also, even targets of the same rank as you still take 2d10+5 hits per round as long as they are within your line of sight.

- **Extra:**
  - **Use:** Consume a **Casting Action**.
  - **Cost:** 3 [[Spirituality]].
  - **Effect:** Endow the Ferryman “no longer thinking” property to one or more designated targets.
    - Halve their physical damage.
    - Make them immune to vital blows.
    - Halve the damage of curses.
    - Otherwise as usual: they are treated as an undead creature; they decay, rot, wither, die, and lose the sense of freshness for 24 hours.

- **Limits:** As described in this section's prose.


### The Language of the Dead

```yaml ability
id: death-seq-03-the-language-of-the-dead
name: The Language of the Dead
pathway: death
sequence: 3
status: adapted
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Anyone who hears your dead mans language.
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d6 + 1
  notes: Sanity and Rationality damage is prose-defined as either 1d4 or 1d6 plus 1 based on GM adjudication.
scaling:
- when: lower_intensity_mode
  changes:
    effect_roll: 1d4
tags:
- offense
text: 'Effect: The language of the dead is not only a language the living cannot understand;
  it also carries screams and roars from the depths of the underworld as a mental
  attack. Use: As a Casting Action, once per encounter. Targeting and range: Anyone
  who hears your dead mans language. Damage: Those who hear it suffer 1d4/1d6+1 Sanity
  / Rationality hits. GM decides whether to use 1d4 or 1d6+1 in a given situation.
  Interaction with Words of the Dead / rebuke: It can be released at the same time
  as the previous [[Words of the Dead]] effect.'
```





- **Effect:** The language of the dead is not only a language the living cannot understand; it also carries screams and roars from the depths of the underworld as a **mental attack**.

- **Use:** As a **Casting Action**, once per encounter.

- **Targeting and range:** Anyone who hears your dead man’s language.

- **Damage:**
  - Those who hear it suffer 1d4/1d6+1 Sanity / Rationality hits.
  - GM decides whether to use 1d4 or 1d6+1 in a given situation.

- **Interaction with Words of the Dead / rebuke:**
  - It can be released at the same time as the previous [[Words of the Dead]] effect.
  - If released at the same time, the effect of rebuke and negotiation against the attack of its Willpower Defense can allow the above sanity appraisal to be used for the easy-to-crazy effect of the Visionary.
  - GM decides the exact procedure for this interaction.

- **RAW clarification text (kept, condensed without changing mechanics):**
  - The 1d4+1/1d6+1 sanity check only uses rd20 against your existing sanity, and the rd20 was not a big success.
  - If you used the rebuke effect against the enemy’s Will defense, the big success of the rebuke effect’s diplomacy check equals the great success of this sanity test.
  - Throwing 20 for the scolding value makes the sanity test full.
  - For the Audience, values of 18, 19, and 20 all make their sanity test full.

- **Extra:**
  - **Use:** As a **Full-Round Action**, directly transform a creature into your slave.
  - **Effect:** The creature is regarded as an undead creature.
  - **Time/limits:**
    - It takes 3 minutes for a Beyonder who is not a demigod; demigods are immune to direct conversion.
    - An undead creature of your strength is only a Full-Round Action.
    - The converted creature must be weaker than you.
    - You cannot directly convert a demigod.

  - **Special case (RAW text):**
    - If a creature grants you undead qualities and is one person lower than you, this requires two of your -4 [[Words of the Dead check]] against their Will defense **in the same round**.
    - This does not take three minutes; it is achieved with a Full-Round Action, for as long as they are undead.

- **Limits:** As described in this section's prose.
