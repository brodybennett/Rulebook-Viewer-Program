---
title: 'Sequence 9: Arbiter'
id: arbiter-seq-09
tags:
- pathway:arbiter
- sequence:9
---






# Justiciar Pathway: Sequence 9

## Arbiter

> **Lore:** Represents order and rules, corresponding to the Tarot card “Judgment.”  
> **Lore:** Possesses convincing charisma and sufficient authority, as well as excellent fighting ability to deal with the unexpected.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +1.
- Your [[Fighting (Skill)]] skills rise by 1 level.

### Reputation Growth

```yaml ability
id: arbiter-seq-09-reputation-growth
name: Reputation Growth
pathway: arbiter
sequence: 9
status: canonical
type: passive
action: none
cost: {}
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
- buff
text: 'Whenever you arbitrate a non-repetitive, challenging dispute and uphold justice,
  your Reputation [[Reputation]] skill goes up by 1 level. Such increased Reputation:
  Will not provide you with assets. Will only increase your personal authority. Can
  (at most) quickly increase to mastery. Skill Ranks Limit: This improvement is limited
  to 1 time per day, so as to leave enough time for your reputation to start spreading.
  From training a proficient a advanced, you need to preside over justice 2 and 3
  times respectively; advancement caps at Advanced. Creating a character that isn''t
  just promoted can boost growth skills with double the potion''s Intuition (INT).
  [[Potion]]'
```





- Whenever you arbitrate a non-repetitive, challenging dispute and uphold justice, your **Reputation** [[Reputation]] skill goes up by 1 level.
- Such increased Reputation:
  - Will not provide you with assets.
  - Will only increase your personal authority.
  - Can (at most) quickly increase to mastery. Skill Ranks
- **Limit:** This improvement is limited to 1 time per day, so as to leave enough time for your reputation to start spreading.
- From training -> proficient -> advanced, you need to preside over justice **2** and **3** times respectively; advancement caps at **Advanced**.
- Creating a character that isn't just promoted can boost growth skills with **double the potion's Intuition (INT)**. [[Potion]]

- **Effect:** Reputation Growth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Arbitrating Authority

```yaml ability
id: arbiter-seq-09-arbitrating-authority
name: Arbitrating Authority
pathway: arbiter
sequence: 9
status: adapted
type: active
action: cast
cost: {}
roll: 1d20 + @attr.cha + @skill.reputation
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.reputation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted from explicit Reputation-based social replacement and conflict-stop contest against Willpower Defense.
scaling:
- when: target_is_preconfirmed_hostile
  changes:
    effect_note: Stop command does not apply.
tags:
- defense
- social
text: 'Effect: Your Reputation and Charisma-related identification is favorable +2.
  This does not affect your assets and appearance, but your personality charm. [[Charisma]]
  When performing any [[Social skill appraisal]] , you can replace the corresponding
  skill with a Reputation appraisal, replace social interaction with your charm and
  authority, and communicate based on your personality charm and authority to make
  people convincing. In the event of conflict, you can shout Stop!, and your Reputation
  will fight against all Willpower Defense defenses to stop the conflict. Limits:
  The effect does not include the target that has been determined to be hostile. [[Hostile
  (status)]] It can temporarily...'
```





- **Effect:**
  1. Your Reputation and **Charisma**-related identification is favorable +2. This does not affect your assets and appearance, but your personality charm. [[Charisma]]
  2. When performing any [[Social skill appraisal]] , you can replace the corresponding skill with a Reputation appraisal, replace social interaction with your charm and authority, and communicate based on your personality charm and authority to make people convincing.
  3. In the event of conflict, you can shout “Stop!”, and your Reputation will fight against all Willpower Defense defenses to stop the conflict.
- **Limits:**
  - The effect does not include the target that has been determined to be hostile. [[Hostile (status)]]
  - It can temporarily calm the creatures affected by emotions and stop the creatures whose desires are detonated. [[Desire detonation]]
  - Desire explosions are not included, and the emotional state will not be cleared. [[Desire explosion]]
  - This ability cannot be stolen or recorded. [[Stolen/Recorded abilities]]

### Fighting Skills

```yaml ability
id: arbiter-seq-09-fighting-skills
name: Fighting Skills
pathway: arbiter
sequence: 9
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.str + @skill.fighting
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.str + @skill.fighting
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Adapted as a persistent combat package; damage_roll is the extra fighting damage rider applied to normal attacks.
scaling:
- when: sequence_7_or_5_upgrade
  changes:
    effect_note: Extra evasion increases by 1 level at each listed upgrade.
tags:
- detection
- buff
- offense
- defense
text: 'Effect: Your Fighting (including subdivision) increases the damage by 1d6,
  and the damage type is the same as the original damage. In addition to [[Credit]]
  , your Fighting (including subdivision) skills can also be quickly improved. The
  limit and number of upgrades are the same as your Reputation, but the condition
  for improvement is changed to accept at least 2 hours of real, non-repeated effective
  guidance, and the maximum reaches proficient. Proficient It is beneficial +2 to
  [[Special action appraisals]] such as critical strike / two combo / close shooting,
  excluding first aid / surprise attack, and does not affect special actions that
  simply gain benefits. For example, gaining moment...'
```





- **Effect:**
  1. Your Fighting (including subdivision) increases the damage by 1d6, and the damage type is the same as the original damage.
  2. In addition to [[Credit]] , your Fighting (including subdivision) skills can also be quickly improved. The limit and number of upgrades are the same as your Reputation, but the condition for improvement is changed to accept at least 2 hours of real, non-repeated effective guidance, and the maximum reaches proficient. Proficient
  3. It is beneficial +2 to [[Special action appraisals]] such as critical strike / two combo / close shooting, excluding first aid / surprise attack, and does not affect special actions that simply gain benefits. For example, gaining momentum and aiming will not change from +2 to +4. Only affects identification.
  4. You gain [[id:alias-fast-dodge|Fast dodge]] , retain full physical defense against [[Firearms]] (excluding light/lightning), and gain 1 extra level of dodge. Dodge
- **Scaling:**
  - Sequence 7 and [[Sequence 5]]: Your extra evasion increases by 1 level. [[Evasion]]
- **Limits:**
  - This is the effect brought by the potion and cannot be stolen or recorded.

### Verdict

```yaml ability
id: arbiter-seq-09-verdict
name: Verdict
pathway: arbiter
sequence: 9
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.cha + @skill.reputation
opposed_by: willpower_defense
range: Choose 1 target who has committed a crime within the [[Field of Vision]].
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.reputation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted from explicit Reputation versus Will contest to enforce crime-related ruling content.
scaling:
- when: target_sequence_higher_than_you
  changes:
    check_penalty_per_sequence: -2
- when: ruling_executed_by_target
  changes:
    effect_note: Corresponding mysticism crime label is cleared and cannot be re-judged for the same offense on that target.
tags:
- ritual
- detection
- control
- social
text: 'Cost: 1 Casting Action Casting Action; consume 3 spirituality points [[Spirituality]].
  Targeting and range: Choose 1 target who has committed a crime within the [[Field
  of Vision]]. Use: Say the keyword judgment, then say the content of your judgment
  (for example, My verdict is, leave it!). Use the Reputation test to counter its
  Will Test. Effect: If the test is successful, the opponent must fulfill the content.
  The content of the ruling specified by you should be closely related to the crime
  committed (for example, you cannot make the target kill itself for stealing).'
```





- **Cost:** 1 **Casting Action** Casting Action; consume 3 **spirituality points** [[Spirituality]].
- **Targeting and range:** Choose 1 target who has committed a crime within the [[Field of Vision]].
- **Use:**
  - Say the keyword “judgment,” then say the content of your judgment (for example, “My verdict is, leave it!”).
  - Use the Reputation test to counter its Will Test.
- **Effect:**
  1. If the test is successful, the opponent must fulfill the content.
  2. The content of the ruling specified by you should be closely related to the crime committed (for example, you cannot make the target kill itself for stealing).
  3. As long as your verdict is executed by the target, the target’s corresponding crime will be cleared in [[Mysticism]]. It can be understood that a criminal is labeled as a crime. After the corresponding crime is cleared, you can no longer judge the same crime on that target.
- **Modifiers:**
  - For each 1 Sequence the target is higher than you: -2 disadvantage to the Reputation check of the Judgment ability.
  - 

- Generally speaking, the rulings you can enforce are as follows:

#### Misdemeanor offenses

(harassment, abuse, stealing/taking things of no value to the original owner, etc.; offenses against public morals are also crimes)

1. **“Leave!”**: The target must perform a **movement action** Movement Action immediately, and the direction of all movement actions within 1 round must be away from this place.
2. **“Return it!”**: If the target takes something that does not belong to it and is related to the convicted crime, it is required to return it immediately.
3. **“Apologize!”**: If the target committed a fault and it is related to the crime for which it was convicted, it is immediately forced to apologize.

#### Moderate crimes

(robbery of things important to the original owner, indecent, intentionally wounding, vandalism, burglary, etc.)

1. **“Surrender!”**: The target must confess its crime and criminal intent, and be arrested by you voluntarily; this lasts for 1 round.
2. **“Confession!”**: Similar to but not the same as self-surrender; it does not necessarily admit the crime, but it will expose the criminal process and accomplices.
3. **“Repent!”**: Has the two effects of “Return it!” and “Apologize!” at the same time; regret emerges in the heart; lasts for 1 round.

#### Serious crimes

(attempted/completed murder, intentionally causing serious injury, attempted/completed forced sex, endangering public safety, etc.)

1. **“Follow the law!”**: The target cannot perform movement actions for 1 round, nor can it endanger the enforcer/victim.
2. **“Atonement!”**: You designate one or more things owned by the target to be handed over, at most equivalent to the damage it caused. If the damage caused it cannot afford, or it is something that cannot really be recovered, the target needs to self-mutilate/suicide within 1 round.

- Enforceable awards for more serious crimes include content in less serious crimes, and the Arbitrator can expand further awards at their discretion.

> **GM Note:** The severity of crimes is determined by the GM, and theft, fraud, etc. can be judged according to the value involved.

- **Limits:** As described in this section's prose.


### Vision

```yaml ability
id: arbiter-seq-09-vision
name: Vision
pathway: arbiter
sequence: 9
status: adapted
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted check mapping for interpretation tasks while Vision is active; activation itself is a free toggle with upkeep.
scaling:
- when: vision_active
  changes:
    check_bonus: 1
    effect_note: Spiritual Intuition tests gain +1 while Vision is active.
- when: target_is_ordinary_spirit_body_under_24h
  changes:
    effect_note: Recently deceased ordinary spirit bodies are visible by default.
tags:
- ritual
- detection
- divination
- utility
text: 'Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect:
  You activate vision, and your vision gains the following benefits: Etheric body:
  You can roughly tell whether the other partys body is good or bad through the color
  of the aura, but you cant get detailed information. Spiritual body: You can confirm
  whether an object/creature has spirituality, which cannot identify extraordinary
  people. Mental body: You can see whether the other party is thinking, but only so,
  and you cannot get more detailed information. Astral body: You cannot see the astral
  body. When in the state of spiritual vision, your [[Spiritual Intuition Test]] is
  beneficial +1.'
```





> **Lore:** You gain vision, but it is not as effective for you as your own Intuition (INT).
- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate vision, and your vision gains the following benefits:


  1. **Etheric body:** You can roughly tell whether the other party’s body is good or bad through the color of the aura, but you can’t get detailed information.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality, which cannot identify extraordinary people.
  3. **Mental body:** You can see whether the other party is thinking, but only so, and you cannot get more detailed information.
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your [[Spiritual Intuition Test]] is beneficial +1.
- **Notes:**
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding path. Pathway
  - The colors seen by the spirit vision allow you to see each other in the dark, but you can only see the existence of colors, and it is still possible to get lost in the dark, because the colors you can see are limited; you cannot use them to distinguish the undead biology.
  - Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours.
- **Limits:**
  - Spirit Vision cannot be recorded or stolen.
