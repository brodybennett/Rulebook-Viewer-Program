---
title: 'Sequence 6: Gatekeeper'
id: death-seq-06
tags:
- pathway:death
- sequence:6
---






# Death Pathway: Sequence 6

> **Lore:** Start to set foot in the Spirit World, recruit messengers by yourself, and get help from some Spirit World creatures.

## Gatekeeper

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength +1, constitution +1, agility +1, inspiration +1.
- **Knowledge of the Dead:** can be learned from the master. [[Knowledge of the Dead]]

### Words of the Dead

```yaml ability
id: death-seq-06-words-of-the-dead
name: Words of the Dead
pathway: death
sequence: 6
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
conditions:
- dead
tags:
- utility
text: 'Effect: can bypass the protection of flesh and blood, elevating communication
  with a spirit body to drive or even enslave. [[Words of the Dead]]'
```





- **Effect:** can bypass the protection of flesh and blood, elevating communication with a spirit body to drive or even enslave. [[Words of the Dead]]

- **Limits:** As described in this section's prose.


### Drive the Dead

```yaml ability
id: death-seq-06-drive-the-dead
name: Drive the Dead
pathway: death
sequence: 6
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
conditions:
- dead
tags:
- utility
text: 'Effect: the number and quality of natural spirits, undead creatures, and Spirit
  World creatures you can drive have exploded. Capacity: from now on, the number of
  dead you can drive is no longer equal to your inspiration; instead, it equals your
  Spirit Body Strength. Spirit Body Strength: your (inspiration + will + half constitution,
  rounded up) multiplied by twice. This calculation represents the strength of your
  spirit body. [[Spirit Body Strength]] Sequence 5: replace the 2 multiplier with
  3.'
```





- **Effect:** the number and quality of natural spirits, undead creatures, and Spirit World creatures you can drive have exploded.
- **Capacity:** from now on, the number of dead you can drive is no longer equal to your inspiration; instead, it equals your **Spirit Body Strength**.
  - **Spirit Body Strength:** your (inspiration + will + half constitution, rounded up) multiplied by twice.
  - This calculation represents the strength of your spirit body. [[Spirit Body Strength]]
- **Sequence 5:** replace the **×2** multiplier with **×3**.

- **Limits:** As described in this section's prose.


### Language of the Dead

```yaml ability
id: death-seq-06-language-of-the-dead
name: Language of the Dead
pathway: death
sequence: 6
status: adapted
type: toggle
action: swift
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.knowledge
opposed_by: difficulty_value
range: 1 target within 50 meters.
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.knowledge
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: check_roll maps the repeated Knowledge of the Dead confrontation against spirit-body strength; damage_roll is the baseline cold-strike package when spirit-body separation is complete.
scaling:
- when: target_is_higher_sequence_or_tier
  changes:
    effect_note: Apply the listed -2 penalties per higher sequence or higher character tier.
- when: spirit_body_state_at_sequence_6_to_5
  changes:
    damage_roll: 2d6
- when: spirit_body_state_above_sequence_5
  changes:
    damage_roll: 3d6
conditions:
- dead
tags:
- ritual
text: 'Cost: 1 Swift Action; consuming 1 spirituality point per round. [[Spirituality]]
  Use: at the beginning of each round, make 1 Knowledge of the Dead identification/check.
  Targeting and range: 1 target within 50 meters. Effect: you chant awkward, jerky,
  and piercing words the living can never understand, bypassing the physical body
  and affecting the spiritual body. While you continue chanting, communication with
  the spirit body is upgraded to drive, even slavery. You choose one of the following
  effects to use: Living creature (spirit-body separation) Check Knowledge of the
  Dead against the targets spirit body strength (inspiration + will + half constitution,
  rounded up, then 2). If you succe...'
```





- **Cost:** 1 Swift Action; consuming 1 spirituality point per round. [[Spirituality]]
- **Use:** at the beginning of each round, make 1 **Knowledge of the Dead** identification/check.
- **Targeting and range:** 1 target within 50 meters.
- **Effect:** you chant awkward, jerky, and piercing words the living can never understand, bypassing the physical body and affecting the spiritual body. While you continue chanting, communication with the spirit body is upgraded to drive, even slavery.
- You choose one of the following effects to use:
  1. **Living creature (spirit-body separation)**
- Check **Knowledge of the Dead** against the target’s spirit body strength (inspiration + will + half constitution, rounded up, then ×2). If you succeed, the target’s spirit body floats up uncontrollably and separates from the body inch by inch.
     - Judgment of the situation:
       - Each Sequence level the chosen target is higher than yours: -2 penalty on **Knowledge of the Dead** checks.
       - For every 1 character the chosen target is higher than you: -2 disadvantage to the **Knowledge of the Dead** check; if the chosen target is 2 higher than you, ignore the great success.
       - The chosen target has the same Sequence and character as you: no penalty on **Knowledge of the Dead** checks.
       - For each Sequence level the chosen target is lower than you: +2 benefit on **Knowledge of the Dead** checks.
       - For each character the chosen target is lower than you: +2 benefit on **Knowledge of the Dead** checks.
     - Each time your **Knowledge of the Dead** successfully hits the target’s spiritual body strength once, its spiritual body separates by 1 level:
       - Successful identification 1 time: immediately notice the spirit body has begun to separate from the physical body, but there are no negative effects for the time being.
       - Successful identification 2 times: the spirit body is separated from the body in half; 1 spellcasting/attack/Swift Action/free action is lost; only 1 Swift Action is left in 1 round.
       - Successful identification 3 times: the spirit body is completely separated from the physical body; it is regarded as an undead creature and enters **Spirit Body State**. [[Spirit Body State]]
     - **Spirit Body State:**
       - **Blood volume** is the value of the strength of the spirit body. For each Sequence level, the upper limit of blood volume +5; for each character, the upper limit of blood volume +10. Blood Volume
       - It is regarded as an undead creature.
       - It gains flying ability and 5 points Curse, cold resistance, immune to physical and poison. [[Curse]]
       - Sequence 9–8 Extraordinary: gain the characteristic of inflicting 1d6 cold damage in Attack Action; unable to use own extraordinary ability.
       - Sequence 6–5 Extraordinary: attack actions cause 2d6 cold damage; can use extraordinary abilities; possess wraith possession. [[Wraith Possession]]
       - Higher-order Extraordinary: the Attack Action causes 3d6 cold damage and additionally has the wraith scream. [[Wraith Scream]]
     - **Warning:** the Extraordinary whose spirit body leaves the physical body will suffer all kinds of targeted blows from undead creatures.
       - Returning to the physical body is a movement action; it fits with its own body, but it needs to use another Full-Round Action to fit into the body.
       - This kind of fit is limited to your own body. Before the fit, any successful **Words of the Dead** will make it leave the body directly.
     > **GM Note:** Similarly, **Language of the Dead** can be used for evil spirits possessing anything; when doing so, treat the strength of the spirit body against evil spirits as if you were choosing a living creature.
  2. **Undead creature (coercive action / enslavement)**
     - Choose 1 undead creature; you upgrade communication to drive and enslave.
     - Check **Knowledge of the Dead** against its spirit strength. After a successful check, you select any one of the freedom/attack/casting/move actions of the undead creature once. [[Spirit Strength]]
     - This is based on the premise that an undead creature does not take the initiative to obey your orders.
     - If its level is lower than Sequence 6–5, then as long as your **Knowledge of the Dead** is successfully identified, it will be directly enslaved by you, and it will be regarded as the dead you commanded.
     - Even if it doesn’t take the initiative to obey your orders, if it falls into a helpless state and you use this ability again, you can still enslave it. [[Helpless State]]
- For a spirit body that has separated from its own body: if it is separated from its body for 72 hours and cannot return, its body is considered dead and the spirit body dissipates.
     - The **Words of the Dead** only have the effect of coercive action on natural spirits; because the natural spirits are not dead in essence, and cannot be compelled to enslave.

- **Limits:** As described in this section's prose.


### Entering the Spirit World

```yaml ability
id: death-seq-06-entering-the-spirit-world
name: Entering the Spirit World
pathway: death
sequence: 6
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
- mobility
text: 'Use: you can enter the Spirit World at the beginning of your turn. Effect:
  in about 5 minutes, you find the entrance of the Spirit World and thus enter the
  Spirit World. Benefits: you can directly communicate with spirit bodies and recruit
  messengers; you may also get help from some Spirit World creatures. Limits: you
  will also get lost in the Spirit World, so you should refrain from exploring or
  ask spirit bodies for directions, and cant travel through the Spirit World. Reference:
  for details about the Spirit World, see [[Chapter Twelve: Special Regions]]. You
  can start to find your own affiliation in the Spirit World. [[Spirit World Affiliation]]
  Sequence 5: with the help of the percept...'
```





- **Use:** you can enter the Spirit World at the beginning of your turn.
- **Effect:** in about 5 minutes, you find the entrance of the Spirit World and thus enter the Spirit World.
- **Benefits:** you can directly communicate with spirit bodies and recruit messengers; you may also get help from some Spirit World creatures.
- **Limits:** you will also get lost in the Spirit World, so you should refrain from exploring or ask spirit bodies for directions, and can’t travel through the Spirit World.
- **Reference:** for details about the Spirit World, see [[Chapter Twelve: Special Regions]]. You can start to find your own affiliation in the Spirit World. [[Spirit World Affiliation]]
- **Sequence 5:** with the help of the perception of the underworld, you can use the underworld as a reference standard to know your position in the Spirit World, so that you will no longer get lost. [[Underworld]] [[Perception of the Underworld]]

### Signing the Necromancer Contract

```yaml ability
id: death-seq-06-signing-the-necromancer-contract
name: Signing the Necromancer Contract
pathway: death
sequence: 6
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
text: 'Process: Prepare a piece of parchment, write down the terms to be observed
  with the other party, and finally press your hand on the parchment to establish
  a contractual relationship. The rest of the contract process is the same as that
  in [[Chapter Twelve: Special Regions]]. Before Sequence 6, you do not have the ability
  to sign a necromancer contract, and the necromancer contract can also be used in
  other fields. [[Necromancer Contract]] The contract can also be established orally,
  without parchment; the corresponding content can be chanted directly in ancient
  Hessian. [[Ancient Hessian]] In this regard, you can directly refer to the notarys
  rules for drafting the contract in Sequence 6...'
```





- **Process:**
  1. Prepare a piece of parchment, write down the terms to be observed with the other party, and finally press your hand on the parchment to establish a contractual relationship.
  2. The rest of the contract process is the same as that in [[Chapter Twelve: Special Regions]]. Before Sequence 6, you do not have the ability to sign a necromancer contract, and the necromancer contract can also be used in other fields. [[Necromancer Contract]]
  3. The contract can also be established orally, without parchment; the corresponding content can be chanted directly in ancient Hessian. [[Ancient Hessian]]
     - In this regard, you can directly refer to the notary’s rules for drafting the contract in Sequence 6 of the Sun Path. [[Notary Rules]] [[Sun]]
- **Special:** this is a benefit from the potion and cannot be stolen or recorded.

- **Effect:** Signing the Necromancer Contract resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Raise Undead

```yaml ability
id: death-seq-06-raise-undead
name: Raise Undead
pathway: death
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
conditions:
- dead
tags:
- ritual
text: 'Cost: 1 Casting Action; consuming 2 spiritual points. [[Spirituality]] Targeting:
  choose 1 unrequited corpse. [[Unrequited Corpse]] Effect: make it resurrect as your
  dead. Choose one of the following outcomes: Corpse that has been dead for less than
  one month: wake up as a living corpse; the body decay stops, but the existing decay
  remains. [[Living Corpse]] Corpses that died in water within one month: wake up
  as water ghosts, and the rest are equivalent to living corpses. [[Water Ghost]]
  Corpse that has been dead for more than 1 month: wake up as a skeleton. [[Skeleton]]
  Other possible resurrections, shadows or resentful souls, are generally born naturally
  and cannot be aroused actively....'
```





- **Cost:** 1 Casting Action; consuming 2 spiritual points. [[Spirituality]]
- **Targeting:** choose 1 unrequited corpse. [[Unrequited Corpse]]
- **Effect:** make it “resurrect” as your dead.
- Choose one of the following outcomes:
  1. Corpse that has been dead for less than one month: wake up as a living corpse; the body decay stops, but the existing decay remains. [[Living Corpse]]
  2. Corpses that died in water within one month: wake up as water ghosts, and the rest are equivalent to living corpses. [[Water Ghost]]
  3. Corpse that has been dead for more than 1 month: wake up as a skeleton. [[Skeleton]]
  4. Other possible “resurrections,” shadows or resentful souls, are generally born naturally and cannot be aroused actively. [[shadow]] [[Resentful Soul]]
- **Special:** you should not wake up a living corpse that has been dead for too long. The standard is more than 1 week.
  - The living corpse awakened in this way generally has many places of decay. Any investigation and appraisal against it will be found if it passes a Difficulty Value 15. fester
  - (Decomposition within 1 week can be covered with clothing.)

- **Limits:** As described in this section's prose.
