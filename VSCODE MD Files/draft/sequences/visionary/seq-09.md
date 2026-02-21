---
title: 'Sequence 9: Spectator'
id: visionary-seq-09
tags:
- pathway:visionary
- sequence:9
---






# Visionary Pathway: Sequence 9

## Spectator

- See also: Visionary

> **Lore:** In ancient times, the Visionary Pathway was called the “Dragon” path and was associated with the spiritual realm. Its mythic creature is depicted as a dragon and corresponds to the Tarot card “Justice.”

You are a **Spectator**: a bystander-like observer with outstanding spirit and keen insight into “actors” in secular society, able to read people through expression, behavior, speech habits, and subtle movements—and to influence outcomes from behind the scenes.

## Advancement

### Main Ingredients

- [[Manhal Fish Eyes]] ×1 pair
- [[Black-Horned Fish Blood]] 35 ml

### Auxiliary Materials

- [[Pure Water]] 80 ml
- [[Colchicum Essence]] 5 drops
- [[Bovine Peony Powder]] 13 g
- [[Fairy Flowers]] 7 petals

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2, **Charisma (CHA)** +1  
  - This Charisma (CHA) is *personality charm* and does not affect appearance. [[Charisma (CHA)]]
  - Intuition

### Enhanced Learning

```yaml ability
id: visionary-seq-09-enhanced-learning
name: Enhanced Learning
pathway: visionary
sequence: 9
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
  effect_roll: "1"
  notes: "No roll; ends when you enter an emotion or shock and imposes -4 on emotion checks against you."
scaling: []
tags:
- buff
text: 'You become better at mastering skills related to psychology and psychological
  guidance. If you complete an effective, real course of at least 2 hours, your corresponding
  skills increase by 1 level. [[Skills]] To advance skill levels: Training Proficiency:
  learn 2 times. Proficiency Advanced: learn 3 times. A Sequence 9 potion supports
  you reaching Advanced for now; after that, your learning rate cannot gain a substantial
  improvement. [[Potions]] *Limits Learning can only be done once per day.'
```





You become better at mastering skills related to psychology and psychological guidance.

- If you complete an effective, real course of at least 2 hours, your corresponding skills increase by 1 level. [[Skills]]
- To advance skill levels:
  - Training → Proficiency: learn **2** times.
  - Proficiency → Advanced: learn **3** times.
- A Sequence 9 potion supports you reaching **Advanced** for now; after that, your learning rate cannot gain a substantial improvement. [[Potions]]

**Limits**
- Learning can only be done once per day.
- Characters of higher Sequences can use **twice** the Intuition (INT) brought by potions to improve their growth skills. Higher Sequences

- **Effect:** Enhanced Learning resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Perfect Recall

```yaml ability
id: visionary-seq-09-perfect-recall
name: Perfect Recall
pathway: visionary
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.psychology
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: "Difficulty Value 20 psychology check to remove emotional effects not above Personality."
scaling: []
tags:
- utility
text: Under the premise of not being affected by extraordinary factors, you do not
  forget things you have seen or heard. [[Extraordinary Factors]]
```





- Under the premise of not being affected by extraordinary factors, you do not forget things you have seen or heard. [[Extraordinary Factors]]

- **Effect:** Perfect Recall resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spectator State

```yaml ability
id: visionary-seq-09-spectator-state
name: Spectator State
pathway: visionary
sequence: 9
status: canonical
type: active
action: free
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
- fear
tags:
- debuff
- defense
text: 'You can enter a detached observational mode to read others real thoughts from
  details. Use: 1 Free Action to enter Spectator State. [[Spectator State]] Effect:
  While in Spectator State, you observe others real thoughts through details. End
  Condition: Your Spectator State ends when you fall into an emotion or [[Shock]].
  [[Conditions]] Resistance: When a creature attempts to make you enter anger, fear,
  or charm (but not shock), their identification/check is at -4 disadvantage against
  you.'
```





You can enter a detached observational mode to read others’ real thoughts from details.

- **Use:** 1 Free Action to enter **Spectator State**. [[Spectator State]]
- **Effect:** While in Spectator State, you observe others’ real thoughts through details.
- **End Condition:** Your Spectator State ends when you fall into an emotion or [[Shock]]. [[Conditions]]

- **Resistance:** When a creature attempts to make you enter **anger**, **fear**, or **charm** (but not **shock**), their identification/check is at **-4 disadvantage** against you.

- **Limits:** As described in this section's prose.


### Remove Emotional Effects

```yaml ability
id: visionary-seq-09-remove-emotional-effects
name: Remove Emotional Effects
pathway: visionary
sequence: 9
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
- mobility
text: 'Use: 1 Casting Action Check: Psychology check, Difficulty 20. [[Psychology]]
  Effect: Remove emotional effects on yourself not greater than [[Personality]].'
```





- **Use:** 1 Casting Action
- **Check:** Psychology check, Difficulty 20. [[Psychology]]
- **Effect:** Remove emotional effects on yourself not greater than [[Personality]].

- **Limits:** As described in this section's prose.


### Observe Others

```yaml ability
id: visionary-seq-09-observe-others
name: Observe Others
pathway: visionary
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.psychology
opposed_by: difficulty_value
range: Choose 1 creature within your field of vision.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: "Difficulty Value tiers 10/15/20/25; great success grants +2 psychology-related checks vs the target until their style changes; big failure alerts the target."
scaling: []
tags:
- detection
- mobility
text: 'Make a focused read of a visible target. Check: Make a Psychology check. Targeting
  and range: Choose 1 creature within your field of vision. Effect: Gain information
  based on the check result: 1) Difficulty 10: Confirm the targets current status
  based on dress / habits / furnishing style of the room. 2) Difficulty 15: Confirm
  the targets general thoughts / purposes from body language (no details). 3) Difficulty
  20: Confirm the targets character from demeanor / expression / conversation, and
  know how to get along with them. 4) Difficulty 25: Confirm possible relationships
  between the target and anyone around them based on gaze direction / sneak glances
  / small movements.'
```





Make a focused read of a visible target.

- **Check:** Make a Psychology check.
- **Targeting and range:** Choose 1 creature within your field of vision.
- **Effect:** Gain information based on the check result:

1) Difficulty 10: Confirm the target’s current status based on dress / habits / furnishing style of the room.  
2) Difficulty 15: Confirm the target’s general thoughts / purposes from body language (no details).  
3) Difficulty 20: Confirm the target’s character from demeanor / expression / conversation, and know how to get along with them.  
4) Difficulty 25: Confirm possible relationships between the target and anyone around them based on gaze direction / sneak glances / small movements.  
5) Great success: Summarize the target’s “mental model.” Social/psychology-related identifications gain a +2 benefit regarding that target until their style of doing things changes. If the target is possessed/replaced, the +2 benefit still exists but does not work. [[Possession]]  
6) Big failure: You still get the corresponding result, but the target notices you are observing them.

**Special**
- If a character proactively roleplays something like “restrain body movements and do not make any performance” *before* being observed, then at the difficulties above, you can no longer obtain information based on “body language.”

**Limits**
- You cannot get content that lacks intelligence. Example: if someone wants to obtain a formula through you, you can only know they have other plans. [[Intelligence]]
- Every time you obtain 1 piece of information, your “observation appraisal” gains a +2 benefit; this stacks. Exposed details count as information. [[Stacking Modifiers]]
- If a [[Faceless Man]] pretends to be someone else, and you know habits of the original person that the Faceless Man does not, you may be able to see through the disguise. [[Disguise]]
- This Audience status is passive and cannot be recorded or stolen.
- Limited by intelligence, the observed results may not match the actual situation.

- **Limits:** As described in this section's prose.


### Passive Observation

```yaml ability
id: visionary-seq-09-passive-observation
name: Passive Observation
pathway: visionary
sequence: 9
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
text: As long as someone reveals certain details in front of you, the GM may immediately
  allow you to make an identification to obtain information.
```





- As long as someone reveals certain details in front of you, the **GM** may immediately allow you to make an identification to obtain information.

- **Effect:** Passive Observation resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Psychological Guidance

```yaml ability
id: visionary-seq-09-psychological-guidance
name: Psychological Guidance
pathway: visionary
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: willpower_defense
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
- defense
text: 'You subtly influence and secretly guide things to develop in the direction
  you want. Setup: First determine one thing you want to guide, then confirm the result
  you want to guide. Constraint: The guided result cannot contradict the intention
  of the person being guided, and must be relevant and reasonable enough. Requirement:
  You must take actions to make the guidance happen (not necessarily limited to words).
  Opposition: Psychological Guidance is opposed to Willpower Defense. *Procedure (example
  structure) 1) Confirm what you want to guide (e.g., guide a lady regarding marriage).
  2) Confirm the result you want to guide (e.g., she accepts a third partys proposal
  and abandons her husband).'
```





You subtly influence and secretly guide things to develop in the direction you want.

- **Setup:** First determine one thing you want to guide, then confirm the result you want to guide.
- **Constraint:** The guided result cannot contradict the intention of the person being guided, and must be relevant and reasonable enough.
- **Requirement:** You must take actions to make the guidance happen (not necessarily limited to words).
- **Opposition:** Psychological Guidance is opposed to Willpower Defense.

**Procedure (example structure)**
1) Confirm what you want to guide (e.g., guide a lady regarding marriage).  
2) Confirm the result you want to guide (e.g., she accepts a third party’s proposal and abandons her husband).  
3) Take actions to achieve guidance (e.g., mention rumors about the husband; point out the third party’s benefits).  
4) When the target faces the relevant choice, make your appraisal; the GM resolves success against Willpower Defense.

**Modifiers (GM adjudication of reasonableness applies)**
- Initial judgment: Psychological Guidance is **-8 unfavorable**.
- Apply the following adjustments:

1) You have no understanding of the target: -2 unfavorable.  
2) It is known you are a spectator: -2 unfavorable (the target knows you are a spectator and knows the spectator ability can take effect).  
3) You know the target’s status: +2 beneficial.  
4) You know the target’s identity: +2 beneficial.  
5) You know the target’s character: +2 beneficial.  
6) You know any relationship network of the target: +2 beneficial.  
7) You know the target’s habits: +2 beneficial.  
8) You know the target’s weakness: +2 beneficial; only applies when the guidance content is related to that weakness.

- If the Psychological Guidance penalty becomes 0 due to the advantages/disadvantages above, Psychological Guidance succeeds by default, excluding targets more than 1 Sequence higher than you.

**On Success**
- The guided creature must act according to the guided content, but cannot detect abnormalities.
- If the guided target actively examines the guided details, they can use Intuition to counter your identification result at that time and realize something is wrong.

**Limits**
- This is an improvement brought by the potion, so it cannot be stolen or recorded.

- **Effect:** Psychological Guidance resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spiritual Vision

```yaml ability
id: visionary-seq-09-spiritual-vision
name: Spiritual Vision
pathway: visionary
sequence: 9
status: canonical
type: toggle
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: "No roll; cost is per round while active and grants +2 to Spiritual Intuition tests."
scaling: []
tags:
- ritual
- detection
- healing
- mobility
text: 'You gain more outstanding spiritual vision due to your Intuition (INT). Use:
  1 free action to activate. Cost: 1 spirituality point per round while active. Effect:
  While active, your vision gains the following benefits: 1) Etheric Body: See the
  targets health status through aura color; find where the body is uncomfortable/has
  problems. For specific organs, you can see inside through an unthickened door and
  confirm the number of people inside. 2) Spiritual Body: Confirm whether an object/creature
  has spirituality. This does not identify extraordinary people. You can also see
  inside through a door, identify whether there is ritual magic power present, and
  penetrate a spiritual wall. [[Ritual...'
```





You gain more outstanding spiritual vision due to your Intuition (INT).
- **Use:** 1 **free action** to activate.
- **Cost:** 1 **spirituality point per round** while active.
- **Effect:** While active, your vision gains the following benefits:


1) **Etheric Body:** See the target’s health status through aura color; find where the body is uncomfortable/has problems. For specific organs, you can see inside through an unthickened door and confirm the number of people inside.  
2) **Spiritual Body:** Confirm whether an object/creature has spirituality. This does not identify extraordinary people. You can also see inside through a door, identify whether there is ritual magic power present, and penetrate a spiritual wall. [[Ritual Magic]] [[Spiritual Wall]]  
3) **Mental Body:** See colors representing the other person’s emotions, but only as general content (e.g., depressed vs uneasy). Negative emotion is usually a dark tone.  
4) **Astral Body:** You cannot see the astral body.  
5) While in Spiritual Vision, your [[Spiritual Intuition]] test gains a +2 benefit.

**Sequence 8 Improvement**
- At Sequence 8, you can see detailed content of the other party’s mental body: the specific emotional state (nervous, etc.). Visionary Pathway Sequence 8

> **GM Note:** Dead creatures are usually dull in color and cannot be recognized. Spiritual materials usually have spirituality. The color of a material in Spiritual Vision usually represents its corresponding pathway—this does not mean you can see a Beyonder’s power. [[Beyonder]]
>
> **GM Note:** Colors seen in Spiritual Vision can help you see others in the dark, but you only perceive the existence of color and can still get lost in the dark. Unlike dead creatures, undead creatures display deep black “spirituality color” rather than having none. [[Undead]]
>
> **GM Note:** Spirit Vision can see some ordinary spirit bodies by default if they have not dissipated for 24 hours.

**Limits**
- Spirit Vision cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
