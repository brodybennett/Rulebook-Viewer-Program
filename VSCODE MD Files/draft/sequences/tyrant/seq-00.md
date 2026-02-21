---
title: 'Sequence 0: Tyrant'
id: tyrant-seq-00
tags:
- pathway:tyrant
- sequence:0
---






# Tyrant Pathway: Sequence 0

## Tyrant

- See also: Sequence

> **Lore:** This **Sequence** represents dominion over lightning, oceans, fear, and large-scale natural catastrophe.

## Advancement

### Advancement Ritual

- **Advancement Ritual:**  
  - Hundreds of thousands of followers who obey you and hold fear-based faith are required.  
  - You must challenge a true god alone and survive.  
  - You consume the potion within an atmosphere of fear and obedience.  
  - The core requirement is the courage to challenge the gods while bearing massive fear and obedience.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2, Charisma +1.

---

### Celestial Thunder

```yaml ability
id: tyrant-seq-00-celestial-thunder
name: Celestial Thunder
pathway: tyrant
sequence: 0
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
  damage_roll: 1d10
  heal_roll: null
  effect_roll: "1"
  notes: Bonus lightning damage applies to all lightning abilities; Yi Lei Wan Tang splash damage uses Lightning Storm resolution.
scaling: []
damage_types:
- lightning
tags:
- buff
- defense
- offense
text: 'Effect: You can create planet-level violent lightning waves. All lightning-related
  abilities you use deal +1d10 lightning damage. This bonus is calculated separately
  and also increases the base 5d6 lightning damage of your lightning abilities. When
  you use [[Yi Lei Wan Tang]], although it requires a single primary body as the main
  target, you also deal significant damage each round to other nearby creatures besides
  the main target. This additional damage is treated as damage from [[Lightning Storm]].
  This secondary damage benefits from Celestial Thunders bonus damage and is resolved
  using the same Disaster Attack procedure as Lightning Storm (check vs Physical Defense).
  Targeting and rang...'
```





- **Effect:**  
  - You can create planet-level violent lightning waves.  
  - All lightning-related abilities you use deal **+1d10 lightning damage**. This bonus is calculated separately and also increases the base 5d6 lightning damage of your lightning abilities.  
  - When you use [[Yi Lei Wan Tang]], although it requires a single primary body as the main target, you also deal significant damage each round to other nearby creatures besides the main target. This additional damage is treated as damage from [[Lightning Storm]].  
  - This secondary damage benefits from **Celestial Thunder**’s bonus damage and is resolved using the same Disaster Attack procedure as **Lightning Storm** (check vs Physical Defense).  

- **Targeting and range:**  
  - Within 100 meters of any lightning you create, a powerful electromagnetic storm accompanies it, destroying all information structures.  
  - Informational creatures of the Hermit pathway cannot avoid your lightning damage.  
  - Your lightning can cover the entire world. If you choose, you can keep a planet continuously filled with your lightning storms.

---

- **Limits:** As described in this section's prose.


### Sweeping Tides

```yaml ability
id: tyrant-seq-00-sweeping-tides
name: Sweeping Tides
pathway: tyrant
sequence: 0
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
  damage_roll: 1d10
  heal_roll: null
  effect_roll: "1"
  notes: Bonus water damage applies to all water-related abilities.
scaling: []
tags:
- buff
- offense
text: 'Effect: You can create waves capable of flooding a planet. All your water-related
  damage is increased by +1d10, and the upper damage limit is greatly increased. You
  can use ocean-related abilities (such as waves) to submerge all land on a planet,
  turning it into a world consisting only of oceans. --'
```





- **Effect:**  
  - You can create waves capable of flooding a planet.  
  - All your water-related damage is increased by **+1d10**, and the upper damage limit is greatly increased.  
  - You can use ocean-related abilities (such as waves) to submerge all land on a planet, turning it into a world consisting only of oceans.

---

- **Limits:** As described in this section's prose.


### Tyrant

```yaml ability
id: tyrant-seq-00-tyrant
name: Tyrant
pathway: tyrant
sequence: 0
status: canonical
type: active
action: free
cost: {}
roll: 1d20 + @attr.str
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.str
  damage_roll: 1d10
  heal_roll: null
  effect_roll: null
  notes: Bonus damage applies versus targets one Sequence lower; Frightening Authority uses Strength vs Willpower Defense to inflict Terrified.
scaling: []
tags:
- defense
- offense
text: 'Effect: You absolutely suppress targets below your level. When facing an enemy
  whose Sequence is one level lower than yours: Your physical defense, Constitution
  Defense, and Will defense are +5. Your damage check gains an additional +1d10. Use:
  Once per turn, as a free action. Effect (Frightening Authority): Make a Strength
  check against the targets Willpower Defense.'
```





- **Effect:**  
  - You absolutely suppress targets below your level.  
  - When facing an enemy whose **Sequence** is one level lower than yours:  
    - Your physical defense, Constitution Defense, and Will defense are **+5**.  
    - Your damage check gains an additional **+1d10**.  

- **Use:** Once per turn, as a free action.  

- **Effect (Frightening Authority):**  
  - Make a Strength check against the target’s Willpower Defense.  
  - On a success, the target enters a [[Terrified State]] that lasts for the entire encounter.

- **Limits:** As described in this section's prose.
