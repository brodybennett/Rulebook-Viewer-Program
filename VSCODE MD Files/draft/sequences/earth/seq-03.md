---
title: 'Sequence 3: Ancient Bane'
id: earth-seq-03
tags:
- pathway:earth
- sequence:3
---






# Mother Pathway: Sequence 3

**Pathway:** Earth Pathway.

## Ancient Bane

## Advancement

### Advancement Ritual

**Ceremony:** Open up an area in the depths of the forest. Use natural materials to carefully manufacture a cemetery and coffins that have not yet been buried; the more detailed and exquisite, the better.

Bring the dead who represent various classes and have not been rested as usual to this place, including:
- nobles
- merchants
- soldiers
- civilians
- vagabonds
- dead **Beyonder** [[Beyonder]]s
- the remains of demigods [[Demigod]]

After burying all coffins representing all classes and different groups of people, personally hold a prayer and requiem ceremony for them. Let the plants in the forest protect you together after exorcising evil spirits, and take the potion during baptism and prayers to the earth [[Mother Earth]].

> **GM Note:** RAW labels this as an “unofficial ceremony.”

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Strength** +1, **Constitution** +2, **Agility (DEX)** +1.

### Earth

```yaml ability
id: earth-seq-03-earth
name: Earth
pathway: earth
sequence: 3
status: adapted
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: 2d3
  effect_roll: "1"
  notes: Heal roll maps spirituality recovery; effect roll maps fixed sanity recovery per corpse.
scaling: []
tags:
- ritual
text: 'Use: Once per round, as a free action Free Action, choose an ordinary corpse.
  Effect: The corpses spirit and body are engulfed in the earth, resting body and
  spirit, returning it to the bosom of Mother Earth [[Mother Earth]]. Aftereffects:
  Each time you do this, you regain 2d3 points of spirituality [[Spirituality]] and
  1 point of Sanity / Rationality [[Sanity / Rationality]].'
```





- **Use:** Once per round, as a **free action** Free Action, choose an ordinary corpse.
- **Effect:** The corpse’s spirit and body are engulfed in the earth, resting body and spirit, returning it to the bosom of Mother Earth [[Mother Earth]].
- **Aftereffects:** Each time you do this, you regain 2d3 points of **spirituality** [[Spirituality]] and 1 point of **Sanity / Rationality** [[Sanity / Rationality]].

- **Limits:** As described in this section's prose.


### Pallbearer

```yaml ability
id: earth-seq-03-pallbearer
name: Pallbearer
pathway: earth
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
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Damage roll represents the stated bonus damage against undead.
scaling: []
tags:
- debuff
- offense
text: 'Effect: You deal an additional 2d6 damage to undead [[Undead]]. Effect: Damage
  to you from curses is halved when it is undead damage.'
```





- **Effect:** You deal an additional 2d6 damage to undead [[Undead]].
- **Effect:** Damage to you from curses is halved when it is undead damage.

- **Limits:** As described in this section's prose.


### Soul to Earth

```yaml ability
id: earth-seq-03-soul-to-earth
name: Soul to Earth
pathway: earth
sequence: 3
status: adapted
type: active
action: cast
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.biology
opposed_by: physical_defense
range: One or more undead [[Undead]] creatures within line of sight [[line of sight]].
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.biology
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Check roll maps the stated biological defense contest; damage roll maps the per-round vitality/spirit loss.
scaling:
- when: undead_sequence_lower_by_3_or_more
  changes:
    effect_note: Target is buried immediately after its turn.
- when: undead_sequence_lower_by_2
  changes:
    effect_note: Target is entombed after one full round.
- when: undead_sequence_lower_by_1
  changes:
    effect_note: Target can attempt a Difficulty Value 25 Strength appraisal to break free.
- when: undead_sequence_equal
  changes:
    effect_note: Burial completes after five rounds; target can still attempt to break free.
- when: incorporeal_undead_sequence_5
  changes:
    effect_note: Requires a two-round initiation for incorporeal undead at Sequence 5.
- when: living_target
  changes:
    effect_note: Living targets only become buried once their hit points reach 0.
tags:
- ritual
- defense
text: 'Cost: 5 points of spirituality [[Spirituality]]. Use: A spellcasting action
  Spellcasting Action. Targeting and range: One or more undead [[Undead]] creatures
  within line of sight [[line of sight]]. Effect: Biological defense against physical
  defense [[Biological Defense]] [[Physical Defense]]. Targets are entangled in plants,
  and the body is quickly assimilated into plants, as if it has experienced a hundred
  years of wind and frost. Effect: An undead so swept up is considered bound [[Bound]]
  and loses 2d6 hit points Hit Points at the end of each turn, or spirit if it is
  a spirit. *Undead resolution by relative Sequence Level Sequence Level: Undead creatures
  three or more Sequence Levels l...'
```





- **Cost:** 5 points of **spirituality** [[Spirituality]].
- **Use:** A **spellcasting action** Spellcasting Action.
- **Targeting and range:** One or more undead [[Undead]] creatures within line of sight [[line of sight]].
- **Effect:** Biological defense against physical defense [[Biological Defense]] [[Physical Defense]]. Targets are entangled in plants, and the body is quickly assimilated into plants, as if it has experienced a hundred years of wind and frost.
- **Effect:** An undead so swept up is considered **bound** [[Bound]] and loses 2d6 **hit points** Hit Points at the end of each turn, or spirit if it is a spirit.

**Undead resolution by relative Sequence Level** Sequence Level:
- Undead creatures three or more **Sequence Levels** lower than you: are buried directly after its turn.
- Undead creatures two sequence levels lower than you: immediately entombed after a full round.
- Undead creatures one sequence level lower than you: requires two full rounds, and allows a **Strength appraisal** [[Strength Appraisal]] (Difficulty Value Difficulty Value 25) against breaking free.
- Undead creatures of the same level as you: it takes a full five rounds, and it can also break free, but it will continue to be affected by the effects of restraint and spiritual loss of life.

**Special:**
- This ability requires a two-round initiation for incorporeal undead [[Incorporeal]] of Sequence 5, and is normal for levels below this level.

**Living creatures or things:**
- This ability can also work on living creatures or things, but the living creature cannot be buried until its **hit points** Hit Points reach 0, and it is continuously allowed to try to break free.
- When its hit points reach 0, it is immediately buried.

**Supplement (Vegetative State):**
- Whenever this ability imprisons a creature, the target will enter a **vegetative state** [[Vegetative State]] every time it suffers the loss of life and spirituality of Soul to Earth.
- In the vegetative state, only one free action can be performed per round, and it cannot be combined with other reduced actions.
- The effect stacks.
- The duration of the vegetative state after breaking free is equal to the time of being restrained.

**Re-shackle (after breaking free):**
- **Cost:** 4 points of **spirituality** [[Spirituality]].
- **Use:** When a creature breaks free, you use your biology to fight against it.
- **Resolution:** The difficulty of the fight is the result of the **Strength appraisal** [[Strength Appraisal]] when the opponent broke free.
- **Limits:** Each target can only be reshackled in this way once per **encounter** Encounter.

**Sequence 2 notes (as written in RAW):**
- Against non-demigod undead, it only takes the time your turn ends.
- Against demigod level, it takes two rounds but cannot break free through Strength confrontation.
- Against angel level [[Angel]], it still takes a full five rounds, suffering the same bind and life drain effects while being able to break free.
- At the same time, this skill of you in Sequence 2 treats living creatures and dead creatures equally.
