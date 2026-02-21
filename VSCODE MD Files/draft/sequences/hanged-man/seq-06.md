---
title: 'Sequence 6: Rose Bishop'
id: hanged-man-seq-06
tags:
- pathway:hanged-man
- sequence:6
---






# Hanged Man Pathway: Sequence 6

## Rose Bishop

> **Lore:** Mastering flesh and blood magic, Bishop Rose excels at physical healing and can become pure flesh and blood to evade detection by hiding inside other bodies—at a lethal cost to the host when it exits. It must frequently replenish flesh and blood.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Constitution +2, Strength +2, Agility (DEX) +1, Intuition (INT) +1.
- **Skills:**
  - Your Biology is included in your [[Rapid Improvement Category]] (up to Proficient).
  - Occult can be promoted to [[Master]].

### Bishop Rose Traits

```yaml ability
id: hanged-man-seq-06-bishop-rose-traits
name: Bishop Rose Traits
pathway: hanged-man
sequence: 6
status: canonical
type: passive
action: none
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
  notes: Passive trait package; no roll required.
scaling: []
tags:
- healing
- offense
text: You are long-term considered a Corrupted Creature [[Corrupted Creature]]. You
  cannot be critically hit [[Critical Hit]] by effects other than the [[Weakness Attack]]
  of the [[Red Priest]]. Your physical state no longer represents your remaining health,
  and you can survive even if you are almost turned into a corpse. This is a potion
  effect and cannot be stolen or recorded.
```





- You are long-term considered a **Corrupted Creature** [[Corrupted Creature]].
  - You cannot be critically hit [[Critical Hit]] by effects other than the [[Weakness Attack]] of the [[Red Priest]].
- Your physical state no longer represents your remaining health, and you can survive even if you are almost turned into a corpse.
- This is a potion effect and cannot be stolen or recorded.

- **Effect:** Bishop Rose Traits resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Flesh Devour

```yaml ability
id: hanged-man-seq-06-flesh-devour
name: Flesh Devour
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Touch; one helpless creature.
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Passive/active modes scale with Flesh Stack; damage dice apply only at higher stacks.
scaling:
- when: flesh_stack_50_or_more
  changes:
    effect_note: Gain 3 Armor and 3 Physical Damage Reduction (non-stacking).
- when: flesh_stack_120_or_more
  changes:
    effect_roll: 1d3
    effect_note: As a Big Volume Creature, melee vs medium targets adds 1d3 damage and +1m reach.
tags:
- utility
text: 'Cost: No Sanity / Rationality [[Sanity / Rationality]]. Use: Varies by creature
  size (swift / casting / full-round; see Devouring time by size below). Targeting
  and range: Touch; one helpless creature. Effect: The target is brought into your
  flesh. Creatures brought into your flesh become your Flesh Stack and provide Satiety
  [[Satiety]]. Flesh Stack is the value that determines how much flesh and blood you
  can hold; you can stack it up to 150. A creature provides Flesh Stacks based on
  the size table below. Excluding [[Extraordinary]], larger creatures usually provide
  more Flesh Stacks.'
```





- **Cost:** No **Sanity / Rationality** [[Sanity / Rationality]].
- **Use:** Varies by creature size (swift / casting / full-round; see “Devouring time by size” below).
- **Targeting and range:** Touch; one helpless creature.
- **Effect:**
  - The target is brought into your flesh.
  - Creatures brought into your flesh become your **Flesh Stack** and provide **Satiety** [[Satiety]].
  - **Flesh Stack** is the value that determines how much flesh and blood you can hold; you can stack it up to 150.
  - A creature provides Flesh Stacks based on the size table below. Excluding [[Extraordinary]], larger creatures usually provide more Flesh Stacks.
- **Flesh Stacks by size (life limit):**
  - (If the following creatures die tragically and their limbs are mutilated, the host will judge how much flesh and blood are left.)
  1. Tiny creatures (bugs, ants): Count every 10 as 1; 1 Flesh Stack per ten.
  2. Small creatures (mouse, bird, hand, steak): 2d2 Flesh Stacks.
  3. Small and medium-sized creatures (cats, dogs): 7+1d3 Flesh Stacks; large dogs get an additional +1d3.
  4. Medium-sized creatures (humans, murlocs, young lions or tigers): 10+2d3 Flesh Stacks.
  5. Medium and large creatures (adult lions, tigers, bears, cows): 20 Flesh Stacks; meat pigs, etc. +1d5.
  6. Large creatures (giants, large creatures, Feysacs): 20+2d4 Flesh Stacks.
  7. Very large creatures (creatures comparable in size to a ship, 4-meter or 6-meter giants, creatures that can cause ship destruction): 60+10d2 Flesh Stacks, or even more.
  8. Extraordinary-related creatures: Directly calculate the upper limit of blood volume Blood Volume, and restore their **Spirituality** up to the target’s maximum; the spiritual recovery can exceed half of the upper limit.
  - The above random values determine individual differences.
- **Devouring time by size:**
  - Devouring ① requires only 1 Swift Action.
  - ②–③: 1 Casting Action.
  - ④–⑤: 1 Full-Round Action.
  - ⑥: 2 full-round actions.
  - ⑦: At least 3 full-round actions (depending on the situation).
- **Special (Extraordinary-related creatures):**
  - Ensure their characteristics [[Characteristics]] have been extracted first; otherwise devouring may lead to promotion identification.
  - If characteristics are not extracted first, devouring may trigger a standard promotion check when grazing ends.

- **Limits:** As described in this section's prose.


### Flesh Alteration

```yaml ability
id: hanged-man-seq-06-flesh-alteration
name: Flesh Alteration
pathway: hanged-man
sequence: 6
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
  notes: No explicit dice expression in source text.
scaling: []
tags:
- defense
- offense
text: 'Effect: You can alter your flesh; your flesh is affected by your Flesh Stack.
  This ability has two usages: passive and active. Passive (subordinate to Flesh Devour):
  This passive part cannot be recorded. Stealing will not cause flesh and blood to
  disintegrate. This is a permanent physical change; it does not require continued
  spell consumption to maintain. When your Flesh Stack reaches 50: Gain 3 Armor [[Armor]]
  and 3 Physical Damage Reduction [[Physical Damage Reduction]]. These do not stack
  with other physical benefits.'
```





- **Effect:** You can alter your flesh; your flesh is affected by your Flesh Stack.
- This ability has two usages: passive and active.
- **Passive (subordinate to Flesh Devour):**
  - This passive part cannot be recorded. Stealing will not cause flesh and blood to disintegrate.
  - This is a permanent physical change; it does not require continued spell consumption to maintain.
  - When your Flesh Stack reaches 50:
    - Gain 3 Armor [[Armor]] and 3 Physical Damage Reduction [[Physical Damage Reduction]].
    - These do not stack with other physical benefits.
  - When your Flesh Stack reaches 120:
    - Strength +1; Constitution +1.
    - You are considered a **Big Volume Creature** [[Big Volume Creature]].
    - **Large creature benefits (while considered a Big Volume Creature):**
      - Melee against medium-sized creatures increases damage by 1d3 and attack range by 1 meter.
      - Medium-sized creatures give you +2 to identification and attack checks.
  - Being bulky affects your appearance, but you can compress flesh so that the benefits of bulky creatures disappear.
    - Compressing flesh increases flesh density to avoid changes in appearance.
    - Compressing flesh does not affect the attribute bonuses gained from Flesh Stack.
  - Flesh Stack contributes to your maximum Vitality first, until your max Vitality reaches 80.
    - Given a Flesh Stack cap of 150, on the premise of not affecting max Vitality, the Flesh Stack you can freely use is: `150-(80-your max Vitality)`.
- **Active:** You can change the appearance and form of your physical body.
  1. **Appearance adjustment:** You can change your initial charm from 1 to 6.
     - Changing 1 point takes 1 day.
     - Changing a major appearance takes 1 week.
     - Unlike [[Faceless]], this change is gradual “pinching and modeling” little by little.
  2. **Incarnation of flesh and blood:** 1 Move Action.
     - Change from a human form into a wriggling pool of flesh and blood.
     - You can enter places that are usually inaccessible, or enter the body of a helpless, voluntary target.
     - While inside, it is up to you to perform flesh and blood fusion; otherwise you simply stay inside.
     - Once incarnated, you have liquid qualities that allow you to seep into floors and similar spaces where struggling creatures are generally inaccessible.
  3. **Fusion of flesh and blood:** 1 spellcasting action.
     - Prerequisite: You are incarnated inside the host’s body.
     - You and the host’s flesh and blood fuse; the threads of the spirit body overlap.
     - This cannot be discovered by the [[Marionette Master]], the [[Eye of the Secret]], etc.
     - This does not include beings higher than Sequence 1.
     - **Warning:** If you perform flesh and blood fusion, getting out of the body causes the death of the host; for each point above 1, you take combat damage.
  4. **Flesh shaping:** 1 Casting Action.
     - Change your body into various shapes and perform corresponding functions (e.g., turn your upper body into a vortex to draw the gas in the area onto you alone; block in front of others to resist damage).
     - You can turn body parts into tools like blades; the effect corresponds to the usual version, excluding precision firearms.
  5. **Flesh Wrap:** 1 attack/Move Action.
     - Prerequisite: Flesh shaping.
     - Wrap objects that have not been transformed into flesh piles inside your body to store or transport them to a safe location for further processing.
     - Wrapped objects cannot be compressed; wrapping objects taller than you can leave them exposed.
     - You can digest wrapped objects at any time.
     - If a contaminated object is not digested in time, the effect ends and it is expelled with damage.

- **Limits:** As described in this section's prose.


### Cellular Proliferation

```yaml ability
id: hanged-man-seq-06-cellular-proliferation
name: Cellular Proliferation
pathway: hanged-man
sequence: 6
status: canonical
type: passive
action: none
cost: {}
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
  notes: No explicit dice expression in source text.
scaling: []
tags:
- healing
- buff
text: 'Effect: Your cells grow faster than normal living organisms. Passive (Flesh
  Stack regeneration): Based on your Flesh Stack, every 12 hours, even if you dont
  devour any flesh and blood, your Flesh Stack value can also be +10. This auto-recovering
  Flesh Stack ends when your upper limit of life reaches 80 [[Life Cap]], because
  the upper limit of life brought by Flesh Stack increases with Sequence; at higher
  Sequence this becomes the corresponding higher upper limit of life. *Flesh Magic:
  You gain the following flesh magic; every Rose Bishop is an expert in flesh magic.
  The following flesh and blood magic are all separate abilities, and only one benefit
  can be selected when creating [[Extraor...'
```





- **Effect:** Your cells grow faster than normal living organisms.
- **Passive (Flesh Stack regeneration):**
  1. Based on your Flesh Stack, every 12 hours, even if you don’t devour any flesh and blood, your Flesh Stack value can also be +10.
  2. This auto-recovering Flesh Stack ends when your upper limit of life reaches 80 [[Life Cap]], because the upper limit of life brought by Flesh Stack increases with Sequence; at higher Sequence this becomes the corresponding higher upper limit of life.

**Flesh Magic:** You gain the following flesh magic; every “Rose Bishop” is an expert in flesh magic. The following flesh and blood magic are all separate abilities, and only one benefit can be selected when creating [[Extraordinary Items]].

- **Limits:** As described in this section's prose.


### Flesh Cloak

```yaml ability
id: hanged-man-seq-06-flesh-cloak
name: Flesh Cloak
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 3
  flesh_stack: 20
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
  notes: No roll required; resistance uses consumed Flesh Stack as a hit buffer.
scaling:
- when: flesh_cloak_max_stack
  changes:
    effect_note: Can consume up to 40 Flesh Stacks per encounter; excess grants no extra benefit.
- when: divine_or_higher_status_damage
  changes:
    effect_note: Divine damage consumes +5 resist times; higher-status damage consumes +3 resist times.
tags:
- ritual
- offense
text: 'Cost: 3 points of Spirituality; 20 Flesh Stacks total (max 40 per encounter).
  Use: 1 Swift Action. Effect: Weave scarlet flesh and fallen blood into a strange,
  viscous red cloak that wraps your body and grants: Gain 5 points of external damage
  reduction [[External Damage Reduction]]; this can be superimposed with the reduction
  from Flesh Stack. The cloak can withstand a limited number of damages equal to the
  value of Flesh Stack consumed. Each time it suffers non-physical damage, deduct
  1 time. If it suffers from divine power [[Divine Power]], deduct 5 times each time.
  It can be repaired by repeated casting.'
```





- **Cost:** 3 points of **Spirituality**; 20 Flesh Stacks total (max 40 per encounter).
- **Use:** 1 Swift Action.
- **Effect:** Weave scarlet flesh and fallen blood into a strange, viscous red cloak that wraps your body and grants:
  1. Gain 5 points of external damage reduction [[External Damage Reduction]]; this can be superimposed with the reduction from Flesh Stack.
  2. The cloak can withstand a limited number of damages equal to the value of Flesh Stack consumed.
     - Each time it suffers non-physical damage, deduct 1 time.
     - If it suffers from divine power [[Divine Power]], deduct 5 times each time.
     - It can be repaired by repeated casting.
  3. Making the Flesh Cloak consumes 20 Flesh Stacks; you can consume up to 40 Flesh Stacks per encounter; consuming more than 40 does not grant additional benefits.
  4. The Flesh Stacks of the Flesh Cloak can be recovered by devouring flesh and blood, which consumes 1 Full-Round Action.
- **Special:**
  - Damage from a target with Status/Rank higher than yours consumes 3 more resist times; holy damage [[Holy Damage]] consumes 5 more times.
  - If it is 2 characters higher than you, regardless of damage type, the cloak is annihilated after resisting 1 effect; holy causes the cloak to not even take effect.  

- **Limits:** As described in this section's prose.


### Flesh Bomb

```yaml ability
id: hanged-man-seq-06-flesh-bomb
name: Flesh Bomb
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: cast
cost:
  blood: 5
roll: 1d20 + @attr.dex + @skill.throwing
opposed_by: physical_defense
range: Choose 1 target; throw against physical defense [[Physical Defense]].
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.dex + @skill.throwing
  damage_roll: 3d6 + 1d6
  heal_roll: null
  effect_roll: null
  notes: Damage roll includes physical (3d6) and poison (1d6); on a miss, damage is halved.
scaling:
- when: check_fails
  changes:
    effect_note: Damage is halved (rounded up) on a failed throw.
- when: limb_thrown
  changes:
    effect_note: Damage is doubled and can affect a 10m area; caster suffers -4 to rolls and halved movement until Flesh Mending.
- when: planted_bomb
  changes:
    cost: {flesh_stack: 5}
    effect_note: Planted bombs can be detonated within 100m; detonation costs 3 spirituality.
tags:
- debuff
- defense
- offense
text: 'This ability has two uses. Thrown flesh bomb Cost: Consumes 5 points of blood.
  Use: 1 spellcasting action. Targeting and range: Choose 1 target; throw against
  physical defense [[Physical Defense]]. Effect: Deal 3d6 physical damage and 1d6
  poison damage [[Poison Damage]]. On failure, damage is halved (rounded up).'
```





- This ability has two uses.

1. **Thrown flesh bomb**
   - **Cost:** Consumes 5 points of blood.
   - **Use:** 1 spellcasting action.
   - **Targeting and range:** Choose 1 target; “throw” against physical defense [[Physical Defense]].
   - **Effect:**
     - Deal 3d6 physical damage and 1d6 poison damage [[Poison Damage]].
     - On failure, damage is halved (rounded up).
     - Two creatures standing next to each other count as the same target.
   - **Special:**
     - It consumes blood only; ignore the pile limit.
     - You may tear off one of your limbs and throw it:
       - The bomb’s damage is doubled.
       - This usage can affect all creatures within a 10-meter area.
       - You take a -4 penalty each time you fight or roll; movement is halved, until you use [[Flesh Mending]] (restores Flesh Stacks up to max).
2. **Planted flesh bomb**
   - **Cost:** Consumes 5 Flesh Stacks.
   - **Use:** 1 spellcasting action; requires physical contact.
   - **Targets:** An ordinary person who is helpless, voluntary, or a target who is 1 lower than you.
   - **Effect:** After casting, the target is regarded as being planted by you as a flesh bomb (status).
     - **Planting a flesh bomb status:** There is a flesh bomb in the body.
       - Creatures that are less than large in size are only allowed to stack 5 points of flesh.
       - The owner of the flesh bomb can detonate them at any time within a range of 100 meters.
       - Damage caused by the bomb in the body is doubled.
     - **Detonate:** Detonating a bomb is a Casting Action; costs 3 points of Spirituality; per round, you can detonate at most equal to the number of Inspirations.
     - Ordinary people who are detonated die on the spot by default and become a blood storm.
       - The corpse causes another 1 time of damage to creatures around 5 meters away from the conventional blood bomb; it is no longer an explosion, but depends on the harmful substances of the blood storm and the human body.
   - (Generally speaking, this use can’t work on yourself, because the bomb will also hurt you, and the damage caused is not worth the loss.)

- **Limits:** As described in this section's prose.


### Flesh Manipulation

```yaml ability
id: hanged-man-seq-06-flesh-manipulation
name: Flesh Manipulation
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 3
  flesh_stack: 20
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
  notes: Healing is based on Flesh Stack consumed (up to 20 per use); no explicit dice roll.
scaling:
- when: mutilated_from_flesh_bomb
  changes:
    effect_note: Consumes the same Flesh Stack lost to restore the body.
tags:
- control
text: 'Use: 1 Swift Action; once per round. Effect: Animate the flesh and blood of
  a lifeless host to perform 1 action. Example: You can use your Flesh Cloak or [[Flesh
  Blanket]] to grapple [[Grapple]] the enemy. The bonus of flesh is its Flesh Stack/2.
  The Flesh Stack also represents its Vitality. For the rest, refer to Flesh Blanket.
  Additional uses (each consumes a free action controlled by flesh and blood): Precisely
  manipulate the shape of flesh and blood; make it melt and become fluid; draw words
  and portraits yourself.'
```





- **Use:** 1 Swift Action; once per round.
- **Effect:** Animate the flesh and blood of a lifeless host to perform 1 action.
  - Example: You can use your Flesh Cloak or [[Flesh Blanket]] to grapple [[Grapple]] the enemy.
    - The bonus of flesh is its Flesh Stack/2.
    - The Flesh Stack also represents its Vitality.
    - For the rest, refer to Flesh Blanket.
- **Additional uses (each consumes a free action controlled by flesh and blood):**
  1. Precisely manipulate the shape of flesh and blood; make it melt and become fluid; draw words and portraits yourself.
  2. Based on ①, stop all reactions of the flesh and blood and even make the blood solid without polluting the surroundings.
  3. Think of it as a kind of “clone” of you: let it enter a specific area instead of you.
     - It cannot exceed 100 meters from you.
     - You do not share your senses with it; it can at most work within your sight.
  4. Based on ③, because it has no intelligence and you are manually manipulating it, you cannot “create” flesh and blood creatures to become servants.
     - Manipulation precision is not enough; you can only use abstract forms such as cloaks and giant carpets.
  5. Leave a simple spiritual imprint in flesh and blood (e.g., a sentence as a message).
     - Other Rose Bishops can perceive the content of the spiritual imprint.
     - Other Rose Bishops can also obtain the information you left by divination on the flesh and blood.
- **Passive:** When you have this ability, you can directly use external flesh and blood with no living owner as the material for your flesh magic (e.g., immediately suppress the life of a bomb-dead host into a cape).

- **Limits:** As described in this section's prose.


### Flesh Healing

```yaml ability
id: hanged-man-seq-06-flesh-healing
name: Flesh Healing
pathway: hanged-man
sequence: 6
status: canonical
type: active
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
- healing
- offense
text: 'Cost: 3 points of Spirituality; up to 20 Flesh Stacks per use. Use: 1 Swift
  Action; 1 time per round. Effect: You use your accumulated flesh and blood to heal
  damage. If you have lost the upper limit of your flesh and blood piles, or they
  are all destroyed and your bodys health is lost, the Flesh Stacks you consume can
  be refilled into your healthrestoring health or increasing your life cap again.
  Special: If you were mutilated when you cast Flesh Bomb, Flesh Healing consumes
  the same amount of Flesh Stack you lost when you cast Flesh Bomb to restore your
  body.'
```





- **Cost:** 3 points of Spirituality; up to 20 Flesh Stacks per use.
- **Use:** 1 Swift Action; 1 time per round.
- **Effect:** You use your accumulated flesh and blood to heal damage.
  - If you have lost the upper limit of your flesh and blood piles, or they are all destroyed and your body’s health is lost, the Flesh Stacks you consume can be refilled into your health—restoring health or increasing your life cap again.
- **Special:** If you were mutilated when you cast Flesh Bomb, Flesh Healing consumes the same amount of Flesh Stack you lost when you cast Flesh Bomb to restore your body.

- **Limits:** As described in this section's prose.


### Blanket of Flesh

```yaml ability
id: hanged-man-seq-06-blanket-of-flesh
name: Blanket of Flesh
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: physical_defense
range: self
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
- defense
text: 'Cost: 3 points of Spirituality; at least 10 and at most 40 Flesh Stacks. Use:
  1 Swift Action; once per round. Effect: Create a giant blanket of fur that you can
  manipulate with flesh to perform 1 action each round. Its actions are limited; unless
  you have more ideas, it can only perform grappling special actions. For every 10
  Flesh Stacks consumed, the blanket can grab 1 person; consuming 40 Flesh Stacks
  allows it to grab 3 people at the same time. Determine its action bonus, mobility,
  and physical defense using its current Flesh Stack/2. Agility (DEX) and dodge are
  half of those values (rounded down). Roll: rd20 + action bonus against the targets
  physical defenses; on success, grapple it.'
```





- **Cost:** 3 points of Spirituality; at least 10 and at most 40 Flesh Stacks.
- **Use:** 1 Swift Action; once per round.
- **Effect:** Create a giant blanket of fur that you can manipulate with flesh to perform 1 action each round.
  1. Its actions are limited; unless you have more ideas, it can only perform grappling special actions.
  2. For every 10 Flesh Stacks consumed, the blanket can grab 1 person; consuming 40 Flesh Stacks allows it to grab 3 people at the same time.
  3. Determine its action bonus, mobility, and physical defense using its current Flesh Stack/2.
     - Agility (DEX) and dodge are half of those values (rounded down).
     - Roll: rd20 + action bonus against the target’s physical defenses; on success, grapple it.
  4. Grappled people must stand together; the distance between them cannot exceed Flesh Stack/2.
  5. The blanket’s Flesh Stack value is its health value; if its health value is lower than 10, it cannot continue the grapple action.

- **Limits:** As described in this section's prose.


### Flesh Bullet

```yaml ability
id: hanged-man-seq-06-flesh-bullet
name: Flesh Bullet
pathway: hanged-man
sequence: 6
status: canonical
type: active
action: attack
cost:
  flesh_stack: 2
roll: 1d20 + @attr.int + @skill.shooting
opposed_by: physical_defense
range: One or more targets.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.shooting
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Each bullet deals 1d6 physical damage; burst fire applies cumulative penalties.
scaling:
- when: burst_fire
  changes:
    effect_note: Apply a -2 penalty per additional shot after the first in a burst.
tags:
- defense
- offense
text: 'Cost: 2 Flesh Stacks per bullet. Use: 1 Attack Action; up to 6 consecutive
  shots. Targeting and range: One or more targets. Effect: Meat sticks protrude from
  your body and shoot at targets. Make an attack of Intuition (INT) + shooting against
  physical defense, ignoring agility and evasion in physical defense. Each meat stick
  deals 1d6 physical damage. Aftereffects: Gain a -2 penalty per shot in a burst,
  starting with the second shot.'
```





- **Cost:** 2 Flesh Stacks per bullet.
- **Use:** 1 Attack Action; up to 6 consecutive shots.
- **Targeting and range:** One or more targets.
- **Effect:**
  - Meat sticks protrude from your body and shoot at targets.
  - Make an attack of Intuition (INT) + shooting against physical defense, ignoring agility and evasion in physical defense.
  - Each meat stick deals 1d6 physical damage.
- **Aftereffects:** Gain a -2 penalty per shot in a burst, starting with the second shot.

- **Limits:** As described in this section's prose.
