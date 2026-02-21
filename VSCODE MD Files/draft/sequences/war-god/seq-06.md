---
title: 'Sequence 6: Dawn Paladin'
id: war-god-seq-06
tags:
- pathway:war-god
- sequence:6
---






# Twilight Giant Pathway: Sequence 6

> **Lore:** Possessing giant-like power, you can fill the surroundings with morning light. This light can break illusions, disperse the shadows of resentful souls, and weaken evil spirits.

## Dawn Paladin

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +1, Intuition (INT) +1.
- **Skill Gain:** Occultism +1 level.

> **GM Note:** Your giant strength can make every step you take shake the surroundings; this effect can be controlled.

### Armor of Dawn

```yaml ability
id: war-god-seq-06-armor-of-dawn
name: Armor of Dawn
pathway: war-god
sequence: 6
status: canonical
type: active
action: free
cost:
  spirituality: 3
roll: null
opposed_by: physical_defense
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: "No roll; gap critical strikes gain +1d6 damage, and gaps repair after 2 rounds."
scaling: []
tags:
- ritual
- defense
- offense
text: 'As a free action and at the expense of 3 spirituality points, you create a
  suit of silver-white armor covering your entire body (including gauntlets, breastplates,
  and crowned helmets, among other pieces). It has no obvious weight. Cost: 3 spirituality
  points Use: Free action Effect: You gain 5 points of armor and 3 points of external
  damage reduction. Different judgments are made according to the following conditions:
  Gap (Defense Breached): If an attack breaks through your physical defense and causes
  10 effective damage, that part of the Armor of Dawn is considered to have a Gap.
  While that part has a Gap, a critical strike there ignores the benefits of Armor
  of Dawn and gains a damage...'
```





As a free action and at the expense of 3 spirituality points, you create a suit of silver-white armor covering your entire body (including gauntlets, breastplates, and crowned helmets, among other pieces). It has no obvious weight.

- **Cost:** 3 spirituality points
- **Use:** Free action
- **Effect:** You gain 5 points of armor and 3 points of external damage reduction.

Different judgments are made according to the following conditions:

1. **Gap (Defense Breached):** If an attack breaks through your physical defense and causes ≥ 10 effective damage, that part of the Armor of Dawn is considered to have a **Gap**.
   - While that part has a Gap, a critical strike there ignores the benefits of Armor of Dawn and gains a damage bonus of 1d6.

2. **Unbroken Defense Limit:** If the attack continues but does not meet the Gap condition above, Armor of Dawn can only provide you with 2 defenses at most on the same body part; from the third time, you can be hit by a vital blow.
   - As long as the opponent’s Identification result is > your Agility (DEX) + Dodge, if it fails, it is regarded as being blocked by your armor.
   - The additional 1d6 damage bonus from a Gap critical strike does not apply under the Unbroken Defense condition.

3. **Repair Armor:** Damage to Armor of Dawn is automatically repaired; a Gap is fully restored after 2 rounds.

- At [[Sequence 5]]: Armor of Dawn is changed to 7 points of armor, 5 points of external damage reduction, and the number of damages that have not broken through the defense is 3 times.

- **Limits:** As described in this section's prose.


### Gather Dawn

```yaml ability
id: war-god-seq-06-gather-dawn
name: Gather Dawn
pathway: war-god
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 3
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: "Weapon damage dice: Sword 1d8 or 2d6 + STR, Quick Bow 1d3 + half STR, Longbow 1d8 + STR, Whip 1d4 + half STR; each hit adds 1d6 vs spirit creatures; Sequence 5 adds 1d2 to base damage."
scaling: []
tags:
- ritual
- defense
- offense
text: 'You can gather (condense) different weapons. The strongest is a two-handed
  giant sword. Use: 1 Swift Action Cost: 3 spiritual points Effect: Condense any one
  of the weapons below. The weapon lasts for 8 rounds. Borrowing Protection: When
  using these weapons to perform the special action of [[Borrowing Protection]], you
  get the armor corresponding to the volume of the item. *Special: If the enemy is
  no more than 1 Sequence higher than you, when the dawn weapon is about to be destroyed,
  you can spend 1 spirituality to recast it immediately. Available weapons: Sword
  of Dawn: The medium/large Sword of Dawn can cause damage of 1d8+Strength / 2d6+Strength
  damage dice respectively.'
```





You can gather (condense) different weapons. The strongest is a two-handed giant sword.

- **Use:** 1 Swift Action
- **Cost:** 3 spiritual points
- **Effect:** Condense any one of the weapons below. The weapon lasts for 8 rounds.
- **Borrowing Protection:** When using these weapons to perform the special action of [[Borrowing Protection]], you get the armor corresponding to the volume of the item.

**Special:** If the enemy is no more than 1 Sequence higher than you, when the dawn weapon is about to be destroyed, you can spend 1 spirituality to recast it immediately.

Available weapons:

1. **Sword of Dawn:** The medium/large Sword of Dawn can cause damage of 1d8+Strength / 2d6+Strength damage dice respectively.
   - The large Sword of Dawn is a two-handed giant sword that can attack targets within 1 meter.
   - Against enemies in contact (0 distance), your Identification/attack is at -2 disadvantage.

2. **Dawn Quick Bow:** Deals 1d3 + half Strength damage bonus damage.
   - 1 Attack Action can shoot up to 3 arrows.
   - Each arrow needs to use 1 Swift Action and consumes 1 spiritual concentration.
   - Shooting range (in meters) equals your Strength value.

3. **Dawn Longbow:** Deals 1d8 + Strength damage bonus damage.
   - Same as (2), but 1 Attack Action can shoot only 1 arrow, and the range is twice your Strength value.

4. **Dawn Whip:** Deals 1d4 + half Strength damage bonus damage.
   - 1 Attack Action can attack up to 3 times in a row.
   - You can choose a target within 1 meter.
   - The second Identification is -4 disadvantageous; the third Identification is -6 disadvantageous.

**Special (Cleansing Effect):** Every hit of your Dawn weapon increases the restraint damage by 1d6 against spirit creatures.

- At [[Sequence 5]]: All your Dawn weapons add 1d2 to their base damage.
- [[GM Adjudication]] With GM approval, you can create other reasonable Dawn weapons; all Dawn weapons deal holy damage.

- **Limits:** As described in this section's prose.


### Create Dawn

```yaml ability
id: war-god-seq-06-create-dawn
name: Create Dawn
pathway: war-god
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: 50m
target: designated target(s)
duration: Every 1 point of spirituality lasts for 1 minute.
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
- debuff
text: 'You fill the surroundings with bright, clean, and holy dawn, which can break
  illusions, disperse the shadows of resentful souls, and weaken evil spirits. Use:
  1 Casting Action Duration: Every 1 point of spirituality lasts for 1 minute. Area:
  A dawn field within 50 meters of you as the center; it moves with you. Effects within
  the morning sun: The brightness within the range is like dawn; there is no longer
  shadow and darkness. Within the range, hallucinations from targets up to 1 Sequence
  higher than you are automatically dispelled. Without Extraordinary characteristics,
  ordinary wraith shadows are purified immediately. Extraordinary spirit creatures
  with a certain strength start to suffe...'
```





You fill the surroundings with bright, clean, and holy dawn, which can break illusions, disperse the shadows of resentful souls, and weaken evil spirits.

- **Use:** 1 Casting Action
- **Duration:** Every 1 point of spirituality lasts for 1 minute.
- **Area:** A dawn field within 50 meters of you as the center; it moves with you.

Effects within the morning sun:

1. The brightness within the range is like dawn; there is no longer shadow and darkness.
2. Within the range, hallucinations from targets up to 1 Sequence higher than you are automatically dispelled.
3. Without Extraordinary characteristics, ordinary wraith shadows are purified immediately. Extraordinary spirit creatures with a certain strength start to suffer 1d6 sacred damage every round, and the skill and attribute evaluation continues to suffer -2 disadvantages.
4. Creatures of fallen/darkness feel uncomfortable at most; this is a narrative effect only unless otherwise specified.

- **Effect:** Create Dawn resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Storm of Light

```yaml ability
id: war-god-seq-06-storm-of-light
name: Storm of Light
pathway: war-god
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 2d6 + 1d6
  heal_roll: null
  effect_roll: null
  notes: "Mysticism check vs Physical Defense (ignores DEX/Dodge). Damage is 2d6 holy + 1d6 fire; insert mode also hits you; storm adds 1d6 restraint vs spirits; Sequence 5 upgrades to 3d6 holy + 1d6 fire and no self-damage."
scaling: []
damage_types:
- fire
tags:
- ritual
- defense
text: 'You create a storm of light that sweeps the surroundings, which can directly
  destroy the human body, eliminate resentful souls, and traumatize evil spirits.
  Use: 1 Casting Action Cost: 3 points of spirituality Requirement: Must be cast with
  a weapon. If it is a dawn weapon, the consumption of spirituality can be changed
  to consume its duration of 2 rounds as an alternative. Choose one of the following:
  Insert into the ground: You insert the weapon into the ground, making it bloom with
  the color of the morning light, creating a 10-meter Storm of Light centered on you.
  Resolution: Make a Mysticism check against each creatures Physical Defense (ignore
  Agility (DEX) and Dodge bonuses). This a...'
```





You create a storm of light that sweeps the surroundings, which can directly destroy the human body, eliminate resentful souls, and traumatize evil spirits.

- **Use:** 1 Casting Action
- **Cost:** 3 points of spirituality
- **Requirement:** Must be cast with a weapon.
  - If it is a dawn weapon, the consumption of spirituality can be changed to consume its duration of 2 rounds as an alternative.

Choose one of the following:

1. **Insert into the ground:** You insert the weapon into the ground, making it bloom with the color of the morning light, creating a 10-meter Storm of Light centered on you.
   - Resolution: Make a Mysticism check against each creature’s Physical Defense (ignore Agility (DEX) and Dodge bonuses). This attack counts as holy/light for resistances.
   - Damage: Deals 2d6 holy and 1d6 fire damage to all creatures in the area, including you.
   - Armor interaction: You count as a breach of the Armor of Dawn; you lose the Armor of Dawn on your lower body.

2. **Sweep out:** You choose a direction within 10 meters, sweep out the weapon, and create a Storm of Light that sweeps away.
   - Unlike (1), this specifies a direction without harming you.
   - Damage: Causes 2d6 holy and 1d6 fire damage.

**Special:** Storm of Light increases 1d6 damage of divine restraint against spiritual enemies.

- At [[Sequence 5]]: Storm of Light is changed to 3d6 holy and 1d6 fire damage, and does not cause damage to you.

- **Effect:** Storm of Light resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
