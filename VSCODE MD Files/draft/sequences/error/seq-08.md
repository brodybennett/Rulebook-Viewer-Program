---
title: 'Sequence 8: Swindler'
id: error-seq-08
tags:
- pathway:error
- sequence:8
---






# Error Pathway: Sequence 8

> **Lore:** Scammers take pleasure in deceiving others and can create illusions to deceive opponents.

## Swindler

## Advancement

- Each time you complete a **non-repetitive, challenging** swindle or deceit, choose any one skill (persuade/talk/please/deceive) that is primarily used in the swindle; that skill increases by 1 level.
- The same as the promotion of Sequence 9. Sequence 9
  - Bullying the weak does not meet the promotion requirements.
  - The promotion range, and the level that can be promoted to, are equal to Sequence 9's **Detection** at **Mastery**. [[master/detection]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Agility (DEX)** +2, **Constitution** +1, **Intuition (INT)** +1.
- Your **Persuasion**, **Speech**, **Pleasing**, and **Intimidation** skills increase by 1 level.

### Charisma

```yaml ability
id: error-seq-08-charisma
name: Charisma
pathway: error
sequence: 8
status: adapted
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
  effect_roll: "2"
  notes: Effect roll captures the +2 Charisma bonus applied to Charisma-related checks.
scaling:
- when: intimidation_checks
  changes:
    effect_note: Intimidation checks may use Charisma instead of their usual attribute.
tags:
- social
text: 'Effect: Whenever you make a Charisma-related skill check, you gain a temporary
  +2 bonus to Charisma (this does not affect your appearance). At the same time, the
  relevant attributes of your Intimidation test can be replaced by Charisma. Any of
  the above benefits will disappear for people who perceive your true face. If a target
  mistakenly thinks you have evil intentions, you do not gain these benefits against
  that target. Limits: (This is the effect brought by 1 potion and cannot be recorded
  or stolen.) [[potion effect recording/stealing]]'
```





- **Effect:**
  1. Whenever you make a **Charisma**-related skill check, you gain a temporary +2 bonus to **Charisma** (this does not affect your appearance).
  2. At the same time, the relevant attributes of your **Intimidation** test can be replaced by **Charisma**.
     - Any of the above benefits will disappear for people who perceive your true face.
     - If a target mistakenly thinks you have evil intentions, you do not gain these benefits against that target.
- **Limits:** (This is the effect brought by 1 potion and cannot be recorded or stolen.) [[potion effect recording/stealing]]

### Extraordinary Eloquence

```yaml ability
id: error-seq-08-extraordinary-eloquence
name: Extraordinary Eloquence
pathway: error
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.cha + @skill.persuade
opposed_by: willpower_defense
range: This affects all targets who hear the words.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.persuade
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Any social skill can be used for the opposed check; alternative skills are represented in scaling.
scaling:
- when: deception_based_delivery
  changes:
    check_roll: 1d20 + @attr.cha + @skill.deception
- when: fast_talk_delivery
  changes:
    check_roll: 1d20 + @attr.cha + @skill.fast_talk
- when: intimidation_delivery
  changes:
    check_roll: 1d20 + @attr.cha + @skill.intimidation
- when: performance_delivery
  changes:
    check_roll: 1d20 + @attr.cha + @skill.performance
conditions:
- fear
tags:
- ritual
- debuff
- defense
- social
text: 'Use: 1 Casting Action Casting Action Cost: 2 points of Spirituality [[Spirituality]]
  Check: Any social skill check against Willpower Defense Willpower Defense Targeting
  and range: This affects all targets who hear the words. Effect: Choose one of the
  following benefits to apply: You need to state a point of view in a form that matches
  the characteristics of your identification skills. [[identification skills]] Afterwards,
  the target who hears your speech will feel that your speech is very reasonable and
  calm down. You choose any one of the mental states of fear, anger, charm, temporary
  madness, etc., and immediately terminate it; this does not include shock, extraordinary
  madness, uncerta...'
```





- **Use:** 1 **Casting Action** Casting Action
- **Cost:** 2 points of **Spirituality** [[Spirituality]]
- **Check:** Any social skill check against **Willpower Defense** Willpower Defense
- **Targeting and range:** This affects all targets who hear the words.
- **Effect:** Choose one of the following benefits to apply:
  1. You need to state a point of view in a form that matches the characteristics of your identification skills. [[identification skills]]  
     Afterwards, the target who hears your speech will feel that your speech is very reasonable and calm down. You choose any one of the mental states of fear, anger, charm, temporary madness, etc., and immediately terminate it; this does not include shock, extraordinary madness, uncertain madness, etc.  
     [[mental states]]
  2. You express a point of view, and the target who hears the point of view must believe it, but every time they hold a clue that is contrary to your point of view, they can use **Detection** Detection to counter your social identification results to detect the clues, and vigilant and hostile targets are immune.
- **Special:**
  - For every 1 clue, you gain **+2** on **Scouting**. [[Scouting]]\r\n  - If the target knows very well about things related to the point of view, you must succeed on Scouting or the effect is invalid.

- **Limits:** As described in this section's prose.


### Misleading Thinking

```yaml ability
id: error-seq-08-misleading-thinking
name: Misleading Thinking
pathway: error
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 2
roll: 1d20 + @attr.cha + @skill.deception
opposed_by: willpower_defense
range: Choose 1 target.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.deception
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Deception check resolves the "cheats vs Willpower Defense" contest.
scaling: []
conditions:
- dead
tags:
- ritual
- defense
text: 'Use: 1 Casting Action Casting Action Cost: 2 points of Spirituality [[Spirituality]]
  Targeting and range: Choose 1 target. Check: Cheats against Willpower Defense Willpower
  Defense Effect: You need to express your point of view in words before using the
  ability, and then you equate two things with the same affix. Things that are equated
  with the same affixes cannot have contradictory affixes at the same time. For example,
  apples and pears are both fruits, so apples can be equal to pears, but water cannot
  be equal to fire, living things cannot be equal to dead things, nobles cannot be
  equal to vagrants or wanderers. Relying on the above content as a benchmark, whether
  the equal sign is est...'
```





- **Use:** 1 **Casting Action** Casting Action
- **Cost:** 2 points of **Spirituality** [[Spirituality]]
- **Targeting and range:** Choose 1 target.
- **Check:** Cheats against **Willpower Defense** Willpower Defense
- **Effect:**
  1. You need to express your point of view in words before using the ability, and then you equate two things with the same affix.
  2. Things that are equated with the same affixes cannot have contradictory affixes at the same time. For example, apples and pears are both fruits, so apples can be equal to pears, but water cannot be equal to fire, living things cannot be equal to dead things, nobles cannot be equal to vagrants or wanderers.
  3. Relying on the above content as a benchmark, whether the equal sign is established or not is determined by the **GM**. Once established, within 1 round, the target affected by you must believe it is true. After 1 round, if they find that the two things are not completely consistent, the effect will be cancelled.
- **Special:** This does not affect things that the target knows very well, and things that are important; some skills are treated as Proficient by default. For example, you can't tell a pharmacist who is proficient in pharmacy that cold medicine is equal to painkiller, unless the medicine is similar in curing certain diseases.

- **Limits:** As described in this section's prose.


### Mind Disturbance

```yaml ability
id: error-seq-08-mind-disturbance
name: Mind Disturbance
pathway: error
sequence: 8
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target.
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
- ritual
- detection
- social
text: 'Use: 1 Casting Action Casting Action Cost: 3 points of Spirituality [[Spirituality]]
  Targeting and range: Choose 1 target. Effect: You create 1 hallucination. You create
  an illusion with fully customized content. Only when the other party recognizes
  that it may be an illusion can they use Detection/Intuition (INT) against Deception
  [[Deception]] to detect that the illusion is false. Therefore, this only works once
  per target per day. Unlike the magician''s hallucination, the magician''s hallucination
  will make all the existences within 10 meters see the false image, but the trickster''s
  mind disturbance does not have this range limit. In contrast, the trickster''s hallucination
  can only make...'
```





- **Use:** 1 **Casting Action** Casting Action
- **Cost:** 3 points of **Spirituality** [[Spirituality]]
- **Targeting and range:** Choose 1 target.
- **Effect:** You create 1 hallucination.
  1. You create an illusion with fully customized content. Only when the other party recognizes that it may be an illusion can they use **Detection**/**Intuition (INT)** against **Deception** [[Deception]] to detect that the illusion is false. Therefore, this only works once per target per day.
  2. Unlike the magician's hallucination, the magician's hallucination will make all the existences within 10 meters see the false image, but the trickster's mind disturbance does not have this range limit. In contrast, the trickster's hallucination can only make one person see.
     [[magician's hallucination]]
- **Special:** By default, only the chosen target perceives this hallucination. If the illusion directly implicates others (GM call), they may contest false perception once alerted.

- **Limits:** As described in this section's prose.


### Quick Dodge

```yaml ability
id: error-seq-08-quick-dodge
name: Quick Dodge
pathway: error
sequence: 8
status: canonical
type: passive
action: none
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
  notes: Passive feature; no roll.
scaling: []
tags:
- debuff
- defense
- offense
text: 'Effect: When facing guns, you fully retain the agility and dodge in Physical
  Defense [[Physical Defense]], which does not include light and lightning. [[light
  and lightning]] When you face an attack that is slower than a gun, you can dodge
  more quickly, and you get an extra level of dodge. [[dodge levels]] Limits: (This
  is the effect brought by 1 potion and cannot be stolen or recorded.) [[potion effect
  recording/stealing]]'
```





- **Effect:**
  1. When facing guns, you fully retain the agility and dodge in **Physical Defense** [[Physical Defense]], which does not include light and lightning. [[light and lightning]]
  2. When you face an attack that is slower than a gun, you can dodge more quickly, and you get an extra level of dodge. [[dodge levels]]
- **Limits:** (This is the effect brought by 1 potion and cannot be stolen or recorded.) [[potion effect recording/stealing]]
