---
title: 'Sequence 4: Secrets Sorcerer'
id: apprentice-seq-04
tags:
- pathway:apprentice
- sequence:4
---






# Door Pathway: Sequence 4

## Secrets Sorcerer

> **Lore:** You possess a “secret-keeping” talent, can perform **Space Hiding** and **Spatial Exile**, and use various **Doors** as defenses.

## Advancement

### Advancement Ritual

- **Target:** A target with **Sequence 4 or higher**.

### Special Characteristic Appearance

- **Special Characteristic (Appearance):** A crystal ball made of insects. [[Crystal Ball]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2. Intuition
- Your navigating skills increase by 2 skill levels. [[Navigating Skills]]
- Choose three training abilities to become proficient. [[Training Ability]] Proficient
- Choose three more skills for training. [[Skill Training]]
- Two originally proficient skills can be upgraded to advanced. [[Advanced]]

### Keeping Secrets

```yaml ability
id: apprentice-seq-04-keeping-secrets
name: Keeping Secrets
pathway: apprentice
sequence: 4
status: canonical
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: persistent
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
- detection
- defense
text: 'Use: Passive. Effect: You can keep secrets, shielding induction, detection,
  divination, prophecy, and spiritual intuition from a person no higher than you;
  these are no longer useful against you. [[Induction]] Detection [[id:alias-divination|Divination]]
  [[id:alias-prophecy|Prophecy]] [[Spiritual Intuition]] They may know your existence
  indirectly, but they can no longer know other information about you; your actions
  are usually not directly targeted by scrying. [[Scrying]] Even for detection or
  prophecy higher than your level: if you do not reveal the kept secret at a certain
  moment and do not leave divination or prophecy clues, angel or higher-level detection
  usually cannot directly obt...'
```





- **Use:** Passive.
- **Effect:** You can keep secrets, shielding induction, detection, divination, prophecy, and spiritual intuition from a person no higher than you; these are no longer useful against you. [[Induction]] Detection [[id:alias-divination|Divination]] [[id:alias-prophecy|Prophecy]] [[Spiritual Intuition]]
- They may know your existence indirectly, but they can no longer know other information about you; your actions are usually not directly targeted by scrying. [[Scrying]]
- Even for detection or prophecy higher than your level: if you do not reveal the kept secret at a certain moment and do not leave divination or prophecy clues, angel or higher-level detection usually cannot directly obtain effective information by divining “what are you hiding.” [[Angel]] [[Divination Clue]]
- **Counter-scry:** The GM determines the procedure/effects (smashing a crystal ball is one possible method).

- **Limits:** As described in this section's prose.


### Gate to Another World

```yaml ability
id: apprentice-seq-04-gate-to-another-world
name: Gate to Another World
pathway: apprentice
sequence: 4
status: adapted
type: active
action: full-round
cost: {}
roll: 1d20 + @attr.int + @skill.navigation
opposed_by: difficulty_value
range: Up to planetary scale (GM decides campaign-appropriate limits).
target: designated target(s)
duration: persistent (until dissolved as a free action)
dice:
  check_roll: 1d20 + @attr.int + @skill.navigation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted from the explicit Navigator Identification requirement to open the correct gate.
scaling:
- when: sequence_2_or_higher
  changes:
    effect_note: Scope expands to all places in the universe you have previously visited.
tags:
- mobility
text: 'Use: At will. Use (Action): Full-Round Action. [[Full-Round Action]] Range:
  Up to planetary scale (GM decides campaign-appropriate limits). Duration: The door
  remains permanent until you use [[Dissolve]] as a Free Action. Free Action Access/Opening:
  A successful [[Navigator Identification]] is usually required to open the correct
  door. Special: You can now travel to places like [[Mirror World]]. Sequence 2: The
  scope includes all the places in the universe you have been to.'
```





- **Use:** At will.
- **Use (Action):** **Full-Round Action**. [[Full-Round Action]]
- **Range:** Up to planetary scale (GM decides campaign-appropriate limits).
- **Duration:** The door remains permanent until you use [[Dissolve]] as a **Free Action**. Free Action
- **Access/Opening:** A successful [[Navigator Identification]] is usually required to open the correct door.
- **Special:** You can now travel to places like [[Mirror World]].
- **Sequence 2:** The scope includes all the places in the universe you have been to.

- **Effect:** Gate to Another World resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Illusion

```yaml ability
id: apprentice-seq-04-illusion
name: Illusion
pathway: apprentice
sequence: 4
status: adapted
type: active
action: free
cost:
  spirituality: 10
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: difficulty_value
range: self
target: self
duration: 1 encounter
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted from the prose instruction to resolve follow-up checks using the same initial door contest.
scaling:
- when: stacked_door_layers
  changes:
    effect_note: Overflow damage transfers through each door layer, then to the user after the last layer breaks.
tags:
- ritual
- mobility
- defense
text: 'Cost: 10 points of Spirituality. [[Spirituality]] Use (Action): Free Action.
  Effect: You become a gate of illusion: the main body appears behind the gate, and
  the attacker is in two different worlds, facing you from far away. [[Illusory Gate]]
  You immediately create an independent door in front of you (covered with mysterious
  patterns) that lasts for an encounter. Encounter After creating the illusory door,
  you are directly separated into the independent space inside the door. This space
  can only be accessed through the door or by breaking the door. While in the separate
  space, you cannot travel through the [[Spirit World]], but you can disarm the door
  at any time as a Free Action. Follow...'
```





- **Cost:** 10 points of **Spirituality**. [[Spirituality]]
- **Use (Action):** **Free Action**.
- **Effect:** You become a gate of illusion: the main body appears behind the “gate,” and the attacker is in two different worlds, facing you from far away. [[Illusory Gate]]
- You immediately create an independent door in front of you (covered with mysterious patterns) that lasts for an encounter. Encounter
- After creating the illusory door, you are directly separated into the independent space inside the door. This space can only be accessed through the door or by breaking the door.
- While in the separate space, you cannot travel through the [[Spirit World]], but you can disarm the door at any time as a **Free Action**.
- **Follow-up:** Make the same check as the initial door contest.
- **Door Statistics:** Doors have 40 **Vitality** and 25 **Defense**. [[Vitality]] [[Defense]]
- **Stacking Doors:** If there is already a door, doors can be duplicated. You can stack another door after one door, layer by layer. If the damage suffered by the previous door exceeds its upper limit, the excess damage is borne by the next door.
- If the last door is damaged, overflow damage from the last door is resolved against your own physical defense, and you do not enjoy bonuses from agility and dodge. [[Physical Defense]] Agility (DEX) Dodge
- **Failure:** The GM decides the failure outcome.
- **Limits:** This door can only accommodate you alone. While inside the door, you are not considered a target within the range of vision.

### Space Hiding

```yaml ability
id: apprentice-seq-04-space-hiding
name: Space Hiding
pathway: apprentice
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 5
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
scaling: []
tags:
- ritual
- stealth
- mobility
- defense
text: 'Effect (Concept): Grabbing the void with the right hand can distort a space
  area, cut it into two parts, and hide one part. The only way to get out of the hidden
  space is through the door or by unhiding it. This can be used to create space pockets.
  [[Space Pocket]] Use (Action): Casting Action. Casting Action Cost: 5 points of
  Spirituality. Effect: Hide a piece of space in the current range; there must be
  a door to leave. Door Statistics (Typical): This door usually has 25 Defense and
  40 Vitality. Camouflage: You can camouflage the door to look the way you like, but
  it must be different from the wall; you can also cover it with something. What Counts
  as a Door: A door does not have to be...'
```





- **Effect (Concept):** Grabbing the void with the right hand can distort a space area, cut it into two parts, and hide one part. The only way to get out of the hidden space is through the door or by unhiding it. This can be used to create space pockets. [[Space Pocket]]
- **Use (Action):** **Casting Action**. Casting Action
- **Cost:** 5 points of **Spirituality**.
- **Effect:** Hide a piece of space in the current range; there must be a door to leave.
- **Door Statistics (Typical):** This door usually has 25 **Defense** and 40 **Vitality**.
- **Camouflage:** You can camouflage the door to look the way you like, but it must be different from the wall; you can also cover it with something.
- **What Counts as a Door:** A door does not have to be a long door; it is a conspicuous entrance/exit. It cannot be as small as an ant, but it can be window-sized. You can directly enter it when you touch it.
- **Leaving Hidden Space:** Even a mystic must pass through a door to leave a hidden space, or unhide as a **Free Action**.
- **Limits:** Generally, you can’t stack another hidden space inside a hidden space, and you can’t directly travel to the outside world while in a hidden space; you can only travel inside.
- **Visibility/Discovery:** From the outside world, the hidden area disappears out of thin air. For example, if a 50-square-meter house has 3 square meters hidden, then in others’ eyes it is directly missing 3 square meters. Therefore, to hide, you must choose a sufficiently hidden location to avoid discovery.
- **Observation:** You can use a crystal ball or a mirror to observe the situation outside the hidden space through astrology. As much as you can see from here when the space is not hidden, you can see as much when it is hidden. For example, if you hide part of a room, you can only see the inside of the room in the hidden space, but not the outside. [[Astrology]] [[Mirror]]
- **Durability:** Connected doors/spaces share a single Vitality pool.

> **GM Note:** Space Hiding can be treated as turning half a structure into an “inner world” and the other half into an “outer world.” Entering the inner world from the outside requires passing through one of the structure’s doors (which may be disguised as a secret door). This can create secret bases or hidden rooms in downtime, but the hidden space cannot be taken
