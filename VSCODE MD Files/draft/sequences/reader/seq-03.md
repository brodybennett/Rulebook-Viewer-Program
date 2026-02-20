---
title: 'Sequence 3: Cognizer'
id: reader-seq-03
tags:
- pathway:reader
- sequence:3
---





# White Tower Pathway: Sequence 3

## Cognizer

> **Lore:** A Cognizer pursues “insight” into the world’s underlying rules. Against them, secrets are hard to keep—strengths, weaknesses, and hidden truths tend to be exposed.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Gain a deep understanding of a rule at the bottom of the world, try to fill in its weaknesses, then find out its weaknesses on this basis, repeating until it cannot be handled. (Unofficial ceremony.)

> **Lore:** Under the impact of chaotic and disordered underlying knowledge, you create your own fortress and anchor. Repeated processing pushes the stability of the fortress to the limit until it “belongs to you” in the mystic sense.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +2, Education +2; your Occult skills increase by 1 level; your Detection skills increase by 2 levels; all Science skills increase by 1 level.

### Master the Mysteries

```yaml ability
id: reader-seq-03-master-the-mysteries
name: Master the Mysteries
pathway: reader
sequence: 3
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
- utility
text: 'Effect: You see the rules of the world and master many deep mysteries. From
  now on, regardless of what you were like before, you know most mystic knowledge
  in this world by default (including [[Sequence 0]], [[King of Angels]], Higher Sequences,
  and part of the [[Starry Sky]]). Most esoteric setting knowledge you know as a Player
  can be summarized on your character sheet. Your Education-related skill checks and
  attribute checks automatically succeed when they are not contested and you are not
  using an ability. Limits: This is a potion effect and cannot be stolen or recorded.'
```




- **Effect:**
  - You “see” the rules of the world and master many deep mysteries.
  - From now on, regardless of what you were like before, you know most mystic knowledge in this world by default (including [[Sequence 0]], [[King of Angels]], Higher Sequences, and part of the [[Starry Sky]]).
  - Most esoteric setting knowledge you know as a Player can be summarized on your character sheet.
  - Your Education-related skill checks and attribute checks **automatically succeed** when they are not contested and you are not using an ability.
- **Limits:**
  - This is a potion effect and cannot be stolen or recorded.

### Insight

```yaml ability
id: reader-seq-03-insight
name: Insight
pathway: reader
sequence: 3
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target object you can see (within your [[Field of Vision]]).
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- divination
- detection
text: 'Cost: 8 points of [[Spirituality]]. Use: 1 Casting Action. Targeting and range:
  Choose 1 target object you can see (within your [[Field of Vision]]). Effect: Conduct
  a Detection appraisal on the target. This ability ignores [[id:alias-anti-divination|Anti-Divination]].
  Same as the previous ability, but ordinary misleading/incorrect information cannot
  cause Insights information to be wrong; Insight can only be affected by other extraordinary
  abilities (e.g., [[Secret]]). [[MISSING REF: Insight references a previous ability
  it is the same as, but that ability is not included in this chunk.]]'
```




- **Cost:** 8 points of [[Spirituality]].
- **Use:** 1 Casting Action.
- **Targeting and range:** Choose 1 target object you can see (within your [[Field of Vision]]).
- **Effect:**
  - Conduct a Detection appraisal on the target.
  - This ability ignores [[id:alias-anti-divination|Anti-Divination]].
  - “Same as the previous ability,” but ordinary misleading/incorrect information cannot cause Insight’s information to be wrong; Insight can only be affected by other extraordinary abilities (e.g., [[Secret]]).  
    [[MISSING REF: Insight references a “previous ability” it is “the same as,” but that ability is not included in this chunk.]]
  - Repeated Insights yield the same results unless new leads are obtained.
  - If the selected target is only a portrait/image, resolve Insight according to [[Basic Deduction]] with no Success Level restrictions; however, you cannot use the extended reasoning option of Basic Deduction (only basic results).

- **Appraisal Results (by Difficulty):**
  - **Difficulty 25:** Reveal the target’s current Extraordinary Path, its approximate Sequence level, and—if it is not an Extraordinary thing—**all** information about it, including its owner and who has been in contact with it before.
  - **Difficulty 30:** In addition to the above, learn what the target is best at and least good at; immediately know the target’s top 3 skills, the highest skill level, and the lowest skill level.
    (This includes weaknesses in an extraordinary or normal sense, likes, dislikes, weaknesses, and things the target is not good at dealing with.)  
  - **Difficulty 35:** In addition to the above, learn whether the target has extraordinary items; the item’s current Path and approximate Sequence level; and judge the item’s current state (semi-crazy, on the verge of losing control, or other special states).
  - **Difficulty 40:** In addition to the above, learn the target’s highest and lowest attributes; current blood volume, spirituality, and sanity; and the upper limits of blood volume, spirituality, and sanity.
  - **Difficulty 45:** In addition to the above, learn the specific values of the target’s resistance, reduction, and the three defenses (physics, constitution, and will), as well as the target’s approximate personality.  
    [[Personality]]

- **Success/Failure Extremes:**
  - **Big Success:** Based on your Success Level, you gain the detailed part of any information you could have obtained (e.g., complete skill list and levels; whether the target has changed Pathway and what it was; or the complete 6 attribute values).  
    Targets understood by Difficulty 45 or Big Success grant you **advantage** on subsequent Insight/identification checks against them for the rest of the encounter.
  - **Big Failure:** You fail to control the extent of your ability and still obtain information equivalent to the final appraisal result, but the target immediately hears a spiritual alarm and knows the alarm points to you—feeling your secret is clear at a glance.

- **More Insights (Difficulty 40):**
  - More Insights generally require clues, and can confirm the Path and level involved in an extraordinary event, whether it involves secrets, whether the truth is false, and so on.

- **Special Situations:**
- Understanding the mythical form of Sequence 2 and Above, [[Informational Creatures]], and targets with **Personality at least 1 higher than yours** in the Hermit pathway immediately causes you to suffer a corresponding sanity blow, even if you have already suffered a blow.  
  - Knowledge obtained through Insight can only be within the scope of your knowledge. If the target is not within the [[22 Pathways]] and you do not have the corresponding knowledge, you only get false information that fits within your scope of knowledge and similar pathways (you do not realize the incongruity until you get new leads).
  - For skills/strengths/weaknesses not within your knowledge, you can only know what they are like, but not what they are.

- **Limits:** As described in this section's prose.
