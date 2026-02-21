---
title: 'Sequence 7: Werewolf'
id: mutant-seq-07
tags:
- pathway:mutant
- sequence:7
---






# Chained Pathway: Sequence 7

## Werewolf

> **Lore:** Werewolves possess strong self-recovery, terrifying strength, agility, and speed. Their claws and teeth rival extraordinary weapons of the same Sequence, can cut through steel, and are inherently poisonous. They also know dark spells that can control targets soaked in werewolf poison and transform them into short-lived, subordinate werewolf-like monsters.

- **Curse:** Killing and bloodlust at the full moon.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Strength** +1, **Constitution (CON)** +1, **Agility (DEX)** +1.
- Your **Mysticism** has joined the rapid growth category of **Sequence** 9, and can be improved to proficiency at most.

### Transform Werewolf

```yaml ability
id: mutant-seq-07-transform-werewolf
name: Transform Werewolf
pathway: mutant
sequence: 7
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: About 8 hours.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d4
  notes: Sanity check loss is 1/1d4 when transforming.
scaling: []
tags:
- ritual
- detection
- healing
- debuff
text: 'Use: Swift Action; perform an SC (1/1d4). Effect: You immediately transform
  into a werewolf. Duration: About 8 hours. While transformed: Strength +2, Constitution
  +2, Agility (DEX) +3. You gain: [[Pursuit]], Blade Swipe, Fast Healing, Fast Dodge,
  Werewolf Transformation, Spiritual Curse, Night Vision, and other abilities. You
  are considered a creature of darkness and dislike sunlight, though sunlight has
  no actual effect on you.'
```





- **Use:** **Swift Action**; perform an SC (1/1d4).
- **Effect:** You immediately transform into a werewolf.
- **Duration:** About 8 hours.
- **While transformed:**
  - **Strength** +2, **Constitution** +2, **Agility (DEX)** +3.
  - You gain: [[Pursuit]], **Blade Swipe**, **Fast Healing**, **Fast Dodge**, **Werewolf Transformation**, **Spiritual Curse**, **Night Vision**, and other abilities.
  - You are considered a creature of darkness and dislike sunlight, though sunlight has no actual effect on you.

- **Limits:** As described in this section's prose.


### Blade Swipe

```yaml ability
id: mutant-seq-07-blade-swipe
name: Blade Swipe
pathway: mutant
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
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Damage also includes +1d6 poison and Strength damage dice.
scaling: []
tags:
- debuff
- defense
- offense
text: 'Effect: Your claws are as reflective as metal, with black nails as long as
  daggers. Damage: 1d6 curse + 1d6 poison + Strength damage dice (physical); total
  damage is the sum of these components. Limits: This damage cannot be superimposed
  with other weapons at the same time. Notes: The front paws of the wolf are still
  five fingers; Blade Swipe does not require the palm to become wolf-shaped. It can
  only work on the nails, making them grow like daggers. Your claws ignore armors
  whose hardness is equal to steel or less than steel. This includes all kinds of
  skin armors. This does not include armors made of supernatural power (such as [[Dawn]]),
  armors enchanted with supernatural power, or ar...'
```





- **Effect:** Your claws are as reflective as metal, with black nails as long as daggers.
- **Damage:** 1d6 curse + 1d6 poison + Strength damage dice (physical); total damage is the sum of these components.
- **Limits:** This damage cannot be superimposed with other weapons at the same time.
- **Notes:**
  1. The front paws of the wolf are still five fingers; **Blade Swipe** does not require the palm to become wolf-shaped. It can only work on the nails, making them grow like daggers.
  2. Your claws ignore armors whose hardness is equal to steel or less than steel. This includes all kinds of skin armors.
     - This does **not** include armors made of supernatural power (such as [[Dawn]]), armors enchanted with supernatural power, or armor brought by dragon scales.
     - This does not ignore [[Damage Reduction]], it only allows you to break through the corresponding defense.
     - At the same time, your teeth can get this benefit too.

### Werewolf Transformation

```yaml ability
id: mutant-seq-07-werewolf-transformation
name: Werewolf Transformation
pathway: mutant
sequence: 7
status: canonical
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.int
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: 1d6
  effect_roll: 1d3
  notes: Targets take a sanity check loss (1/1d3) on transformation and gain fast healing (1d6 per round).
scaling: []
tags:
- ritual
- debuff
- defense
- offense
text: 'Cost: Consumes 2 points of [[Spirituality]]. Use: Casting Action. Test: Intuition
  Test against the Willpower Defense. Targeting and conditions: Choose a target you
  have dealt poison damage to with Blade Swipe, and the poison has been soaked into
  the target for five minutes. Poison damage is ignored if it is fully negated by
  [[Poison Resistance]]. Effect: After the Casting Action, the target is transformed
  into your follower and is regarded as a werewolf-like creature. Limits and guidance:'
```





- **Cost:** Consumes 2 points of [[Spirituality]].
- **Use:** **Casting Action**.
- **Test:** Intuition Test against the Willpower Defense.
- **Targeting and conditions:**
  - Choose a target you have dealt poison damage to with **Blade Swipe**, and the poison has been soaked into the target for five minutes.
  - Poison damage is ignored if it is fully negated by [[Poison Resistance]].
- **Effect:** After the **Casting Action**, the target is transformed into your follower and is regarded as a werewolf-like creature.
- **Limits and guidance:**
  1. The target cannot die, but can fall into a helpless state. This ability is generally used for ordinary people or existences weaker than you.
  2. If the target’s Sequence level is higher than yours, it usually requires the target to be in a helpless state to do so.
  3. Werewolf transformation has no effect on targets one higher than you, and provokes [[Sanity / Rationality Rolls]] for [[Mythic Creatures]].
- **Werewolf-like creatures:**
  - Usually become indifferent and fearless of death.
  - Unable to disobey the master’s order, no matter how unreasonable the order is.
  - Appearance still belongs to human beings.
  - A werewolf-like creature can take SC (1/1d3) as a **Swift Action** to become [[Half-Lycanthropy]].
    - The creature grows thick hair like a werewolf, gains **Strength** +2 and **Agility (DEX)** +2, and has 1d6 **Fast Healing**.
  - Without further benefit, this werewolf-like creature can only live for 24 hours, whether transformed or not.
- **Purging the poison:**
  - The poison from **Blade Swipe** can be purged; initially requiring only a 10 [[Medicine Check]] as a **Casting Action**.
  - **Difficulty Value** +5 every minute.
  - Any extraordinary ability related to healing can also gain this effect, without the need for a medical check.
  > **GM Note:** The setting’s education level is not widespread enough; if this person is not an intellectual, they may not even have the consciousness to attempt this.

- **Limits:** As described in this section's prose.


### Fast Healing

```yaml ability
id: mutant-seq-07-fast-healing
name: Fast Healing
pathway: mutant
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
  heal_roll: 1d6
  effect_roll: null
  notes: Passive regeneration per round.
scaling:
- when: sequence_6_or_higher
  changes:
    heal_roll: 2d6
tags:
- healing
- stealth
- offense
text: 'Use: Passive. Effect: Once per round, you recover 1d6 hit points. Notes: When
  you have this ability, you will not be in a near-death state due to reasons other
  than insufficient health, except against attacks from multiple attackers in the
  same round. In form of expression: even if there is a hideous wound on your abdomen
  and the intestines flow out, you only need to wash the intestines and stuff them
  back, and the wound will heal. Sequence 6: Instead, restore 2d6 hit points each
  time.'
```





- **Use:** Passive.
- **Effect:** Once per round, you recover 1d6 hit points.
- **Notes:**
  1. When you have this ability, you will not be in a near-death state due to reasons other than insufficient health, except against attacks from multiple attackers in the same round.
  2. In form of expression: even if there is a hideous wound on your abdomen and the intestines flow out, you only need to wash the intestines and stuff them back, and the wound will heal.
- **Sequence 6:** Instead, restore 2d6 hit points each time.

- **Limits:** As described in this section's prose.


### Night Vision

```yaml ability
id: mutant-seq-07-night-vision
name: Night Vision
pathway: mutant
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
  effect_roll: "4"
  notes: "Passive penalty: willpower -2 and sanity checks are +4 disadvantageous."
scaling: []
tags:
- detection
text: 'Effect: You have a normal range of vision in the dark, but you still need a
  certain amount of low light to achieve this effect; Night Vision cannot work in
  completely dark places.'
```





- **Effect:** You have a normal range of vision in the dark, but you still need a certain amount of low light to achieve this effect; **Night Vision** cannot work in completely dark places.

- **Limits:** As described in this section's prose.


### Fast Dodge

```yaml ability
id: mutant-seq-07-fast-dodge
name: Fast Dodge
pathway: mutant
sequence: 7
status: canonical
type: active
action: cast
cost: {}
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
  notes: No roll; fixed armor and cold resistance bonuses.
scaling: []
tags:
- defense
text: 'Effect: For firearms, you get full agility and dodge defense. Additional rule:
  When you face guns instead of light/lightning, you retain full physical defense
  and get 1 extra level of dodge. (For extra dodge, see [[Defense and Dodge Types]].)'
```





- **Effect:** For firearms, you get full agility and dodge defense.
- **Additional rule:** When you face guns instead of light/lightning, you retain full physical defense and get 1 extra level of dodge.
  - (For extra dodge, see [[Defense and Dodge Types]].)

- **Limits:** As described in this section's prose.


### Hair Armor

```yaml ability
id: mutant-seq-07-hair-armor
name: Hair Armor
pathway: mutant
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
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- defense
- offense
text: 'Effect: Your armor +3; gain 5 points of cold resistance. Limits: Cannot be
  superimposed with other armor. Fire damage: If you take fire damage, Hair Armor
  does not apply to resist.'
```





- **Effect:** Your armor +3; gain 5 points of cold resistance.
- **Limits:** Cannot be superimposed with other armor.
- **Fire damage:** If you take fire damage, **Hair Armor** does not apply to resist.

### Spiritual Curse

```yaml ability
id: mutant-seq-07-spiritual-curse
name: Spiritual Curse
pathway: mutant
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
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- divination
- debuff
text: 'Effect: Unless you are a person higher than you, whether you are transformed
  or not, any [[id:alias-divination|Divination]] and psychic means can only see a
  figure covered in black hair, and cannot see your true face. Higher Sequence level:
  When you obtain a new form, it will affect the abilities of divination and psychic
  communication, and the presented form will also become the characteristics of your
  new form. For example, a [[Living Corpse]] will see a figure indistinguishable from
  a human but filled with a gloomy aura, making it impossible to see its face clearly;
  while a [[Ghost]] will only see a face that is transparent as if it does not exist,
  or a face covered by darkness. If you...'
```





- **Effect:** Unless you are a person higher than you, whether you are transformed or not, any [[id:alias-divination|Divination]] and psychic means can only see a figure covered in black hair, and cannot see your true face.
- **Higher Sequence level:** When you obtain a new form, it will affect the abilities of divination and psychic communication, and the presented form will also become the characteristics of your new form.
  1. For example, a [[Living Corpse]] will see a figure indistinguishable from a human but filled with a gloomy aura, making it impossible to see its face clearly; while a [[Ghost]] will only see a face that is transparent as if it does not exist, or a face covered by darkness.
  2. If you commit crimes in the previous heterogeneous form at a higher Sequence level, then the divination will also reveal the previous image.

- **Limits:** As described in this section's prose.


### Partial Transformation

```yaml ability
id: mutant-seq-07-partial-transformation
name: Partial Transformation
pathway: mutant
sequence: 7
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
- defense
text: 'Use: 1 Swift Action; 1 time per round. Effect: You gain 1 of the above traits,
  which does not require a [[Sanity / Rationality Rolls]]. Partial transformation
  can also be used to adjust in reverse. For example, if you become a werewolf but
  dont want to be conspicuous because of the werewolfs appearance, you can use partial
  transformation to cancel Hair Armor, which will also make you lose the benefit of
  Hair Armor. Sequence 6: Even if you become a living corpse, you can use partial
  transformation to gain the benefits of a werewolf, gain some of the characteristics
  of a werewolf, or use the ability of a living corpse under the appearance of a werewolf.
  However, the Strength, Constitution (...'
```





- **Use:** 1 **Swift Action**; 1 time per round.
- **Effect:**
  1. You gain 1 of the above traits, which does not require a [[Sanity / Rationality Rolls]].
  2. Partial transformation can also be used to adjust in reverse. For example, if you become a werewolf but don’t want to be conspicuous because of the werewolf’s appearance, you can use partial transformation to cancel **Hair Armor**, which will also make you lose the benefit of **Hair Armor**.
- **Sequence 6:**
  - Even if you become a living corpse, you can use partial transformation to gain the benefits of a werewolf, gain some of the characteristics of a werewolf, or use the ability of a living corpse under the appearance of a werewolf.
  - However, the Strength, Constitution (CON), and Agility (DEX) bonuses brought by the werewolf itself can only be obtained by completely turning into a werewolf.
  - If you become a werewolf at all, you will lose the [[Power of the Undead]], the [[Skin of Steel]], and not including the [[Control of Decay and Cold]].
  - Note: Although it is possible to do this while in the [[Wraith State]], it is meaningless, because the Wraith can't deal physical damage even if it gets the benefit of the werewolf.
- **Sequence 4:** Some transformations can still be used in the [[Puppet State]].

- **Limits:** As described in this section's prose.


### Spiritual Alienation

```yaml ability
id: mutant-seq-07-spiritual-alienation
name: Spiritual Alienation
pathway: mutant
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
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- control
text: 'Effect: Because you often satisfy your desire to kill during the full moon,
  your spirit has become alienated. Limits (who gains this): This is a side note;
  only xenos that consistently indulge themselves on most full moon nights will get
  this effect. While possessing Spiritual Alienation: The holders will attribute will
  continue to be temporarily -2, and all sanity checks will be +4 disadvantageous.
  Because sanity appraisal is the opposite of normal appraisalthe larger the value
  of normal appraisal, the better, and the smaller the value of sanity appraisal,
  the betterthis more easily leads to loss of control. Extra: When possessing Spiritual
  Alienation, every 1 hour of behavior of indulgi...'
```





- **Effect:** Because you often satisfy your desire to kill during the full moon, your spirit has become alienated.
- **Limits (who gains this):** This is a side note; only xenos that consistently indulge themselves on most full moon nights will get this effect.
- **While possessing Spiritual Alienation:**
  1. The holder’s will attribute will continue to be temporarily -2, and all sanity checks will be +4 disadvantageous.
  2. Because sanity appraisal is the opposite of normal appraisal—the larger the value of normal appraisal, the better, and the smaller the value of sanity appraisal, the better—this more easily leads to loss of control.
- **Extra:** When possessing Spiritual Alienation, every 1 hour of behavior of indulging self-desire will restore 1 point of sanity. What form this behavior takes depends on your own values.
  > **GM Note:** An Extraordinary with Spiritual Alienation will inevitably become more ruthless, more distorted, and gradually lose the emotions that normal humans should have.
- **Remove Spiritual Alienation:** If you do not release yourself on three full moon nights in a row, you will not be affected by Spiritual Alienation temporarily. However, once you release yourself on any subsequent full moon night to satisfy your desire to kill, you will fall into a state of Spiritual Alienation again.

- **Limits:** As described in this section's prose.


### Full Moon Curse

```yaml ability
id: mutant-seq-07-full-moon-curse
name: Full Moon Curse
pathway: mutant
sequence: 7
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.wil
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.wil
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Must pass DV 15 will test each round under full moon or transform.
scaling: []
tags:
- debuff
- defense
text: 'Effect: The moon will curse you. Limits: The Curse of the Full Moon is an inherent
  effect once one possesses the power of a werewolf, and cannot be recorded or stolen.
  Under the full moon: Your madness has only one kindviolent tendencyand the desire
  for killing and bloodthirsty will reach its peak. When being illuminated by the
  full moon, you must pass a will test with a Difficulty Value of 15 every round;
  otherwise you will automatically become a werewolf, and the corresponding sanity
  will be deducted. Until you leave the full moon, you will fall into madness and
  start killing and bloodthirsty. If you fail the will test (or otherwise resist transforming,
  GM decides): You lose an action e...'
```





- **Effect:** The moon will curse you.
- **Limits:** The Curse of the Full Moon is an inherent effect once one possesses the power of a werewolf, and cannot be recorded or stolen.
- **Under the full moon:**
  1. Your madness has only one kind—violent tendency—and the desire for killing and bloodthirsty will reach its peak.
  2. When being illuminated by the full moon, you must pass a will test with a **Difficulty Value** of 15 every round; otherwise you will automatically become a werewolf, and the corresponding sanity will be deducted. Until you leave the full moon, you will fall into madness and start killing and bloodthirsty.
     - **If you fail the will test (or otherwise resist transforming, GM decides):** You lose an action each round, are excruciatingly painful, and don't gain the benefit of insane immediate actions from full moon madness.
- **Sedatives:** If you take sedatives (1–2 pills), you don’t need to suppress the madness and you can act normally, but the same kind will be invalid after 4 doses.
- When a new full moon curse is acquired, the original full moon curse will be overwritten.
