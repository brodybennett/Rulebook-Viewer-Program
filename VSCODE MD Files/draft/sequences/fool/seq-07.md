---
title: 'Sequence 7: Magician'
id: fool-seq-07
tags:
- pathway:fool
- sequence:7
---






# Fool Pathway: Sequence 7

## Magician

- See also: Pathway containing Sequence 7: Magician

You possess fast casting skills: no need to chant spells, no need to infuse spirituality-just a simple action lets you cast the corresponding spell or spell-like ability, including:
- Injury Transfer
- Flame Jump
- Manipulate Flames
- Air Bomb
- Paper Doll Substitute
- Illusion (create hallucinations)
- False "breathing underwater"
- Bone Softening
- Turn Paper into Soldiers

## Advancement

### Main Materials

- A piece of the real rhizome of the Misty Treant
- All the spinal fluid of the evil-patterned black panther

### Auxiliary Materials

- Pure water x60ml
- Misty treant juice x30ml
- Water-shaped gem powder x3g
- Psychedelic essential oil x4 drops

### Acting Rules

- Do more active performances, but don't do unprepared performances.
- Challenge the impossible-even if the final result is only false, try to get the applause of the audience.
- Control the attention of the target.

## Extraordinary Abilities

### Attribute Gain

- **Intuition (INT)** +1
- **Agility (DEX)** +2
- Your **skillful hand** rises by 1 level.

Performance improvement:
- Every time you complete a well-prepared performance that conforms to the rules of magician impersonation, your **performance skill** increases by 1 level.
- From advanced -> proficient, proficient -> erudite, and erudite -> master, it takes **2**, **3**, and **4** times to improve respectively.

### Injury Transfer

```yaml ability
id: fool-seq-07-injury-transfer
name: Injury Transfer
pathway: fool
sequence: 7
status: adapted
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose 1 living creature whose wound your limb touched.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Check is only required when forcing hostile wound relocation; self-relocation is automatic.
scaling:
- when: target_is_dying
  changes:
    effect_note: Fatal wound can be moved to non-fatal location to end dying state.
- when: hostile_vital_transfer
  changes:
    opposed_by: physical_defense
    effect_note: Successful transfer can apply corresponding critical-location consequences.
tags:
- defense
- healing
- offense
- utility
text: 'Use: 1 Casting Action Cost: 2 spirit points Targeting and range: Choose 1 living
  creature whose wound your limb touched. Effect: You transfer the wound in the vital
  position to less important places such as the arm, turning the fatal injury into
  a minor injury. [[Vital Strike]] If the creature is under one type of vital strike
  effect, you can transfer the vital strike effect of this part to another limb part
  (e.g., transfer the vital strike effect of the head to the arm), and the shock and
  extra damage brought by the vital strike will be transferred remove. The creature
  suffers the vital blow effect of the arm, and the additional damage that is not
  originally included will also be reflect...'
```





- **Use:** 1 **Casting Action**
- **Cost:** 2 **spirit points**
- **Targeting and range:** Choose 1 living creature whose wound your limb touched.
- **Effect:** You transfer the wound in the vital position to less important places such as the arm, turning the fatal injury into a minor injury.
  - [[Vital Strike]]

1. If the creature is under one type of vital strike effect, you can transfer the vital strike effect of this part to another limb part (e.g., transfer the vital strike effect of the head to the arm), and the shock and extra damage brought by the vital strike will be transferred remove.  
   - The creature suffers the vital blow effect of the arm, and the additional damage that is not originally included will also be reflected in the arm.
2. If the creature is dying, the fatal injury can be transferred to the non-fatal part; multiple fatal injuries can be transferred multiple times to terminate the dying.  
   - [[Dying]]
3. If you want to transfer the wound on the enemy's arm to his head, fighting against physical defense, you will be able to do it successfully and cause corresponding additional damage, but this usually can only expose the other person's skin and bones at most, unless the transfer is fatal hurt.  
   - [[Physical Defense]]
4. A creature's wound can only be transferred on itself; the wound cannot be transferred from one person to another.

- **Limits:** As described in this section's prose.


### Flame Jump

```yaml ability
id: fool-seq-07-flame-jump
name: Flame Jump
pathway: fool
sequence: 7
status: adapted
type: active
action: swift
cost:
  spirituality: 3
roll: 1d20 + @attr.dex + @skill.dodge
opposed_by: difficulty_value
range: Choose a fire or flame whose location you know, within 30 meters.
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.dex + @skill.dodge
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted check is only for edge-case reactive escapes and hazard timing; normal flame-to-flame reposition is deterministic.
scaling:
- when: used_as_reactive_escape
  changes:
    effect_note: May be declared at free-action priority to avoid eligible incoming damage.
- when: incoming_attack_is_bullet_or_lightning_or_similar
  changes:
    effect_note: Flame Jump avoidance clause does not apply.
- when: sequence <= 6
  changes:
    range: Choose a fire or flame whose location you know, within 40 meters.
tags:
- ritual
- mobility
- offense
text: 'Use: 1 Swift Action Limits: 1 time per round Cost: 3 spirituality points Targeting
  and range: Choose a fire or flame whose location you know, within 30 meters. Effect:
  The fire you left on yourself and the original flame flash, similar to teleportation,
  with the help of the special spirit world. If there is an ignited flame within 30
  meters, after casting, your body will be covered by flames, and the flame you selected
  will immediately rise to the size of a human figure, allowing you to jump out of
  it. If there is fire (matches and other combustibles) within 30 meters, you need
  to use the fire to ignite it first before using this ability on it. This ability
  can be used to avoid damage wit...'
```





- **Use:** 1 **Swift Action**
- **Limits:** 1 time per round
- **Cost:** 3 **spirituality points**
- **Targeting and range:** Choose a fire or flame whose location you know, within 30 meters.
- **Effect:** The fire you left on yourself and the original flame flash, similar to teleportation, with the help of the special spirit world.

1. If there is an ignited flame within 30 meters, after casting, your body will be covered by flames, and the flame you selected will immediately rise to the size of a human figure, allowing you to jump out of it.
2. If there is fire (matches and other combustibles) within 30 meters, you need to use the fire to ignite it first before using this ability on it.
3. This ability can be used to avoid damage with free-action priority, except against bullets, light, lightning, or similar high-speed damage. You cannot also use quick dodge during Flame Jump. You may combine it with a paper doll double; for area damage, if Flame Jump exits the affected area, you do not take the paper-doll half-damage transfer.
4. The flames you can jump include poisonous flames and black flames, and you will not be hurt by them only at the moment when your flames jump.

Special:
- When holding the ability of flame jump, you can sense flames that have ignited within 30 meters around you.

### Manipulate Flames

```yaml ability
id: fool-seq-07-manipulate-flames
name: Manipulate Flames
pathway: fool
sequence: 7
status: canonical
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: physical_defense
range: Choose a flame or kindling within 30 meters of a location you know (any combustibles
  including matches).
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Primary mode is pillar fire (2d6). Other modes swap damage profile as listed in scaling.
scaling:
- when: matchbox_explosion_mode
  changes:
    damage_roll: 6d6
    effect_note: Consumes one qualifying matchbox use; cannot combine with other modes.
- when: weapon_coating_mode
  changes:
    damage_roll: 1d6
    duration: sustained
    upkeep_cost: {spirituality: 1}
- when: chained_trigger_mode
  changes:
    effect_note: Up to 3 rapid spark triggers per snap sequence before further cast-spend pressure applies.
damage_types:
- fire
tags:
- ritual
- control
- defense
- offense
text: 'Use: 1 Casting Action Cost: 1 point of spirituality Requirements: You must
  snap your fingers or simulate the sound of snapping your fingers. Targeting and
  range: Choose a flame or kindling within 30 meters of a location you know (any combustibles
  including matches). Limits: You can only choose 1 usage at a time. The usage options
  are: Choose one or more fire seeds. Whenever a creature reaches the location of
  the fire seeds, you can make it shoot up a pillar of fire, causing damage. Each
  fire pillar causes 2d6 fire damage. Mysticism against physical defense, ignoring
  agility and dodge.'
```





- **Use:** 1 **Casting Action**
- **Cost:** 1 point of **spirituality**
- **Requirements:** You must snap your fingers or simulate the sound of snapping your fingers.
- **Targeting and range:** Choose a flame or kindling within 30 meters of a location you know (any combustibles including matches).
- **Limits:** You can only choose 1 usage at a time. The usage options are:

1. Choose one or more fire seeds. Whenever a creature reaches the location of the fire seeds, you can make it shoot up a pillar of fire, causing damage.
   - Each fire pillar causes **2d6** fire damage.
   - **Mysticism** against physical defense, ignoring agility and dodge.
   - This ignores high-speed dodge.
   - Each finger snap triggers 1 spark, up to 3 with no disadvantages; repeated bursts consume spirituality.
   > **GM Note:** Example from RAW: put matches in a straight line; as the enemy moves, trigger up to 3 matches in turn to produce 3 pillars of fire.
2. Choose a whole box of matches (at least 20 matches left in the box). The small space in the box lets you create a small explosion.
   - Use this box of matches as a kindling.
   - Causes **6d6** fire damage at a time.
   - Cannot trigger other uses.
3. Continuously add **1d6** fire damage to the weapon that draws paper as a soldier.
   - Consume **1 spirituality point** every round.
4. Control the fireballs and flames from the enemy to take effect: delay the explosion or slow the speed.
   - Make the final value of the corresponding identification **-4**.

Special:
- The magician can only control fire for a moment; you can't shape fire for a long time, or create a wall of fire.
- After the potion is digested or promoted: you can start to summon flame out of thin air; no fire is needed, but it can only last for a moment unless there is a combustible object. It is too late to use this method to jump the flame.

- **Effect:** Manipulate Flames resolves using its yaml ability block and section prose.


### Air Bomb

```yaml ability
id: fool-seq-07-air-bomb
name: Air Bomb
pathway: fool
sequence: 7
status: canonical
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.shooting
opposed_by: physical_defense
range: Select 1 or more targets within the field of vision.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.shooting
  damage_roll: 1d8
  heal_roll: null
  effect_roll: null
  notes: Check ignores agility/dodge components as stated in prose.
scaling:
- when: second_shot_same_cast_action
  changes:
    check_penalty: -2
- when: third_shot_same_cast_action
  changes:
    check_penalty: -4
damage_types:
- physical
tags:
- ritual
- defense
- offense
text: 'Use: 1 Casting Action Cost: 1 point of spirituality Targeting and range: Select
  1 or more targets within the field of vision. Requirements: Need to snap fingers
  or simulate the sound of snapping fingers. Check: Intuition (INT) + shooting against
  physical defense, ignoring the agility and dodge in physical defense. Effect: If
  the identification is successful, it causes 1d8 physical damage (comparable to a
  custom revolver). Limits: You can fire 3 times in a single Casting Action: From
  the second shot: -2 penalty'
```





- **Use:** 1 **Casting Action**
- **Cost:** 1 point of **spirituality**
- **Targeting and range:** Select 1 or more targets within the field of vision.
- **Requirements:** Need to snap fingers or simulate the sound of snapping fingers.
- **Check:** Intuition (INT) + shooting against physical defense, ignoring the agility and dodge in physical defense.
- **Effect:** If the identification is successful, it causes **1d8** physical damage (comparable to a custom revolver).
- **Limits:** You can fire 3 times in a single Casting Action:
  - From the second shot: **-2** penalty
  - From the third shot: **-4** penalty

### Paper Doll Substitute

```yaml ability
id: fool-seq-07-paper-doll-substitute
name: Paper Doll Substitute
pathway: fool
sequence: 7
status: adapted
type: active
action: free
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Check is used for anti-divination mode only; substitution displacement itself has no roll.
scaling:
- when: anti_divination_mode
  changes:
    opposed_by: difficulty_value
    effect_note: Success excludes chosen information from relevant divination channels.
- when: area_attack_and_exit_fails
  changes:
    effect_note: Take half damage (rounded up).
tags:
- ritual
- defense
- utility
text: 'Use: 1 free action Cost: 5 spirituality points and 1 paper figurine Effect:
  Choose one of the following effects to take effect: Immediately before you are about
  to be attacked, you take the initiative to replace yourself with a paper doll, resisting
  an attack or other effects, completely nullifying the effect. You reappear at most
  8 meters away; the latter is incidental displacement effect. Special (area attacks):
  If the doubleaTMs displacement doesnaTMt allow you to leave the area of influence,
  you take half damage. Half damage is rounded up. Must be used immediately. Because
  it is an active ability, you must recognize the corresponding threat to be a substitute.
  An effect that has alrea...'
```





- **Use:** 1 **free action**
- **Cost:** 5 **spirituality points** and 1 **paper figurine**
- **Effect:** Choose one of the following effects to take effect:

1. Immediately before you are about to be attacked, you take the initiative to replace yourself with a paper doll, resisting an attack or other effects, completely nullifying the effect. You reappear at most **8 meters** away; the latter is incidental displacement effect.
   - Special (area attacks): If the double's displacement doesn't allow you to leave the area of influence, you take **half damage**. Half damage is rounded up.
   - Must be used immediately. Because it is an active ability, you must recognize the corresponding threat to be a substitute.
   - An effect that has already taken effect on you cannot be a substitute. Example: once the plague of the witch takes effect, the subsequent deterioration cannot be a substitute.
  - Note: Against targets higher than your Sequence by 2+, this substitute is too late to apply.
2. You destroy a paper figurine with flames, etc., and choose 1 item of specific mystic information related to you (e.g., you plan to attack someone next). Realize anti-divination, and conduct a mystic appraisal as the difficulty of anti-divination.
   - When successful, this information will be excluded in related divination, spiritual intuition, prophecy, unless it exceeds the corresponding difficulty.
   - [[id:alias-anti-divination|Anti-Divination]]
3. You turn a paper figurine into an image that is exactly the same as you. In the eyes of others, it is another you, but closer to a wax figure that is completely the same but does not move. Hallucinations can bring it to life.
   - Creating hallucinations can last for **half an hour** in this usage.
   - Can fake the color of the aura, the ups and downs of the limbs, etc.
   - Cannot communicate.
   - Special: When the paper figurine turns into a dummy, your body can become invisible, but you cannot leave the dummy within **8 meters**.

- **Limits:** As described in this section's prose.


### Illusion

```yaml ability
id: fool-seq-07-illusion
name: Illusion
pathway: fool
sequence: 7
status: adapted
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.cha + @skill.deception
opposed_by: difficulty_value
range: Affect the environment within **8 meters** around you.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.deception
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Illusion creation contests observer verification checks (detection/spiritual intuition context).
scaling:
- when: target_sequence_at_least_user_plus_1
  changes:
    effect_note: Higher-sequence observers default to identifying the illusion as false.
tags:
- ritual
- control
- detection
- social
text: 'Use: 1 Casting Action Cost: 2 spiritual points Targeting and range: Affect
  the environment within 8 meters around you. Effect: You influence your surroundings
  to create near-real illusions with colours, sounds, and smells; you create an illusion.
  The content of the hallucination is customized; the created hallucination has color,
  sound, and smell at the same time, and is extremely real. Any creature that witnesses
  the illusion must actively recognize that it may be an illusion and try to identify
  it before fighting. Confrontation is a deception against detection/inspiration identification.
  Because this ability will generally be exposed after being used once, the subject
  deceived by the il...'
```





- **Use:** 1 **Casting Action**
- **Cost:** 2 **spiritual points**
- **Targeting and range:** Affect the environment within **8 meters** around you.
- **Effect:** You influence your surroundings to create near-real illusions with colours, sounds, and smells; you create an illusion.

1. The content of the hallucination is customized; the created hallucination has color, sound, and smell at the same time, and is extremely real.
2. Any creature that witnesses the illusion must actively recognize that it may be an illusion and try to identify it before fighting.
3. Confrontation is a deception against detection/inspiration identification. Because this ability will generally be exposed after being used once, the subject deceived by the illusion will continue to have doubts about the illusion; creating illusions is usually only used once for the same person.

Special:
- Beings higher than your Sequence by 1+ default to directly perceiving hallucinations as false.

- **Limits:** As described in this section's prose.


### False "breathing underwater"

```yaml ability
id: fool-seq-07-false-breathing-underwater
name: False "breathing underwater"
pathway: fool
sequence: 7
status: canonical
type: active
action: cast
cost:
  sanity: 1
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
  notes: Utility tube effect; no explicit check or contested roll is described.
scaling: []
conditions:
- invisible
tags:
- stealth
text: 'Use: As a Casting Action Cost: 1 sanity point Effect: You create an invisible
  thin tube of air that is invisible, 5 meters long. You can breathe through its mouth
  and exhale through its nose, ensuring "underwater breathing" in an environment with
  a water depth of less than 5 meters. Or, in an environment with toxins and harmful
  gases, you can use it to breathe air up to 5 meters above to avoid ingesting toxins,
  as long as the range of toxins does not exceed this length.'
```





- **Use:** As a **Casting Action**
- **Cost:** 1 **sanity point**
- **Effect:** You create an invisible thin tube of air that is invisible, **5 meters** long.
  - You can breathe through its mouth and exhale through its nose, ensuring "underwater breathing" in an environment with a water depth of less than **5 meters**.
  - Or, in an environment with toxins and harmful gases, you can use it to breathe air up to **5 meters** above to avoid ingesting toxins, as long as the range of toxins does not exceed this length.

- **Limits:** As described in this section's prose.


### Bone Softening

```yaml ability
id: fool-seq-07-bone-softening
name: Bone Softening
pathway: fool
sequence: 7
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
  effect_roll: 1d6
  notes: Effect roll applies only to critical-location redirection branch (1-5 redirected, 6 avoids vital hit).
scaling:
- when: critical_redirection_branch
  changes:
    effect_roll: 1d6
    effect_note: Resolve redirected hit location table.
conditions:
- restrained
tags:
- control
text: 'You soften your bones, freeing you from handcuffs, ropes, and boxes. Use: 1
  Casting Action. Whenever you fall into a grapple, or get restrained by handcuffs,
  ropes, and other small things, you can soften your bones and break free immediately.
  This does not include oversize bondage where the xeno demigod lets your clothing
  bind yourself. Use: 1 Casting Action. Whenever you realize that you are about to
  fall into a critical blow, even if you are in a state of physical restraint, you
  can soften your bones, barely bend your waist, and your upper body will fall backwards,
  avoiding this time vital blow. Exclude the vital parts that you avoided, and perform
  a 1d6: 1a5 is other vital points; 6 me...'
```





You soften your bones, freeing you from handcuffs, ropes, and boxes.

1. **Use:** 1 **Casting Action**. Whenever you fall into a grapple, or get restrained by handcuffs, ropes, and other small things, you can soften your bones and break free immediately.
   - This does not include oversize bondage where the xeno demigod lets your clothing bind yourself.
2. **Use:** 1 **Casting Action**. Whenever you realize that you are about to fall into a critical blow, even if you are in a state of physical restraint, you can soften your bones, barely bend your waist, and your upper body will fall backwards, avoiding this time vital blow.
   - Exclude the vital parts that you avoided, and perform a 1d6: 1-5 is other vital points; 6 means the vital points are not hit.

- **Effect:** Bone Softening resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Turn Paper into Soldiers

```yaml ability
id: fool-seq-07-turn-paper-into-soldiers
name: Turn Paper into Soldiers
pathway: fool
sequence: 7
status: adapted
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + @attr.dex + @skill.fighting
opposed_by: physical_defense
range: self
target: created paper weapon
duration: 5 minutes
dice:
  check_roll: 1d20 + @attr.dex + @skill.fighting
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted to include downstream attack resolution when using created paper weapons; base cast action itself has no contested check.
scaling:
- when: weapon_hits_hard_object
  changes:
    effect_note: Paper weapon breaks after 3 hard-object impacts.
- when: sequence <= 6
  changes:
    duration: 7 minutes
    effect_note: Paper weapon breaks after 4 hard-object impacts.
tags:
- ritual
- defense
- offense
text: 'You can turn paper into sharp objects, and also into sticks, bricks, and other
  weapons for a short time. Use: 1 Casting Action Cost: 1 point of spirituality Requirements:
  As long as you prepare paper corresponding to the approximate shape, you can make
  it sharp immediately after ashakinga and turn it into a weapon. The effect of the
  manufactured weapon is equal to that in aWeapon Paradigm,a but you can only manufacture
  cold weapons, not complex hot weapons. The effect lasts five minutes, and can be
  used by others. [[Weapon Paradigm]] Although it becomes sharper, it still does not
  get rid of the characteristics of paper. If a paper weapon hits a hard object such
  as armor, it will be damage...'
```





You can turn paper into sharp objects, and also into sticks, bricks, and other weapons for a short time.

- **Use:** 1 **Casting Action**
- **Cost:** 1 point of **spirituality**
- **Requirements:** As long as you prepare paper corresponding to the approximate shape, you can make it sharp immediately after "shaking" and turn it into a weapon.

1. The effect of the manufactured weapon is equal to that in "Weapon Paradigm," but you can only manufacture cold weapons, not complex hot weapons. The effect lasts **five minutes**, and can be used by others.  
   - [[Weapon Paradigm]]
2. Although it becomes sharper, it still does not get rid of the characteristics of paper. If a paper weapon hits a hard object such as armor, it will be damaged after being used **three times**.
3. Different weapons require different shapes of paper. Example: whips need long strips of paper; sticks need to roll the paper together first. You need to cut it in advance or use it according to the situation.

- **Effect:** Turn Paper into Soldiers resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Quick-casting technique

```yaml ability
id: fool-seq-07-quick-casting-technique
name: Quick-casting technique
pathway: fool
sequence: 7
status: canonical
type: active
action: free
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
- offense
text: 'Limits: Once per round Use: As a free action Effect: You can use any one of
  the spellcasting action abilities of: Manipulate Flames Air Bomb Turn Paper into
  Soldiers False "breathing underwater" Bone Softening'
```





- **Limits:** Once per round
- **Use:** As a **free action**
- **Effect:** You can use any one of the spellcasting action abilities of:
  - Manipulate Flames
  - Air Bomb
  - Turn Paper into Soldiers
  - False "breathing underwater"
  - Bone Softening
  - Injury Transfer
- (This is a potion benefit that cannot be stolen or recorded.)

### Magician's performance props

```yaml ability
id: fool-seq-07-magicianatms-performance-props
name: MagicianaTMs performance props
pathway: fool
sequence: 7
status: canonical
type: passive
action: none
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
  notes: Inventory-slot framework only; checks happen in downstream use or GM adjudication.
scaling: []
tags:
- utility
text: 'A prepared magician is completely different from an unprepared magician. Many
  abilities need corresponding materials prepared for consumption in advance. Excluding
  other items you usually carry, the number of props you can prepare is: Wearing normal
  clothes: 4 material slots with 2a4 pockets. Wear a performance tuxedo: 8 material
  slots, with 4a8 pockets, including hidden pockets. Wearing Spellcasting Wizard Robes:
  12 material slots with 8a12 pockets, including secret pockets. The props do not
  need to be determined by your reputation because they are cheap. Slots occupied
  by different props: Paper doll stand-in: every 3 paper doll stand-ins occupy one
  slot; you need to cut them out in adva...'
```





A prepared magician is completely different from an unprepared magician. Many abilities need corresponding materials prepared for consumption in advance. Excluding other items you usually carry, the number of props you can prepare is:

- Wearing normal clothes: **4 material slots** with 2-4 pockets.
- Wear a performance tuxedo: **8 material slots**, with 4-8 pockets, including hidden pockets.
- Wearing Spellcasting Wizard Robes: **12 material slots** with 8-12 pockets, including secret pockets.

The props do not need to be determined by your reputation because they are cheap. Slots occupied by different props:

1. Paper doll stand-in: every **3** paper doll stand-ins occupy **one** slot; you need to cut them out in advance.
2. Matchbox: each box of matches occupies **1** slot. There are **90** matches in a box, and every **30** matches is placed in a slot.
3. Drawing Paper into Soldiers: any kind of paper that can be turned into drawing paper into soldiers occupies **1** slot; you need to decide the shape in advance.

The rest of the props are determined by the GM according to their size. If you do not adjust the position of the props in advance before each battle, when a big failure occurs, you will be regarded as taking the wrong props (the substitute took out a match).

> **GM Note:** RAW guidance: if you want to play a magician, a performance tuxedo is the most appropriate option; wizard robes may affect the performance.

- **Effect:** MagicianaTMs performance props resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
