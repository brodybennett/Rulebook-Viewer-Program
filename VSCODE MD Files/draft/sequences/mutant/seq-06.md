---
title: 'Sequence 6: Wraith'
id: mutant-seq-06
tags:
- pathway:mutant
- sequence:6
---






# Chained Pathway: Sequence 6

## Wraith

- Your body can be as hard as steel. As long as your head is not broken, other injuries are not fatal.
- You have improved power, have mastered some death-like spells, and skillfully use extraordinary cold and decay.
- **Curse:** You long for human warm blood and fresh flesh. This state is especially severe during the full moon; if you do not give up self-control, you will suffer so much that you lose the ability to fight.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength +1, constitution +1, agility +1; your mysticism can be quickly improved to proficiency.

After taking the potion:

1. You will be regarded as a **Living Corpse** for a long time. This is a permanent effect brought by the potion.
2. You are regarded as an **Undead Creature** for a long time, gaining 5 points of resistance to curse, cold, and poison damage.
3. You get blade swing, fast dodge, night vision, and fast healing in **Werewolf Form**.

Note: In **Living Corpse** form, you will appear cold and gloomy, unlike a living creature. For details, refer to [[Death Pathway: Sequence 9]].

You gain the power of the undead, a frost aura, an **Immortal Body**, and the extraordinary ability to summon undead.

Even though you get werewolf-based enhancements, that doesn’t mean you’ll still look like a werewolf unless you tweak it yourself. For example, the benefit of blade swipe is now a trait of your purely human hand, which won’t manifest wolf traits by default.

### The Power of the Living Corpse

```yaml ability
id: mutant-seq-06-the-power-of-the-living-corpse
name: The Power of the Living Corpse
pathway: mutant
sequence: 6
status: canonical
type: active
action: full-round
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
  notes: Restores vitality equal to half your maximum (rounded up) and applies temporary -3 CON on trigger.
scaling: []
tags:
- mobility
- debuff
- offense
text: 'Effect: You unleash a berserk attack that tears your opponent apart. While
  in Living Corpse state: your strength +3, constitution +2, and agility +2. Acceleration
  (Full-Round Action): Through a Full-Round Action, charge up your strength and prepare
  to accelerate, then start running at full speed until you slow down or stop. Your
  moving speed is multiplied by 2 times, and the speed is faster than a steam train
  at its peak. This full-round acceleration can be performed while performing a movement
  action, but it must be running in a roughly constant direction; it is considered
  that you are gradually accelerating during the running process. Manifestation: While
  gaining the benefits of undead...'
```





- **Effect:** You unleash a berserk attack that tears your opponent apart.
- While in **Living Corpse** state: your strength +3, constitution +2, and agility +2.
- **Acceleration (Full-Round Action):**
  1. Through a Full-Round Action, charge up your strength and prepare to accelerate, then start running at full speed until you slow down or stop. Your moving speed is multiplied by 2 times, and the speed is faster than a steam train at its peak.
  2. This full-round acceleration can be performed while performing a movement action, but it must be running in a roughly constant direction; it is considered that you are gradually accelerating during the running process.
- **Manifestation:** While gaining the benefits of undead power, every step you take shakes the environment and doubles your weight. You can adjust this manifestation as a Swift Action if you don’t want to be so conspicuous; this does not include running at full speed.
- **Grapple (special action):** If you perform a special action grapple in this state, and you deal damage to the target every round with the grapple, if the opponent’s Vitality is reduced to 0 due to this, it is considered to be directly torn by you.

- **Limits:** As described in this section's prose.


### Immortal Body

```yaml ability
id: mutant-seq-06-immortal-body
name: Immortal Body
pathway: mutant
sequence: 6
status: canonical
type: active
action: cast
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
  notes: No roll; fixed armor, damage reduction, and resistance values.
scaling: []
conditions:
- dying
damage_types:
- lightning
- holy
tags:
- healing
- offense
text: 'Effect: Your body heals quickly. Trigger: Once per round, it triggers automatically
  whenever your Vitality reaches 0. Your physique is temporarily -3, and half of your
  health is restored to your health. The Constitution (CON) reduction can only be
  paid by you (it cannot be transferred or offset by others). If the end of your life
  is an effective, vital blow to your head, then Immortal Body cannot be triggered.
  If the end of your life is holy damage or lightning damage, Immortal Body also cannot
  be triggered. The damage that ends your life must not put you in a near-death state,
  but directly end your life to take effect. For dying, see [[Special State]]. *Sequence
  5: Wraith state (referenc...'
```





- **Effect:** Your body heals quickly.
- **Trigger:** Once per round, it triggers automatically whenever your Vitality reaches 0.
  1. Your physique is temporarily -3, and half of your health is restored to your health. The Constitution (CON) reduction can only be paid by you (it cannot be transferred or offset by others).
  2. If the end of your life is an effective, vital blow to your head, then **Immortal Body** cannot be triggered.
  3. If the end of your life is holy damage or lightning damage, **Immortal Body** also cannot be triggered.
  4. The damage that ends your life must not put you in a near-death state, but directly end your life to take effect.

For dying, see [[Special State]].

**Sequence 5: Wraith state** (reference): Because it is a spirit body, physical regeneration is meaningless, so it cannot use **Immortal Body**. But despite this, if the resentful soul dies, or even gets a headshot, it can still continue to perform a round of operations without a head and is almost considered dead. This ability has no effect if you die without entering a ghost/spirit-body state.

- **Limits:** As described in this section's prose.


### Steel Skin

```yaml ability
id: mutant-seq-06-steel-skin
name: Steel Skin
pathway: mutant
sequence: 6
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
damage_types:
- physical
- fire
tags:
- defense
- offense
text: 'Effect: Your skin is as hard as steel. Armor: Your armor is +6 (does not stack
  with other armor). Damage reduction/resistance: You gain 10 physical damage reduction,
  and you gain 20 fire damage resistance. Immunities/negations: You are immune to
  vital blows. You will not drown; you do not need to breathe. Big success will not
  cause additional damage to you; that is, big success cannot obtain the effect of
  guaranteed damage to you. Special (stun): If you are hit by a pistol or a more explosive
  weapon aimed at your head at close range (i.e., a vital blow), although it will
  not cause damage, it will still cause a stun state.'
```





- **Effect:** Your skin is as hard as steel.
- **Armor:** Your armor is +6 (does not stack with other armor).
- **Damage reduction/resistance:** You gain 10 physical damage reduction, and you gain 20 fire damage resistance.
- **Immunities/negations:**
  - You are immune to vital blows.
  - You will not drown; you do not need to breathe.
  - Big success will not cause additional damage to you; that is, big success cannot obtain the effect of guaranteed damage to you.
- **Special (stun):** If you are hit by a pistol or a more explosive weapon aimed at your head at close range (i.e., a vital blow), although it will not cause damage, it will still cause a stun state.
- **Defense-breaking and exceptions:**
  1. If you have suffered five critical blows, and all five critical blows hit the same part, then the last critical blow can break the defense.
  2. Blade swipe/corroding claws and other attacks that can ignore defense can still hit you vitally, and are effective with great success.
  3. The guaranteed weak point attack in [[Reaper’s Fatal Attack]] is still valid for you.

- **Limits:** As described in this section's prose.


### Extraordinary Weight

```yaml ability
id: mutant-seq-06-extraordinary-weight
name: Extraordinary Weight
pathway: mutant
sequence: 6
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
- mobility
- control
- buff
text: In Living Corpse state, your weight suddenly increases, and every step when
  running is enough to shake the environment, crushing your opponent like a chariot.
  You cannot float, blow, or suspend in any sense. If you are already in midair, you
  will fall down suddenly, and your legs will hit the ground firmly, leaving a pair
  of sunken marks. This will not affect your movement speed, and in a critical state,
  you will usually not be able to move in any sense due to other peoples actions.
  At the same time, this is controllable to a certain extent. When you dont need this
  effect, you can restrain it as much as possible. (Extraordinary weight is not an
  independent extraordinary ability, but an ex...
```





In **Living Corpse** state, your weight suddenly increases, and every step when running is enough to shake the environment, crushing your opponent like a chariot.

1. You cannot float, blow, or suspend in any sense. If you are already in midair, you will fall down suddenly, and your legs will hit the ground firmly, leaving a pair of sunken marks.
2. This will not affect your movement speed, and in a critical state, you will usually not be able to move in any sense due to other people’s actions.

At the same time, this is controllable to a certain extent. When you don’t need this effect, you can restrain it as much as possible.

(Extraordinary weight is not an independent extraordinary ability, but an explanation of **The Power of the Living Corpse**. If you lose **The Power of the Living Corpse**, this also disappears; with **The Power of the Living Corpse**, you also have extraordinary weight.)

- **Effect:** Extraordinary Weight resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Rotten Finger

```yaml ability
id: mutant-seq-06-rotten-finger
name: Rotten Finger
pathway: mutant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: 3d6
  heal_roll: null
  effect_roll: null
  notes: Damage also includes +2d6 poison; double damage against plants, spider silk, or hair. Occult identification can replace the raw Intuition check.
scaling: []
damage_types:
- poison
- curse
tags:
- ritual
- detection
- control
- debuff
- defense
- offense
text: '*Rot control: you can accurately grasp the supernatural ability of the rot.
  Cost: 2 spirituality points Use: 1 spellcasting action; choose a target within your
  field of vision. Effect: Put your thumb up next to your index finger, aimed at the
  opponent. Intuition (INT) or occult identification against physical defense; success
  causes the air at the target to explode immediately, and wisps of black air rise
  upwards, dealing 3d6 curse damage and 2d6 poison damage. Special: If the target
  selected by Finger of Rot is a type of plant, spider silk, or hair, the damage dealt
  is doubled.'
```





**Rot control**: you can accurately grasp the supernatural ability of the rot.

- **Cost:** 2 spirituality points
- **Use:** 1 spellcasting action; choose a target within your field of vision.
- **Effect:**
  1. Put your thumb up next to your index finger, aimed at the opponent.
  2. Intuition (INT) or occult identification against physical defense; success causes the air at the target to explode immediately, and wisps of black air rise upwards, dealing 3d6 curse damage and 2d6 poison damage.
- **Special:** If the target selected by Finger of Rot is a type of plant, spider silk, or hair, the damage dealt is doubled.

- **Limits:** As described in this section's prose.


### Blessing of Rot

```yaml ability
id: mutant-seq-06-blessing-of-rot
name: Blessing of Rot
pathway: mutant
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: 1 encounter
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Bonus 1d6 curse damage plus an additional 1d6 poison damage on hit.
scaling: []
damage_types:
- poison
- curse
tags:
- ritual
- debuff
- offense
text: 'Cost: 1 spirituality point Use: 1 Swift Action Duration: 1 encounter Effect:
  Add a rotten breath to one of your body parts (e.g., a fist). You cannot add it
  to a weapon that is not a body part. After blessing, the damage caused by this body
  part adds 1d6 curse and 1d6 poison damage. Special: Extra damage only; double the
  effect on plants, spider silk, and hair.'
```





- **Cost:** 1 spirituality point
- **Use:** 1 Swift Action
- **Duration:** 1 encounter
- **Effect:**
  1. Add a rotten breath to one of your body parts (e.g., a fist). You cannot add it to a weapon that is not a body part.
  2. After blessing, the damage caused by this body part adds 1d6 curse and 1d6 poison damage.
- **Special:**
  - Extra damage only; double the effect on plants, spider silk, and hair.
  - If you buff the soles of your boots, the place you walk takes on a rotten smell, the ground shows rotten mud, and creatures that move where you walk have a movement speed of -2.
  - Even if it is metal, there will be some signs of decay under the power of decay, unless it is a [[Beyonder material]].
  - If you are one level above the material, the decay still applies.

- **Limits:** As described in this section's prose.


### Spreading Ice

```yaml ability
id: mutant-seq-06-spreading-ice
name: Spreading Ice
pathway: mutant
sequence: 6
status: canonical
type: active
action: full-round
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Ice wall has 10 HP and 10 defense; no roll to create.
scaling: []
tags:
- ritual
- mobility
- control
- defense
text: '*Ice control: You have the extraordinary ability to master the cold, making
  things condense into frost, covering them with white snow, and scattering romantic
  snowflakes. Cost: 1 spirituality point Use: 1 Casting Action Effect: Choose a body
  part; make hoarfrost condense on it, and quickly spread a cold and transparent ice
  layer. If that body part is in contact with the ground or other things, make the
  ice that diffuses from it spread rapidly, freezing 1 target you choose; Intuition
  (INT) or mysticism against physical defense. A successful identification causes
  the target to lose a movement action and be shackled by ice. Bonus (Full-Round Action):
  As a Full-Round Action, expending 2 spiri...'
```





**Ice control:** You have the extraordinary ability to master the cold, making things condense into frost, covering them with white snow, and scattering romantic snowflakes.

- **Cost:** 1 spirituality point
- **Use:** 1 Casting Action
- **Effect:**
  1. Choose a body part; make hoarfrost condense on it, and quickly spread a cold and transparent ice layer.
  2. If that body part is in contact with the ground or other things, make the ice that diffuses from it spread rapidly, freezing 1 target you choose; Intuition (INT) or mysticism against physical defense. A successful identification causes the target to lose a movement action and be shackled by ice.
- **Bonus (Full-Round Action):** As a Full-Round Action, expending 2 spirituality points, you stir up the cold, turning it into a hurricane that sweeps around you. Cold snowflakes suddenly fall; the surrounding area is covered with ice; trees are covered with white edges; this is regarded as a cold environment.
  - **Cold environment of living corpses:** In the environment, all creatures without cold resistance have -3 movement.

**Sequence 5** (reference): The cold field of the Full-Round Action only needs 1 Casting Action to release, manifested as a silent scream that stirs up cold power (not the scream of the wraith).

- **Limits:** As described in this section's prose.


### Ice Wall Consolidation

```yaml ability
id: mutant-seq-06-ice-wall-consolidation
name: Ice Wall Consolidation
pathway: mutant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: physical_defense
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
damage_types:
- physical
- fire
tags:
- ritual
- mobility
- defense
- offense
text: 'Cost: 1 spirituality point Use: 1 Casting Action Effect: Create an ice wall.
  The ice wall has 10 points of life and 10 points of defense. Physical and fire damage
  it receives is half, rounded up. It cannot resist attacks that cannot be blocked
  by the ice wall. If the ice wall is destroyed, overflow damage needs to fight against
  your physical defense again. If an attack does not break through the ice wall, then
  if it has side effects, it cannot take effect on your body. Note: The ice wall cannot
  move with you, which means you cannot move behind the ice wall. However, the agility
  and dodge of physical defense will not be affected, because you can dodge sideways
  at the moment the ice wall sh...'
```





- **Cost:** 1 spirituality point
- **Use:** 1 Casting Action
- **Effect:**
  1. Create an ice wall. The ice wall has 10 points of life and 10 points of defense. Physical and fire damage it receives is half, rounded up. It cannot resist attacks that cannot be blocked by the ice wall.
  2. If the ice wall is destroyed, overflow damage needs to fight against your physical defense again.
  3. If an attack does not break through the ice wall, then if it has side effects, it cannot take effect on your body.

Note: The ice wall cannot move with you, which means you cannot move behind the ice wall. However, the agility and dodge of physical defense will not be affected, because you can dodge sideways at the moment the ice wall shatters.

You can also use this to freeze an inorganic substance; the frozen inorganic substance receives half of the physical damage and half of the fire damage, rounded up.

- **Limits:** As described in this section's prose.


### Blessing of Cold

```yaml ability
id: mutant-seq-06-blessing-of-cold
name: Blessing of Cold
pathway: mutant
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: 1 encounter
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Bonus 1d6 cold damage and -2 penalty to the target's next check on hit.
scaling: []
damage_types:
- cold
tags:
- ritual
- defense
- offense
text: 'Cost: 1 spirituality point Use: 1 Swift Action Duration: 1 encounter Effect:
  Choose a body part; attacks with it deal an additional 1d6 cold damage, permeating
  your fist or other parts with bursts of cold air. This also causes the victims muscles
  to tremble and hoarfrost to condense; their next check takes a -2 penalty. A significant
  layer of ice quickly condenses on the wall hit by a fist blessed with cold power.
  Soles option: If you buff the soles, thin ice condenses wherever you walk. Targets
  without cold resistance or balance ability will lose their balance if there is a
  big failure on the thin ice you walk on. (See [[Special Status]].)'
```





- **Cost:** 1 spirituality point
- **Use:** 1 Swift Action
- **Duration:** 1 encounter
- **Effect:**
  1. Choose a body part; attacks with it deal an additional 1d6 cold damage, permeating your fist or other parts with bursts of cold air.
  2. This also causes the victim’s muscles to tremble and hoarfrost to condense; their next check takes a -2 penalty.
  3. A significant layer of ice quickly condenses on the wall hit by a fist blessed with cold power.
- **Soles option:** If you buff the soles, thin ice condenses wherever you walk. Targets without cold resistance or balance ability will lose their balance if there is a big failure on the thin ice you walk on. (See [[Special Status]].)

Note: Cold Buff is contradictory to Rot Bless, in the sense that they cannot be used on the same body part. The most you can do is spread ice on the soles of your boots, add rot to your fists, and use these two abilities on different body parts, instead of giving one part both frost and rot at the same time. You can have a rotten left hand and a cold right hand, but an Attack Action can only use one of them.

- **Limits:** As described in this section's prose.


### Ice Crystal Arrow

```yaml ability
id: mutant-seq-06-ice-crystal-arrow
name: Ice Crystal Arrow
pathway: mutant
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Arrow is detected with DV 25 appraisal; otherwise treated as caught off guard. Redirecting the arrow uses a quick action.
scaling: []
conditions:
- caught_off_guard
tags:
- detection
- defense
text: '*Sequence 5: You have gained an additional cold ability. Use: 1 Casting Action;
  occult vs. physical defense; choose 1 target. Effect: Occultism against physical
  defense. Speed is regarded as a gun. This ice crystal thin arrow is close to transparency
  and needs detection and identification of Difficulty Value 25; otherwise, it enjoys
  the effect of being caught off guard. 1 quick action: you can suddenly change the
  direction of this ice crystal thin arrow and treat it as a special action without
  consuming your special-action slot.'
```





**Sequence 5:** You have gained an additional cold ability.

- **Use:** 1 Casting Action; occult vs. physical defense; choose 1 target.
- **Effect:**
  1. Occultism against physical defense. Speed is regarded as a gun. This ice crystal thin arrow is close to transparency and needs detection and identification of **Difficulty Value 25**; otherwise, it enjoys the effect of being caught off guard.
  2. 1 quick action: you can suddenly change the direction of this ice crystal thin arrow and treat it as a special action without consuming your special-action slot.

- **Limits:** As described in this section's prose.


### Manipulate Living Corpses

```yaml ability
id: mutant-seq-06-manipulate-living-corpses
name: Manipulate Living Corpses
pathway: mutant
sequence: 6
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Living corpse puppet attack deals 1d6 physical damage; puppet has listed fixed stats.
scaling: []
conditions:
- dead
damage_types:
- physical
tags:
- ritual
- healing
- debuff
- defense
- offense
text: 'You can easily wake up dead corpses and cultivate puppets. This is a death-like
  spell. Cost: 3 spirituality points Use: 1 Casting Action; choose: 1 corpse that
  has not been [[requiemed]] and has been dead for less than 1 month, or an existing
  Living Corpse (the living corpse should have no owner, or the owner is 1 rank lower
  than you). Effect: You make it your puppet. *Zombie (puppet stats): 15 health, 15
  physical defense (5 points for agility and dodge); it has no Fighting or Willpower
  Defense rolls (use its flat defenses). A living corpse has 5 points of resistance
  to cold, curse, and poison. Its attack causes 1d6 physical damage. It looks like
  an ordinary person but has many places on...'
```





You can easily wake up dead corpses and cultivate puppets. This is a death-like spell.

- **Cost:** 3 spirituality points
- **Use:** 1 Casting Action; choose:
  - 1 corpse that has not been [[requiemed]] and has been dead for less than 1 month, **or**
  - an existing **Living Corpse** (the living corpse should have no owner, or the owner is 1 rank lower than you).
- **Effect:** You make it your puppet.

**Zombie** (puppet stats): 15 health, 15 physical defense (5 points for agility and dodge); it has no Fighting or Willpower Defense rolls (use its flat defenses).

1. A living corpse has 5 points of resistance to cold, curse, and poison. Its attack causes 1d6 physical damage. It looks like an ordinary person but has many places on its body.
2. If there is a disease that can affect the living corpse, then it can be done against physical defense of **Difficulty Value 15**, such as the [[Witch’s Plague]].

Note: You should not wake up a living corpse that has been dead for too long; the standard is more than 1 week. A living corpse awakened this way generally has many places of decay. Any investigation and appraisal against it that succeeds at **Difficulty Value 15** will find festering on its body. (Decomposition within 1 week can be covered with clothing.)

The undead creatures driven by you are not equal to [[Secret Puppets]], and may not necessarily share senses. However, you can use your thoughts to give them orders within 100 meters without moving, and they will complete the orders even if they leave the range.

- **Limits:** As described in this section's prose.


### Full Moon Curse

```yaml ability
id: mutant-seq-06-full-moon-curse
name: Full Moon Curse
pathway: mutant
sequence: 6
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
  notes: Observers can attempt DV 15 Intuition appraisal to sense your killing intent; full moon triggers madness.
scaling: []
tags:
- debuff
text: 'Rule: Full Moon Curse is an inherent effect once possessing The Power of the
  Living Corpse, and cannot be recorded or stolen. Rule: Unlike werewolves, even if
  you are not illuminated by the full moon, you will fall into a state of potential
  madness. Status of latent madness: You usually yearn for human warm blood and fresh
  flesh and blood. If the creatures you meet pass Difficulty Value 15 Intuition (INT)
  appraisal, they will obviously feel your suppressed or unsuppressed killing intent.
  Unless there are special circumstances, the symptoms of madness you usually fall
  into default to violent tendencies. The full moon shines: You immediately fall into
  a state of madness, and the desire for...'
```





- **Rule:** **Full Moon Curse** is an inherent effect once possessing **The Power of the Living Corpse**, and cannot be recorded or stolen.
- **Rule:** Unlike werewolves, even if you are not illuminated by the full moon, you will fall into a state of potential madness.
- **Status of latent madness:** You usually yearn for human warm blood and fresh flesh and blood. If the creatures you meet pass **Difficulty Value 15** Intuition (INT) appraisal, they will obviously feel your suppressed or unsuppressed killing intent. Unless there are special circumstances, the symptoms of madness you usually fall into default to violent tendencies.
- **The full moon shines:** You immediately fall into a state of madness, and the desire for blood and flesh becomes extremely serious.
- **If you don’t (i.e., do not give up self-control):** You continually lose 1 action to suppress the state, at the cost of intense pain, and you don’t gain the frantic immediate action benefit of full moon madness.
- **Sedatives:** If you take sedatives (two and a half pills), you don’t need to suppress the madness and you can act normally, but the same type will be invalid after 4 doses.
- **Time limit:** Without a sedative and without doing so, any actions other than Freedom/Swift will not be possible if it exceeds 2 hours.
- **Special:** When acquiring a new full moon curse, the original full moon curse will be overwritten.

- **Effect:** Full Moon Curse resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
