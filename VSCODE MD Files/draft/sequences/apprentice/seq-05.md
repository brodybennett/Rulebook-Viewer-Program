---
title: 'Sequence 5: Traveler'
id: apprentice-seq-05
tags:
- pathway:apprentice
- sequence:5
---






# Door Pathway: Sequence 5

## Traveler

- **Traveler's Gate:** Travel through the **Spirit World** while sensing the outside world and self-positioning; can also perform short-distance continuous flashing to create a “siege” effect by one person. [[Spirit World]]
- **Invisible Hand:** Capable of taking pictures from a distance.

## Advancement

### Advancement Ritual

- **Ritual:** Set up special coordinates in four completely different places far apart in the depths of the **Spirit World**. [[Spirit World]]
- **Function:** After taking the magic potion, you will start to wander in the **Spirit World** uncontrollably. When you initially master the power, you will find that you have lost your way. At this time, you can use the four special coordinates to return to the real world.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2.
- Your navigating skill increases by 2 skill levels.

### Traveler's Gate

```yaml ability
id: apprentice-seq-05-traveler-s-gate
name: Traveler's Gate
pathway: apprentice
sequence: 5
status: adapted
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
  notes: No explicit fixed roll expression in source text; this block tracks two action-economy modes and their movement effects.
scaling:
- when: long_distance_spirit_world_travel_mode
  changes:
    action: cast
    effect_note: Travel distance scales to Intuition + Willpower + half Constitution (rounded up) kilometers.
- when: short_distance_continuous_flash_mode
  changes:
    action: swift
    max_flashes_per_round: 12
    effect_note: Each flash is up to 6 meters and grants free-action-priority evasive repositioning until flash budget is consumed.
tags:
- ritual
- detection
- mobility
text: '*Traveler''s Gate is also referred to as the Gate of Teleportation. It enables
  teleportation/travel as a self-positioning Spirit World shuttle that can sense the
  outside world. [[Spirit World]] This ability can be used in two ways: 1) Long-distance
  Spirit World travel Use: One Casting Action. Cost: "Spirit" refers to Spirituality
  in this section. Effect: You can travel long distances in the Spirit World, and
  you can always sense the reality of the outside world while in the Spirit World.
  You can transmit up to inspiration + will + half constitution (rounded up) km.'
```





**Traveler's Gate** is also referred to as the “Gate of Teleportation.” It enables teleportation/travel as a self-positioning **Spirit World** shuttle that can sense the outside world. [[Spirit World]]

This ability can be used in two ways:

1) **Long-distance Spirit World travel**
   - **Use:** One **Casting Action**.
- **Cost:** "Spirit" refers to **Spirituality** in this section.
   - **Effect:**
     - You can travel long distances in the **Spirit World**, and you can always sense the reality of the outside world while in the **Spirit World**.
     - You can transmit up to “inspiration + will + half constitution (rounded up)” km.
     - You can also use this to directly enter the **Spirit World**.
   - **Reference:** For the **Spirit World**, please refer to “Chapter Twelve: Special Areas”. [[Chapter Twelve: Special Areas]]

2) **Short-distance continuous flashing**
   - **Use:** 1 **Swift Action**, up to 12 times in one round. Its priority is regarded as a **free action**. The Swift Action is the sum of 12 flashes; less than 12 times still occupy a swift.
   - **Effect:** You perform short-distance continuous flashing (no more than 6 meters), which not only allows you to avoid attacks, but also allows you to create a siege effect by yourself, and gain the following benefits:
- **Limits:** If the enemy has any Door Pathway travelers, this exclusion applies (more than one character present).
     - Any **Extraordinary Ability** that targets you cannot hit you, including abilities that do not require identification—excluding area attacks, light, and lightning; but you retain the agility and evasion of the full physical defense against them.
     - Under the premise of the second article, if you maintain the flashing state and trigger **Premonition of Danger**, the original physical defense of **Premonition of Danger** against light and lightning can be replaced by a temporary +4 effect of physical defense. [[id:alias-premonition-of-danger|Premonition of Danger]]
     - If there is a situation where your 12 flashes in one round are consumed, it will be considered that the attacks have become so dense that you cannot dodge them, and you will be hit, because only 6 seconds have actually passed in one round.
     - If the number of times is used up, you can no longer get any of the above effects.

### Invisible Hand


```yaml ability
id: apprentice-seq-05-invisible-hand
name: Invisible Hand
pathway: apprentice
sequence: 5
status: adapted
type: active
action: attack
cost: {}
roll: 1d20 + @attr.str + @skill.fighting
opposed_by: physical_defense
range: line of sight (effective interaction span scales with Intuition)
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.str + @skill.fighting
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted remote-contact attack roll token. If using this to deliver another touch ability, resolve with that ability's own roll/effects.
scaling:
- when: using_touch_or_opening_ability_through_hand
  changes:
    effect_note: Use the delivered ability's normal roll, cost, and effects.
- when: intuition_increases
  changes:
    effect_note: Reach and manipulation breadth of the invisible hand increase with Intuition.
conditions:
- invisible
tags:
- stealth
- offense
- utility
text: 'Effect: You can take pictures from a distance. You are considered to be able
  to capture objects at any position equal to the range of Intuition (INT), perform
  attack actions, or perform abilities that require physical contact (such as opening
  doors). How much Intuition (INT) you have represents how much your invisible hand
  can dabble. Special: The invisible hand does not lose health. It has a Strength
  attribute equal to your Strength. It cannot work outside of line of sight.'
```





- **Effect:**
  - You can take pictures from a distance.
  - You are considered to be able to capture objects at any position equal to the range of **Intuition (INT)**, perform attack actions, or perform abilities that require physical contact (such as opening doors).
  - How much **Intuition (INT)** you have represents how much your invisible hand can dabble.
- **Special:**
  - The invisible hand does not lose health.
  - It has a Strength attribute equal to your Strength.
  - It cannot work outside of line of sight.

- **Limits:** As described in this section's prose.


### Records

```yaml ability
id: apprentice-seq-05-records
name: Records
pathway: apprentice
sequence: 5
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
  notes: No explicit dice expression in source text.
scaling:
- when: base_capacity
  changes:
    capacity_seq_4_to_3: 4
    capacity_seq_6_to_5: 15
    capacity_seq_9_to_7: 30
- when: recording_sequence_4_to_3_abilities
  changes:
    effect_note: Sequence 4-3 records are no longer halved.
tags:
- buff
text: 'Effect: The number and strength of Extraordinary Abilities you can record have
  been increased. [[recording extraordinary abilities]] From now on, you can record:
  4 Sequence 4-3 abilities 15 Sequence 6-5 abilities 30 Sequence 9-7 abilities The
  effects of Sequence 4-3 abilities will no longer be halved.'
```





- **Effect:** The number and strength of **Extraordinary Abilities** you can record have been increased. [[recording extraordinary abilities]]
- **From now on, you can record:**
  - 4 Sequence 4-3 abilities
  - 15 Sequence 6-5 abilities
  - 30 Sequence 9-7 abilities
- The effects of Sequence 4-3 abilities will no longer be halved.

- **Limits:** As described in this section's prose.
