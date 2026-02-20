---
title: 'Sequence 7: Shadow Ascetic'
id: hanged-man-seq-07
tags:
- pathway:hanged-man
- sequence:7
---





# Hanged Man Pathway: Sequence 7

> **Lore:** Can hide in the shadows and wield shadow powers.

## Shadow Ascetic

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** constitution +2, agility +1, strength +1, inspiration +1.
- Your **mysticism** [[Mysticism]] can be quickly upgraded to **erudition** [[Erudition]].
- **Stealth** [[Stealth]] is added to your rapid improvement category [[Rapid Improvement Category]] and can be improved to **proficiency** at most Proficiency.

### Darkvision

```yaml ability
id: hanged-man-seq-07-darkvision
name: Darkvision
pathway: hanged-man
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- detection
text: 'Effect: You can see normally even in environments without any light.'
```




- **Effect:** You can see normally even in environments without any light.

- **Limits:** As described in this section's prose.


### Shadow Lurking

```yaml ability
id: hanged-man-seq-07-shadow-lurking
name: Shadow Lurking
pathway: hanged-man
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- mobility
- debuff
- defense
- offense
text: 'Cost: 2 points of spirituality [[Spirituality]]. Use: 1 movement action Movement
  Action to enter shadow state [[Shadow State]]. Effect: Your body suddenly disintegrates
  like a body of water, merges into the shadow, and enters shadow state: 1 You become
  a movable shadow; agility +3, affecting physical defense [[Physical Defense]] and
  mobility. 2 Gain high-speed dodge [[High-Speed Dodge]], keep complete physical defense
  against guns instead of light and lightning, and gain an extra level of dodge Dodge
  when facing attacks that are slower than guns; but in shadow state, you cannot perform
  actions other than using shadow abilities [[Shadow Abilities]]. 3 Even in an environment
  without other s...'
```




- **Cost:** 2 points of **spirituality** [[Spirituality]].
- **Use:** 1 **movement action** Movement Action to enter **shadow state** [[Shadow State]].
- **Effect:** Your body suddenly disintegrates like a body of water, merges into the shadow, and enters **shadow state**:
  - ① You become a movable shadow; agility +3, affecting **physical defense** [[Physical Defense]] and mobility.
  - ② Gain **high-speed dodge** [[High-Speed Dodge]], keep complete **physical defense** against guns instead of light and lightning, and gain an extra level of **dodge** Dodge when facing attacks that are slower than guns; but in **shadow state**, you cannot perform actions other than using shadow abilities [[Shadow Abilities]].
  - ③ Even in an environment without other shadows, you can move freely as an independent shadow; but if you hide in a dark area or in an existing shadow, you will be considered **invisible** [[Invisible]], and exposure will result in detection and tracking.
  - ④ In this state, you can pass through places that cannot be entered under normal circumstances, but you can still be hit by abilities.
  - ⑤ Exiting the **shadow state** is also a **movement action**, and the form of expression is to "grow" out of the shadow.
- **Special:** [[Master Puppet]], [[Eye of Mystery]], and [[id:alias-spirit-vision|Spirit Vision]] of the Wheel of Fortune pathway can directly discover you.

- **Limits:** As described in this section's prose.



### Shadow Package

```yaml ability
id: hanged-man-seq-07-shadow-package
name: Shadow Package
pathway: hanged-man
sequence: 7
type: active
action: move
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- mobility
- offense
text: 'Use: 1 Attack Action Attack Action or Move Action Move Action. Cost: No spirituality
  expended. Limits: This is a special action, not an extraordinary ability. This special
  action can only be used in shadow state. Effect: Every time you take an Attack Action
  or Move Action, you can choose a target to let the shadow state "extend" from the
  ground. Because you can''t cover multiple targets at once, you need to decide the
  order of the targets.'
```




- **Use:** 1 **Attack Action** Attack Action or **Move Action** Move Action.
- **Cost:** No **spirituality** expended.
- **Limits:**
  - This is a special action, not an extraordinary ability.
  - This special action can only be used in **shadow state**.
- **Effect:**
  - Every time you take an **Attack Action** or **Move Action**, you can choose a target to let the **shadow state** "extend" from the ground.
  - Because you can't cover multiple targets at once, you need to decide the order of the targets.
  - Fight against its **physical defenses**, and success will put it into a **grapple state** [[Grapple State]].
- **Manifestation:** You jump onto the first target and wrap it around, then let the shadow quickly extend to the next target.

### Shadow Hide

```yaml ability
id: hanged-man-seq-07-shadow-hide
name: Shadow Hide
pathway: hanged-man
sequence: 7
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- detection
- stealth
text: 'Cost: 2 sanity points [[Sanity / Rationality Points]] per use. Use: 1 Swift
  Action Swift Action. Effect: You cause your entire appearance to be covered in shadow.
  1 Others cannot see your shadow-covered face, and can only distinguish the shape
  and general type of your clothing, but cannot distinguish the color or further characteristics.
  2 You are regarded as a dark shadow, but unlike hiding in the shadow, you have an
  entity and can perform all normal activities. 3 As long as you deliberately hide
  yourself, then in dark environments and other shadows, your stealth test +4 is beneficial.
  Special: [[Master Puppet]], [[Eye of Mystery]], and [[Vision of Destiny]] can directly
  see your true face.'
```




- **Cost:** 2 **sanity points** [[Sanity / Rationality Points]] per use.
- **Use:** 1 **Swift Action** Swift Action.
- **Effect:** You cause your entire appearance to be covered in shadow.
  - ① Others cannot see your shadow-covered face, and can only distinguish the shape and general type of your clothing, but cannot distinguish the color or further characteristics.
  - ② You are regarded as a dark shadow, but unlike hiding in the shadow, you have an entity and can perform all normal activities.
  - ③ As long as you deliberately hide yourself, then in dark environments and other shadows, your stealth test +4 is beneficial.
- **Special:** [[Master Puppet]], [[Eye of Mystery]], and [[Vision of Destiny]] can directly see your true face.

- **Limits:** As described in this section's prose.


### Shadow Manipulation

```yaml ability
id: hanged-man-seq-07-shadow-manipulation
name: Shadow Manipulation
pathway: hanged-man
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- defense
text: 'Cost: 2 points of spirituality. Use: 1 Casting Action Casting Action. Targeting
  and range: Select up to 3 targets within the field of vision [[Field of Vision]].
  You shape the existing shadows to a certain extent, and the range of influence is
  as high as 1 kilometer. Resolution: mysticism counters physical defense. Effect:
  The shadows beyond the range of vision cannot be used accurately, and can only allow
  other Beyonders [[Beyonder]] to detect abnormalities with spiritual intuition [[Spiritual
  Intuition]].'
```




- **Cost:** 2 points of **spirituality**.
- **Use:** 1 **Casting Action** Casting Action.
- **Targeting and range:**
  - Select up to 3 targets within the **field of vision** [[Field of Vision]].
  - You shape the existing shadows to a certain extent, and the range of influence is as high as 1 kilometer.
- **Resolution:** **mysticism** counters **physical defense**.
- **Effect:**
  - The shadows beyond the range of vision cannot be used accurately, and can only allow other **Beyonders** [[Beyonder]] to detect abnormalities with **spiritual intuition** [[Spiritual Intuition]].
  - This ability can't really shape the shadows into specific shapes; it can only turn them into an amorphous "fluid" to attack.
  - The damage depends on the concentration of the surrounding shadows or darkness:
    - ① Areas with shadows caused by occlusion in daylight: 1d6 **curse damage** [[Curse Damage]].
    - ② Areas with shadows caused by occlusion at dusk: 2d6 **curse damage**.
    - ③ Areas without high-intensity light in the dark night: 3d6 **curse damage**; high-intensity light is regarded as dusk.
    - ④ Others: A room with sufficient light is regarded as dusk, and a room without light is regarded as night, regardless of the actual time.
- **Special:** In places continuously illuminated by **divine power** [[Divine Power Illumination]], as long as the corresponding power continues to exist, the intensity of the shadow will drop by 1 level, and the day level will disappear directly, causing you to be unable to use the ability.

- **Limits:** As described in this section's prose.
