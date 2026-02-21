---
title: 'Sequence 4: Calamity Priest'
id: tyrant-seq-04
tags:
- pathway:tyrant
- sequence:4
---






# Tyrant Pathway: Sequence 4

## Calamity Priest

## Advancement

### Advancement Ritual

- **Advancement Ritual:** The ritual must be performed in the midst of an active natural disaster environment capable of producing earthquakes and tsunamis. The potion must be consumed and endured in this environment until the ritual concludes.  
[[Advancement Rituals]]

---

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1.  
- Increase one skill of your choice by 1 level.

---

### Earth Manipulation

```yaml ability
id: tyrant-seq-04-earth-manipulation
name: Earth Manipulation
pathway: tyrant
sequence: 4
status: canonical
type: active
action: free
cost:
  vitality: 20
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
- defense
text: 'Use: Free action, once per turn (choose one option). Effect: You shape earth
  and terrain. Choose one benefit: Raise or lower the ground by up to 10 meters. Dig
  passages through earth at your movement speed. Create an Earth Wall: Defense: 20
  Vitality: 25'
```





- **Use:** Free action, once per turn (choose one option).
- **Effect:** You shape earth and terrain.

Choose one benefit:

- Raise or lower the ground by up to 10 meters.
- Dig passages through earth at your movement speed.
- Create an **Earth Wall**:
  - Defense: 20  
  - Vitality: 25  
  - If damage exceeding the wall’s remaining Vitality is dealt, excess damage may affect creatures hiding behind it.  
  - Resolve spillover using the same attack Identification that hit the wall; excess damage applies to one creature directly behind it.

[[Cover]]
[[Terrain]]

---

- **Limits:** As described in this section's prose.


### Rock Tide Stomp

```yaml ability
id: tyrant-seq-04-rock-tide-stomp
name: Rock Tide Stomp
pathway: tyrant
sequence: 4
status: canonical
type: active
action: attack
cost: {}
roll: 1d20 + 20
opposed_by: physical_defense
range: All targets within 10100 meters (excluding you).
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + 20
  damage_roll: 5d6 + 2d6
  heal_roll: null
  effect_roll: null
  notes: On success, magma eruption deals 5d6 fire and 2d6 physical damage; fire damage is halved on the seabed.
scaling: []
tags:
- defense
- offense
text: 'Use: Attack Action. Targeting and Range: All targets within 10100 meters (excluding
  you). Effect: You stomp, cracking the ground and triggering a magma eruption. Make
  a Disaster Attack with +20 [[Disaster Attack]] against each targets Physical Defense.
  On success, magma erupts: 5d6 fire area damage 2d6 physical damage Limits: Only
  functions on ground or seabed.'
```





- **Use:** Attack Action.
- **Targeting and Range:** All targets within 10–100 meters (excluding you).
- **Effect:** You stomp, cracking the ground and triggering a magma eruption.
  - Make a **Disaster Attack** with +20 [[Disaster Attack]] against each target’s Physical Defense.
  - On success, magma erupts:
    - 5d6 fire area damage  
    - 2d6 physical damage  
- **Limits:** Only functions on ground or seabed.
- **Aftereffects:** Fire damage is halved when used on the seabed.


---

## Disaster Linkage Rules (“Final Disaster”)

If multiple different disasters occur simultaneously in the same area, their damage is doubled.

- This is not an Extraordinary Ability.
- It is an environmental disaster interaction rule.
- It cannot be simulated or stolen.
- Any pathway involving disasters may trigger these linkages as a special judgment.

### Non-Stacking Clause

Repeated benefit descriptions from different disaster sources do not stack.

> Example: If lightning gains bonus damage to wet targets in multiple rules, that bonus applies only once.

---

### Disaster Linkage Effects

#### Tornado

Linked with: Tsunami, Lava, Rainstorm, Blizzard.

- Tornado deals 1d6 physical damage per round to affected targets.
- This damage represents objects carried by other disasters.

#### Earthquake

Linked with: Lava, Tsunami, Rainstorm.

- With Lava: Lava damage increases by 1d6.
- With Tsunami or Rainstorm: Creates a persistent **Undercurrent**.

**Undercurrent Rules**

- Moving in affected water requires a Difficulty 15 Luck check.
- On failure, the creature is pulled underwater.
- Each round underwater, make:
  - Difficulty 15 Agility (DEX) check **or**
  - Difficulty 20 Swimming check  
  to escape.
- While trapped:
  - No movement actions.
  - Surface targets are usually out of attack range.
- After 3 rounds:
  - Demigod or lower creatures begin suffocating:
    - –2 to all checks
    - Lose 1d6 Vitality per round until escape or death.

[[Suffocation]]
[[Conditions]]

#### Tsunami

Linked with: Lava, Thunderstorm.

- With Lava:
  - Lava fire damage is halved.
  - High-temperature gas forms.
  - On a critical failure while in the lava’s area:
    - Inhale toxic gas → take 1d6 poison damage.
- With Thunderstorm:
  - All affected creatures gain the **Wet** state.
  - Wet targets take +1d6 lightning damage.

[[Wet State]]

#### Rainstorm

Linked with: Lava, Thunderstorm.

- On land: Lava damage reduced by 2d6.
- In water: Lava damage halved.
- Thunderstorm linkage: Same Wet interaction as above.

#### Lava

Linked with: Blizzard and other listed disasters.

- With Blizzard:
  - Blizzard cold damage reduced by 2d6.
  - No identification penalty; blindness effect still applies.
  - Lava damage reduced by 1d6.

---

### Large-Scale Disaster Bonus Rule

Only applies to disasters whose affected area is measured in kilometers.

- If two different disaster types affect the field:
  - At the start of each round, affected targets take +1d6 disaster damage.
- For each additional different disaster type beyond two:
  - Bonus increases by +1d6.

> **Lore:** Large disasters persist longer and are more chaotic, increasing destructive synergy.

---

## Cataclysm Wreaks

You create a major disaster.

- **Use:** 1 Casting Action, once per round.
- **Cost:** 6 Spirituality.  
[[Spirituality]]
- **Targeting:** Minimum area: a hall. Maximum: several-kilometer radius.
- **Effect:** Choose one disaster type below.
  - Make a +20 Disaster Attack vs Physical Defense.
- **Duration:** Kilometer-scale disasters last at least 1 hour.
- **Limits:** Small-scale disasters usually cannot coexist; if they do, use Disaster Linkage Rules.
- Each disaster type is an independent ability for purposes of theft or copying effects.

[[Theft Abilities]]

---

### Tornado

- Failing a Difficulty 20 Strength or Agility (DEX) check:
  - Creature is in **Blown State** for 3 rounds (cannot move).
  - Wind shifts 50 m; may suffer 2d6 falling damage.

[[Falling Damage]]

---

### Earthquake

- Causes severe geological destruction.
- Deals 5d6 physical damage to most ground creatures; they are knocked off balance.
- Small-scale quake may form a large crater.
- Tremors detectable beyond 1 km.

---

### Tsunami

- Sea areas only.
- Waves advance 2 km at 100 m/round.
- Subside after 5 minutes.
- Damage: 10d6.

---

### Lava

- Land or seabed only.
- Magma erupts and floods terrain.
- Damage: 4d6 fire + 1d6 physical.
- Lava later solidifies.

---

### Torrential Rain

- Lasts 5 minutes.
- Unsheltered creatures become **Wet**.
- Wet creatures take +1d6 lightning damage.
- Area becomes a water region:
  - Water depth: 2 m above ground.
  - Movement Power –5.
- Creatures are visually impaired:
  - –4 Perception.
  - Not considered fully Blind.

[[Movement Power]]

---

### Thunderstorm

- Deals 5d6 lightning damage to most creatures.
- Ignores Physical Defense from Agility (DEX) or Dodge.
- Counts as 3 separate attacks (consume 3 substitutes; apply reduction separately for each).
- Damage vs undead: 6d6.
- If cast during heavy rain: counts as 5 attacks.


---

### Blizzard

- Deals 3d6 cold damage.
- Visibility near zero.
- Creatures without cold resistance:
  - –2 to all checks.
  - Considered Blind.
- When cast, choose wind direction:
  - With wind: Movement Power +50%.
  - Against wind: Movement Power halved.

---

> **GM Note:** Disasters should remain natural phenomena; artificial disasters (e.g., smog) are generally excluded.

---

> **Lore:** Cataclysms reshape terrain and climate, with effects varying by environment.
