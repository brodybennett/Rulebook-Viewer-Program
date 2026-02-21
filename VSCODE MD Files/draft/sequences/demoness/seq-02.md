---
title: 'Sequence 2: Catastrophe'
id: demoness-seq-02
tags:
- pathway:demoness
- sequence:2
---






# Demoness Pathway: Sequence 2

## Catastrophe

> **Lore:** Blizzards, floods, tsunamis, and earthquakes are all within her domain.

- See also: [[Demoness]]

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Proactively trigger a disaster that can destroy a city-state. In the process of causing the death of civilians, it also causes serious damage and far-reaching effects to local buildings and various facilities. In the center or final ruins of this disaster, take the [[Potion]].
  > **GM Note:** Marked as an “unofficial ceremony” in the source text.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Agility (DEX) +2, Constitution +1, Strength +1, Charisma (CHA) +1.

### Cataclysm Wreaks

```yaml ability
id: demoness-seq-02-cataclysm-wreaks
name: Cataclysm Wreaks
pathway: demoness
sequence: 2
status: adapted
type: active
action: cast
cost:
  spirituality: 6
roll: 1d20 + @attr.cha + @skill.charisma
opposed_by: physical_defense
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.cha + @skill.charisma
  damage_roll: 5d6
  heal_roll: null
  effect_roll: null
  notes: Baseline mapping uses the explicit Charisma vs Physical Defense resolution; disaster-specific damage rolls are in scaling.
scaling:
- when: hurricane_mode
  changes:
    effect_roll: 2d10
    effect_note: Targets failing Strength or Agility Difficulty Value 20 checks can take 2d10 falling damage.
- when: earthquake_mode
  changes:
    damage_roll: 5d6 + 5
- when: tsunami_mode
  changes:
    damage_roll: 10d6
- when: lava_mode
  changes:
    damage_roll: 5d6
- when: thunderstorm_mode
  changes:
    damage_roll: 5d6
- when: thunderstorm_mode_vs_undead
  changes:
    damage_roll: 6d6
- when: blizzard_mode
  changes:
    damage_roll: 3d6
- when: meteorite_mode
  changes:
    damage_roll: 10d6
- when: heavy_rain_mode
  changes:
    damage_roll: null
    effect_note: Heavy rain primarily changes terrain/visibility instead of dealing direct damage.
damage_types:
- physical
tags:
- ritual
- mobility
- defense
- offense
- social
text: 'You create a terrible catastrophe. Cost: 6 spiritual points ([[Spirituality]])
  Use: 1 Casting Action (Casting Action); 1 time per round; once per encounter Effect:
  Choose 1 disaster to take effect. Charisma checks counter Physical Defense ([[Physical
  Defense]]), and can affect areas of a city. Disaster options: Hurricane: Strong
  winds ravage an area. If you fail a Strength or Agility (DEX) check with Difficulty
  Value 20 (Difficulty Value), most of the trees, animals, and humans in the area
  are in a Blowing state ([[Blowing]]). The wind moves 50 meters, and affected creatures
  may take 2d10 falling damage as a result. Earthquake: Against Physical Defense,
  dealing 5d6+5 physical damage to mo...'
```





You create a terrible catastrophe.

- **Cost:** 6 **spiritual points** ([[Spirituality]])
- **Use:** 1 **Casting Action** (Casting Action); 1 time per round; once per encounter
- **Effect:** Choose 1 disaster to take effect. **Charisma** checks counter **Physical Defense** ([[Physical Defense]]), and can affect areas of a city.
- **Disaster options:**
  - **Hurricane:** Strong winds ravage an area. If you fail a Strength or Agility (DEX) check with **Difficulty Value** 20 (Difficulty Value), most of the trees, animals, and humans in the area are in a **Blowing** state ([[Blowing]]). The wind moves 50 meters, and affected creatures may take 2d10 falling damage as a result.
  - **Earthquake:** Against **Physical Defense**, dealing 5d6+5 physical damage to most creatures on the ground; these creatures are in a **Loss of Balance** state ([[Loss of Balance]]).
  - **Tsunami:** Can only be used in the sea area. You release huge waves, advancing 2 kilometers at a speed of 100 meters per round, submerging all ships on the way, and causing a lot of damage (10d6).
  - **Lava:** Works only on land. The ground begins to erupt lava, dealing 5d6 fire damage to most creatures.
  - **Heavy rain:** The sky begins to rain heavily; after a few minutes, this place is regarded as a [[Body of Water]], and you can’t see your fingers in the heavy rain.
  - **Thunderstorm:** Deals 5d6 lightning damage to most creatures, rising to 6d6 for [[Undead]].
  - **Blizzard:** Deals 3d6 cold damage to most creatures, and you can’t see your fingers in the blizzard.
  - **Meteorite:** The meteorite bombards the ground, causing 10d6 physical damage to everyone present.

- **Limits:** As described in this section's prose.
