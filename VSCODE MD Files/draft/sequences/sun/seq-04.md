---
title: 'Sequence 4: Unshadowed'
id: sun-seq-04
tags:
- pathway:sun
- sequence:4
---






# Sun Pathway: Sequence 4

## Unshadowed

- You can purify depravity, filth, corrosion, darkness, evil, disease, and similar forces, causing them to dissipate quickly until nothing remains.
- Based on this principle, you can remove mental pollution within Extraordinary characteristics. [[Extraordinary Characteristics]]
- You repel contact with other magical items and Extraordinary characteristics, allowing Extraordinary characteristics to be separated out a little bit. [10] [[Magical Items]]

## Advancement

### Auxiliary Materials

- **Main Material:**
  - A drop of “Sun” blood. [[Sun Blood]]
  - *Or instead:* three feathers of an adult sun bird **and** a piece of sacred brilliance stone. [[Adult Sun Bird Feathers]] [[Sacred Brilliance Stone]]
- **Auxiliary Materials:**
  - 60 ml blood of the sun god bird. [[Sun God Bird Blood]]
  - 30 ml associated liquid of the sacred glow stone. [[Sacred Glow Stone Liquid]]
  - 7 drops mutated golden hand orange juice. [[Mutated Golden Hand Orange Juice]]
  - 10 g magma heart powder. [[Magma Heart Powder]]

### Advancement Ritual

- **Advancement Ritual:** Strip out the strongest and least willing to give up emotions, then take the potion, and infuse these emotions back in the process. [11] [[Advancement Rituals]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Agility (DEX) +1, Intuition (INT) +1, Constitution +1; Religion skill +1 level; Mysticism skill +1 level. [[Attributes]] [[Skills]]

### Darkness: Endless Light

```yaml ability
id: sun-seq-04-darkness-endless-light
name: 'Darkness: Endless Light'
pathway: sun
sequence: 4
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
  effect_roll: 1d5
  notes: Damage components from curses, cold, toxins, and acids are each reduced to 1d5.
scaling: []
tags:
- detection
- debuff
- buff
- offense
text: 'Use: 1 Swift Action. Swift Action Effect: Endless light dispels all pollution.
  There will be no shadows within your vision and the surrounding range. [[Realm of
  No Darkness]] The negative effects brought by curses, cold, toxins, and acids cannot
  be produced. [[Curses]] [[Toxins]] Damage from curses, cold, toxins, and acids can
  still be caused, but each separately-calculated damage component becomes 1d5. Example:
  2d6 + 2d6 becomes 1d5 + 1d5. The increased damage of each Sequence level is calculated
  independently (not combined into a single die pool). Example: Witchs Black Flame
  is 3d6, plus +1d6 at Sequence 6 and +1d6 at Sequence 5, so it is 3d6 + 1d6 + 1d6
  (not 5d6). Therefore, in the rea...'
```





- **Use:** 1 **Swift Action**. Swift Action
- **Effect:** Endless light dispels all pollution.
  - There will be no shadows within your vision and the surrounding range. [[Realm of No Darkness]]
  - The negative effects brought by curses, cold, toxins, and acids cannot be produced. [[Curses]] [[Toxins]]
  - Damage from curses, cold, toxins, and acids can still be caused, but each separately-calculated damage component becomes **1d5**.
    - Example: **2d6 + 2d6** becomes **1d5 + 1d5**.
    - The increased damage of each Sequence level is calculated independently (not combined into a single die pool).
      - Example: Witch’s Black Flame is **3d6**, plus **+1d6** at Sequence 6 and **+1d6** at Sequence 5, so it is **3d6 + 1d6 + 1d6** (not **5d6**). Therefore, in the realm of no darkness, Black Flame at Sequence 5 is **1d5 + 1d5 + 1d5**. [[Witch Black Flame]]
  - In the realm of no darkness, a creature cannot be dreamed, and an object cannot be concealed or invisible, except for psychological invisibility. [[Dreaming]] [[Invisibility]]
    - Psychological invisibility cannot cause sanity damage. [[Sanity / Rationality Damage]]
  - Otherwise, the scene is always regarded as daytime.

- **Sequence 3:** The range expands to a radius of 1 kilometer. You may create a boundary barrier that blocks holy attacks from outside if they are lower than your Sequence level. You can still target creatures inside the barrier with your own abilities, and the barrier can interact with the “Dark Realm” barrier normally. [[Holy Attacks]] [[Dark Realm]]

- **Limits:** As described in this section's prose.


### Spear of Darkness

```yaml ability
id: sun-seq-04-spear-of-darkness
name: Spear of Darkness
pathway: sun
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose 1 target; use **Mysticism** to attack the targets **Physical Defense**.
  [[Mysticism]] [[Physical Defense]]
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 5d6 + 8
  heal_roll: null
  effect_roll: null
  notes: On a failed attack, damage is halved.
scaling: []
damage_types:
- holy
tags:
- ritual
- defense
- offense
text: 'Cost: 5 points of Spirituality. [[Spirituality]] Use: 1 Casting Action. Casting
  Action Targeting and range: Choose 1 target; use Mysticism to attack the targets
  Physical Defense. [[Mysticism]] [[Physical Defense]] Effect: On a hit, deal 5d6+8
  holy damage. On a failed attack, the damage is halved. [[Holy Damage]] Additional
  effect: If this attack misses and hits the air, the entire night city enters a short
  day in an instant. Naming: Spear of Darkness, gun of darkness, and Spear of Radiance
  refer to this same ability.'
```





> **Lore:** You accumulate radiance into a spear of pure sunlight and throw it; it can expand into a miniature sun bright enough to illuminate a city.

- **Cost:** 5 points of **Spirituality**. [[Spirituality]]
- **Use:** 1 **Casting Action**. Casting Action
- **Targeting and range:** Choose 1 target; use **Mysticism** to attack the target’s **Physical Defense**. [[Mysticism]] [[Physical Defense]]
- **Effect:** On a hit, deal **5d6+8 holy damage**. On a failed attack, the damage is halved. [[Holy Damage]]
- **Additional effect:** If this attack misses and hits the air, the entire night city enters a short “day” in an instant.
  - **Naming:** “Spear of Darkness,” “gun of darkness,” and “Spear of Radiance” refer to this same ability.

> **Lore:** Along the flight path, it absorbs surrounding light, making the environment shift from bright to dim, dim to pitch-black, then release an intensely condensed white radiance like a miniature sun from the hit direction.

- **Limits:** As described in this section's prose.


### Yang Yan

```yaml ability
id: sun-seq-04-yang-yan
name: Yang Yan
pathway: sun
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 6
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Mysticism attacks all physical defenses in the field except the sun path. [[Sun]]
  [[Physical Defense]]
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 4d8 + 5
  heal_roll: null
  effect_roll: null
  notes: Choose holy or fire damage; half damage on failed attack.
scaling: []
damage_types:
- fire
- holy
tags:
- ritual
- defense
- offense
text: 'Cost: 6 points of Spirituality. [[Spirituality]] Use: 1 Casting Action. Casting
  Action Targeting and range: Mysticism attacks all physical defenses in the field
  except the sun path. [[Sun]] [[Physical Defense]] Effect: A huge pure light ball
  entwined with countless sacred flames emerges out of thin air, envelops enemies,
  and quickly melts themdealing 4d8+5 holy or fire damage, or half as much damage
  on failure. [[Fire Damage]] [[Holy Damage]] Notes: Choose holy or fire damage when
  you cast it. It can cause great damage to creatures in the filthy, corrupted, and
  undead domains, and can even directly destroy them. However, the attack range is
  large, and it is easy to accidentally injure one...'
```





> **Lore:** You open your arms halfway, as if embracing the gift of the gods.

- **Cost:** 6 points of **Spirituality**. [[Spirituality]]
- **Use:** 1 **Casting Action**. Casting Action
- **Targeting and range:** Mysticism attacks all physical defenses in the field except the sun path. [[Sun]] [[Physical Defense]]
- **Effect:** A huge pure light ball entwined with countless sacred flames emerges out of thin air, envelops enemies, and quickly melts them—dealing **4d8+5 holy or fire damage**, or half as much damage on failure. [[Fire Damage]] [[Holy Damage]]
- **Notes:** Choose **holy** or **fire** damage when you cast it. It can cause great damage to creatures in the “filthy,” “corrupted,” and “undead” domains, and can even directly destroy them. However, the attack range is large, and it is easy to accidentally injure one’s own side. Creatures of the [[Sun]] are exempt from the effect. [[Undead]]

- **Limits:** As described in this section's prose.


### Pure White Ray

```yaml ability
id: sun-seq-04-pure-white-ray
name: Pure White Ray
pathway: sun
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Select 1 target; **Occult** versus **Physical Defense**. [[Occult]] [[Physical
  Defense]]
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 3d6 + 3
  heal_roll: null
  effect_roll: null
  notes: "Alternate defense: resist Willpower Defense at -4 penalty and cost 5 spirituality."
scaling: []
damage_types:
- fire
- holy
tags:
- ritual
- buff
- defense
- offense
text: 'Cost: 3 points of Spirituality. [[Spirituality]] Use: 1 Casting Action (usable
  while physically bound). [[Physically Bound]] Casting Action Targeting and range:
  Select 1 target; Occult versus Physical Defense. [[Occult]] [[Physical Defense]]
  Effect: Deal 3d6+3 fire or holy damage. Alternate defense: This ability can be replaced
  with resist Willpower Defense, but your check takes a -4 penalty, and the Spirituality
  cost increases to 5 points. Willpower Defense'
```





> **Lore:** Light condenses into a scorching, dazzling ray.

- **Cost:** 3 points of **Spirituality**. [[Spirituality]]
- **Use:** 1 **Casting Action** (usable while physically bound). [[Physically Bound]] Casting Action
- **Targeting and range:** Select 1 target; **Occult** versus **Physical Defense**. [[Occult]] [[Physical Defense]]
- **Effect:** Deal **3d6+3 fire or holy damage**.
- **Alternate defense:** This ability can be replaced with resist **Willpower Defense**, but your check takes a **-4 penalty**, and the Spirituality cost increases to **5** points. Willpower Defense

- **Limits:** As described in this section's prose.


### Sacred Armor

```yaml ability
id: sun-seq-04-sacred-armor
name: Sacred Armor
pathway: sun
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 4
roll: null
opposed_by: none
range: self
target: self
duration: Lasts for one encounter. Encounter
dice:
  check_roll: null
  damage_roll: 2d6
  heal_roll: null
  effect_roll: "1"
  notes: Grants armor/DR; body touch against undead/fallen/dark deals 2d6 holy damage.
scaling: []
damage_types:
- holy
tags:
- ritual
- control
- buff
- defense
- offense
text: 'Cost: 4 points of Spirituality. [[Spirituality]] Use: 1 Casting Action. Casting
  Action Effect: You create an armor of light made of pure golden radiance. The armor
  has 5 Armor and 3 Damage Reduction (all damage reduction). [[Armor]] [[Damage Reduction]]
  Against attacks from the undead, fallen, and dark realms, the Armor increases to
  10 and Damage Reduction increases to 5. [[Undead]] [[Fallen]] [[Dark Realm]] The
  body touch of the undead, fallen, and dark realms will counteract 2d6 holy damage,
  without additional restraint. [[Holy Damage]] Duration: Lasts for one encounter.
  Encounter'
```





> **Lore:** A tide of pure golden light gushes from your body, condensing into armor.

- **Cost:** 4 points of **Spirituality**. [[Spirituality]]
- **Use:** 1 **Casting Action**. Casting Action
- **Effect:** You create an armor of light made of pure golden radiance.
  - The armor has **5 Armor** and **3 Damage Reduction** (all damage reduction). [[Armor]] [[Damage Reduction]]
  - Against attacks from the undead, fallen, and dark realms, the Armor increases to **10** and Damage Reduction increases to **5**. [[Undead]] [[Fallen]] [[Dark Realm]]
  - The body touch of the undead, fallen, and dark realms will counteract **2d6 holy damage**, without additional restraint. [[Holy Damage]]
- **Duration:** Lasts for one encounter. Encounter

- **Limits:** As described in this section's prose.


### Sunlight Interpretation

```yaml ability
id: sun-seq-04-sunlight-interpretation
name: Sunlight Interpretation
pathway: sun
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: The range is about a city.
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
- divination
- detection
text: 'Effect: You can sense whats happening near the sunlight you are in contact
  with. [[Sunlight Interpretation]] Targeting and range: The range is about a city.
  Limits: The perception picture of this ability can be affected by anti-divination.
  [[id:alias-anti-divination|Anti-Divination]]'
```





- **Effect:** You can sense what’s happening near the sunlight you are in contact with. [[Sunlight Interpretation]]
- **Targeting and range:** The range is about a city.
- **Limits:** The perception picture of this ability can be affected by anti-divination. [[id:alias-anti-divination|Anti-Divination]]
