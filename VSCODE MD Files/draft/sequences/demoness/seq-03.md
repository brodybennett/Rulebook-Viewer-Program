---
title: 'Sequence 3: Unaging'
id: demoness-seq-03
tags:
- pathway:demoness
- sequence:3
---






# Demoness Pathway: Sequence 3

## Unaging

- See also: [[Demoness]]

> **Lore:** Eternal youth—strange and difficult to kill. Skilled in resurrection and rebirth, petrification, and transmitting power through the **Mirror World** [[Mirror World]]. Can perfectly present the charm of women at every stage, matching skin condition and facial features.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Create a man-made disaster that can cause at least 10,000 people to suffer, and under the high pressure of hatred, escape the revenge and punishment that the disaster will bring immediately. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Agility (DEX) +2, Constitution +1, Willpower (WIL) +1, Charisma +2, Intuition (INT) +2.

### Extraordinary Lifespan

```yaml ability
id: demoness-seq-03-extraordinary-lifespan
name: Extraordinary Lifespan
pathway: demoness
sequence: 3
status: adapted
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
  heal_roll: 2d10
  effect_roll: null
  notes: Heal roll applies on each successful Mirror World rebirth.
scaling:
- when: each_resurrection
  changes:
    effect_note: Reduce Spiritual Limit by 5 after each rebirth.
- when: death_in_mirror_world
  changes:
    heal_roll: null
    effect_note: No resurrection occurs if death happens in the Mirror World.
tags:
- defense
- healing
text: You will not grow old or die; your lifespan will exceed at least 1400 years
  without weakening. Whenever you die, you will be reborn in the Mirror World [[Mirror
  World]], recovering 2d10 Vitality Points Vitality Points. The number of resurrections
  is up to you. Each time you resurrect, reduce your Spiritual Limit [[Spiritual Limit]]
  by 5 points (your limit -5). You get one chance at your resurrection. Rebirth from
  the Mirror World appears in the nearest mirror, or a mirror you have set in advance.
  If your death is in the Mirror World, you will not be able to resurrect.
```





- You will not grow old or die; your lifespan will exceed at least 1400 years without weakening.
- Whenever you die, you will be reborn in the **Mirror World** [[Mirror World]], recovering 2d10 **Vitality Points** Vitality Points.
- The number of resurrections is up to you. Each time you resurrect, reduce your **Spiritual Limit** [[Spiritual Limit]] by 5 points (your limit -5). You get one chance at your resurrection.
- Rebirth from the Mirror World appears in the nearest mirror, or a mirror you have set in advance.
- If your death is in the Mirror World, you will not be able to resurrect.

- **Effect:** Extraordinary Lifespan resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Medusa

```yaml ability
id: demoness-seq-03-medusa
name: Medusa
pathway: demoness
sequence: 3
status: canonical
type: active
action: free
cost: {}
roll: 1d20 + @attr.cha
opposed_by: physical_defense
range: All targets within your line of sight.
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Each round, roll Charisma against Physical Defense to advance petrification.
scaling: []
tags:
- debuff
- buff
- defense
- offense
- social
text: 'Cost: Free Action Free Action. Use: Once per round. Effect: You cause all targets
  within your line of sight to begin petrifying. This is a curse [[Curse]] effect
  that can be dispelled [[Dispel]] or resisted by Resistance [[Resistance]]. Targeting
  and range: All targets within your line of sight. Progression: Each round, use your
  Charisma to attack the physical defenses [[Physical Defense]] of all creatures within
  your line of sight, and if successful, increase the Petrification Level by 1. Petrification
  Level 1: The creature''s skin is partially stained with lime, leaving only one Free
  Action Free Action per round. Petrification Level 2: The creature''s limbs are almost
  frozen, and it takes...'
```





- **Cost:** **Free Action** Free Action.
- **Use:** Once per round.
- **Effect:** You cause all targets within your line of sight to begin petrifying. This is a **curse** [[Curse]] effect that can be dispelled [[Dispel]] or resisted by **Resistance** [[Resistance]].
- **Targeting and range:** All targets within your line of sight.
- **Progression:** Each round, use your Charisma to attack the **physical defenses** [[Physical Defense]] of all creatures within your line of sight, and if successful, increase the **Petrification Level** by 1.

- **Petrification Level 1:** The creature's skin is partially stained with lime, leaving only one **Free Action** Free Action per round.
- **Petrification Level 2:** The creature's limbs are almost frozen, and it takes two turns to move and attack. At this time, it can give up one of the actions to complete one of the actions in one turn, and there is still one **Free Action** Free Action.
- **Petrification Level 3:** The creature can take no **Move Actions** Move Action, takes two turns to attack, and only one **Free Action** Free Action.
- **Petrification Level 4:** The creature turns to stone until someone removes its curse. Killing the target during this phase is considered death, and the independent **Vitality Points** Vitality Points of the petrified state are half of the current hit points.

- **Limits:** As described in this section's prose.
