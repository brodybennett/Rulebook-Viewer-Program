---
title: 'Sequence 6: Judge'
id: arbiter-seq-06
tags:
- pathway:arbiter
- sequence:6
---






# Justiciar Pathway: Sequence 6

## Judge

Set new rules for a certain area. Everything in the area must abide by the rules and act; if they violate them, they will be bound by the rules.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- Strength +1
- Constitution +1
- Agility (DEX) +1
- Intuition (INT) +1
- You can start to learn **Law** more quickly.

- Whenever you, as a judge, sum up the guilt of a certain type of non-repetitive case and pronounce a verdict based on appropriate reasons and standards that meet the crime, your legal skills will rise by 1 level.
- For growth and restrictions, refer to Sequence 9: Most Knowledgeable.

### Authority

```yaml ability
id: arbiter-seq-06-authority
name: Authority
pathway: arbiter
sequence: 6
status: canonical
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: All targets within 50 meters.
target: designated target(s)
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
- debuff
text: 'Cost: None (no Spirituality required). Use: 1 Free Action to turn on/off. Targeting
  and range: All targets within 50 meters. Effect: All creatures immediately feel
  your majesty. Their skill/attribute evaluation is -2 disadvantageous (a kind of
  fear). Except for the fear caused by you, the emotions of all creatures within the
  range will not have a substantial impact, but they still exist. Exploding desires
  can still force people to act, but continuous compulsory action will only take effect
  once, and the explosion of desires will still be effective. Targets lower than your
  Sequence level will not be able to look directly at you, and targets lower than
  your level will directly bow their hea...'
```





> **Lore:** You have indescribable majesty, which is a qualitative change in the ability of the [[Arbitrator]].

- **Cost:** None (no **Spirituality** required).
- **Use:** 1 **Free Action** to turn on/off.
- **Targeting and range:** All targets within 50 meters.
- **Effect:**
  1. All creatures immediately feel your majesty. Their skill/attribute evaluation is **-2 disadvantageous** (a kind of fear).
  2. Except for the fear caused by you, the emotions of all creatures within the range will not have a substantial impact, but they still exist. Exploding desires can still force people to act, but continuous compulsory action will only take effect once, and the explosion of desires will still be effective.
  3. Targets lower than your Sequence level will not be able to look directly at you, and targets lower than your level will directly bow their heads and feel oppressed.
- **At Sequence 5:** The effect of (1) is changed to a real fear effect, but it will not force the target to move.  
  [[Sequence 5]]

- **Limits:** As described in this section's prose.


### Prohibition!

```yaml ability
id: arbiter-seq-06-prohibition
name: Prohibition!
pathway: arbiter
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 2
roll: null
opposed_by: none
range: Choose 1 room/house within 50 meters (range) to affect.
target: designated target(s)
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
text: 'You set new rules for a certain area; everything in the area must follow the
  rules and act. All Laws below require speaking the language that leverages the power
  of nature to use. [[Language that leverages the power of nature]] Cost: 2 Spirituality.
  Use: 1 Swift Action, 1 time per round. Targeting and range: Choose 1 room/house
  within 50 meters (range) to affect. Effect: Push your palm forward and say: aThis
  place is forbidden (forbidden content)!a You formulate a rule that everyone must
  obey. Counteracting the prohibition decree:'
```





You set new rules for a certain area; everything in the area must follow the rules and act.

All Laws below require speaking the language that leverages the power of nature to use.  
[[Language that leverages the power of nature]]

- **Cost:** 2 Spirituality.
- **Use:** 1 **Swift Action**, 1 time per round.
- **Targeting and range:** Choose 1 room/house within 50 meters (range) to affect.
- **Effect:** Push your palm forward and say: "This place is forbidden (forbidden content)!" You formulate a rule that everyone must obey.
- **Counteracting the prohibition decree:**
  - One must first act contrary to it.
  - "Relevant attributes are identified as the difficulty of 'Law + Intuition (INT) + Will' against the judge."
  - It is forbidden to use Intuition (INT) to fight against teleportation, and it is forbidden to use Agility (DEX) to fight against concealment, and so on.
  - Even if you succeed in countering the law, your actions can only take effect once, and you still need to continue to fight the next execution.
  - If the confrontation fails, the action you perform will not be refunded.\r\n  - Resolve counteraction using the standard Prohibition check described above.
- **Limits:**
  - You can maintain at most prohibitive laws equal to the number of your Inspirations.
  - Stacking the same laws will double the difficulty.
  - The content of the laws must be specific and not broad. (Example: not all desires can be banned, but individual desires can be prohibited.)
- **Other rules:**
  - Violating your laws is not considered a crime.

**Choose one of the following Prohibition types when you declare it:**

1. **Prohibited ability/behavior**
   - You read out a type of extraordinary ability or prohibited behavior; the two are not contradictory.
   - Examples:
     - "Teleportation is prohibited here!": [[Spirit World Shuttle]], [[Flame Leap]], [[Moon Flash]], etc. cannot be executed, but does not include swapping positions.
     - "Hiding is prohibited here!": [[Invisibility]] / [[shadow hiding]] is forced to reveal. [[Wraith]] is still a spirit body but exposed. Stealth behavior in the conventional sense will also force the body to leave the bunker so that the appearance is exposed to everyone.
     - "Flying is prohibited here!": Flying units will immediately begin falling to the ground, but gliding/floating is not considered flying.
   - A sentence of prohibition does not necessarily have only one content, but at most two. (Example: "Flying and floating are prohibited here!")  
     The two concepts banned together should be similar (example: flying is similar to floating; stealing is not similar to cheating).
   - **Special:** More than one creature will still be blocked by the law, but can consume 1 more spellcasting/attack to successfully execute the ability.

2. **Forbidden to exist**
   - You read out that a creature type is forbidden, and the corresponding creature will be excluded immediately.
   - Examples:
     - "Ghosts and ghosts are forbidden here": ghost/ghost creatures are immediately repelled from the ruled area you designate and unable to enter again.
     - "Zombies and skeletons are prohibited here": same effect as above.
   - To resist the forbidden existence, you need to make 1 **Will test** at the beginning of each round.
   - **Special:**
     - Direct prohibition of existence is invalid for targets with more than 1 character (GM-defined threshold).
     - You must specify a type of creature; it cannot be broad. (Example: you can prohibit ghosts/living corpses/skeletons, but you cannot directly prohibit "the dead" and the existence of creatures.)

### Imprisoned!

```yaml ability
id: arbiter-seq-06-imprisoned
name: Imprisoned!
pathway: arbiter
sequence: 6
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.law
opposed_by: physical_defense
range: Choose 1 target.
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: 1d20
  notes: Adapted from explicit Intuition plus Law versus Physical Defense check and wall-break threshold formula.
scaling:
- when: target_attempts_to_break_prison_wall
  changes:
    effect_note: Required break damage equals 1d20 plus Intuition plus Law of the judge at cast time.
tags:
- ritual
- defense
- control
text: 'Cost: 3 points of Spirituality. Use: 1 Spellcasting Action. Targeting and range:
  Choose 1 target. Check: Intuition (INT) + Law against physical defense; ignores
  armor. Effect: The target is considered to be in a [[Bound State]]. The targetaTMs
  attack/displacement cannot reach the outside world, but the outside world can attack
  the target. To escape, it needs to cause damage equal to the judgeaTMs ard20 + Intuition
  (INT) + Lawa to the wall. The external damage will also damage the wall when it
  hits the target.'
```





> **Lore:** The surroundings of the target become viscous, as if forming a huge amber, or enclosing a sealed transparent wall.

- **Cost:** 3 points of Spirituality.
- **Use:** 1 **Spellcasting Action**.
- **Targeting and range:** Choose 1 target.
- **Check:** Intuition (INT) + Law against physical defense; ignores armor.
- **Effect:**
  - The target is considered to be in a [[Bound State]].
  - The target's attack/displacement cannot reach the outside world, but the outside world can attack the target.
  - To escape, it needs to cause damage equal to the judge's "rd20 + Intuition (INT) + Law" to the wall. The external damage will also damage the wall when it hits the target.
  - **Special:**
    - Spiritual bodies cannot pass through the wall from the inside, but can enter from the outside.
    - Imprisonment is divided by area rather than creatures, so creatures that are possessed or overlapped will be imprisoned together.  

- **Limits:** As described in this section's prose.


### Confinement!

```yaml ability
id: arbiter-seq-06-confinement
name: Confinement!
pathway: arbiter
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: Choose a room/building or area within 50 meters.
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
- stealth
text: 'Cost: 3 Spirituality. Use: 1 Casting Action. Targeting and range: Choose a
  room/building or area within 50 meters. Effect: Instantly inflicts the same effect
  as Imprisoned on the area you choose, but in the form of pure invisible walls. Until
  you cancel the spell or the wall is destroyed, no existence can escape here, and
  the displacement cannot reach the outside world. Sound in the confinement environment
  will not be transmitted to the outside (equivalent to being isolated). If a creature
  is located at the edge of the confinement range when the confinement is just cast
  and can escape the range by taking actions to avoid the confinement effect, the
  countermeasure automatically fails.'
```





> **Lore:** The whole environment suddenly froze, as if there was an invisible barrier that even spirit bodies could not penetrate.

- **Cost:** 3 Spirituality.
- **Use:** 1 **Casting Action**.
- **Targeting and range:** Choose a room/building or area within 50 meters.
- **Effect:**
  - Instantly inflicts the same effect as Imprisoned on the area you choose, but in the form of pure invisible walls.
  - Until you cancel the spell or the wall is destroyed, no existence can escape here, and the displacement cannot reach the outside world.
  - Sound in the confinement environment will not be transmitted to the outside (equivalent to being isolated).
  - If a creature is located at the edge of the confinement range when the confinement is just cast and can escape the range by taking actions to avoid the confinement effect, the countermeasure automatically fails.

- **Limits:** As described in this section's prose.


### Release!

```yaml ability
id: arbiter-seq-06-release
name: Release!
pathway: arbiter
sequence: 6
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: Choose within 50 meters; you can choose a target other than yourself.
target: designated target(s)
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
- control
text: 'This ability has two uses: Release your own effects Cost: None. Use: 1 Swift
  Action, 1 time per round. Effect: Release a kind of Imprisoned/Confinement effect
  you created. Release another binding/sealing effect Cost: 3 Spirituality. Use: 1
  Spellcasting Action.'
```





> **Lore:** You disintegrate the invisible prison around you.

This ability has two uses:

1. **Release your own effects**
   - **Cost:** None.
   - **Use:** 1 **Swift Action**, 1 time per round.
   - **Effect:** Release a kind of Imprisoned/Confinement effect you created.

2. **Release another binding/sealing effect**
   - **Cost:** 3 Spirituality.
   - **Use:** 1 **Spellcasting Action**.
   - **Targeting and range:** Choose within 50 meters; you can choose a target other than yourself.
   - **Effect (as written):**\r\n     - For non-spiritual binding/sealing effects: make an **Intuition (INT) + Law** check to break free; otherwise use the caster's **Intuition (INT) + Will** as the opposing check.\r\n     - For each **Sequence** the caster is higher than you: **-2 disadvantage** on the check.\r\n     - Apply normal disadvantage rules only; do not stack additional "character" penalties.\r\n     - The binding/closing effect achieved by the [[Black Emperor]] approach through distortion falls into this category.\r\n     - Distortion of behavior/intent, or an effect of loss of action similar to shock/spiritual body string, as long as there is no material restraint, does not belong to this category.

- **Limits:** As described in this section's prose.


### Whip!

```yaml ability
id: arbiter-seq-06-whip
name: Whip!
pathway: arbiter
sequence: 6
status: adapted
type: active
action: attack
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.law
opposed_by: physical_defense
range: Choose 1 target within 5 meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Damage roll represents base whip die; add half Strength (rounded up) as stated in prose.
scaling:
- when: second_attack_in_chain
  changes:
    additional_cost: {spirituality: 1}
- when: third_attack_in_chain
  changes:
    additional_cost: {spirituality: 1}
tags:
- ritual
- stealth
- defense
- offense
text: 'Cost: 2 points of Spirituality (first attack). Use: 1 Attack Action. Targeting
  and range: Choose 1 target within 5 meters. Check: Intuition (INT) + Law against
  physical defense. Effect: When you swing your right hand, you are considered to
  have an invisible soft whip. You deal 1d6 + half-strength damage dice; the damage
  is rounded up. You can attack up to three times in a row and make three identifications.
  Each additional identification consumes 1 more Spirituality.'
```





> **Lore:** Make the target seem to be hit by an invisible soft whip; the clothes are broken, the flesh is split open, and the bones are exposed.

- **Cost:** 2 points of Spirituality (first attack).
- **Use:** 1 **Attack Action**.
- **Targeting and range:** Choose 1 target within 5 meters.
- **Check:** Intuition (INT) + Law against physical defense.
- **Effect:**
  - When you swing your right hand, you are considered to have an invisible soft whip.
  - You deal 1d6 + half-strength damage dice; the damage is rounded up.
  - You can attack up to three times in a row and make three identifications. Each additional identification consumes 1 more Spirituality.
- **Special:**
  - This essentially allows you to hold an invisible soft whip as a weapon, so your original weapon has no effect.
  - (Whiplashes created with the Law cannot be synergized with [[Whip of Pain]].)

- **Limits:** As described in this section's prose.


### Exile!

```yaml ability
id: arbiter-seq-06-exile
name: Exile!
pathway: arbiter
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: Choose 1 target within 50 meters.
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
- detection
text: 'Cost: 3 Spirituality. Use: 1 Casting Action. Targeting and range: Choose 1
  target within 50 meters. Effect: You specify 1 direction; the target will be thrown.
  How many meters will be thrown depends on your aInspiration + Law.a No need to identify.
  You can choose air; stop after hitting an obstacle.'
```





> **Lore:** Create an invisible majestic force that can even blow away spirit bodies.

- **Cost:** 3 Spirituality.
- **Use:** 1 **Casting Action**.
- **Targeting and range:** Choose 1 target within 50 meters.
- **Effect:**
  - You specify 1 direction; the target will be thrown.
  - How many meters will be thrown depends on your "Inspiration + Law."
  - No need to identify.
  - You can choose air; stop after hitting an obstacle.
  - For every 2 points of Constitution the target has, the distance to be thrown is reduced by 1 meter (which may cause 1d6 physical damage from the fall).
- **Special:** For non-corporeal creatures such as spirits/ghosts, for every 3 points of Agility (DEX), the distance to be thrown is reduced by 1 meter.

- **Limits:** As described in this section's prose.


### Death!

```yaml ability
id: arbiter-seq-06-death
name: Death!
pathway: arbiter
sequence: 6
status: adapted
type: active
action: attack
cost:
  spirituality: 8
roll: 1d20 + @attr.int + @skill.law
opposed_by: physical_defense
range: Select a target within 50 meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Damage is fixed-value based (Inspiration plus Law) in both modes, so no direct damage dice are encoded.
scaling:
- when: ranged_body_part_judgment_mode
  changes:
    action: cast
    effect_note: Resolve as ranged fixed-value body-part judgment; does not take vital-hit penalty.
tags:
- ritual
- defense
- offense
text: 'After declaring the target dead, you cause powerful damage. Targeting and range:
  Select a target within 50 meters. Use: This ability has the following two uses:
  Melee collision Cost: 8 points of Spirituality. Use: 1 Attack Action. Check: Intuition
  (INT) + Legal identification against physical defense, ignoring agility and dodge;
  excluding targets that can [[Avoid light/lightning]]. Effect:'
```





After declaring the target dead, you cause powerful damage.

- **Targeting and range:** Select a target within 50 meters.
- **Use:** This ability has the following two uses:

1. **Melee collision**
   - **Cost:** 8 points of Spirituality.
   - **Use:** 1 **Attack Action**.
   - **Check:** Intuition (INT) + Legal identification against physical defense, ignoring agility and dodge; excluding targets that can [[Avoid light/lightning]].
   - **Effect:**
     - Your body is united with some strange power, dragging afterimages to collide to the enemy.
     - This is a melee effect.
     - The damage you deal will increase by a fixed value of "Inspiration + Law" value; the damage type remains the same.

2. **Ranged body-part judgment**
   - **Cost:** 8 Spirituality.
   - **Use:** 1 **Casting Action**.
   - **Check:** Intuition (INT) + Legal identification against physical defense, ignoring agility and dodge; excluding targets that can [[Avoid light/lightning]].
   - **Effect:**
     - You specify 1 of its body parts to only cause "Inspiration + Law" fixation value damage.
     - This is a ranged effect (only for ranged use).
     - It does not take the hit penalty for a vital hit.

- **Limits:** As described in this section's prose.
