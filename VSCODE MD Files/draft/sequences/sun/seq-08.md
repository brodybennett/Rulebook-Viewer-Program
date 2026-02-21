---
title: 'Sequence 8: Light Suppliant'
id: sun-seq-08
tags:
- pathway:sun
- sequence:8
---






# Sun Pathway: Sequence 8

## Light Suppliant

- You can perform some spells and rituals in the [[Solar Realm]].
- You are restrained by dead bodies and [[Ghosts]]: while within 10 meters of a corpse or ghost, your Sun-domain checks suffer -2 disadvantage and your holy damage is reduced by 1d6 (minimum 0).

## Advancement

### Auxiliary Materials

- **Main Materials (choose one):**
  - [[Glowstone]]
  - [[Blazing Soul Powder]]
  - [[Mirror Hedgehog Blood]]
  - [[Lava Troll Heart]]
- **Auxiliary Materials:**
  - [[Phnom Penh Sunflower]] ×1
  - [[Aconite Juice]] ×3 drops

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1; Agility (DEX) +1; Intuition (INT) +1; Constitution +1.
- **Rapid Improvement:** Mysticism is included in the category of [[Rapid Improvement]] and can be quickly improved to Proficiency.

### White Vision

```yaml ability
id: sun-seq-08-white-vision
name: White Vision
pathway: sun
sequence: 8
status: canonical
type: toggle
action: swift
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
- ritual
- detection
text: 'Cost: 1 [[Spirituality]] per minute while active. Use: 1 Swift Action to activate.
  Effect: You can see in total darkness. Anything hidden by darkness or shadow is
  revealed. Limits: This ability belongs to [[Summoning Light]]. If Summoning Light
  is lost, this ability disappears (and vice versa).'
```





> **Lore:** Golden sunlight gathers in your eyes until they resemble two miniature suns.

- **Cost:** 1 **[[Spirituality]]** per minute while active.
- **Use:** 1 **Swift Action** to activate.
- **Effect:**
  - You can see in total darkness.
  - Anything hidden by darkness or shadow is revealed.
- **Limits:**
  - This ability belongs to **[[Summoning Light]]**.
  - If Summoning Light is lost, this ability disappears (and vice versa).
- **Ending:** You may end the effect as a free action.

### Brightness

```yaml ability
id: sun-seq-08-brightness
name: Brightness
pathway: sun
sequence: 8
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: none
range: With you as the center, you illuminate a 10-meter area with divine power.
target: designated target(s)
duration: Maintenance continues to consume Casting Actions.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: Applies restrained damage each round to dark/corrupt/undead in the area; costs 2 spirituality per round.
scaling: []
conditions:
- restrained
damage_types:
- holy
tags:
- ritual
- detection
- control
- offense
text: 'Use: 1 Casting Action. Cost: Each round consumes 2 [[Spirituality]]. Duration:
  Maintenance continues to consume Casting Actions. Targeting and range: With you
  as the center, you illuminate a 10-meter area with divine power. Effect: In this
  area, the effects of darkness, corruption, and undead that are not higher than you
  by 1 character level or 2 Sequence levels will be cleared. As long as the radiance
  is maintained, dark, corrupted, and undead creatures in the area begin to suffer
  [[Holy Damage]] equal to your Restrained Damage each round. [[Resentful Soul]] is
  exposed to spiritual vision; when taking damage, its body begins to vaporize.'
```





> **Lore:** You raise your arms in prayer and emit pure, clear radiance.

- **Use:** 1 **Casting Action**.
- **Cost:** Each round consumes 2 **[[Spirituality]]**.
- **Duration:** Maintenance continues to consume Casting Actions.
- **Targeting and range:** With you as the center, you illuminate a 10-meter area with divine power.
- **Effect:**
  - In this area, the effects of darkness, corruption, and undead that are not higher than you by 1 character level or 2 Sequence levels will be cleared.
  - As long as the radiance is maintained, dark, corrupted, and undead creatures in the area begin to suffer **[[Holy Damage]]** equal to your **Restrained Damage** each round.
  - [[Resentful Soul]] is exposed to spiritual vision; when taking damage, its body begins to “vaporize.”
- **Sequence 7:**
  - It can be replaced by a clear and warm power that ordinary people cannot detect, and it does not need to bloom.
  - **Clarification:** The light becomes invisible to ordinary observers, but all effects still apply.
- **Clarification:** This clears effects caused by darkness/corruption/undead abilities; it does not remove the creature type itself.

- **Limits:** As described in this section's prose.


### Call the Holy Light

```yaml ability
id: sun-seq-08-call-the-holy-light
name: Call the Holy Light
pathway: sun
sequence: 8
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose 1 target within your field of vision.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 2d6 + 1d6
  heal_roll: null
  effect_roll: null
  notes: Ignores Agility (DEX) and Evasion; Sequence 7 damage is 3d6 holy + 1d6 fire.
scaling: []
damage_types:
- fire
- holy
tags:
- ritual
- detection
- defense
- offense
text: 'Use: 1 Casting Action. Cost: Consume 3 [[Spirituality]]. Targeting and range:
  Choose 1 target within your field of vision. Resolution: [[Occult vs Physical Defense]],
  ignoring Agility (DEX) and Evasion in Physical Defense. Effect: Deal 2d6 Holy damage
  and 1d6 Fire damage. Sequence 7: Damage changes to 3d6 Holy damage and 1d6 Fire
  damage.'
```





> **Lore:** A pure beam of light wrapped in flames descends from the roof or sky.

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 3 **[[Spirituality]]**.
- **Targeting and range:** Choose 1 target within your field of vision.
- **Resolution:** **[[Occult vs Physical Defense]]**, ignoring Agility (DEX) and Evasion in Physical Defense.
- **Effect:** Deal 2d6 Holy damage and 1d6 Fire damage.
- **Sequence 7:** Damage changes to 3d6 Holy damage and 1d6 Fire damage.

- **Limits:** As described in this section's prose.


### Purification

```yaml ability
id: sun-seq-08-purification
name: Purification
pathway: sun
sequence: 8
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose 1 target within 10 meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Voluntary targets are purified without a check; involuntary targets use Occult vs Physical Defense. Voluntary restrained targets take 1d6 holy damage.
scaling: []
conditions:
- restrained
damage_types:
- holy
tags:
- ritual
- mobility
- control
- offense
text: 'Use: 1 Casting Action. Cost: Consume 2 [[Spirituality]]. Targeting and range:
  Choose 1 target within 10 meters. Limits: Unlike Call the Holy Light, this ability
  does not cause damage to ordinary creatures (except as noted below). Effect (Voluntary
  target): Purification succeeds by default and removes the following effects (excluding
  out-of-control, near-out-of-control, permanent madness, etc.): See [[Conditions]].
  Special (Voluntary restrained creature): It deals 1d6 Holy damage and the creature
  is restrained, although it also clears the effect.'
```





> **Lore:** You pray to cleanse filth and corruption.

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 2 **[[Spirituality]]**.
- **Targeting and range:** Choose 1 target within 10 meters.
- **Limits:** Unlike “Call the Holy Light,” this ability does not cause damage to ordinary creatures (except as noted below).
- **Effect (Voluntary target):** Purification succeeds by default and removes the following effects (excluding out-of-control, near-out-of-control, permanent madness, etc.):
  - See **[[Conditions]]**.
- **Special (Voluntary restrained creature):**
  - It deals 1d6 Holy damage and the creature is restrained, although it also clears the effect.
- **Effect (Involuntary target):**
  - Resolve with **[[Occult vs Physical Defense]]**; on success, apply the same clearing effect as above.
- **Clearing stronger effects:**
  - An effect caused by more than 1 character level or 2 Sequence levels above yours needs 4 uses to be completely cleared.
  - After 2 uses, the effect is halved (rounded down).
  - It may not be cleared if it is greater than 2 characters.
  - **Clarification:** If the effect source is 2+ Sequences higher than you, it cannot be cleared.
- **Sequence 7:**
  - Requires 3 uses to completely clear effects caused by more than 1 character level or 2 Sequence levels above yours.
  - The effect is halved after 1 use.

- **Effect:** Purification resolves using its yaml ability block and section prose.


### Sun Path Restraint

```yaml ability
id: sun-seq-08-sun-path-restraint
name: Sun Path Restraint
pathway: sun
sequence: 8
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
  damage_roll: 1d6
  heal_roll: null
  effect_roll: "1"
  notes: Adds +1d6/+2d6/+3d6 holy damage versus dark/corrupt/undead respectively.
scaling: []
conditions:
- restrained
damage_types:
- holy
tags:
- control
- buff
- offense
text: 'Restraint Rule: Holy Damage is restrained against three creature typesdark,
  corrupted, and undeadand causes additional effects. When you hit a dark, corrupted,
  or undead creature with an offensive Sun Path extraordinary ability (including [[Solar
  Holy Water]]), increase damage as follows: Dark creatures: +1d6 Holy damage. Corrupted
  creatures: +2d6 Holy damage. Undead: +3d6 Holy damage. Restrained Damage: The bonus
  Holy damage from the restraint rule above. If a holy effect is a transmutation ability,
  its secondary effect (which may deal Holy damage equal to Restrained Damage) is
  listed separately (e.g., Brightness). Creature typing is marked in the corresponding
  pathways (example: [[Moon...'
```





- **Restraint Rule:** **Holy Damage** is restrained against three creature types—dark, corrupted, and undead—and causes additional effects.
- When you hit a dark, corrupted, or undead creature with an offensive Sun Path extraordinary ability (including [[Solar Holy Water]]), increase damage as follows:
  - **Dark creatures:** +1d6 Holy damage.
  - **Corrupted creatures:** +2d6 Holy damage.
  - **Undead:** +3d6 Holy damage.
- **Restrained Damage:** The bonus Holy damage from the restraint rule above.
- If a holy effect is a “transmutation ability,” its secondary effect (which may deal Holy damage equal to Restrained Damage) is listed separately (e.g., Brightness).
- Creature typing is marked in the corresponding pathways (example: [[Moon Pathway: Sequence 7]]).

- **Effect:** Sun Path Restraint resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Solar Rituals

```yaml ability
id: sun-seq-08-solar-rituals
name: Solar Rituals
pathway: sun
sequence: 8
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
- defense
text: 'You have mastered some rituals in the solar realm. This is knowledge brought
  by the potion, so it cannot be stolen or recorded. In the Fifth Age, the object
  of prayer is [[Eternal Sun]] by default. [[Fifth Age]] *Holy Water Prayer Process:
  A general ritual process of about 5 minutes. Creates: 1 bottle of [[Solar Holy Water]]
  (golden liquid). Solar Holy Water (use): Resolution: Throwing against Physical Defense.'
```





- You have mastered some rituals in the solar realm.
- This is knowledge brought by the potion, so it cannot be stolen or recorded.
- In the Fifth Age, the object of prayer is **[[Eternal Sun]]** by default. [[Fifth Age]]

**Holy Water Prayer**

> **Lore:** Golden rainwater emerges above the altar and converges into a bottle of sun-blessed liquid.

- **Process:** A general ritual process of about 5 minutes.
- **Creates:** 1 bottle of [[Solar Holy Water]] (golden liquid).
- **Solar Holy Water (use):**
  - **Resolution:** Throwing against Physical Defense.
  - **Effect on normal creatures:** No effect.
  - **Effect on restrained types:** Deal 2d6 Holy damage to dark, corrupted, undead, and other creatures; apply Sun Path restraint; the creature begins to “vaporize.”
  - **Additional effects:**
    1. For creatures sprinkled with holy water, cold-related effects are cleared (including restrained creatures).
    2. Normal creatures taking holy water gain 5 points of cold, curse, and poison resistance for 5 minutes, and the cold effect is cleared.
    3. If there are resentful spirits or ghosts in the user’s body, it causes damage to them while the user gains the benefits.

**Purification Ritual**

- **Process:** A general ritual process of about 5 minutes.
- **Effect:** You entrust the gods to solve power you cannot cleanse.
  1. When the ritual is completed, the god you prayed to performs purification; the target must be within the area of the **[[Ritual Magic]]**.
  2. If the effects of the purified darkness, corruption, and immortality are not higher than the prayed-to target by 2 characters, they can be completely cleared.
- **Special:**
  - In the case of more than two persons, it usually depends on the severity of the pollution.
  - If the pollution is only a part of indirect force, it can be completely eliminated. Otherwise, it generally leaves hidden dangers.
  - “Indirect power” generally means you did not provoke the other party’s direct “care,” and the effect is not directly exerted by the other party’s body.
  - **Clarification:** If the pollution source is 2+ Sequences higher than you, results depend on severity and may not fully clear.

**Salvation Ritual**

- **Process:** A general ritual process of about 5 minutes.
- **Effect:** You create a relatively safe area for the sun.
  1. When the ritual is completed, the ritual area continues to be covered with warm, clear power; any dark, corrupt, undead, and other creatures in the area continuously suffer sacred damage equal to Restrained Damage each round.
  2. At the same time, normal creatures in the area continuously receive the same benefits as Solar Holy Water; this remains valid for 5 minutes after leaving the area.
- > **GM Note:** In a dangerous area, this ritual provides temporary safety but may not be decisive for escape.

**Using Solar Rituals Without Following the Eternal Blazing Sun**

- A Sun Path Extraordinary who is not a follower of the **[[Eternal Blazing Sun]]** can still use the rituals above if they have mastered sufficient methods to please the relevant gods.
- Even so, they must make a **[[Lucky Appraisal]]** to get a response.
- If you believe in a god hostile to the Eternal Blazing Sun, there may be no response at all.

- **Limits:** As described in this section's prose.
