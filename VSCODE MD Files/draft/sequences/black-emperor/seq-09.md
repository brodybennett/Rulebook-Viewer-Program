---
title: 'Sequence 9: Lawyer'
id: black-emperor-seq-09
tags:
- pathway:black-emperor
- sequence:9
---






# Black Emperor Pathway: Sequence 9

## Lawyer

> **Lore:** Represents the shadow of order and the dark side of rules, corresponding to the Tarot card "Emperor". [[Tarot (Emperor)]]

- Good at discovering and exploiting loopholes in rules and opponents’ weaknesses; possesses excellent eloquence and speculative logic; adept at using the power of order.

Note: "Dark Emperor" and "Black Emperor" are treated as the same entity/alias.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** Intuition +2.
- **Skill Increase:** [[Persuasion]], [[Speech]], [[Intimidation]], [[Pleasing]], and other possible social skills increase by 1 level.

- **Skill Growth (Guidance):**
  - ① Whenever you receive at least 2 hours of real and effective guidance, your legal skills increase by 1 level. You can only learn this once a day.
  - From training to proficiency, to advanced, to mastery, you need to learn 2, 3, 4 times, up to mastery.
  -

- **Skill Growth (Exploiting Loopholes):**
  - ② Whenever you use loopholes in rules or logic to make an intelligent creature make a wrong decision, choose Law / Persuasion / Spoken Skills / Intimidation / Pleasant or other social skills to increase by 1 level.
  - Growth limit, efficiency, and number of times are the same as ①.
  - > **GM Note:** Examples include secretly changing concepts with words, avoiding the important and focusing on the minor, generalizing the whole, or putting the cart before the horse.

- When creating a character who has not just been promoted, the growth skill gains **2x Intuition (INT)** points from the potion. [[Potion]]
-

### Conversational and Eloquent

```yaml ability
id: black-emperor-seq-09-conversational-and-eloquent
name: Conversational and Eloquent
pathway: black-emperor
sequence: 9
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.cha + @skill.psychology
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: persistent
dice:
  check_roll: 1d20 + @attr.cha + @skill.psychology
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Mapped from explicit Psychology and Reconnaissance resistance-test wording; use Investigation if the table resolves Reconnaissance that way.
scaling:
- when: target_is_wary_or_hostile
  changes:
    effect_note: Beneficial misjudgment rider does not apply.
tags:
- defense
- social
text: 1 Whenever you make a [[Social Identification]], you gain a +2 Charisma [[Charisma]]
  bonus. This is Charisma and does not affect appearance. 2 Others will suffer a penalty
  of your Charisma value to your [[Psychology]] / [[Reconnaissance]] test, and your
  Charisma enjoys the bonus of 1. If the test fails, the judgment of you will be in
  a good direction instead of a bad one. Ineffective against wary, hostile targets.
  (This is a benefit from the potion and cannot be stolen or recorded. The Psychology/Reconnaissance
  test is triggered when a target resists distortion.)
```





> **Lore:** You are gracious and trustworthy.

- ① Whenever you make a [[Social Identification]], you gain a +2 **Charisma** [[Charisma]] bonus. This is Charisma and does not affect appearance.
- ② Others will suffer a penalty of your Charisma value to your [[Psychology]] / [[Reconnaissance]] test, and your Charisma enjoys the bonus of ①.
  - If the test fails, the judgment of you will be in a good direction instead of a bad one.
  - Ineffective against wary, hostile targets.
- (This is a benefit from the potion and cannot be stolen or recorded. The Psychology/Reconnaissance test is triggered when a target resists distortion.)
-

- **Effect:** Conversational and Eloquent resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Warp Channeling

```yaml ability
id: black-emperor-seq-09-warp-channeling
name: Warp Channeling
pathway: black-emperor
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
- detection
text: 'Use: Whenever you communicate with an intelligent creature for any 3 minutes,
  you can immediately choose 1 of the following benefits to take effect: 1 Swapping
  concept: You distort the behavior that the other party is about to execute into
  another behavior with similar meaning, such as: Retreating becomes fleeing. Fleeing
  becomes surrendering. Selling becomes selling at a low price. Buying becomes buying
  at a high price. Hiring becomes long-term hire. 2 Generalization: You distort the
  other partys perception of you into another similar meaning, such as:'
```





- **Use:** Whenever you communicate with an intelligent creature for any 3 minutes, you can immediately choose 1 of the following benefits to take effect:
  - ① **Swapping concept:** You distort the behavior that the other party is about to execute into another behavior with similar meaning, such as:
    - Retreating becomes fleeing.
    - Fleeing becomes surrendering.
    - Selling becomes selling at a low price.
    - Buying becomes buying at a high price.
    - Hiring becomes long-term hire.
  - ② **Generalization:** You distort the other party’s perception of you into another similar meaning, such as:
    - Timidity becomes cowardice.
    - Madness becomes ignorance.
    - Ignorance becomes innocence.
    - Suspicion becomes threat.
    - Threat becomes major threat.
  - ③ **Putting the cart before the horse:** You distort what the other party is doing into another meaning, such as:
    - Protecting family members becomes imprisonment.
    - Killing teammates becomes killing friends.
    - Charity becomes hypocrisy.
    - Vigilance for the sake of employers becomes just remembering vigilance and forgetting employers.
- **Special:** This is passive; even if you are in an unconscious state, this ability will take effect as long as there is language communication.

- **Communication content of distorted guidance:**
  - ① When using distortion-guided communication, in your communication with this intelligent creature, the communication content must be related to the distortion effect you expect to achieve.
  - ② For example, turning suspicion into a threat can mention their doubts, and selling at a low price can deliberately mention that the product does not meet the price.
  - ③ As long as the topic in your communication is relevant to it, and you put forward your conclusion at the end, then no matter how much your statement is wrong in details, the other party will subtly believe it.

- **Untwisted guide:**
  - Any intelligent creature that encounters distortion guidance must act according to the result of distortion guidance before receiving information or reminders that contradict existing cognition.
  - There are three ways to release distortion guidance:
    - ① **Self-detection:** Whenever you plan to do something that is not in line with your original intention, you can use an Intuition (INT) test (**Difficulty Value** Difficulty Value 25) to detect something is wrong.
      - For example, you plan to protect your family but start to prepare for imprisonment; arrest threats but plan to kill on the spot.
      - Special: If the distorted cognition has two similar meanings to your own original meaning, then the difficulty of perception is -5 per Sequence level the target is lower than you.
      -
    - ② **Obtaining information:** Once you get any information or reminder that reminds you of your original intention, you will immediately notice that something is wrong.
      - For example, you plan to go to [[Backlund]] but realize that you have already set foot on another land; or you are about to be captured alive but your teammates question why you pulled out a gun.
      - Special: Generally, for things that you don’t know at all (such as whether a person is innocent), once you believe they are innocent due to distortion guidance (because the subject of this matter is not yourself), then basically you cannot rely on self-detection; you can only obtain information.
    - ③ **Higher than 1 level:** Targets with Sequence higher than 1 can immediately conduct a [[Spiritual Intuition]] identification at the moment of being guided.
      - If the identification is successful, it will immediately detect something wrong.
      - Even if the identification fails, the difficulty of subsequent awareness will also be reduced by half, rounded up.
      -
  -

- **Explanation on some abilities of the Black Emperor:**
  - In most cases, especially related to “distortion”, the ability is to transform one meaning into another similar meaning, and the two meanings need to have the same affix:
    - ① **The same affixes:** For example, selling and selling at a low price are both selling; hiring and long-term employment are both hiring; madness and ignorance both have ignorance; ignorance and innocence both have no involvement in the core event; charity and hypocrisy both have goodness.
    - ② **Similar meanings:** The two meanings do not span too much and both belong to similar meanings.
      - Attached sales can be converted into low-priced sales, but high-priced sales cannot be converted into low-priced sales.
      - Employment can be converted into long-term employment, but employment itself cannot be converted into permanent employment.
      - But selling at a high price can turn into a normal sale, and then a normal sale can turn into a low-price sale.
      - Employment can become a long-term employment, and a long-term employment can become a permanent employment.
  - “Distortion” can be cast if the above conditions are met, and whether it meets the above criteria is decided by the GM.
  - The difference between this and the wrong path is that the wrong path has the same affixes but does not have contradictory affixes, while the Black Emperor needs to have similar meanings while having the same affixes as the Error pathway.
  - Regarding spans which have two closely related meanings:
    - Specifically refers to the special situation that is self-perceived during distortion guidance, such as: the original intention is to sell normally, but it is distorted to sell at a low price, and on the basis of selling at a low price, it becomes free again, which is considered to be too far from the original intention.
    - However, if it is distorted to sell at a low price, then distorted to be free, and then changed from free to sell at a low price, it will only be regarded as distorting the similar meaning of level 1, and it will not be affected by the self-perception special difficulty reduction effect if it is calculated based on the original intention.

- **Effect:** Warp Channeling resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spotting Loopholes

```yaml ability
id: black-emperor-seq-09-spotting-loopholes
name: Spotting Loopholes
pathway: black-emperor
sequence: 9
status: adapted
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.law
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.law
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Mapped from explicit Legal Appraisal against listed Difficulty Value tiers.
scaling:
- when: difficulty_value_15
  changes:
    effect_note: Discover contradictions and immediate loophole opportunities.
- when: difficulty_value_20
  changes:
    effect_note: Identify exploitable jurisdiction or process weaknesses.
- when: difficulty_value_25
  changes:
    effect_note: Identify core weakness or overattachment; other loophole forms can also resolve at this tier.
- when: difficulty_value_30
  changes:
    effect_note: Understand the target's core purpose and ideal outcome.
tags:
- ritual
text: 'Use: 1 Spellcasting Action, without consuming Spirituality [[Spirituality]].
  Choose 1 target, conduct 1 [[Legal Appraisal]], and determine the result based on
  the appraisal. Results (by Difficulty Value): Difficulty Value 15: You have discovered
  the contradictions in the other party''s words, the ambiguity of your own requirements,
  and found an opportunity to take advantage of. Difficulty Value 20: You find out
  whether a thing or a place is easy to be taken advantage of in terms of jurisdiction,
  such as: the hotel does not count the names of the residents (easy to disguise identities,
  confuse the public), the ticket inspection is not rigorous, whether the character
  or work of others is sla...'
```





- **Use:** 1 Spellcasting Action, without consuming **Spirituality** [[Spirituality]]. Choose 1 target, conduct 1 [[Legal Appraisal]], and determine the result based on the appraisal.
- **Results (by Difficulty Value):**
  - Difficulty Value 15: You have discovered the contradictions in the other party's words, the ambiguity of your own requirements, and found an opportunity to take advantage of.
  - Difficulty Value 20: You find out whether a thing or a place is easy to be taken advantage of in terms of jurisdiction, such as: the hotel does not count the names of the residents (easy to disguise identities, confuse the public), the ticket inspection is not rigorous, whether the character or work of others is slack and not serious.
  - Difficulty Value 25: You find out whether the other party cares too much about something, which represents their core purpose or weakness.
  - Difficulty Value 30: You basically understand their purpose and the ideal result that the other party wants to achieve.
  - Other loopholes (Difficulty Value 25): the specific form of conflict between the two, the reasons for negligence, etc.
- **Great success:** On the basis of the original success level, you know more detailed information, such as the specific reasons for the contradiction.
- **Big failure:** You still get the information corresponding to the success level, but the other party also understands part of your intention.
- **Special:** Detecting Vulnerabilities can also be used for certain extraordinary factors, such as discovering whether the opponent is afraid of sacredness, flames, whether the opponent's ability has certain restrictions, etc.
- (This is a benefit from the potion and cannot be stolen or recorded. The Psychology/Reconnaissance test is triggered when a target resists distortion.)

- **Effect:** Spotting Loopholes resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Vision
```yaml ability
id: black-emperor-seq-09-vision
name: Vision
pathway: black-emperor
sequence: 9
status: adapted
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Vision is a toggle with per-round upkeep; mapped check roll represents Spiritual Intuition checks while vision is active.
scaling: []
tags:
- ritual
- detection
text: 'Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect:
  You activate vision, and your vision gains the following benefits: When in the state
  of spiritual vision, your Spiritual Intuition test +1 is beneficial. Your vision
  gains the following benefits: 1 Etheric body: You can roughly tell whether the other
  partys body is good or bad through the color of the aura, but you cant get detailed
  information. 2 Spiritual body: You can confirm whether an object/creature has Spirituality,
  which cannot identify extraordinary people. 3 Mental body: You can see whether the
  other party is thinking, but only so, and you cannot get more detailed information.'
```





- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate vision, and your vision gains the following benefits:


- When in the state of spiritual vision, your Spiritual Intuition test +1 is beneficial.
- Your vision gains the following benefits:
  - ① **Etheric body:** You can roughly tell whether the other party’s body is good or bad through the color of the aura, but you can’t get detailed information.
  - ② **Spiritual body:** You can confirm whether an object/creature has Spirituality, which cannot identify extraordinary people.
  - ③ **Mental body:** You can see whether the other party is thinking, but only so, and you cannot get more detailed information.
  - ④ **Astral body:** You cannot see the astral body.
- Notes:
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding Pathway.
  - The colors seen by the spirit vision allow you to see each other in the dark, but you can only see the existence of colors, and it is still possible to get lost in the dark, because the colors you can see are limited, so you cannot use them to distinguish the undead biology.
- Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
