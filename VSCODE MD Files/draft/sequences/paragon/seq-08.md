---
title: 'Sequence 8: Archaeologist'
id: paragon-seq-08
tags:
- pathway:paragon
- sequence:8
---






# Paragon Pathway: Sequence 8

You possess sufficient historical knowledge, wilderness survival knowledge, and taboo knowledge related to ruins. You have a strong enough body and the ability to face these matters, and you can barely use some ritual magic.

## Archaeologist

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +2, Agility (DEX) +1
- Archaeology, history, survival, mysticism, and mysticism language are included in the rapid growth category of Sequence 9, reaching proficiency at most.

### Ritual Use

```yaml ability
id: paragon-seq-08-ritual-use
name: Ritual Use
pathway: paragon
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.archaeology
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.archaeology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: DV 15 checks use the relevant skill (archaeology, history, survival, engineering, physics).
scaling: []
tags:
- ritual
text: 'You can barely use some [[Ritual Magic]]. Effect: While you hold this ability,
  you are qualified to use ritual magic. As long as you are trained in mysticism and
  know how to use rituals, you can use them regardless of whether the skill has reached
  the advanced level. For the ritual magic you can use, refer to [[Common Ritual Magic]].
  Unlike [[Voyeur]] and [[Fortune-Teller]], you cannot develop more ritual magic based
  on these commonly used ritual magic unless someone directly tells you the corresponding
  Knowledge. Special: Only when using ritual magic, if your mysticism has not reached
  the advanced level, then your occultism identification suffers -2 disadvantage.
  This includes making spe...'
```





You can barely use some [[Ritual Magic]].

- **Effect:**
  1. While you hold this ability, you are qualified to use ritual magic. As long as you are trained in mysticism and know how to use rituals, you can use them regardless of whether the skill has reached the advanced level.
  2. For the ritual magic you can use, refer to [[Common Ritual Magic]]. Unlike [[Voyeur]] and [[Fortune-Teller]], you cannot develop more ritual magic based on these commonly used ritual magic unless someone directly tells you the corresponding Knowledge.
- **Special:** Only when using ritual magic, if your mysticism has not reached the advanced level, then your occultism identification suffers -2 disadvantage. This includes making spells, etc.
- **Sequence 6:** Regardless of whether your mysticism has reached the advanced stage or not, you will no longer suffer from the restrictions related to ritual magic, and you can use ritual magic normally.

- **Limits:** As described in this section's prose.


### Forbidden Knowledge

```yaml ability
id: paragon-seq-08-forbidden-knowledge
name: Forbidden Knowledge
pathway: paragon
sequence: 8
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
- detection
text: 'You know or can decipher the history sealed by the church. Effect: When you
  conduct historical and archaeological appraisal of a historical relic or mural,
  even if the relic involves secrets that you dont know, you can dig out the surface
  information contained in it and learn the approximate age of its origin. This information
  is usually destroyed and prohibited by the [[Seven Gods]]. You are considered to
  have known the basic common sense of these histories, so you can learn the superficial
  meaning of these cultural relics. Special: When obtaining age information, the age
  information you can obtain is limited to the [[Quaternary Epoch]], [[Tertiary Epoch]],
  and [[Second Epoch]]. Before t...'
```





You know or can decipher the history sealed by the church.

- **Effect:** When you conduct historical and archaeological appraisal of a historical relic or mural, even if the relic involves secrets that you don’t know, you can dig out the surface information contained in it and learn the approximate age of its origin.
- This information is usually destroyed and prohibited by the [[Seven Gods]]. You are considered to have known the basic common sense of these histories, so you can learn the superficial meaning of these cultural relics.
- **Special:** When obtaining age information, the age information you can obtain is limited to the [[Quaternary Epoch]], [[Tertiary Epoch]], and [[Second Epoch]]. Before the Second Epoch, you can only know that it came from before the Second Epoch, but not the more specific time.

> **Lore:** Example: You know the [[Amon Family]] of the [[Fourth Epoch]], but you don’t know the truth that the Amon family actually has only one person. You know that the gods were not represented by holy brilliance in the past, but you don’t know that the gods used to be represented by sculptures. Why are they sculptures

- **Limits:** As described in this section's prose.


### Organ Investigation

```yaml ability
id: paragon-seq-08-organ-investigation
name: Organ Investigation
pathway: paragon
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: 100m
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
- detection
- mobility
- offense
text: 'You are very keen on organs, traps, and secret doors. Effect: Whenever you
  make a detection appraisal, if there are organs, traps, and hidden doors within
  100 meters of you as the center, you can immediately find them and know where they
  are located. This includes detection and identification performed unconsciously.
  For example, you just want to detect a certain creature, but there happens to be
  a mechanism, secret door, or trap here, so you can find it immediately. Special:
  When you are attacked by a mechanism or a trap, the mechanisms attack identification
  is -4 disadvantageous.'
```





You are very keen on organs, traps, and secret doors.

- **Effect:** Whenever you make a detection appraisal, if there are organs, traps, and hidden doors within 100 meters of you as the center, you can immediately find them and know where they are located.
- This includes detection and identification performed unconsciously. For example, you just want to detect a certain creature, but there happens to be a mechanism, secret door, or trap here, so you can find it immediately.
- **Special:** When you are attacked by a mechanism or a trap, the mechanism’s attack identification is -4 disadvantageous.

- **Limits:** As described in this section's prose.


### Lore Practice

```yaml ability
id: paragon-seq-08-lore-practice
name: Lore Practice
pathway: paragon
sequence: 8
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
- utility
text: 'You gain additional benefits when you use knowledge skills related to archaeology.
  This is just an explanation of the ability of archaeologists, and cannot be recorded
  or stolen. Your skill checks gain the following additional benefits: Archaeological
  identification: 1 archaeological identification with a difficulty of 15, you can
  judge the approximate age of any objecthow many years ago, or the product of which
  eraand even judge the possible incorrect direction of the storage room and coffin.
  This includes not only heritage but also contemporary buildings, whether they are
  new or in disrepair. It even includes whether a creature itself or its characteristics
  fit the age, whether it shoul...'
```





You gain additional benefits when you use knowledge skills related to archaeology.

- This is just an explanation of the ability of archaeologists, and cannot be recorded or stolen.
- Your skill checks gain the following additional benefits:

1. **Archaeological identification:** 1 archaeological identification with a difficulty of 15, you can judge the approximate age of any object—how many years ago, or the product of which era—and even judge the possible incorrect direction of the storage room and coffin. This includes not only heritage but also contemporary buildings, whether they are new or in disrepair. It even includes whether a creature itself or its characteristics fit the age, whether it should have been extinct, or never been found.
2. **History appraisal:** 1 historical appraisal with a difficulty of 15. You can judge whether an extraordinary ability known to you is recorded in past history, including weird and abnormal cases such as a high-sequence ability that only exists in fairy tales.  
   **Special:** This can also determine whether a certain story or information may involve historical mysteries, usually accompanied by taboo knowledge.
3. **Survival identification:** 1 survival identification with a difficulty of 15, you can find out the way to break a certain material trap based on experience. This can also find an area where there might be creatures, and this even involves finding some homeless or dying people in cities trying to survive. This principle is to deduce where these hungry and cold people will go based on the living habits of the creatures themselves.
4. **Engineering identification:** 1 identification with a difficulty of 15, you immediately understand the composition of an object or building (excluding creatures), where to find its weak points, whether it is easy to collapse, and whether a room is missing out of thin air (hidden room).
5. **Physics appraisal:** 1 physics appraisal with a difficulty of 15. You find an exit in a relic or house according to the air flow direction. This may be a window, a vent, or an undiscovered door. The premise of the appraisal is that the exit still exists.

> **GM Note:** More other, rational use of skills depends on the Player’s knowledge of reality.

- **Effect:** Lore Practice resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
