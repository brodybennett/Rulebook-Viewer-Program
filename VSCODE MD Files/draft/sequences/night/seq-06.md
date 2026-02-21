---
title: 'Sequence 6: Nightwatcher'
id: night-seq-06
tags:
- pathway:night
- sequence:6
---






# Darkness Pathway: Sequence 6

## Nightwatcher

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +2.
- Your occult skills increase by 1 level.

### Requiem

```yaml ability
id: night-seq-06-requiem
name: Requiem
pathway: night
sequence: 6
status: canonical
type: active
action: cast
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
conditions:
- fear
tags:
- ritual
- detection
- control
- debuff
text: 'Cost: 1 Casting Action; consume 3 Spirituality. Targeting and range: Select
  1 target within your Field of Vision; affect a range of 130 meters; or Select all
  targets within this range; affects all creatures except you indiscriminately. The
  range of influence can be controlled. Limits: There is no specific limit to the
  number of Requiems. Effect: You appease the soul, smooth out the opponents desires
  and emotions, or put the natural spirit in a relatively peaceful state. The chosen
  creature suffers the following effects, which cannot be superimposed, and no identification
  is required: Mental states such as anger, fear, charm, temporary madness, indeterminate
  madness, and malice are immedia...'
```





- **Cost:** 1 **Casting Action**; consume 3 **Spirituality**.
- **Targeting and range:**
  - Select 1 target within your **Field of Vision**; affect a range of 130 meters; **or**
  - Select all targets within this range; affects all creatures except you indiscriminately.
  - The range of influence can be controlled.
- **Limits:** There is no specific limit to the number of Requiems.
- **Effect:** You appease the soul, smooth out the opponent’s desires and emotions, or put the natural spirit in a relatively peaceful state. The chosen creature suffers the following effects, which cannot be superimposed, and no identification is required:
  1. Mental states such as anger, fear, charm, temporary madness, indeterminate madness, and malice are immediately cleared, and these states will not be generated within 1 round.
     - This does not include shock and awe.
     - This includes stimulants, psychological hints, and the benefits of losing sanity.
     - **Special:** Even if a target that has been permanently insane and out of control undergoes a Requiem, the corresponding madness will reappear after the Requiem ends.
  2. Skill and attribute identification checks suffer **-4**, and 1 attack/casting/movement is lost. This lasts until the end of the **Requiemer**’s next action.
  3. Ordinary undead creatures (shadows, living corpses, etc.) will immediately lose all attack desires, and lose their activity and turn back to ordinary dead bodies or dissipate.
     - Stronger undead (Sequence 1+): movement halved; damage halved.
     - **Note:** The effect of halving is rounded up. The undead creature transformed from an **Extraordinary** is essentially a living thing and will not suffer from the effect of (3).
  4. If the Requiem is an ordinary person or other ordinary creatures, it will lose all desires and cannot perform any actions.
     - **Special:** For targets at least **1 Sequence** higher, the effects of (3) and (4) are **halved** (rounded up), and no action will be lost.

> **Lore:** The invisible fluctuations dissipated unsmoothly, and the surrounding suddenly darkened, as if it was late at night, and the feeling of tranquility and serenity came with a little bit of starlight.

### Spiritual Vision

```yaml ability
id: night-seq-06-spiritual-vision
name: Spiritual Vision
pathway: night
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
conditions:
- invisible
tags:
- ritual
- detection
- buff
text: After reaching the level of Sequence 6, your high Intuition (INT) has really
  enhanced your spiritual vision. From now on, you dont need to activate your spirit
  vision; you can directly use normal vision to spot [[spiritual creatures]]. This
  does not include the advanced invisibility of [[resentful souls]]. This does not
  include [[information creatures]]. (This is the effect brought by 1 potion and cannot
  be stolen or recorded.)
```





- After reaching the level of **Sequence 6**, your high Intuition (INT) has really enhanced your spiritual vision.
- From now on, you don’t need to activate your spirit vision; you can directly use normal vision to spot [[spiritual creatures]].
  - This does not include the advanced invisibility of [[resentful souls]].
  - This does not include [[information creatures]].
- (This is the effect brought by 1 potion and cannot be stolen or recorded.)

- **Effect:** Spiritual Vision resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Ritual Mastery

```yaml ability
id: night-seq-06-ritual-mastery
name: Ritual Mastery
pathway: night
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
- ritual
text: You gain access to ritual magic, able to invoke power from the gods. While holding
  this ability, you gain access to ritual magic, regardless of whether your occult
  skill is advanced or not. For the ritual magic you can use, refer to [[Common Ritual
  Magic]]. (This is the effect brought by 1 potion and cannot be stolen or recorded.)
```





- You gain access to ritual magic, able to invoke power from the gods.
- While holding this ability, you gain access to ritual magic, regardless of whether your occult skill is advanced or not.
- For the ritual magic you can use, refer to [[Common Ritual Magic]].
- (This is the effect brought by 1 potion and cannot be stolen or recorded.)

- **Effect:** Ritual Mastery resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
