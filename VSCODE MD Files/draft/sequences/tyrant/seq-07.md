---
title: 'Sequence 7: Sea Warrior'
id: tyrant-seq-07
tags:
- pathway:tyrant
- sequence:7
---






# Tyrant Pathway: Sequence 7

## Sea Warrior

> **Lore:** Called “Priest Storm” in ancient times, Navigators are scholars of astronomy and geography. Their gifts are tied to the sea and to the [[Lord of Storms]].

- You have an intuitive grasp of magnetic fields, ocean currents, wind direction, and clouds.
- You can move freely underwater for **more than half an hour**.
- You can cast limited water-related spells (some from personal mastery, some as gifts).

## Acting Method

- Stay close to the sea.
- Be proficient in navigation and weather information.
- Pursue exploration and discovery.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +2.
- Your [[Navigator]] skill increases by 1 level.

### Rapid Promotion Compatibility

```yaml ability
id: tyrant-seq-07-rapid-promotion-compatibility
name: Rapid Promotion Compatibility
pathway: tyrant
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
- buff
text: The Navigator is in the [[Rapid Promotion]] system and is not treated as a newly
  promoted character. The [[Potion]] attribute used to increase the growth of this
  skill is Intuition (INT).
```





- The Navigator is in the [[Rapid Promotion]] system and is **not** treated as a newly promoted character.
- The [[Potion]] attribute used to increase the growth of this skill is **Intuition (INT)**.

- **Effect:** Rapid Promotion Compatibility resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Perfect Recall and Orientation

```yaml ability
id: tyrant-seq-07-perfect-recall-and-orientation
name: Perfect Recall and Orientation
pathway: tyrant
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
- buff
text: You do not get lost. Your memory is enhanced; you have photographic memory.
  You can remember all kinds of information that have not been affected by the Extraordinary.
```





- You do not get lost.
- Your memory is enhanced; you have photographic memory.
- You can remember all kinds of information that have not been affected by the Extraordinary.

- **Effect:** Perfect Recall and Orientation resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Far Sight

```yaml ability
id: tyrant-seq-07-far-sight
name: Far Sight
pathway: tyrant
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
- buff
text: Your vision is significantly improved. Your field of vision increases to 500
  meters when unobstructed.
```





- Your vision is significantly improved.
- Your field of vision increases to 500 meters when unobstructed.

- **Effect:** Far Sight resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Fuzzy Probability Calculation

```yaml ability
id: tyrant-seq-07-fuzzy-probability-calculation
name: Fuzzy Probability Calculation
pathway: tyrant
sequence: 7
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Intuition check DV 20; each relevant clue grants +2.
scaling: []
tags:
- detection
- mobility
- offense
text: 'Requirement: You have relevant clues. Use: Make an Intuition (INT) check at
  Difficulty Value 20. Effect: You calculate a fuzzy probability about a matter. Clues:
  Each relevant clue provides a +2 bonus. You can determine the relative distance
  between up to two things within your field of vision without an identification check.
  Special (Blind): Even if you are [[Blind]], if you confirmed the enemys position
  before becoming blind and the enemy has not moved significantly, you can use the
  calculated relative distance to attack without being affected by the blind state.'
```





- **Requirement:** You have relevant clues.
- **Use:** Make an **Intuition (INT)** check at **Difficulty Value 20**.
- **Effect:** You calculate a “fuzzy” probability about a matter.
- **Clues:** Each relevant clue provides a +2 bonus.
  - You can determine the relative distance between up to two things within your field of vision without an identification check.

- **Special (Blind):** Even if you are [[Blind]], if you confirmed the enemy’s position before becoming blind and the enemy has not moved significantly, you can use the calculated relative distance to attack without being affected by the blind state.

- **Limits:** As described in this section's prose.


### Intuitive Grasp

```yaml ability
id: tyrant-seq-07-intuitive-grasp
name: Intuitive Grasp
pathway: tyrant
sequence: 7
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.navigation
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.navigation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Piloting/navigation identifications typically use DV 15.
scaling: []
tags:
- utility
text: 'Effect: You have an intuitive grasp of magnetic fields, ocean currents, wind
  direction, and clouds. Skill Substitution: You may use Intuition (INT) + [[Piloting]]
  instead of Education + Piloting for relevant identifications. Typical Difficulty:
  For reading ocean currents, wind direction, and clouds, this is usually a Piloting
  identification at Difficulty Value 15. Limits: This is a potion benefit; it cannot
  be stolen or recorded.'
```





- **Effect:** You have an intuitive grasp of magnetic fields, ocean currents, wind direction, and clouds.
- **Skill Substitution:** You may use **Intuition (INT) + [[Piloting]]** instead of **Education + Piloting** for relevant identifications.
- **Typical Difficulty:** For reading ocean currents, wind direction, and clouds, this is usually a **Piloting** identification at **Difficulty Value 15**.
- **Limits:** This is a potion benefit; it cannot be stolen or recorded.

### Ocean Blessed

```yaml ability
id: tyrant-seq-07-ocean-blessed
name: Ocean Blessed
pathway: tyrant
sequence: 7
status: canonical
type: passive
action: none
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
text: 'Effect: You are a higher-ranked Blessed One of the ocean and gain all-round
  improvement at sea. Limits (Environment): This is passive and only applies in an
  [[Ocean Environment]]. Bonuses (while applicable): All attributes +1. Skill identifications
  and attribute identifications gain a +2 bonus.'
```





- **Effect:** You are a higher-ranked Blessed One of the ocean and gain all-round improvement at sea.
- **Limits (Environment):** This is passive and only applies in an [[Ocean Environment]].
- **Bonuses (while applicable):**
  - All attributes +1.
  - Skill identifications and attribute identifications gain a +2 bonus.

> **GM Note:** The GM defines what counts as a “marine environment.” Indoor swimming pools generally do not; vast lakes barely do. Do not allow arguments like “there are water molecules in the air, so it counts.”

- **Limits:** As described in this section's prose.


## Water Spells

### Washing

- **Cost:** 1 point of [[Spirituality]].
- **Use:** 1 spellcasting action.
- **Effect:** The area you wipe is immediately cleaned; corresponding stains are removed and it looks brand new.

### Create Huge Wave

- **Cost:** 3 points of Spirituality.
- **Use:** 1 spellcasting action.
- **Targeting and range:** Choose 1 target; up to 3 targets standing together are considered the same target.
- **Effect:** Make an **Intuition (INT) + Navigator** check against the target’s [[Physical Defense]]. On success, deal **3d6 physical damage**.
- **Scaling:** For every Sequence you upgrade, this spell’s physical damage increases by **+1d6**. The wave’s volume is at most equal to the height of the cabin.
- **Aftereffects:** Targets affected by this spell fall into a [[Wet State]].

### Manipulation of Water

- **Cost:** 2 points of Spirituality.
- **Use:** 1 spellcasting action.
- **Effect:** You shape a body of water out of thin air, or shape an existing body of water into the form you want.

1) **Make Clean Water:** You can create a pot of clean, drinkable water (as desired).
2) **Water Body Shaping:** You can shape any body of water within 10 meters into the shape you want, but it cannot be used as a weapon.
3) **Create Water Body (Lubrication):** Affecting something you touch, you create a layer of water at a designated position. This can create lubrication:
   - Pushing-object identification gains a +2 bonus.
   - The distance of pushing is halved.
   - This also applies to lifting/upward movement (distance is halved).
4) **Collapsing Waves:** You can make waves (not of super-large volume) collapse into short-term pouring rain.
5) **Other Reasonable Uses:** The lubrication can also force others to make an **Agility (DEX)** identification at **Difficulty Value 15** or lose their balance on it. Catching the opponent may require fighting against Physical Defense.

- **Aftereffects:** Creatures affected by this spell (including via lubrication effects) fall into a [[Wet State]].

### Water Body Healing

- **Cost:** 3 points of Spirituality.
- **Use:** 1 spellcasting action.
- **Targeting and range:** Choose 1 target.
- **Effect:** Choose **one** of the following:

1) **Emergency Treatment:** Only for minor injuries. Create a water film on the wound; the wound is considered to have received medical treatment.
2) **Speed Up Recovery:** Speeds recovery of minor injuries by halving the time required for natural physical recovery (round up).  
   - For moderate injuries: can only speed up **half an hour**.  
   - For serious injuries: basically invalid.  
   - Can only guarantee a +1 benefit to **Physical Fitness** identification.
3) **Enhanced Benefits (per ②):** If there are minor injuries and “slander” injuries requiring Physical Fitness appraisal, provide +3 and +2 benefits respectively.

- See [[Recovery of Spirituality and Other States]] for the definitions of trauma recovery and minor injury, “slander,” and serious injury.

### Deep Sea Film

- **Cost:** 2 points of Spirituality.
- **Use:** 1 spellcasting action.
- **Targeting and range:** Choose 1 target.
- **Effect:** Create a layer of water film that covers the body surface (or forms into a ball), granting:

1) While covered, the target is isolated from environmental influences other than temperature, and will not be corroded by stepping into substances such as acid—unless the substance layer is more than 1 meter thick.
2) The water film grants the same underwater action effect as your [[Phantom Scale]], and does not stack with it (making it especially effective for others).
3) If a creature is voluntary or helpless, the water film can wrap around its head, gradually reducing the air inside. After 1 round, it begins suffocating and loses **1d6 hit points per round**.

### Corrosive Rain

- **Cost:** 3 points of Spirituality.
- **Use:** 1 spellcasting action.
- **Targeting and range:** Choose a 10-meter area.
- **Effect:** Make a **d20 + 15** identification using a [[Disaster Bonus]]. This resists the Physical Defense of all creatures in the area. Creatures that fail take **2d6 poison damage** (double damage to spider webs, plants, and hair).
- **Sequence Scaling:**
  - At [[id:alias-sequence-6|Sequence 6]], poison damage increases by +1d6.
  - At [[Sequence 5]], the Disaster bonus becomes +20.
- **Aftereffects:** Creatures affected by this spell fall into a [[Wet State]].

### Other Water Spells

- Other GM-approved reasonable water spells may exist.
- **Rule Note:** The **water film** created by spells is **not** considered a wet state. However, **Corrosive Rain**, **Manipulation of Water**, and **Create Huge Wave** cause affected enemies to fall into a [[Wet State]].
