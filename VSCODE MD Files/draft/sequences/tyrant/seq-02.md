---
title: 'Sequence 2: Cataclysm Interrer'
id: tyrant-seq-02
tags:
- pathway:tyrant
- sequence:2
---






# Tyrant Pathway: Sequence 2

## Cataclysm Interrer

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Contend against a real scourge and defeat it in its own right (unofficial rite).  
  [[Scourge]]

---

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2.  
- Increase one chosen skill by 1 level.

---

### Avatar of Scourge

```yaml ability
id: tyrant-seq-02-avatar-of-scourge
name: Avatar of Scourge
pathway: tyrant
sequence: 2
status: canonical
type: active
action: cast
cost:
  spirituality: 10
roll: null
opposed_by: physical_defense
range: All natural disasters affect a minimum area of **1 kilometer** and may extend
  up to **one country** in scope.
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
- defense
- offense
text: 'Cost: 10 Spirituality. [[Spirituality]] Use: 1/round, 1 Casting Action. Effect:
  Choose one natural disaster; it manifests as a real, large-scale disaster as if
  natural. You gain +25 to Disaster Attack rolls against physical defenses. [[Disaster
  Attack]] Targeting and Range: All natural disasters affect a minimum area of 1 kilometer
  and may extend up to one country in scope. Limits: The scope is typically too large
  to confine to a small area; using this ability may devastate an entire port city
  or larger region. Interaction: Each Scourge-type disaster is a separate ability.
  [[Steal]] and [[Record]] can affect only one such disaster ability at a time.'
```





- **Cost:** 10 Spirituality.  
  [[Spirituality]]
- **Use:** 1/round, 1 Casting Action.
- **Effect:** Choose one natural disaster; it manifests as a real, large-scale disaster as if natural. You gain **+25** to **Disaster Attack** rolls against physical defenses.  
  [[Disaster Attack]]
- **Targeting and Range:** All natural disasters affect a minimum area of **1 kilometer** and may extend up to **one country** in scope.
- **Limits:** The scope is typically too large to confine to a small area; using this ability may devastate an entire port city or larger region.
- **Interaction:** Each Scourge-type disaster is a separate ability. [[Steal]] and [[Record]] can affect only one such disaster ability at a time.
- **Disaster Options:**

#### 1. Volcanic Eruption

- At the start of each round, a disaster assessment occurs: all targets on the ground take **5d6 fire damage** and **2d6 physical damage**.
- **Secondary Effects (if a volcano is within the affected range):**

  - **Volcanic Ash**
    - Ash cloud expands from the crater at **0.5 km per round**, up to **100 m** high.
    - Area becomes a volcanic ash environment.
    - Creatures inside suffer **4d6 fire damage/round**, **1d6 poison damage/round**, and are **Blinded**, disoriented, and effectively trapped.  
      [[Blinded]]

  - **Magma**
    - Magma advances at **5 m/round**.
    - Ground becomes a magma environment.
    - On contact: **3d6 fire damage** immediately; then **2d6 fire damage/round**.
    - Normal human limbs dissolve rapidly; creatures become bound when magma solidifies.

  - **Earthquake**
    - Equivalent to a raging disaster earthquake effect.  
      [[id:alias-earthquake|Earthquake]]

  - **Tsunami**
    - Equivalent to a raging disaster tsunami affecting surrounding seas and coastal areas.  
      [[id:alias-tsunami|Tsunami]]

---

#### 2. Meteorite Rain

- Each round, roll **1d3** to determine how many meteorites directly threaten the immediate area.
- Each meteorite deals **6d10 damage** against physical defense.
- Targets unable to avoid the impact take **half damage** even if the disaster attack roll fails.
- In fiction, tens of thousands of meteorites fall nearby (within ~100 m), but only the rolled ones directly threaten creatures.
- After about **5 minutes**, the affected region becomes a blazing disaster zone, often reduced to flames or ruins.

---

#### 3. Typhoon

- Creatures and debris are drawn toward the typhoon.
- Each round: **1d6 physical damage** and forced movement **50 m toward the typhoon**.
- Avoid forced movement with a **Agility (DEX) check (Difficulty Value 20)**.  
  Difficulty Value
- **Additional Effect — Heavy Rain:** Cities near or within the typhoon experience continuous heavy rain equivalent to a disaster-level rainfall.

---

#### 4. Great Rift Valley

- Created alongside a catastrophic earthquake effect.
- Forms a massive rift spanning kilometers; nearby buildings and creatures fall toward it.
- On creation, creatures must make a **Agility (DEX) check (Difficulty Value 20)** or fall.
- **Warning:** The rift may connect to the **Chaos Sea**.  
  [[Chaos Sea]]
  - Beyonders not of the Moon, Earth, Alien, Abyss, Judge, Black Emperor, or Extraterrestrial-related pathways suffer underground pollution when approaching and have a strong tendency toward personality splitting.  
    [[Underground Pollution]]

---

#### 5. Severe Winter

- Within **5 minutes**, the area is covered by hail, snow, and blizzard conditions.
- Non-demigod creatures without cold resistance rapidly suffer hypothermia and die.
- Creatures in the area take **2d6 cold damage/round** and a **–2 penalty to all checks**; these stack with blizzard effects.  
  [[Blizzard]]
- Avalanches may occur, dealing **5d6 cold damage**.
- When mobs near mountains catastrophically fail checks, an avalanche triggers immediately.
- If the winter lasts **3 days**, most life and objects freeze; the region’s sea and ecology become Antarctic-like for an epoch.

---

#### 6. Drought

- Winter effects are gradually nullified; Winter’s full effects are halved.
- Snow stops accumulating and melts; when all snow is gone, Winter ends.
- Plants die rapidly; plant-based abilities from non-homologous land Pathways cannot be activated here.
- Water evaporates quickly; related water abilities cannot be used.
- Creatures without fire resistance suffer a **parched state**.  
  [[Parched]]
- Creatures below demigod level die quickly from dehydration.
- Demigods and above take a **–4 penalty to all checks** due to exhaustion and dehydration.

---

#### 7. Sandstorm

- Sun and moonlight–based summoning effects do not function.
- Visibility drops to zero; creatures are effectively **Blinded**.
- Flying units unable to determine direction fall; those that can have movement halved.

---

#### Other Disasters

- Other natural disasters may be allowed by the GM.  
  [[GM]]
- Man-made disasters (e.g., smog) are excluded.

---

### Summon Meteor

```yaml ability
id: tyrant-seq-02-summon-meteor
name: Summon Meteor
pathway: tyrant
sequence: 2
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + 20
opposed_by: physical_defense
range: Area from **100 m to 1 km** radius.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + 20
  damage_roll: 5d6 + 5d6
  heal_roll: null
  effect_roll: null
  notes: On success, deal 5d6 fire and 5d6 physical damage; on failure, creatures unable to leave still take half damage.
scaling: []
damage_types:
- physical
- fire
tags:
- ritual
- defense
- offense
text: 'Cost: 3 Spirituality. Use: 1 Casting Action. Targeting and Range: Area from
  100 m to 1 km radius. Effect: A single meteor strikes the area. You gain +20 on
  the disaster check against physical defense. [[Disaster Check]] On success: all
  creatures take 5d6 fire damage and 5d6 physical damage. On failure: creatures unable
  to leave the area still take half damage. Aftereffects: Can destroy a ship, building,
  or city block; leaves a large crater.'
```





- **Cost:** 3 Spirituality.
- **Use:** 1 Casting Action.
- **Targeting and Range:** Area from **100 m to 1 km** radius.
- **Effect:** A single meteor strikes the area. You gain **+20** on the disaster check against physical defense.  
  [[Disaster Check]]
  - On success: all creatures take **5d6 fire damage** and **5d6 physical damage**.
  - On failure: creatures unable to leave the area still take **half damage**.
- **Aftereffects:** Can destroy a ship, building, or city block; leaves a large crater.
- **Special:** Extremely rare circumstances may bring spiritual materials from extraterrestrial Pathways; usually destroyed on impact and cannot be triggered by simple success or failure.

---

- **Limits:** As described in this section's prose.


### Humanoid Scourge

```yaml ability
id: tyrant-seq-02-humanoid-scourge
name: Humanoid Scourge
pathway: tyrant
sequence: 2
status: canonical
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 2d6
  heal_roll: null
  effect_roll: "1"
  notes: Once per round, either negate disaster damage or add +2d6 to one disaster damage roll.
scaling: []
tags:
- buff
- defense
- offense
text: 'Use: 1/round, free action. Effect (Defense): When a disaster or natural disaster
  would damage you, you may use your disaster authority to avoid the damage entirely.
  Effect (Offense): Alternatively, add +2d6 to a single disaster or natural disaster
  damage roll. Limits: Damage increase and damage avoidance share the same usage.'
```





- **Use:** 1/round, free action.
- **Effect (Defense):** When a disaster or natural disaster would damage you, you may use your disaster authority to avoid the damage entirely.
- **Effect (Offense):** Alternatively, add **+2d6** to a single disaster or natural disaster damage roll.
- **Limits:** Damage increase and damage avoidance share the same usage.

- **Effect:** Humanoid Scourge resolves using its yaml ability block and section prose.
