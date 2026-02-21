---
title: 'Sequence 1: Dark Angel'
id: hanged-man-seq-01
tags:
- pathway:hanged-man
- sequence:1
---






# Hanged Man Pathway: Sequence 1

## Dark Angel

> **Lore:** The Archangel of the Hanged Man Pathway.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Using the power of corruption, but in a sacred form, the people of a city can be baptized and blessed accordingly. *(Unofficial ceremony.)*

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +1, Charisma +1, Willpower (WIL) +1

### Dark Angel

```yaml ability
id: hanged-man-seq-01-dark-angel
name: Dark Angel
pathway: hanged-man
sequence: 1
status: canonical
type: active
action: free
cost: {}
roll: 1d20
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: 1d20
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Check roll is used for wing recovery after the wings dissipate (recover on 18-20).
scaling:
- when: wing_recovery_roll_18_plus
  changes:
    effect_note: Wings recover on a d20 result of 18-20 at end of round.
tags:
- offense
text: 'Use: As a free action, intertwined virtual black wings appear behind you (like
  9-winged angels), covering most of your body. Effect: Void Black Wings While the
  wings exist: The wings are considered to have Vitality equal to yours *(not counting
  extra life).* [[Extra Life]] The wings have 10 unconditional damage reduction. When
  you take damage, the wings take damage first. You gain a +8 check bonus to all skills.
  You gain +3 to all your attributes.'
```





- **Use:** As a **free action**, intertwined virtual black wings appear behind you (like 9-winged angels), covering most of your body.
- **Effect: Void Black Wings**
  - While the wings exist:
    - The wings are considered to have Vitality equal to yours *(not counting **extra life**).* [[Extra Life]]
    - The wings have **10 unconditional damage reduction**.
    - When you take damage, the wings take damage first.
    - You gain a **+8 check bonus** to all skills.
    - You gain **+3 to all your attributes**.
    - You can avoid the influence of the [[Darkness Realm]].
  - When the wings bear the damage instead of you, it manifests as a dark, viscous, corrupted “ocean” that swallows the enemy’s attack and disappears invisible.
- **Aftereffects: Wing Recovery**
  - When the wings disappear and dissipate, you must either:
    - Go through an [[Encounter Time]] to reorganize, **or**
    - Make a d20 appraisal at the end of each round.
  - While reorganizing/recovering, you cannot be [[Transported]].
  - If the d20 roll is **20, 19, or 18**, your wings recover.
- **Special: Winged State**
  - While in **Winged state**, there is no longer a limit to the number of abilities you can [[Graze On Abilities]].
- **Special: Sea of Wings (Curse)**
  - You can use a **Casting Action** to select a target or an area, and let the sea of wings gradually cover the surface of others; affected creatures gain the **Fallen** status.
    - Casting Action
    - [[Fallen]]
  - If a creature continues to suffer from this effect:
    - After **three rounds**, the opponent begins to transform into a part of the “ocean,” and the opponent’s remaining life becomes the **extra life** of your wings.
    - It takes **five rounds** for an angel-level existence to do so.
    - If the gods and below do not make effective countermeasures after the opponent’s turn, they immediately become part of your wings.
  - This is considered a [[Curse]] that can be marginally dispelled by angel-level abilities or Sun Pathway demigod-level abilities.
    - [[Dispel]]
    - [[Sun]]
    - [[Angel-Level]]
    - [[Demigod-Level]]
    - [[Gods and Below]]

- **Effect:** Dark Angel resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Corruption

```yaml ability
id: hanged-man-seq-01-corruption
name: Corruption
pathway: hanged-man
sequence: 1
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.occultism - 8
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism - 8
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Mysticism check vs Willpower Defense with a -8 penalty drives the corruption outcome.
scaling:
- when: target_is_lower_sequence_hanged_man
  changes:
    effect_note: Lower-sequence Hanged Man targets can be forced into degeneration or collapse.
tags:
- defense
text: 'Use: A spellcasting action. Check: [[Mysticism]] against Willpower Defense;
  with a -8 penalty. Effect: Betrayal You designate a target to corrupt and betray
  its master. For the same level, you can make the targets [[Extraordinary Items]]
  betray, or make part of the targets [[Marionettes]] or [[Clones]] betray. Special:
  Hanged Man Pathway Targets (Lower Sequence) For a target lower than you: if the
  other party and you are both in the Sequence of the Hanged Man, you can directly
  let her body degenerate and betray her soul, and collapse on the spot. If the target
  is a demigod, there can only be one [[Spirit Body]] left that can continue to survive
  an encounter, and can be eliminated midway.'
```





- **Use:** A **spellcasting action**.
- **Check:** [[Mysticism]] against Willpower Defense; with a -8 penalty.
- **Effect: Betrayal**
  - You designate a target to corrupt and betray its master.
  - For the same level, you can make the target’s [[Extraordinary Items]] betray, or make part of the target’s [[Marionettes]] or [[Clones]] betray.
- **Special: Hanged Man Pathway Targets (Lower Sequence)**
  - For a target lower than you: if the other party and you are both in the Sequence of the Hanged Man, you can directly let her body degenerate and betray her soul, and collapse on the spot.
  - If the target is a demigod, there can only be one [[Spirit Body]] left that can continue to survive an encounter, and can be eliminated midway.
- **Special: Secret Puppet Betrayal**
  - You can also let a [[Secret Puppet]] whose personality is inferior to yours betray on the spot and disconnect the [[Thread of the Spirit Body]].
  - Similar products are also suitable for this use method.
  - This is a high-level application of [[Separating the Fallen Mind]], and it will inherit it as a Secret Puppet.
    - [[Avatar Era]]

- **Effect:** Corruption resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
