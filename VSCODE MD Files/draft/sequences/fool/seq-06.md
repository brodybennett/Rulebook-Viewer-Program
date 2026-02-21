---
title: 'Sequence 6: Faceless'
id: fool-seq-06
tags:
- pathway:fool
- sequence:6
---






# Fool Pathway: Sequence 6

## Faceless

- You can instantly observe and recall the appearance and temperament characteristics of everyone you know, and grasp their unique smell.
- People who can change into different appearances, as long as the difference in body size is not too large, can imitate height and voice, but cannot imitate voices with mysterious power; it is only a superficial change and does not involve the essence. [2]

## Advancement

### Main Materials

- The mutated pituitary gland of the [[Thousand-Faced Hunter]]
- The characteristics of the [[human-skinned shadow]]

### Auxiliary Materials

- 80ml of the blood of the hunter with thousands of faces [[Thousand-Faced Hunter]]
- 5 drops of [[black mandala juice]]
- 10g of [[dragon tooth grass powder]]
- 3 hairs of [[deep sea naga]]

## Acting

- **Acting principle:** pretending to be someone else.
- You can pretend to be anyone except yourself.
- While integrating into the role and trying to play it, withdraw from emotion and examine it indifferently; through bit-by-bit comparison, recognize yourself and find the truest self, and avoid being negatively affected by the role due to long-term performance.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2.
- Your fighting skill goes up by 1 level.
- Your disguise goes up by 2 levels.

### Instant Recognition and Recall

```yaml ability
id: fool-seq-06-instant-recognition-and-recall
name: Instant Recognition and Recall
pathway: fool
sequence: 6
status: canonical
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Passive memory and recognition benefit; no explicit random resolution in source text.
scaling: []
tags:
- utility
text: From now on, as long as you have met a person, you can instantly remember their
  appearance, temperament, smell, and characteristics. You can also recall this information
  from people you met before being promoted. If you have only seen a portrait, you
  may only remember appearance. If the person you have met is disguised, you can only
  remember the information of the disguise. As long as they can't completely cover
  up their temperament and behavior habits, even if you don't know their true face,
  you can find them from the crowd at a glance; the GM decides whether this still
  applies if they disguise again.
```





1. From now on, as long as you have met a person, you can instantly remember their appearance, temperament, smell, and characteristics.
   - You can also recall this information from people you met before being promoted.
   - If you have only seen a portrait, you may only remember appearance.
2. If the person you have met is disguised, you can only remember the information of the disguise.
   - As long as they can't completely cover up their temperament and behavior habits, even if you don't know their true face, you can find them from the crowd at a glance; the **GM** decides whether this still applies if they disguise again.

- **Effect:** Instant Recognition and Recall resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Metamorphosis

```yaml ability
id: fool-seq-06-metamorphosis
name: Metamorphosis
pathway: fool
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Form-change utility with no explicit contested check in source text.
scaling:
- when: potion_fully_digested_or_promoted
  changes:
    effect_note: Maximum height adjustment increases from +/-10cm to +/-15cm.
tags:
- ritual
- buff
- social
text: 'Use: 1 Casting Action. Cost: Without expending spirituality. Effect: You undergo
  a physically permanently altered disguise. You can permanently change into someone
  with a different appearance, but it is only a superficial change, not a real one.
  Additional effects: This allows you to freely adjust Charisma between 1a6, but does
  not involve extraordinary strength. Limits and rules: You canaTMt drastically change
  your body shape. You can only increase or decrease your height by 10 centimeters.
  Transformation does not affect the essence; it only changes appearance, and cannot
  change with the clothes. At this stage, your change range is not enough to deform
  the clothes; at most, it is like pa...'
```





- **Use:** 1 Casting Action.
- **Cost:** Without expending **spirituality**.
- **Effect:** You undergo a physically permanently altered disguise. You can permanently change into someone with a different appearance, but it is only a superficial change, not a real one.
- **Additional effects:** This allows you to freely adjust **Charisma** between 1-6, but does not involve extraordinary strength.
- **Limits and rules:**
  1. You can't drastically change your body shape. You can only increase or decrease your height by 10 centimeters.
     > **Lore:** This essentially fills your body with excess flesh and blood; increasing outward height implies losing the flesh and blood that previously filled your body.
  2. Transformation does not affect the essence; it only changes appearance, and cannot change with the clothes. At this stage, your change range is not enough to deform the clothes; at most, it is like painting the surface of the body with a layer of oil paint with the same color as the clothes.
  3. The essence and process of deformation is to adjust the position, color, smell, and characteristics of flesh and blood. Therefore, flesh and blood will wriggle and change to a certain extent; you can change skin color and become the appearance of the opposite sex, but it cannot affect your primary sexual characteristics.
  4. As long as you have heard it and remember it, you can also completely imitate the voice of others; the imitated voice does not have extraordinary effects.
- **The potion is fully digested or promoted:** You can be taller or shorter by 15 cm.

- **Limits:** As described in this section's prose.


### Other Extraordinary Ability Improvements

```yaml ability
id: fool-seq-06-other-extraordinary-ability-improvements
name: Other Extraordinary Ability Improvements
pathway: fool
sequence: 6
status: canonical
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Conditional roll mapping for anti-divination submode where prose shifts identification basis to Spiritual Intuition.
scaling:
- when: anti_divination_using_props
  changes:
    effect_note: Paper Doll Substitute is no longer required; anti-divination checks use Spiritual Intuition mapping.
- when: manipulate_flames_used
  changes:
    effect_note: Manipulate Flames range becomes 40 meters.
- when: flame_jump_used
  changes:
    effect_note: Flame Jump range becomes 40 meters.
- when: air_bomb_used
  changes:
    effect_note: Air Bomb damage becomes 2d6 physical.
- when: false_breathing_underwater_used
  changes:
    effect_note: Air tube length becomes 10 meters.
- when: paper_soldier_used
  changes:
    effect_note: Created weapon lasts 7 minutes and breaks after 4 hard impacts.
- when: illusion_used
  changes:
    effect_note: Illusion gains a temporary +1 bonus to Deception checks.
damage_types:
- physical
tags:
- divination
- mobility
- buff
- offense
text: 'Anti-divination: You donaTMt need a [[Paper Doll Substitute]]; you can use
  any divination props for anti-divination. This usage will not damage the divination
  props (for example, coin divination can be achieved by making coins roll and jump
  in the hand), but the occult identification is changed to inspiration identification.
  Manipulate Fire: The range of Manipulate Fire has been increased to 40 meters. Flame
  Leap: The range of Flame Leap is increased to 40 meters. Air bomb: Changed to 2d6
  physical damage, comparable to the latest rifle. False "breathing underwater": The
  thin air tube is changed to a length of 10 meters. Paper Doll Substitute/Damage
  Transfer: No significant change, only in...'
```





- **Anti-divination:** You don't need a [[Paper Doll Substitute]]; you can use any divination props for anti-divination. This usage will not damage the divination props (for example, coin divination can be achieved by making coins roll and jump in the hand), but the occult identification is changed to inspiration identification.
- **Manipulate Fire:** The range of Manipulate Fire has been increased to 40 meters.
- **Flame Leap:** The range of Flame Leap is increased to 40 meters.
- **Air bomb:** Changed to 2d6 physical damage, comparable to the latest rifle.
- **False "breathing underwater":** The thin air tube is changed to a length of 10 meters.
- **Paper Doll Substitute/Damage Transfer:** No significant change, only increased use times due to spiritual growth.
- **Draw paper as a soldier:** When the created weapon hits a hard object, it is damaged 4 times and lasts for 7 minutes.
- **Illusion:** For this ability only, gain a +1 temporary bonus on **Deception** checks.

- **Effect:** Other Extraordinary Ability Improvements resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
