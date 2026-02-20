---
title: 'Sequence 4: Prophet'
id: reader-seq-04
tags:
- pathway:reader
- sequence:4
---





# White Tower Pathway: Sequence 4

## Prophet

> **Lore:** Begin mastering higher-level mystic knowledge in the field of destiny, awakening **Prophecy** [[id:alias-prophecy|Prophecy]].

> **Lore:** Create a rational anchor within the irrational torrent of fate.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Relying on your own strength, reveal a secret event, calculate its future development, and confirm the development is indeed true. The higher the level of secrecy involved, the better the effect.
  > **GM Note:** This ritual is marked “unofficial ceremony” in the source text.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +2; Education +2; your knowledge of fate and mysticism rises by one level ([[Fate Knowledge]]).

### Proficient in Knowledge

```yaml ability
id: reader-seq-04-proficient-in-knowledge
name: Proficient in Knowledge
pathway: reader
sequence: 4
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- divination
- detection
- buff
text: 'Use: Passive. Effect: Your Spiritual Vision [[id:alias-spiritual-vision|Spiritual
  Vision]] can mark objects that contain knowledge carriers (words, pictures, etc.)
  within your field of vision. Your Spiritual Intuition [[Spiritual Intuition]] can
  perceive similar knowledge carriers within 1 kilometer (directional sense). You
  do not need to touch knowledge carriers to read them, as long as they are within
  your field of vision. You can see text and pictures hidden in clothing or body parts,
  as long as the relevant objects do not have Anti-Divination [[id:alias-anti-divination|Anti-Divination]]
  and Anti-Prophecy [[Anti-Prophecy]] characteristics. Limits: Sequence 3 improvement:
  the intuition...'
```




- **Use:** Passive.
- **Effect:**
  - Your **Spiritual Vision** [[id:alias-spiritual-vision|Spiritual Vision]] can mark objects that contain knowledge carriers (words, pictures, etc.) within your field of vision.
  - Your **Spiritual Intuition** [[Spiritual Intuition]] can perceive similar knowledge carriers within 1 kilometer (directional sense).
  - You do not need to touch knowledge carriers to read them, as long as they are within your field of vision.
  - You can see text and pictures hidden in clothing or body parts, as long as the relevant objects do not have **Anti-Divination** [[id:alias-anti-divination|Anti-Divination]] and **Anti-Prophecy** [[Anti-Prophecy]] characteristics.
- **Limits:**
  - Sequence 3 improvement: the intuition perception range increases to 5 kilometers ([[id:alias-sequence-3|Sequence 3]]).
  - This is a potion effect ([[Potion Effects]]) and cannot be stolen or recorded.

### Quick Reading

```yaml ability
id: reader-seq-04-quick-reading
name: Quick Reading
pathway: reader
sequence: 4
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- mobility
- buff
text: 'Use: Passive. Effect: During the middle and low Sequence period, it takes you
  1 minute to complete library identification with familiarity of knowledgespecifically,
  locating the relevant materials (excluding travel time to retrieve books). You now
  need 5 minutes to read a book that would normally take a month to read (instead
  of a book that would normally take a week to read). Limits: Sequence 3 improvement:
  reading a book that would normally take a month takes 1 minute ([[id:alias-sequence-3|Sequence
  3]]).'
```




- **Use:** Passive.
- **Effect:**
  - During the middle and low Sequence period, it takes you 1 minute to complete “library identification with familiarity of knowledge”—specifically, locating the relevant materials (excluding travel time to retrieve books).
  - You now need 5 minutes to read a book that would normally take a month to read (instead of a book that would normally take a week to read).
- **Limits:**
  - Sequence 3 improvement: reading a book that would normally take a month takes 1 minute ([[id:alias-sequence-3|Sequence 3]]).

### Prophecy

```yaml ability
id: reader-seq-04-prophecy
name: Prophecy
pathway: reader
sequence: 4
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
- ritual
- divination
text: 'Cost: 8 points of Spirituality [[Spirituality]]. Use: 1 Casting Action Casting
  Action. Effect: Conduct a Fate Knowledge Appraisal [[Fate Knowledge Appraisal]]
  and judge the prophecy result based on that appraisal. The prophecy is subject to
  the following Difficulty results: Difficulty 20: Predict exactly what will happen
  in the next hour, excluding the effects of making changes accordingly. Difficulty
  25: Predict exactly what will happen in the next 6 hours, excluding the effects
  of making changes accordingly. Difficulty 30: Predict exactly what will happen in
  the next 12 hours, excluding the effects of making changes accordingly.'
```




- **Cost:** 8 points of **Spirituality** [[Spirituality]].
- **Use:** 1 **Casting Action** Casting Action.
- **Effect:**
  - Conduct a **Fate Knowledge Appraisal** [[Fate Knowledge Appraisal]] and judge the prophecy result based on that appraisal.
  - The prophecy is subject to the following Difficulty results:
    - **Difficulty 20:** Predict exactly what will happen in the next hour, excluding the effects of making changes accordingly.
    - **Difficulty 25:** Predict exactly what will happen in the next 6 hours, excluding the effects of making changes accordingly.
    - **Difficulty 30:** Predict exactly what will happen in the next 12 hours, excluding the effects of making changes accordingly.
    - **Difficulty 35:** Accurately predict what will happen in the next 24 hours, excluding the impact of making changes based on it. After 12 hours, the information begins to blur or contain certain errors.
    - **Difficulty 40 (Long-Term Prediction):** Predict things that will happen in at least one month, up to ten years or decades. The content will be very general, and unless there are enough [[Clues]] the predicted matters must be strongly related to you.
    - **Difficulty 30 (Other Uses):** Prophecy can be used in reverse to infer prior events that led to the current outcome, and can be combined with previous abilities to retrace earlier steps.
- **Limits:**
  - Before obtaining new clues, repeating the same prophecy does not change the result.
  - Foretelling others requires obtaining clues first.
  - Prophecy is not affected by **Anti-Divination** [[id:alias-anti-divination|Anti-Divination]]. It is essentially logical deduction based on [[Fate Knowledge]], so even if anti-divination occurs, key information can still be obtained.
  - Because it relies on deduction, prophecy can lead in the wrong direction if the deduction is based on wrong information.
  - Prophecies lacking clues may be inconsistent with reality. If key information lacks information, it will not be presented and will be replaced by other reasonable content.
- **Aftereffects:**
  - **Great Success** Great Success: Your prediction involves a key piece of information. If you did not have a clue for that key piece of information when you made the prediction, it changes to a key piece of information involving a clue you do have.
  - **Big Failure** Big Failure: Your prophecy leads in a half-true or terribly wrong direction, and you must believe it until you get new clues.


> **GM Note:** Long-term prophecy example: you can predict you will encounter a desperate situation, and that “someone you know somewhere” will help you, but you do not know what the situation is or who will help you. If the indicated place involves someone you do not already know, you may need to go there and befriend people to establish the connection—if you do not, the rescuer may not appear when you encounter difficulties.
>
> **GM Note:** Another example: you can predict the approximate time a major disaster will come because it is strongly related to yourself.
