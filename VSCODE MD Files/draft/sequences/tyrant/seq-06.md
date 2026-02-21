---
title: 'Sequence 6: Wind-blessed'
id: tyrant-seq-06
tags:
- pathway:tyrant
- sequence:6
---






# Tyrant Pathway: Sequence 6

> **Lore:** Blessed by the wind, you command violent air currents, move through the sky, and shape wind into weapons.

## Wind-blessed

## Advancement

### Auxiliary Materials

- Six crystalline feathers of the Blue Shadow Falcon  
- One pair of eyeballs of the Longyan Sea Eagle  

### Acting Requirements

- You must occasionally allow yourself to become irritable or short-tempered to align with the nature of “Gale.”  

---

## Extraordinary Abilities

### Attribute Gain

- **Strength** +1  
- **Constitution** +1  
- **Agility (DEX)** +2  
- **Intuition (INT)** +1  
- [[Skills]] related to piloting, swimming, and diving can be quickly promoted to erudition.  

---

### Deep Vision

```yaml ability
id: tyrant-seq-06-deep-vision
name: Deep Vision
pathway: tyrant
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- detection
text: 'Effect: You maintain normal vision even in completely dark environments. --'
```





- **Effect:** You maintain normal vision even in completely dark environments.  

---

- **Limits:** As described in this section's prose.


### Deep Dive

```yaml ability
id: tyrant-seq-06-deep-dive
name: Deep Dive
pathway: tyrant
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
text: 'Effect: Your phantom scales and underwater breathing support deep diving at
  any depth. Limits: You still cannot exceed the normal duration limits of your phantom
  scales and underwater breathing. Sequence 5 Change: Your phantom scales and water
  breathing no longer count toward underwater duration limits. Normal duration limits:
  Use the durations from Phantom Scale and Water Breathing (10 minutes base, +15 minutes
  per Sequence upgrade). --'
```





- **Effect:** Your phantom scales and underwater breathing support deep diving at any depth.  
- **Limits:** You still cannot exceed the normal duration limits of your phantom scales and underwater breathing.  
- **Sequence 5 Change:** Your phantom scales and water breathing no longer count toward underwater duration limits.  
  - **Normal duration limits:** Use the durations from **Phantom Scale** and **Water Breathing** (10 minutes base, +15 minutes per Sequence upgrade).

---

### Wind Control  
```yaml ability
id: tyrant-seq-06-wind-control
name: Wind Control
pathway: tyrant
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
- control
text: '[[Wind Domain]] You gain the following wind-based abilities. --'
```





[[Wind Domain]]

You gain the following wind-based abilities.

---

- **Effect:** Wind Control resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Short-Distance Flight

```yaml ability
id: tyrant-seq-06-short-distance-flight
name: Short-Distance Flight
pathway: tyrant
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: physical_defense
range: You may take off together with creatures within 5 meters.
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
- mobility
- buff
- defense
text: 'Cost: 1 Swift Action, 1 spirituality Effect: A strong wind engulfs you, allowing
  you to instantly fly up to 10 meters in any direction. You do not need to physically
  move to do so. Targeting and Range: You may take off together with creatures within
  5 meters. Special: While performing short-distance flight, you are considered to
  have Fast Dodge. Against firearms (not light/lightning), you retain full physical
  defense and gain +1 level of dodge. If you already have Fast Dodge, increase your
  dodge level by 1 instead. Sequence 5 Change: Maximum flight distance becomes 20
  meters.'
```





- **Cost:** 1 Swift Action, 1 spirituality  
- **Effect:** A strong wind engulfs you, allowing you to instantly fly up to 10 meters in any direction. You do not need to physically move to do so.  
- **Targeting and Range:** You may take off together with creatures within 5 meters.  
- **Special:**  
  - While performing short-distance flight, you are considered to have **Fast Dodge**.  
  - Against firearms (not light/lightning), you retain full physical defense and gain +1 level of dodge.  
  - If you already have Fast Dodge, increase your dodge level by 1 instead.  
- **Sequence 5 Change:** Maximum flight distance becomes 20 meters.  

---

- **Limits:** As described in this section's prose.


### Glide

```yaml ability
id: tyrant-seq-06-glide
name: Glide
pathway: tyrant
sequence: 6
status: canonical
type: active
action: swift
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
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
text: 'Cost: 1 Swift Action, 1 spirituality Effect: You glide in any direction while
  descending 1 meter per round. Limits: You cannot gain altitude with this ability.
  --'
```





- **Cost:** 1 Swift Action, 1 spirituality  
- **Effect:** You glide in any direction while descending 1 meter per round.  
- **Limits:** You cannot gain altitude with this ability.  

---

### Floating

```yaml ability
id: tyrant-seq-06-floating
name: Floating
pathway: tyrant
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: Up to 5 minutes.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- mobility
text: 'Cost: 1 Swift Action, 1 spirituality Effect: A gust of wind lifts you up to
  5 meters vertically, where you can remain suspended. Duration: Up to 5 minutes.
  Movement: You may move in the air with movement force equal to your Agility (DEX).
  Limits: Height may be adjusted by will; you may choose not to float. Sequence 5
  Change: Maximum vertical height becomes 10 meters. --'
```





- **Cost:** 1 Swift Action, 1 spirituality  
- **Effect:** A gust of wind lifts you up to 5 meters vertically, where you can remain suspended.  
- **Duration:** Up to 5 minutes.  
- **Movement:** You may move in the air with movement force equal to your Agility (DEX).  
- **Limits:** Height may be adjusted by will; you may choose not to float.  
- **Sequence 5 Change:** Maximum vertical height becomes 10 meters.  

---

### Create Air Cushions

```yaml ability
id: tyrant-seq-06-create-air-cushions
name: Create Air Cushions
pathway: tyrant
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: none
range: Up to a 10-meter area
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: No roll; creates silent footing and negates fall damage within the cushion area.
scaling: []
tags:
- ritual
- stealth
- offense
text: 'Cost: 1 Swift Action, 2 spirituality Targeting and Range: Up to a 10-meter
  area Effect: Creatures and objects moving on the air cushion make no sound; stealth
  identification automatically succeeds. The cushion has no physical volume. Falling
  creatures landing on an air cushion are immune to fall damage. If falling from more
  than 100 meters, an additional cushion layer must be created every 100 meters to
  continuously reduce impact. --'
```





- **Cost:** 1 Swift Action, 2 spirituality  
- **Targeting and Range:** Up to a 10-meter area  
- **Effect:**  
  1. Creatures and objects moving on the air cushion make no sound; stealth identification automatically succeeds. The cushion has no physical volume.  
  2. Falling creatures landing on an air cushion are immune to fall damage. If falling from more than 100 meters, an additional cushion layer must be created every 100 meters to continuously reduce impact.  

---

- **Limits:** As described in this section's prose.


### Wind Blade

```yaml ability
id: tyrant-seq-06-wind-blade
name: Wind Blade
pathway: tyrant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.navigation
opposed_by: physical_defense
range: One or more targets within 50 meters
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.navigation
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Each shot costs 1 spirituality; up to 3 shots per casting action. Sequence 5 increases damage by +1d6.
scaling: []
damage_types:
- physical
tags:
- ritual
- buff
- defense
- offense
text: 'Cost: 1 spellcasting action; 1 spirituality per shot Targeting and Range: One
  or more targets within 50 meters Check: Intuition (INT) + piloting vs physical defense
  Effect: Each wind blade deals 2d6 physical damage. Speed is treated as a firearm.
  Limits: One Casting Action allows up to 3 consecutive shots; each may target a different
  creature. When repeatedly attacking the same target, hit identification improves
  instead of decreasing; from the second shot onward, each shot gains a cumulative
  +2 benefit. If you can release Wind Blade as a Swift Action, that version inherits
  the bonus above.'
```





- **Cost:** 1 spellcasting action; 1 spirituality per shot  
- **Targeting and Range:** One or more targets within 50 meters  
- **Check:** Intuition (INT) + piloting vs physical defense  
- **Effect:** Each wind blade deals 2d6 physical damage. Speed is treated as a firearm.  
- **Limits:**  
  1. One Casting Action allows up to 3 consecutive shots; each may target a different creature.  
  2. When repeatedly attacking the same target, hit identification improves instead of decreasing; from the second shot onward, each shot gains a cumulative +2 benefit.  
  3. If you can release Wind Blade as a Swift Action, that version inherits the bonus above.  
- **Manifestation:** Impacts leave cuts like blades across surfaces.  
- **Sequence 5 Change:** Damage increases by 1d6.  

---

### Wind Bind

```yaml ability
id: tyrant-seq-06-wind-bind
name: Wind Bind
pathway: tyrant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int
opposed_by: difficulty_value
range: self
target: 1 creature
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Opposed by target Agility (DEX); on success, target is Bound and must pass DV 20 to break free each round.
scaling: []
tags:
- ritual
- mobility
- control
text: 'Cost: 1 spellcasting action, 3 spirituality Target: 1 creature Check: Intuition
  (INT) vs targets Agility (DEX) Effect: On success, the target gains the [[Bound]]
  state and cannot perform movement actions. Escape: At the start of each round, the
  target may attempt a Difficulty Value 20 skill check to break free. --'
```





- **Cost:** 1 spellcasting action, 3 spirituality  
- **Target:** 1 creature  
- **Check:** Intuition (INT) vs target’s Agility (DEX)  
- **Effect:** On success, the target gains the [[Bound]] state and cannot perform movement actions.  
- **Escape:** At the start of each round, the target may attempt a Difficulty Value 20 skill check to break free.  

---

- **Limits:** As described in this section's prose.


### Wind Attachment

```yaml ability
id: tyrant-seq-06-wind-attachment
name: Wind Attachment
pathway: tyrant
sequence: 6
status: canonical
type: toggle
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: physical_defense
range: 5m
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: "1"
  notes: Hand/weapon effect adds +1d6 physical damage for the round; legs effect boosts movement as listed.
scaling: []
damage_types:
- physical
tags:
- ritual
- mobility
- buff
- defense
- offense
text: 'Cost: 1 Swift Action, 1 spirituality Effect: Choose one effect for 1 round:
  Hand: Your right fist is wrapped in high-speed wind. One Attack Action that round
  deals +1d6 physical damage; applies to combo attacks. Legs: While walking or running
  on land, your movement force increases by +15 for 1 round. Allies within 5 meters
  gain this benefit. Weapons: The Hand effect can be applied to weapons, arrows, or
  firearms without changing their speed. Special (Legs): While active, you are considered
  to have Fast Dodge. Against firearms (not light/lightning), retain full physical
  defense and gain +1 dodge level (or +1 level if already having Fast Dodge). Sequence
  5 Change: Allies within 10 meters be...'
```





- **Cost:** 1 Swift Action, 1 spirituality  
- **Effect:** Choose one effect for 1 round:

1. **Hand:** Your right fist is wrapped in high-speed wind. One Attack Action that round deals +1d6 physical damage; applies to combo attacks.  
2. **Legs:** While walking or running on land, your movement force increases by +15 for 1 round. Allies within 5 meters gain this benefit.  
3. **Weapons:** The Hand effect can be applied to weapons, arrows, or firearms without changing their speed.  

- **Special (Legs):** While active, you are considered to have Fast Dodge. Against firearms (not light/lightning), retain full physical defense and gain +1 dodge level (or +1 level if already having Fast Dodge).  
- **Sequence 5 Change:** Allies within 10 meters benefit.  

---

- **Limits:** As described in this section's prose.


### Sound Transmission

```yaml ability
id: tyrant-seq-06-sound-transmission
name: Sound Transmission
pathway: tyrant
sequence: 6
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
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- mobility
- buff
text: 'Cost: 1 Swift Action; 1 spirituality per sentence Effect: Your voice travels
  up to 100 meters in a chosen direction. Sequence 5 Change: Distance increases by
  100 meters. --'
```





- **Cost:** 1 Swift Action; 1 spirituality per sentence  
- **Effect:** Your voice travels up to 100 meters in a chosen direction.  
- **Sequence 5 Change:** Distance increases by 100 meters.  

---

- **Limits:** As described in this section's prose.


### Wind Pressure Slap

```yaml ability
id: tyrant-seq-06-wind-pressure-slap
name: Wind Pressure Slap
pathway: tyrant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.navigation
opposed_by: physical_defense
range: 10m
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.navigation
  damage_roll: 4d6
  heal_roll: null
  effect_roll: null
  notes: Treated as firearm speed; Sequence 5 increases damage to 5d6.
scaling: []
damage_types:
- physical
tags:
- ritual
- defense
- offense
text: 'Cost: 1 spellcasting action, 3 spirituality Area: All targets within 10 meters
  in front of you Check: Intuition (INT) + navigator vs physical defense Effect: Treated
  as firearm speed; deals 4d6 physical damage. Sequence 5 Change: Damage becomes 5d6.
  --'
```





- **Cost:** 1 spellcasting action, 3 spirituality  
- **Area:** All targets within 10 meters in front of you  
- **Check:** Intuition (INT) + navigator vs physical defense  
- **Effect:** Treated as firearm speed; deals 4d6 physical damage.  
- **Sequence 5 Change:** Damage becomes 5d6.  

---

- **Limits:** As described in this section's prose.


### Create a Gale

```yaml ability
id: tyrant-seq-06-create-a-gale
name: Create a Gale
pathway: tyrant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: difficulty_value
range: 50m
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: Targets make DV 20 Agility checks or lose balance; wind effects and bonuses apply as listed.
scaling: []
tags:
- ritual
- mobility
text: 'Cost: 1 spellcasting action, 3 spirituality Area: All targets within 50 meters
  in front of you Effect: You gain 20 points of forced movement. Targets are blown
  up to 20 meters until beyond the 50-meter area. *Balance and Distance Rules Creatures
  make an Agility (DEX) check (Difficulty Value 20) or lose balance. If voluntarily
  moving 5 meters with the wind, they gain +2 to maintain balance. Creatures that
  lose balance have their blown distance doubled (round up).'
```





- **Cost:** 1 spellcasting action, 3 spirituality  
- **Area:** All targets within 50 meters in front of you  
- **Effect:**  
  - You gain 20 points of forced movement.  
  - Targets are blown up to 20 meters until beyond the 50-meter area.  

**Balance and Distance Rules**

1. Creatures make an Agility (DEX) check (Difficulty Value 20) or lose balance. If voluntarily moving 5 meters with the wind, they gain +2 to maintain balance.  
2. Creatures that lose balance have their blown distance doubled (round up).  
3. For each 1 point of creature size above small, forced movement distance is reduced by 2 meters. Small or tiny creatures automatically lose balance and have distance doubled.  

**Additional Wind Uses**

4. **Extinguish Flames:** 1 Swift Action, 1 spirituality. In a chosen direction, extinguish flames within 50 meters. Fire abilities requiring combustibles cannot ignite. Fire abilities not requiring combustibles suffer −2 disadvantage toward you and −1d6 damage.  
5. **Damage Reduction:** 1 Swift Action, 2 spirituality. When hit by strength-based damage dice, move backward with wind and reduce that damage by 1d6.  
6. **Ally Push:** 1 Swift Action, 2 spirituality. When a creature within 50 meters is about to be targeted by a single-target attack, push it away; the attack suffers −6 disadvantage.  

- **Maintenance:** You may spend 1 spirituality each round to sustain the gale.  
- **Sequence 5 Change:** Maximum ranges become 100 meters; maximum blown distance becomes 40 meters.  

---

- **Limits:** As described in this section's prose.


### Extended Wind Logic

```yaml ability
id: tyrant-seq-06-extended-wind-logic
name: Extended Wind Logic
pathway: tyrant
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
- control
- buff
text: With GM approval, other logical wind-control uses are allowed. If an ability
  that pushes creatures interacts with the Sequence 7 Water Spell, pushing distance
  is increased accordingly.
```





- With GM approval, other logical wind-control uses are allowed.  
- If an ability that pushes creatures interacts with the Sequence 7 Water Spell, pushing distance is increased accordingly.  

- **Effect:** Extended Wind Logic resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
