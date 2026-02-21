---
title: 'Sequence 5: Spirit Guide'
id: death-seq-05
tags:
- pathway:death
- sequence:5
---






# Death Pathway: Sequence 5

A Gatekeeper can sense entrances to the [[Underworld]] and create gates that overlap the [[Spirit World]] and the Underworld. It can drive the [[Undead]] and summon many undead creatures.

It can also use its body as a “cage,” turning it into a small Underworld that can contain a certain number of souls, undead, and [[Natural Spirits]]. This inner realm prevents contained spirits from escaping, provides a suitable environment for them to exist, and can be used to gain unique abilities from them.

## Spirit Guide

## Advancement

### Advancement Ritual

**Ceremony (not official ceremony):**
- First, extract your soul.
- Then, make your body acquire the characteristics of a living person: blood becomes moist again (no longer cold), joints become flexible again, and the face regains blood color.
- Immediately after the soul returns to the body, take the potion.

**Effect (during promotion):**
- At the moment of promotion, the Underworld inside the Beyonder’s body immediately opens, causing the Beyonder’s soul to “die” and be dragged into the Underworld, becoming a wandering lonely soul.
- Therefore, the Beyonder must regain a living-being status in their body to resist becoming an “undead creature” when the Underworld appears inside their body. At the same time, they cannot truly become a living being, or they will lose life upon contact with the Underworld—dying instantly because they are living.
- If the soul remains in the state of an undead creature, but the body has acquired the characteristics of a living person, then after returning, the Beyonder will be in two states—life and death—side by side. This both:
  - resists the Underworld’s undead-creature transformation, and
  - lets the soul adapt to the power of death without actually passing away.

> **GM Note:** Possessing another person does not meet the requirements. First, a body that is not of the Death cannot reach the “pseudo-dead” state. Second, that body may still have its own original spirit body, and conflicting thoughts may lead to loss of control.

## Extraordinary Abilities
### Attribute Gain

- **Attribute Gain:** Not explicitly specified in source (schema placeholder).


### Underworld Perception and Sign

```yaml ability
id: death-seq-05-underworld-perception-and-sign
name: Underworld Perception and Sign
pathway: death
sequence: 5
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
- mobility
text: You can perceive the location of the Underworld. You gain an Underworld in the
  body, with a door as a symbol. The core of this inner Underworld is at the center
  of the forehead, representing the location of the [[God of Death]]. This description
  is cosmetic only and has no mechanical effect.
```





- You can perceive the location of the Underworld.
- You gain an “Underworld in the body,” with a door as a symbol. The core of this inner Underworld is at the center of the forehead, representing the location of the [[God of Death]]. This description is cosmetic only and has no mechanical effect.

- **Effect:** Underworld Perception and Sign resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Inner Underworld

```yaml ability
id: death-seq-05-inner-underworld
name: Inner Underworld
pathway: death
sequence: 5
status: canonical
type: active
action: swift
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
text: 'Effect: You can use your body as a cage to provide a suitable environment for
  your own Underworld. From now on, you can hold a certain number of dead, soul bodies,
  and natural spirits in your body. The number you can hold equals the number of dead
  you can drive using [[Knowledge of the Dead]]. Contained dead are limited to spirit
  bodies; dead with physical bodies cannot enter your body. Use: As a Swift Action,
  you can release any number of spirits contained within you. Special: The Underworld
  in the body is an effect brought by the potion and cannot be [[Stolen]] or [[Recorded]].
  *Benefits: 1) Any soul contained in your body no longer needs to worry about its
  existence time. As long as it...'
```





- **Effect:** You can use your body as a cage to provide a suitable environment for your own “Underworld.”
  - From now on, you can hold a certain number of dead, soul bodies, and natural spirits in your body.
  - The number you can hold equals the number of dead you can drive using [[Knowledge of the Dead]].
  - Contained dead are limited to spirit bodies; dead with physical bodies cannot enter your body.
- **Use:** As a **Swift Action**, you can release any number of spirits contained within you.
- **Special:** The Underworld in the body is an effect brought by the potion and cannot be [[Stolen]] or [[Recorded]].

**Benefits:**
1) Any soul contained in your body no longer needs to worry about its existence time. As long as it does not leave the inner Underworld, its existence time is unlimited.
2) With 1 **Casting Action**, you can use the abilities of a spirit body contained within your inner Underworld.
   - This does not include spirit bodies higher than you by 1 level.
   - To use the abilities of a spirit body higher than you by 1 level, that spirit body must voluntarily lend you the ability each time.
   - Even if the borrowed ability is originally a Swift Action, you still need a Casting Action to use it. If it is a Full-Round Action, it is still a **Full-Round Action**.
3) If someone intends to withdraw a spirit body attached to you, or a spirit body in the inner Underworld within your body, you can make a **Knowledge of the Dead** test with **Intuition (INT)** added as a modifier against it (or against the same identification of Knowledge of the Dead). On a success, your body’s spirit is pulled back.
   - **Special:** This does not include your own spirit body, because instability of your own spirit body causes you to no longer be able to effectively use the inner Underworld.

- **Limits:** As described in this section's prose.



### Gate to the Underworld

```yaml ability
id: death-seq-05-gate-to-the-underworld
name: Gate to the Underworld
pathway: death
sequence: 5
status: adapted
type: active
action: cast
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.knowledge
opposed_by: physical_defense
range: 50m
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: check_roll maps the Ghosts of the Underworld grab check against Physical Defense; other gate effects resolve per prose.
scaling:
- when: use_is_underworld_vortex
  changes:
    check_roll: null
    effect_note: Vortex mode applies forced movement and suction effects without an attack check.
tags:
- ritual
- defense
- offense
text: 'You construct a slightly obscured, bisected bronze gate that creates an entrance
  to the Underworld. This ability has two uses. #### Use 1: Manifest Gate to Seize
  and Draw In Cost: 5 points of [[Spirituality]] Use: 1 Casting Action. Spread five
  fingers and aim your palm at a target within 50 meters. Effect: The Gatekeeper chooses
  one of the following effects to emerge from the gate, or both simultaneously (no
  action required): *A) Ghosts of the Underworld Attack/Check: Intuition (INT) + Knowledge
  of the Dead against the targets [[Physical Defense]], ignoring [[Armor]].'
```





You construct a slightly obscured, bisected bronze gate that creates an entrance to the Underworld.

This ability has two uses.

#### Use 1: Manifest Gate to Seize and Draw In

- **Cost:** 5 points of [[Spirituality]]
- **Use:** 1 **Casting Action**. Spread five fingers and aim your palm at a target within 50 meters.
- **Effect:** The Gatekeeper chooses one of the following effects to emerge from the gate, or both simultaneously (no action required):

**A) Ghosts of the Underworld**
- **Attack/Check:** “Intuition (INT) + Knowledge of the Dead” against the target’s [[Physical Defense]], ignoring [[Armor]].
- **On a successful catch:**
  1) The target cannot use [[Displacement Abilities]], and cannot escape through [[Blurring]].
     - At the beginning of each round, the target must use Strength to oppose “Intuition (INT) + Knowledge of the Dead identification,” or be pulled toward/into the gate by a distance equal to the Gatekeeper’s Knowledge of the Dead skill bonus. While caught, the target continues to be regarded as in a [[Bound State]].
  2) After being caught, the target’s normal movement action can only move closer to the gate.
     - Each time the caught creature suffers damage or a mental influence (e.g., “spiritual puncture,” “dragon power,” etc.), it immediately performs an additional pull check as in (1).
  3) Once completely pulled into the gate, the target is regarded as being sent to the Underworld immediately.
     - Any living creature is deemed to have died on the spot in the Underworld, becoming an Underworld soul: half-dead, half-lived.
     - Demigods of the Death Pathway are not affected.
     - However, “resentful souls/living corpses” before demigods of an “alien path” are also considered living and suffer the instant-death effect.

- **Special:** If the creature entering the Underworld is a dead person, it can find an exit within 24 hours and appears in a random place after finding the exit.

**B) The Vortex of the Underworld**
- **Duration/Condition:** As long as the gate exists.
- **Effect:**
  - The gate creates a terrifying suction force.
  - All gas-related abilities within 50 meters are immediately drawn in and emptied; an ability just released is invalidated if drawn in before it takes effect.
  1) All unowned Tiny and Small things begin to be drawn into the gate.
     - “Unowned” is determined by whether the object is currently held by another creature.
  2) As long as the gate exists, all things within 50 meters are forced to move 2 meters closer to the gate each round.
     - The Tiny and Small objects in (1) move 4 meters instead.
     - This includes individuals already captured by Ghosts of the Underworld; no identification is required.
  3) Any flying unit within 50 meters is forced to approach the gate by 4 meters.
     - If there is a spirit body half separated from a physical body, then when the vortex appears, it immediately increases the separation progress by 1 level.

#### Managing the Gate and Escaping

- Whenever the gate drags a target, the summoner does not need to take any action to decide whether the gate still exists.
  - Generally, if the desired target is dragged in, the summoner should immediately control the gate to close to prevent escape. If the summoner wants to drag again, they can reopen the gate.
- If the summoner cancels the summoning of the gate, it immediately interrupts the drag and the gate’s existence.
- To escape the gate of the Underworld, a creature must attack the gate.

**Gate and revenant hit points and targeting:**
- The gate has hit points equal to the summoner’s **maximum** Vitality, but is independent of the summoner.
- The “nether revenant” is a separate summoned entity with a total of 20 hit points.
- Both are considered undead.

**Why “treated as a whole” but separate:**
- If an attack is made against the gate, it may cause the nether revenant to disappear, but not necessarily cause the gate itself to disappear.
- Example: If a creature is dragged by Ghosts of the Underworld and a holy strike is cast on the gate, if the nether revenant is completely vaporized then the drag is lifted, but the gate can continue to produce revenants and can re-drag targets.

**Damage interactions:**
- If cold damage is dealt to the Underworld soul, its single dragging distance is reduced by 2 meters.
- If the gate’s hit points are less than half (round up), the suction of the vortex is halved.
- When a target is being dragged:
  - If damage is dealt to the dragged target, and the damage form is described as “multiple targets standing together are regarded as the same target,” then that damage also damages the souls of the Underworld (instead of the gate’s hit points).
  - If the dragged target and the gate are within 3 meters, this changes to damaging the gate.

**Independence:**
- The gate’s action is independent of the Gatekeeper’s actions; after summoning it, the Gatekeeper does not need to maintain it continuously.
- The Gatekeeper is only affected by the suction of the vortex of the Underworld.
- Gates of the Underworld made by extraordinary items generally need to consume spells to maintain.

GM decides the gate’s specific goal beyond the rules above.

#### Use 2: Overlapping Gate for Travel

- **Cost:** 3 points of Spirituality
- **Use:** 1 **Casting Action**
- **Effect:** You create a gate that overlaps the Spirit World and the Underworld.
  - You create the same gate, but it is not “manic.”
  - It can be used to freely enter and exit between reality and the Spirit World/Underworld without needing to find an entrance.
  - Before demigods, if your body tries to enter the Underworld, you still die as a living creature.

- **Limits:** As described in this section's prose.


### Nether Wave

```yaml ability
id: death-seq-05-nether-wave
name: Nether Wave
pathway: death
sequence: 5
status: canonical
type: active
action: full-round
cost: {}
roll: null
opposed_by: none
range: Ground or sea area within 100 meters
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
text: 'You turn an area around you into a portal to the Underworld and reality. Cost:
  Indefinite Spirituality (see Duration/Upkeep below) Use: 1 Full-Round Action Targeting
  and range: Ground or sea area within 100 meters Effect: The affected area suddenly
  becomes dark, as if turning into the entrance of helllike a deep, dark ocean. You
  summon any Underworld creatures; they occupy your [[Manipulation Ceiling]] and charge
  your enemies like a tidal wave. *Duration/Upkeep: 1) Before using this ability,
  choose the number of rounds the wave will last. Each round consumes 5 points of
  Spirituality. 2) The end of the continuation does not mean the summoned creatures
  disappear. Instead, within 1 minute af...'
```





You turn an area around you into a portal to the Underworld and reality.

- **Cost:** Indefinite Spirituality (see Duration/Upkeep below)
- **Use:** 1 **Full-Round Action**
- **Targeting and range:** Ground or sea area within 100 meters
- **Effect:** The affected area suddenly becomes dark, as if turning into the entrance of hell—like a deep, dark ocean. You summon any Underworld creatures; they occupy your [[Manipulation Ceiling]] and charge your enemies like a tidal wave.

**Duration/Upkeep:**
1) Before using this ability, choose the number of rounds the wave will last. Each round consumes 5 points of Spirituality.
2) The end of the continuation does not mean the summoned creatures disappear. Instead, within **1 minute** after the wave ends, each species will die or half of the total number of troops will be lost (round up). During this 1-minute window, you can immediately decide to add any number of Underworld creatures.
3) The type and quantity of Underworld creatures “filled in the time” are up to you. After that 1-minute window ends, you need to use a Full-Round Action to summon.
4) If you leave the 100-meter range, the Nether Wave closes immediately.


**Summoned Underworld creatures:**
- Blood Corpse:
  - 25 health
  - 20 physical defense (5 points are agility, dodge, and movement)
  - Ignores the ability to fight against physical and will defense
  - 5 points of cold, curse, and poison resistance
  - Attacks cause 2d6 physical damage
- Many-legged ghost:
  - 20 health
  - 25 physical defense (10 points are agility, dodge, and mobility)
  - 15 points of constitution and will defense
  - 5 points of resistance to cold, curse, and poison
  - Attacks cause 2d6 poison damage
- Pale Skeleton:
  - 25 health
  - 25 physical defense (5 points are agility, dodge, and mobility)
  - Ignores the ability to fight against physical and will defense
  - 5 points of resistance to cold, curse, and poison
  - Attacks cause 2d6 curse damage
  - Takes the minimum non-blunt weapon damage
- Deformed Zombie:
  - 35 health
  - 25 physical defense (5 points are agility, dodge, and movement)
  - Ignores the ability to resist physical and will defense
  - 5 points of cold, curse, and poison resistance
  - Attacks cause 1d6 physical damage

**Special:**
- Underworld creatures cannot exist in reality for more than 1 hour.
- If any combat is carried out during this period, they return to the Spirit World immediately after the encounter due to excessive consumption.

- **Limits:** As described in this section's prose.
