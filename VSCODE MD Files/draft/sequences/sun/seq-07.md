---
title: 'Sequence 7: Solar High Priest'
id: sun-seq-07
tags:
- pathway:sun
- sequence:7
---






# Sun Pathway: Sequence 7

## Solar High Priest

Your capabilities in sun-domain spells and sacrifices are greatly improved.

## Advancement

### Main Materials

- **[[Dawn Rooster]] (Red Crown):** ×1
- **[[Radiant Qiling Tree]] (Fruit):** ×1

### Auxiliary Materials

- **[[Dawn Rooster]] (Blood):** 100 ml
- **"sun" essential oil:** 10 drops
- **Golden hand orange powder:** 8 g
- **Solidified magma:** 5 g

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Agility (DEX) +1, Constitution +1, Intuition (INT) +1.
- **Skill/Path Gain:** Your [[Mysticism]] can be quickly upgraded to [[Erudition]].

### Sun Spells

```yaml ability
id: sun-seq-07-sun-spells
name: Sun Spells
pathway: sun
sequence: 7
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
- ritual
- buff
text: Your spells and ritual abilities are greatly improved. You gain the sun spells
  below in addition to the spells from the [[Prayer Stage]]. From now on, you no longer
  need to adopt a [[Prayer Posture]] to cast extraordinary abilities.
```





Your spells and ritual abilities are greatly improved.

- You gain the sun spells below in addition to the spells from the [[Prayer Stage]].
- From now on, you no longer need to adopt a [[Prayer Posture]] to cast extraordinary abilities.

- **Effect:** Sun Spells resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Immune to Fear

```yaml ability
id: sun-seq-07-immune-to-fear
name: Immune to Fear
pathway: sun
sequence: 7
status: canonical
type: active
action: swift
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
tags:
- ritual
- debuff
text: 'Cost: 2 [[Spirituality]]. Use: Swift Action (Swift Action). Effect: You gain
  immunity to the [[Fear Condition]] for 1 Encounter. Fear states do not arise on
  you. Existing fear states on you are cleared. Special: Fear effects larger than
  1 character of you can still be generated, but their effect is halved (round up).
  Clarification: Fear effects from targets more than 1 Sequence higher than you can
  still be generated, but their effect is halved (round up).'
```





- **Cost:** 2 [[Spirituality]].
- **Use:** **Swift Action** (Swift Action).
- **Effect:** You gain immunity to the [[Fear Condition]] for 1 Encounter.
  - Fear states do not arise on you.
  - Existing fear states on you are cleared.
- **Special:** Fear effects “larger than 1 character of you” can still be generated, but their effect is halved (round up).  
  - **Clarification:** Fear effects from targets more than 1 Sequence higher than you can still be generated, but their effect is halved (round up).

- **Limits:** As described in this section's prose.


### Fire of Light

```yaml ability
id: sun-seq-07-fire-of-light
name: Fire of Light
pathway: sun
sequence: 7
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose a location/area within 10 meters of you. The area of influence is no
  more than 10 meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 2d6 + 1d6
  heal_roll: null
  effect_roll: null
  notes: Creatures touching the fire take 2d6 sacred and 1d6 fire damage; resistance/evasion is ignored when avoiding the area.
scaling: []
tags:
- control
- defense
- offense
text: 'Cost: 2 [[Spirit Points]]. Use: Casting Action (Casting Action). Targeting
  and range: Choose a location/area within 10 meters of you. The area of influence
  is no more than 10 meters. Effect: You create a bright, golden illusory fire (an
  ocean of flame due to density). If creatures in the area try to avoid the bright
  fire, [[Occult]] counters [[Physical Defense]] and ignores dexterity and evasion.
  Any [[Creature Traits]] creatures that touch the fire suffer 2d6 sacred damage and
  1d6 fire damage, and gain the [[Restraint]] effect. This golden illusory flame can
  exist underwater. The flames only spread on things related to darkness, corruption,
  and undeath, and can be extinguished at any tim...'
```





- **Cost:** 2 [[Spirit Points]].
- **Use:** **Casting Action** (Casting Action).
- **Targeting and range:** Choose a location/area within 10 meters of you. The area of influence is no more than 10 meters.
- **Effect:** You create a bright, golden illusory fire (an “ocean” of flame due to density).
  - If creatures in the area try to avoid the bright fire, [[Occult]] counters [[Physical Defense]] and ignores dexterity and evasion.
  - Any [[Creature Traits]] creatures that touch the fire suffer **2d6 sacred damage** and **1d6 fire damage**, and gain the [[Restraint]] effect.
  - This golden illusory flame can exist underwater.
  - The flames only spread on things related to darkness, corruption, and undeath, and can be extinguished at any time according to your will.
- **Limits:** The fire of light has no effect on normal creatures and objects, and cannot ignite normal objects.
- **Scaling:** [[Sequence 5]]: The influence range of bright fire increases to 25 meters.

### Cleansing Slash

```yaml ability
id: sun-seq-07-cleansing-slash
name: Cleansing Slash
pathway: sun
sequence: 7
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Adds restrained damage to the next hit; restraint damage scales to 2d6 (fallen) or 3d6 (undead), +1d6 at Sequence 5.
scaling: []
tags:
- control
- offense
text: 'Cost: 1 [[Spirit Points]]. Use: Swift Action (Swift Action). Can be attached
  to weapons. Effect: The next damage you deal gains restrained damage. Regardless
  of the original damage type, only the additional restrained damage is considered
  holy damage. This can be stacked with [[Purifying Bullets]], but not with other
  holy abilities that already counter damage. Example: A revolver deals 1d8+5 physical
  damage. If it attacks a dark creature: 1d8+5 physical damage + 1d6 holy damage.
  If it is fallen: 2d6 holy damage.'
```





- **Cost:** 1 [[Spirit Points]].
- **Use:** **Swift Action** (Swift Action). Can be attached to weapons.
- **Effect:** The next damage you deal gains restrained damage.
  - Regardless of the original damage type, only the additional restrained damage is considered holy damage.
  - This can be stacked with [[Purifying Bullets]], but not with other holy abilities that already counter damage.
- **Example:** A revolver deals 1d8+5 physical damage.
  - If it attacks a dark creature: 1d8+5 physical damage + 1d6 holy damage.
  - If it is fallen: 2d6 holy damage.
  - If it is undead: 3d6 holy damage.
- **Limits:** Only affects the next damage instance.
  - To apply it to two hits, apply it twice.
  - To apply it to six bullets, apply it six times.
  - You can attack while applying it.
- **Scaling:** [[Sequence 5]]: Increase restraint damage from cleansing slash by 1d6.

### Sacred Oath

```yaml ability
id: sun-seq-07-sacred-oath
name: Sacred Oath
pathway: sun
sequence: 7
status: canonical
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Adds 1d6 fire or holy damage for 2 rounds, or grants +2 Power/+2 Agility; Sequence 5 increases to +3 or 2d6.
scaling: []
tags:
- ritual
- control
- buff
- offense
text: 'Cost: 2 [[Spirituality]]. Use: Swift Action (Swift Action). Requirement: Read
  the corresponding ancient [[Hermetic Words]] in the [[Language of Occultism]]. Effect:
  Choose one effect; only one can be active at a time. Duration: 2 rounds. "Power!":
  Your power +2. Cannot be superimposed with the power brought by [[Singing]]. "Agility
  (DEX)!": Your agility +2. Cannot be superimposed with the agility brought by [[Singing]].
  "Flame!": All your next damage adds 1d6 fire damage for 2 rounds. Free/attack/casting/full
  rounds that already have fire damage cannot increase this benefit. "Holy!": All
  your next damage adds 1d6 holy damage for 2 rounds (no restraint effect). Free/attack/casting/full
  rou...'
```





- **Cost:** 2 [[Spirituality]].
- **Use:** **Swift Action** (Swift Action).
- **Requirement:** Read the corresponding ancient [[Hermetic Words]] in the [[Language of Occultism]].
- **Effect:** Choose one effect; only one can be active at a time. Duration: 2 rounds.
  1. **"Power!":** Your power +2. Cannot be superimposed with the power brought by [[Singing]].
  2. **"Agility (DEX)!":** Your agility +2. Cannot be superimposed with the agility brought by [[Singing]].
  3. **"Flame!":** All your next damage adds 1d6 fire damage for 2 rounds. Free/attack/casting/full rounds that already have fire damage cannot increase this benefit.
  4. **"Holy!":** All your next damage adds 1d6 holy damage for 2 rounds (no restraint effect). Free/attack/casting/full rounds that already have holy damage cannot increase this benefit.
- **Limits:** Once selected, the effect cannot be switched before it ends.
- **Scaling:** [[Sequence 5]]: You can apply sacred oath to other creatures within sight. Attribute increases become +3, and damage increases become 2d6.

### Sun Halo

```yaml ability
id: sun-seq-07-sun-halo
name: Sun Halo
pathway: sun
sequence: 7
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose friendly units within 20 meters of you as the center.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: When used offensively, ignores agility/dodge and applies restrained damage each round to dark/fallen/undead in range.
scaling: []
tags:
- ritual
- control
- debuff
- defense
- offense
text: 'Cost: 2 [[Spirituality]]. Use: Casting Action (Casting Action). Targeting and
  range: Choose friendly units within 20 meters of you as the center. Effect: Anyone
  you consider a friend is affected; you can precisely control the halo to avoid specific
  targets. Effects of fear, cold, curse, poison, darkness, corruption, and undead
  in their bodies are cleared. Dark, corrupted, and undead creatures immediately suffer
  sacred damage equal to the restrained damage, and continue losing it each round
  if they do not leave the range. If using this ability to attack and the opponent
  intends to dodge, [[Mysticism]] counters physical defense, ignoring agility and
  dodge. Scaling: [[Sequence 5]]: Affects f...'
```





- **Cost:** 2 [[Spirituality]].
- **Use:** **Casting Action** (Casting Action).
- **Targeting and range:** Choose friendly units within 20 meters of you as the center.
- **Effect:**
  1. Anyone you consider a friend is affected; you can precisely control the halo to avoid specific targets.
  2. Effects of fear, cold, curse, poison, darkness, corruption, and undead in their bodies are cleared. Dark, corrupted, and undead creatures immediately suffer sacred damage equal to the restrained damage, and continue losing it each round if they do not leave the range.
  3. If using this ability to attack and the opponent intends to dodge, [[Mysticism]] counters physical defense, ignoring agility and dodge.
- **Scaling:** [[Sequence 5]]: Affects friendly units within 50 meters and gains a “qualitatively changed” version of the purification aura.  
  - **Clarification:** The Sequence 5 version also grants the **Purification Aura** benefits to allies in range and continuously applies the restrained‑damage effect to dark/fallen/undead in range each round.

- **Limits:** As described in this section's prose.


### Make Holy Water

```yaml ability
id: sun-seq-07-make-holy-water
name: Make Holy Water
pathway: sun
sequence: 7
status: canonical
type: active
action: full-round
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
- ritual
text: 'Cost: 4 [[Spirituality]]. Use: Full-Round Action ([[Full-Round Action]]). Effect:
  Create one bottle of [[Sun Holy Water]] by saying sun in the mystical language.
  You must prepare a container in advance to carry it, otherwise it spills onto the
  ground. Reference: See [[Holy Water Prayer]] for details. Scaling: [[Sequence 5]]:
  Use becomes 1 Casting Action instead.'
```





- **Cost:** 4 [[Spirituality]].
- **Use:** **Full-Round Action** ([[Full-Round Action]]).
- **Effect:** Create one bottle of [[Sun Holy Water]] by saying “sun” in the mystical language.
  - You must prepare a container in advance to carry it, otherwise it spills onto the ground.
- **Reference:** See [[Holy Water Prayer]] for details.
- **Scaling:** [[Sequence 5]]: Use becomes 1 Casting Action instead.

- **Limits:** As described in this section's prose.


### Sun Ritual

```yaml ability
id: sun-seq-07-sun-ritual
name: Sun Ritual
pathway: sun
sequence: 7
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
  damage_roll: 1d6
  heal_roll: null
  effect_roll: "1"
  notes: Possession attempts by lower-sequence wraith shadows fail and trigger restrained damage; successful possession by higher-level wraith shadows takes 1d6 holy damage per round.
scaling: []
tags:
- ritual
- buff
text: 'Effect: From now on, when you perform ritual magic in the sun domain, occult
  identification automatically succeeds by default. Scaling: [[Sequence 5]]: As long
  as you do not believe in hostile gods, you can still receive a stable response even
  if you are not a believer in the sun. Limits: This effect is brought by a potion,
  is an improvement during the Sequence 8 period, and cannot be recorded or stolen.'
```





- **Effect:** From now on, when you perform ritual magic in the sun domain, occult identification automatically succeeds by default.
- **Scaling:** [[Sequence 5]]: As long as you do not believe in hostile gods, you can still receive a stable response even if you are not a believer in the sun.
- **Limits:** This effect is brought by a potion, is an improvement during the Sequence 8 period, and cannot be recorded or stolen.

### Body of the Sun

```yaml ability
id: sun-seq-07-body-of-the-sun
name: Body of the Sun
pathway: sun
sequence: 7
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
- detection
- control
- debuff
- defense
- offense
text: 'Effect: You obtain a special [[Sun]], making it difficult to be possessed or
  polluted by evil spirit-like monsters. You gain 5 points of resistance to curse,
  cold, and poison; this cannot be superimposed with [[Holy Water]]. Only [[Wraith
  Shadow]] higher than your sequence level (or 1 character higher) can possess you.
  Clarification: Treat 1 character higher as 1 Sequence higher. When a wraith shadow
  attempts possession: It immediately senses the breath of the sun. If it is not higher
  than your sequence level: if it forcibly possesses you, it fails and suffers sacred
  damage equal to the restrained damage. If a higher-level wraith shadow successfully
  possesses you: it suffers 1d6 holy dama...'
```





- **Effect:** You obtain a special [[Sun]], making it difficult to be possessed or polluted by evil spirit-like monsters.
  - You gain 5 points of resistance to curse, cold, and poison; this cannot be superimposed with [[Holy Water]].
  - Only [[Wraith Shadow]] higher than your sequence level (or “1 character” higher) can possess you.  
    - **Clarification:** Treat “1 character higher” as 1 Sequence higher.
- **When a wraith shadow attempts possession:**
  - It immediately senses the breath of the sun.
  - If it is not higher than your sequence level: if it forcibly possesses you, it fails and suffers sacred damage equal to the restrained damage.
  - If a higher-level wraith shadow successfully possesses you: it suffers 1d6 holy damage each round (no additional restraint effect) and does not break away from the possession.
- **Scaling:**
  - [[id:alias-sequence-6|Sequence 6]]: Wraith shadows that are not higher than “1 person of you” also suffer restraint damage when they try to possess you, and immediately leave the possessed state.
  - [[Sequence 5]]: Resistance to curse, cold, and poison becomes 10 points.

- **Limits:** As described in this section's prose.
