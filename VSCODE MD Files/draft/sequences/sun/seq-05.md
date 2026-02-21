---
title: 'Sequence 5: Priest of Light'
id: sun-seq-05
tags:
- pathway:sun
- sequence:5
---






# Sun Pathway: Sequence 5

## Priest of Light

You master magic of the [[Sun Domain]] and can purify dead spirits and filthy creatures within a certain range, making you a natural nemesis of dead spirits. [9]

## Advancement

### Main Materials

- **Main Materials:** The red crown of the Rooster King of Dawn; a piece of pure white glow stone.

### Auxiliary Materials

- **Auxiliary Materials:** 5 grams of rosemary; 7 drops of golden hand orange juice; 10 ml of rock water; 60 ml of the blood of the King of Dawn Rooster.

### Advancement Ritual

- **Advancement Ritual:** In pure darkness, bury your whole body in ice that normally doesn’t melt, then take the potion.

> **Lore:** *(Unofficial)* The divine power at the time of promotion may cause the Beyonder to be purified or even “melted,” so counteractive darkness and ice are used to balance this holiness and scorching heat. Like Icarus flying to the sun, what matters is staying balanced—neither too high nor too low, neither too much nor too little.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1; Agility (DEX) +1; Intuition (INT) +1; Constitution +1.
- Occult skills can be quickly upgraded to master.

**Sun Spells:** You are greatly enhanced in the [[Sun Domain]]. You gain the following new Sun spells. Most are enhancements of previous abilities, but due to qualitative changes they are treated as separate abilities.

### Divine Light

```yaml ability
id: sun-seq-05-divine-light
name: Divine Light
pathway: sun
sequence: 5
status: canonical
type: active
action: cast
cost:
  spirituality: 4
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose 1 target within line of sight. People standing together are regarded
  as the same target.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 4d6 + 2d6
  heal_roll: null
  effect_roll: null
  notes: Ignores Agility (DEX) and Dodge; deals 4d6 holy and 2d6 fire damage.
scaling: []
damage_types:
- fire
- holy
tags:
- ritual
- control
- defense
- offense
text: 'You cause a pure, blazing, thick beam of light to fall from above out of thin
  air. Use: 1 Casting Action. Cost: 4 Spirituality. Targeting and range: Choose 1
  target within line of sight. People standing together are regarded as the same target.
  Resolution: Mysticism counters [[Physical Defense]]. This ignores Agility (DEX)
  and Dodge in physical defense. Effect: After the identification is successful, a
  pure and blazing beam descends directly, vaporizing the target and dealing 4d6 holy
  and 2d6 fire damage, enjoying the [[Restraint Effect]]. Special: Divine Light also
  has the scorching white visual effect associated with this ability.'
```





You cause a pure, blazing, thick beam of light to fall from above out of thin air.

- **Use:** 1 Casting Action.
- **Cost:** 4 **Spirituality**.
- **Targeting and range:** Choose 1 target within line of sight. People standing together are regarded as the same target.
- **Resolution:** Mysticism counters [[Physical Defense]]. This ignores Agility (DEX) and Dodge in physical defense.
- **Effect:** After the identification is successful, a pure and blazing beam descends directly, vaporizing the target and dealing **4d6 holy** and **2d6 fire** damage, enjoying the [[Restraint Effect]].
- **Special:** Divine Light also has the scorching white visual effect associated with this ability.

- **Limits:** As described in this section's prose.


### Purification Aura

```yaml ability
id: sun-seq-05-purification-aura
name: Purification Aura
pathway: sun
sequence: 5
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: Affects an area within 50 meters. You can precisely control which creatures
  are affected (including yourself).
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
conditions:
- fear
tags:
- ritual
- control
- debuff
- defense
text: 'Your halo-like effect dyes the surroundings golden, spreading outward layer
  by layer. Use: Swift Action; once per round. Cost: 2 Spirituality. Effect: Dye your
  surroundings golden, spreading outward, warming allies around you and bringing intense
  courage. This is not a continuous ability. Targeting and range: Affects an area
  within 50 meters. You can precisely control which creatures are affected (including
  yourself). Cleansing: Creatures in the aura clear the effects of fear, darkness,
  poison, cold, immortality, etc. (see [[Conditions]]). Resistance: Creatures in the
  aura gain 5 points of resistance to curse, cold, and poison for 3 rounds. Stacking:
  This cannot be superimposed with holy...'
```





Your halo-like effect dyes the surroundings golden, spreading outward layer by layer.

- **Use:** Swift Action; once per round.
- **Cost:** 2 **Spirituality**.
- **Effect:** Dye your surroundings golden, spreading outward, warming allies around you and bringing intense courage. This is not a continuous ability.
- **Targeting and range:** Affects an area within 50 meters. You can precisely control which creatures are affected (including yourself).
- **Cleansing:** Creatures in the aura clear the effects of fear, darkness, poison, cold, immortality, etc. (see [[Conditions]]).
- **Resistance:** Creatures in the aura gain 5 points of resistance to curse, cold, and poison for 3 rounds.
- **Stacking:** This cannot be superimposed with holy water and the [[Body of the Sun]].
- **Against dark/fallen/undead:** If there are dark, fallen, undead, and other creatures in range, and you intend not to let light surround them, then the occult resists [[Physical Defense]], ignores agility and evasion, and successfully deals holy damage equal to the restrained damage. You can decide whether they enjoy the benefits too.  
  - **Clarification:** If you choose to harm them, they do not receive the aura’s benefits; the restrained damage replaces the benefits for those creatures.

- **Limits:** As described in this section's prose.


### Holy Rain

```yaml ability
id: sun-seq-05-holy-rain
name: Holy Rain
pathway: sun
sequence: 5
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose an area no longer than 50 meters.
target: designated target(s)
duration: 5 rounds.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: Holy rain applies restrained damage each round to dark/corrupt/undead; normal creatures gain listed resistances.
scaling: []
conditions:
- restrained
damage_types:
- holy
tags:
- control
- debuff
- defense
- offense
text: 'You create a rain of solar holy water. Use: 1 Casting Action. Targeting and
  range: Choose an area no longer than 50 meters. Duration: 5 rounds. Effect: Let
  the light shine brightly, as if a round of the sun is rising; holy and pure water
  drops pour down like rain. This creates a Holy Water Rain Environment (see [[Holy
  Water Rain Environment]]). Holy Water Rain Environment: At the beginning of each
  round, dark, corrupt, undead, and other creatures in this area suffer holy damage
  equivalent to the restrained damage. At the same time, normal creatures continue
  to gain 5 points of curse, cold, and poison resistance. Special: This is a celestial
  phenomenon and environmental effect. Therefore,...'
```





You create a rain of solar holy water.

- **Use:** 1 Casting Action.
- **Targeting and range:** Choose an area no longer than 50 meters.
- **Duration:** 5 rounds.
- **Effect:** Let the light shine brightly, as if a round of the sun is rising; holy and pure water drops pour down like rain. This creates a **Holy Water Rain Environment** (see [[Holy Water Rain Environment]]).
- **Holy Water Rain Environment:** At the beginning of each round, dark, corrupt, undead, and other creatures in this area suffer holy damage equivalent to the restrained damage. At the same time, normal creatures continue to gain 5 points of curse, cold, and poison resistance.
- **Special:** This is a celestial phenomenon and environmental effect. Therefore, if there is a creature higher than 1 [[Personality]] of the caster that creates disasters, cold, and other environments, the rain of holy water quickly disappears because it cannot be maintained.  
  - **Clarification:** If a creature more than 1 Sequence higher than the caster creates a disaster‑level or environment‑overriding effect (e.g., severe cold, storm, or similar), Holy Rain ends immediately.

- **Limits:** As described in this section's prose.


### Holy Baptism

```yaml ability
id: sun-seq-05-holy-baptism
name: Holy Baptism
pathway: sun
sequence: 5
status: canonical
type: active
action: cast
cost:
  spirituality: 4
roll: null
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: 1d3
  notes: Unwilling targets are opposed by Physical Defense; restrained targets also take restrained damage.
scaling: []
conditions:
- restrained
- fear
damage_types:
- sanity
tags:
- ritual
- control
- debuff
- defense
text: 'You purify the uncleanness and depravity of a creature. Use: 1 Casting Action.
  Cost: 4 Spirituality. Targeting: Choose the creature in front of you or yourself.
  Effect: Clear the following effects: fear, anger, charm, awe, curse, depravity,
  poison, darkness, temporary madness, uncertain madness, psychological suggestion,
  hypnosis, etc., excluding out-of-control, near-out-of-control, and permanent madness
  (see [[Conditions]]). Unwilling target: If the affected target is unwilling, the
  occult counters [[Physical Defense]]. Aftereffects: The purified creature gains
  1d3 temporary sanity (cannot be superimposed) for 5 minutes (see [[Sanity / Rationality]]).
  This can offset the sanity loss of c...'
```





You purify the uncleanness and depravity of a creature.

- **Use:** 1 Casting Action.
- **Cost:** 4 **Spirituality**.
- **Targeting:** Choose the creature in front of you or yourself.
- **Effect:** Clear the following effects: fear, anger, charm, awe, curse, depravity, poison, darkness, temporary madness, uncertain madness, psychological suggestion, hypnosis, etc., excluding out-of-control, near-out-of-control, and permanent madness (see [[Conditions]]).
- **Unwilling target:** If the affected target is unwilling, the occult counters [[Physical Defense]].
- **Aftereffects:** The purified creature gains **1d3 temporary sanity** (cannot be superimposed) for 5 minutes (see [[Sanity / Rationality]]). This can offset the sanity loss of calculation madness, and it can be converted into sanity protection for promotion (see [[Promotion]]).
- **Restrained target:** If the creature being baptized is a restrained creature, then deal restraint effect damage at the same time (see [[Restraint Effect]]).
- **Special:** The effect of more than 1 character needs to be purified twice; the effect of 1 time is halved; the effect of more than 2 characters cannot be processed.  
  - **Clarification:** Targets 1 Sequence higher require two applications; targets 2+ Sequences higher cannot be purified by this ability.

- **Limits:** As described in this section's prose.


### "God Loves the World"

```yaml ability
id: sun-seq-05-god-loves-the-world
name: '"God Loves the World"'
pathway: sun
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
- ritual
text: 'You change celestial phenomena to a certain extent and call out sunshine. Use:
  1 Casting Action. Cost: 4 spiritual points. Effect: You read the corresponding sentence;
  immediately, bright sunshine appears in the sky. Areas that are currently sunlit
  are immediately considered Warm. Warm Environment: All cold effects caused by the
  [[Cold Extraordinary Ability]] are cleared. The cold environment still exists but
  cannot take effect, but the cleared effect can be reapplied by the cold ability,
  and the cold environment can also be recreated to cover the sun.'
```





You change celestial phenomena to a certain extent and call out sunshine.

- **Use:** 1 Casting Action.
- **Cost:** 4 spiritual points.
- **Effect:** You read the corresponding sentence; immediately, bright sunshine appears in the sky. Areas that are currently sunlit are immediately considered **Warm**.
- **Warm Environment:** All cold effects caused by the [[Cold Extraordinary Ability]] are cleared. The cold environment still exists but cannot take effect, but the cleared effect can be reapplied by the cold ability, and the cold environment can also be recreated to cover the sun.

- **Limits:** As described in this section's prose.


### Additional Sun Domain Spells

```yaml ability
id: sun-seq-05-additional-sun-domain-spells
name: Additional Sun Domain Spells
pathway: sun
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
- utility
text: For other Sun Domain spells, see the Sequence 7 Sun Domain spell list in the
  Sun pathway. Sequence 7 Ability List
```





- For other Sun Domain spells, see the **Sequence 7** Sun Domain spell list in the Sun pathway. Sequence 7 Ability List

> **GM Note:** With [[GM]] permission, a priest of light can learn or create two additional Sun Domain divine spells beyond the default list. This must be reasonable and approved.

- **Effect:** Additional Sun Domain Spells resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
