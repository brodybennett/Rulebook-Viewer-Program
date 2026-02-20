---
title: 'Sequence 1: Key of Stars'
id: apprentice-seq-01
tags:
- pathway:apprentice
- sequence:1
---





# Door Pathway: Sequence 1

## Key of Stars

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Change the trajectory of the stars, or seal a celestial body.

> **GM Note:** The RAW describes this as an â€œunofficial ceremony.â€

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** inspiration +2; pilot skill increased by 2 skill levels.

### Authority Locating

```yaml ability
id: apprentice-seq-01-authority-locating
name: Authority Locating
pathway: apprentice
sequence: 1
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- mobility
text: 'Cost: 3 points of spirituality. Use: Free action. Effect: You locate a person''s
  true position through the authority of the [[Door]]. You must come into contact
  with a medium associated with the opponent (such as props they have used). You then
  directly locate their true position in the entire universe through the stars. Limits:
  This ability also has a significant effect on the [[Deity]].'
```




- **Cost:** 3 points of spirituality.
- **Use:** **Free action.**
- **Effect:** You locate a person's true position through the authority of the [[Door]]. You must come into contact with a medium associated with the opponent (such as props they have used). You then directly locate their true position in the entire universe through the stars.
- **Limits:** This ability also has a significant effect on the [[Deity]].

### Teleportation (Shifting Stars)

```yaml ability
id: apprentice-seq-01-teleportation-shifting-stars
name: Teleportation (Shifting Stars)
pathway: apprentice
sequence: 1
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- mobility
text: 'Use: Free action. Effect: You can teleport to any place in this universe immediately;
  lower-level obscuration/sealing can be pried open and does not stop this effect.'
```




- **Use:** **Free action.**
- **Effect:** You can teleport to any place in this universe immediately; lower-level obscuration/sealing can be pried open and does not stop this effect.

- **Limits:** As described in this section's prose.



### Gate

```yaml ability
id: apprentice-seq-01-gate
name: Gate
pathway: apprentice
sequence: 1
type: active
action: cast
cost: {}
roll: null
opposed_by: willpower_defense
range: A supernatural ability or a thing within your range of vision.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- defense
text: 'Cost: 5 points of spirituality. Use: Spellcasting action. Check: [[Mysticism]]
  against Willpower Defense; minus -8 is disadvantageous. Check: [[Mysticism]] against
  Willpower Defense; apply -8 to the overall contest result. Targeting and range:
  A supernatural ability or a thing within your range of vision. Effect: You directly
  seal the target for three rounds at a time. You seal a supernatural ability or a
  thing within your range of vision. For one target, seal only one supernatural ability
  at a time. Across different targets (or repeated uses), there is no total upper
  limit on active seals.'
```




- **Cost:** 5 points of spirituality.
- **Use:** **Spellcasting action.**
- **Check:** [[Mysticism]] against Willpower Defense; minus -8 is disadvantageous.  
- **Check:** [[Mysticism]] against Willpower Defense; apply **-8** to the overall contest result.
- **Targeting and range:** A supernatural ability or a thing within your range of vision.
- **Effect:** You directly seal the target for **three rounds** at a time.
  - You seal a supernatural ability or a thing within your range of vision.
  - For one target, seal only one supernatural ability at a time. Across different targets (or repeated uses), there is no total upper limit on active seals.
  - Extraordinary items of the same personality can directly seal the entire thing, making it unusable for three rounds.
- **Limits:**
  - Because this ability requires a Casting Action, there is generally no time for the extraordinary ability of free actions to be sealed.
  - The sealed ability must be recognized, such as within your field of vision.
- **Scaling by level:**
  - You can seal **three extraordinary abilities** at a time for a target lower than you; this lasts for one Encounter.
  - You can also seal the entire [[Extraordinary Item]] for one encounter.
  - If you make a target voluntary, **or** if the target is one level below you and becomes helpless (including extraordinary items that no one holds for a time), **or** if the target is two levels below you, you can make this seal last forever.
- **Awareness and special cases:**
  - The moment any seal is sealed, it immediately arouses the [[Spiritual Intuition]] of the other party, making them aware of this.
  - Spiritual intuition is not a supernatural ability; it can only be sealed if the target is voluntary or one level lower than you and in a helpless state.
  - If you seal an extraordinary item, its owner will notice it when the extraordinary item is held, and the moment its owner touches the item if it is not held.
- **Removing a seal:**
  - Sealing is a kind of extraordinary ability. It can be removed by other extraordinary abilities of the same level, or by finding the correct method (designed by the GM; usually only one level lower than the ability of the sealer can try to do so).
- **Area of influence:**
  - If you want to seal all supernatural items and [[Door]] indiscriminately, you can affect the entire continent; all judgments follow the above content.
- **At Sequence 0:**
  - You can affect the entire world and strengthen the level of all sealed items to the extent that other Sequence 0s cannot be used in an encounter.

### Spoon

```yaml ability
id: apprentice-seq-01-spoon
name: Spoon
pathway: apprentice
sequence: 1
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: An object within your field of vision.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- mobility
text: 'Cost: 3 points of spirituality. Use: Free action (once in a Round). Targeting
  and range: An object within your field of vision. Effect: You unseal a thing. The
  specific effect of this ability is similar to that of a door, but the direction
  is different and the effect is different. Effect: You unseal a thing. The specific
  effect is similar to the general [[Door]] mechanics. You can release things that
  have been blocked by supernatural objects such as [[Occult]], or conscious thoughts
  that have been blocked by [[Hypnosis]], but you must be aware of its existence.
  This essentially uses the power of location to find the keys, or lockholes, of these
  seals, thereby opening them. If there is a s...'
```




- **Cost:** 3 points of spirituality.
- **Use:** **Free action** (once in a Round).
- **Targeting and range:** An object within your field of vision.
- **Effect:** You unseal a thing. The specific effect of this ability is similar to that of a door, but the direction is different and the effect is different.  
- **Effect:** You unseal a thing. The specific effect is similar to the general [[Door]] mechanics.
  - You can release things that have been blocked by supernatural objects such as [[Occult]], or conscious thoughts that have been blocked by [[Hypnosis]], but you must be aware of its existence.
  - This essentially uses the power of location to find the keys, or lockholes, of these seals, thereby opening them.
  - If there is a special item whose negative effect is restricted by some kind of seal, you can directly remove it and let it return to its original state within three rounds. Permanence is decided by the GM.

- **Interaction with restricted abilities:**
  - Restricted extraordinary abilities are also regarded as a seal.
  - You can choose one of the effects of the [[Requiem Aura]] to invalidate it for three rounds, and you can also make the ability of the judged person invalidated again.
  - You can also cancel any one of them: the bound state of the target.
  - But you can't restore extraordinary abilities stolen from their **owner** (the stolen person) or removed by a **judged person** via Invalidation Law.

- **What counts as a seal:**
  - The premise of making a seal must be that there is a corresponding thing in order to seal the thing.
  - You can't seal something that doesn't exist.
  - The Requiem Aura's restrictions on [[Undead]] just block the exit; the concept of undead still exists.
  - The [[Invalidation Law]] only curbs the use of extraordinary abilities, but the abilities still exist.
  - The ability that is stolen or deprived is regarded as disappearing, so it does not exist and cannot be regarded as a seal.
- **At Sequence 0:**
  - You can affect the whole world and weaken all seals.

- **Limits:** As described in this section's prose.
