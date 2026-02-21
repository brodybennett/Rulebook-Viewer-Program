---
title: 'Sequence 3: Balancer'
id: arbiter-seq-03
tags:
- pathway:arbiter
- sequence:3
---






# Justiciar Pathway: Sequence 3

## Balancer

> **GM Note:** "The number of Extraordinary abilities that can be taken away has greatly increased." appears in the source; treat this as using the **Invalidation Law** procedure.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Based on the law, resolve a state-level chaos that has been swept up, **or** hunt and bring to justice an angel-level or near-angel-level existence with "chaos" as its core, **Sequence 2 or higher**. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +1, Agility (DEX) +1, Strength +1, Constitution +1.
- Legal skills increase by 1 skill level.

### Chaos Hunter

```yaml ability
id: arbiter-seq-03-chaos-hunter
name: Chaos Hunter
pathway: arbiter
sequence: 3
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.law
opposed_by: difficulty_value
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted appraisal token for jurisdiction sight and remote trial-linking; the core bonus package is passive.
scaling:
- when: target_is_black_emperor_pathway
  changes:
    effect_note: Skill bonus becomes +8 and attribute appraisal bonus is +4 while damage identification bonus remains +4.
- when: sequence_2_or_higher
  changes:
    effect_note: Anyone violating your established system inside jurisdiction is included in order-sight tracking.
tags:
- offense
- detection
- divination
- utility
text: 'Effect: From now on, you and your disciplinary knights gain a +4 bonus in skill
  identification and damage identification for all criminals and undead, corrupt,
  dark, and other natural forces that affect order. For the [[Black Emperor]]: +8
  skill bonus, +4 attribute check; damage identification bonus remains +4 (unchanged
  from the baseline above). OrderaTMs sight: Within a kilometer of you, or when you
  are in your jurisdiction, order becomes your eyes. You make up to two laws based
  on the realms of unholy, undead, fallen, and dark. When corresponding behaviors
  or creatures appear in your jurisdiction, they are considered violators of the law
  and become criminals. You can immediately cast s...'
```





- **Effect:**
  - From now on, you and your disciplinary knights gain a +4 bonus in skill identification and damage identification for all criminals and undead, corrupt, dark, and other natural forces that affect order.
  - For the [[Black Emperor]]: +8 skill bonus, +4 attribute check; damage identification bonus remains **+4** (unchanged from the baseline above).  
  - **Order's sight:** Within a kilometer of you, or when you are in your **jurisdiction**, order becomes your eyes.
    - You make up to two laws based on the realms of unholy, undead, fallen, and dark.
    - When corresponding behaviors or creatures appear in your jurisdiction, they are considered violators of the law and become criminals.
    - You can immediately cast sight from a distance and perform a **trial**.
      - If a trial is held, your connection with the other party is reduced, immediately interrupted, and cannot be tracked again within half a day.
      - Without a trial, you can continue to observe the criminal through the boundaries of the district.
  - This is considered a [[id:alias-divination|Divination]] or [[id:alias-prophecy|Prophecy]] effect and will be affected by corresponding [[Counter-Divination]].
    - It usually does not work well for spirit creatures and spirits.
    - It will not trigger the [[Witch's Curse]].
- **Limits:**
  - Up to two laws may be made (as above).
  - After you hold a trial (as above), you cannot track that target again within half a day.

- **At Sequence 2:** Anyone who violates the system you have established, or the system under your jurisdiction, is included in your sight in the jurisdiction.

### Messenger of Order

```yaml ability
id: arbiter-seq-03-messenger-of-order
name: Messenger of Order
pathway: arbiter
sequence: 3
status: canonical
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- debuff
text: 'Use: Once per Round, as a Free Action, eliminate: a power related to darkness,
  corruption, and undead domains, and curses on your body. Limits / Modifiers: For
  curses higher than your Sequence level, the effect is halved, and a free action
  is also consumed.'
```





- **Use:** Once per Round, as a Free Action, eliminate:
  - a power related to darkness, corruption, and undead domains, **and**
  - curses on your body.
- **Limits / Modifiers:**
  - For curses higher than your Sequence level, the effect is halved, and a free action is also consumed.

> **GM Note:** Starting from this Sequence, due to a lack of information on the extraordinary abilities in the original work, some abilities of the Judge Pathway (Sequence 3-0) are original to the supplementers.

- **Effect:** Messenger of Order resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
