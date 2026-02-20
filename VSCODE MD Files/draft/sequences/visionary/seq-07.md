---
title: 'Sequence 7: Psychiatrist'
id: visionary-seq-07
tags:
- pathway:visionary
- sequence:7
---





# Visionary Pathway: Sequence 7

## Psychiatrist

> **Lore:** Known as a “psychoanalyst” in ancient times. Their physical fitness is strengthened, and they can directly affect targets.

- **Ability List:** Shock and Awe (Dragon Power), Frenzy, Mental Suggestion, Soothe (Comfort), Mind Reading
- **Main Materials:** Mirror Dragon Eyes (pair), Elder Tree Fruit

**Skill Growth:** Use the same growth rules as Sequence 9 for psychology-related skills (2 hours of effective training = +1 level, once per day, up to **Proficiency**).

## Advancement

### Auxiliary Materials

- **Auxiliary Materials:** Mirror Dragon Eyes ×2, Elder Tree Fruit ×1

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +1, Strength +1, Constitution +1, Agility (DEX) +1
- Psychology / Psychological Guidance can quickly learn to **Erudition** (a rank above **Master**). Skill Ranks

### Passive Traits

```yaml ability
id: visionary-seq-07-passive-traits
name: Passive Traits
pathway: visionary
sequence: 7
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
- detection
- buff
text: 'Enhanced Smell: You can distinguish subtler smells to better grasp real thoughts.
  In Mind-Reader State, your passive bonus increases to +6. Darkvision: You can clearly
  see items hidden in the dark. Careful Speech: You cannot accidentally reveal something.
  Every word you say has been carefully considered. If a similar situation occurs,
  the GM can remind you and allow you to withdraw the corresponding contentunless
  you do so on purpose. Special: This is not absolute. If some means bypass your mental
  activities (such as hypnosis), you can still be forced to reveal information.'
```




- **Enhanced Smell:** You can distinguish subtler smells to better grasp real thoughts. In **Mind-Reader State**, your passive bonus increases to +6.
- **Darkvision:** You can clearly see items hidden in the dark.
- **Careful Speech:** You cannot accidentally reveal something. Every word you say has been carefully considered. If a similar situation occurs, the **GM** can remind you and allow you to withdraw the corresponding content—unless you do so on purpose.
  - **Special:** This is not absolute. If some means bypass your mental activities (such as hypnosis), you can still be forced to reveal information.

- **Effect:** Passive Traits resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Shock and Awe (Dragon Power)

```yaml ability
id: visionary-seq-07-shock-and-awe-dragon-power
name: Shock and Awe (Dragon Power)
pathway: visionary
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target, or an area within 10 meters.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- debuff
text: 'Also known as group chaos. You make enemies panic as if facing a dragon. Cost:
  3 points of Spirituality Use: 1 Casting Action Targeting and range: Choose 1 target,
  or an area within 10 meters. Effect: The effect succeeds by default. When you use
  this ability, your pupils lighten, become light-gold, and (if they become vertical)
  the following effects last for 1 round: Ordinary people with Willpower 23: gain
  Fear and Awe; immediately run wildly to get away from the source of fear. Ordinary
  people with Willpower 4: gain Fear and Awe; immediately flee to get away from the
  source of fear.'
```




Also known as “group chaos.” You make enemies panic as if facing a dragon.

- **Cost:** 3 points of **Spirituality**
- **Use:** 1 **Casting Action**
- **Targeting and range:** Choose 1 target, or an area within 10 meters.
- **Effect:** The effect succeeds by default.
  - When you use this ability, your pupils lighten, become light-gold, and (if they become vertical) the following effects last for 1 round:
    1. **Ordinary people** with **Willpower** 2–3: gain **Fear** and **Awe**; immediately run wildly to get away from the source of fear.
    2. **Ordinary people** with Willpower 4: gain **Fear** and **Awe**; immediately flee to get away from the source of fear.
       > **GM Note:** “Above-average” targets in the Willpower 2–4 category may be frightened into incontinence.
    3. **Ordinary people** with Willpower 6, or **Beyonders** with increased Intuition (INT) or Willpower: gain **Fear** and **Awe**; they may resist the forced movement from Fear. If the resistance succeeds, they can only spin in place and cannot move. See [[Special Status]].
    4. **Beyonders** of Sequence 7, or Willpower 6+: gain **Shock** and **Fear**; resistance to forced movement is successful by default. They stand still trembling and spinning in place, but still cannot truly perform a moving action.
- **Limits / Special:**
  - When affecting more than 1 character, Will defense against the targets can only be effective with a [[Psychology Check]].
- **Repeated Use (Dragon Might):** If Dragon Might is used continuously, the effect is downgraded:
  - Result ① becomes ②
  - Result ② becomes ③
  - Result ④ “only lasts for 3 rounds, and then 1 round”
  - The level dropped equals the number of consecutive uses.
  - **Clarification:** On the first consecutive use that would apply result ④, the duration is 3 rounds; on subsequent consecutive uses, it lasts only 1 round.

- **Limits:** As described in this section's prose.


### Frenzy

```yaml ability
id: visionary-seq-07-frenzy
name: Frenzy
pathway: visionary
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target within your field of vision.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
text: 'Detonates the targets emotional or mental state, causing them to fall into
  frenzy. Cost: 3 points of Spirituality Use: 1 Casting Action Targeting and range:
  Choose 1 target within your field of vision. Effect: The target must be in at least
  one madness symptom or emotional state (excluding Stunned and indeterminate madness
  itself). The target suffers 1 Sanity / Rationality loss per emotional state and
  1d3 Sanity / Rationality loss per madness symptom; the detonated emotional state
  is immediately cleared. Manifestation (non-mechanical): When you cast it, your pupils
  lighten, become light-gold, and may become vertical.'
```




Detonates the target’s emotional or mental state, causing them to fall into “frenzy.”

- **Cost:** 3 points of **Spirituality**
- **Use:** 1 **Casting Action**
- **Targeting and range:** Choose 1 target within your field of vision.
- **Effect:**
  - The target must be in at least one madness symptom or emotional state (excluding **Stunned** and “indeterminate madness itself”).
  - The target suffers **1 Sanity / Rationality** loss per emotional state and **1d3 Sanity / Rationality** loss per madness symptom; the detonated emotional state is immediately cleared.
- **Manifestation (non-mechanical):** When you cast it, your pupils lighten, become light-gold, and may become vertical.

- **Limits:** As described in this section's prose.


### Mental Suggestion

```yaml ability
id: visionary-seq-07-mental-suggestion
name: Mental Suggestion
pathway: visionary
sequence: 7
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
text: 'You suggest the target through specific actions, language, and media. Cost:
  1 point of Spirituality per use Use: 1 Casting Action Method (choose one): Action:
  1 Free Action. Your eyes reflect a light-golden color; you can plant psychological
  hints on witnesses. You may also use candles, a finger, and similar actions to draw
  focus to a specific object. Language: Speak a discourse containing the psychological
  hint; you must specify a target (or choose your own discourse). Effect: To apply
  a suggestion, you must tell the GM the plain text of the hint content. The suggestion
  may achieve the following effects (as approved by the GM): Keep in good condition:
  Set a time period or trigger conditi...'
```




You suggest the target through specific actions, language, and media.

- **Cost:** 1 point of **Spirituality** per use
- **Use:** 1 Casting Action
- **Method (choose one):**
  - **Action:** 1 **Free Action**. Your eyes reflect a light-golden color; you can plant psychological hints on witnesses. You may also use candles, a finger, and similar actions to draw focus to a specific object.
  - **Language:** Speak a discourse containing the psychological hint; you must specify a target (or choose your own discourse).
- **Effect:** To apply a suggestion, you must tell the **GM** the plain text of the hint content. The suggestion may achieve the following effects (as approved by the GM):
  1. **Keep in good condition:** Set a time period or trigger condition. When met, for 5 minutes the target gains a +2 beneficial bonus to skill and attribute appraisals, and a beneficial -2 to Sanity / Rationality loss.
  2. **Stay awake:** Set a time period or trigger condition. When the target enters a dream, they realize they are in a dream.
  3. **Answer questions:** Set a time period or trigger condition. For 5 minutes, the target strongly wants to answer questions and may lie.
  4. **Follow the promise:** This can be your hint, or it can directly affect a promise made by the target. Breaking the promise requires a Will Test. The **Difficulty Value** is your “Intuition (INT) + Charisma + Psychological Guidance bonus.”
     - If the target attempts to break the promise and fails the Will Test, they cannot attempt that same break again for 3 hours.
  5. **Complete a certain action:** Set a time period or trigger condition, and select a certain identification in that period. This identification gains a +1 beneficial bonus, and this mental suggestion can be stacked.
  6. **Contain emotions:** Set a time period or trigger condition; use “Intuition (INT) + Charisma + Psychological Guidance” as the Difficulty Value.
     - **Actively generated emotions:** Each time a related emotion appears, use Intuition (INT) to identify against the Difficulty Value; if the identification fails, it is not generated.
     - **Emotions caused by the outside world:** The emotion’s source uses the corresponding ability identification—or an Intuition (INT) identification—against this Difficulty Value.
  7. **Perform a certain behavior:** This can be long-term or short-term. The effect is equivalent to “Follow the promise,” such as going to a certain church at a certain time every day.
  8. Other more allowable and reasonable psychological hints set by the GM; refer to the above effects.
- **Special suggestive situations:**
  1. **Target is not voluntary:** Use 1 Psychological Guidance to resist the Willpower Defense to succeed, and gain bonuses/penalties equivalent to [[Thinking Simulation]].
     - Use the same modifiers as **Thinking Simulation** (start at -8 disadvantage and apply Psychological Guidance understanding modifiers). [[id:alias-thinking-simulation|Thinking Simulation]]
  2. **Suggestion involves life / the most important thing:** The mental suggestion is immediately dismissed by default and has no effect.
  3. **Suggestion in combat/chaos area:** The suggestion fails by default and cannot be executed successfully.
  4. **Suggestion not triggered:** A suggestion lasts for a maximum of 1 month.
  5. **Multiple hints:** A creature can receive at most a number of hints equal to (their Intuition (INT) attribute value ÷ 2) at the same time.
  6. **Content aligns with the target’s willingness:** If it is reasonable enough, gentle enough, and is something the target would have done, the GM can let the Player follow cues by letting the Player see only relevant information.
  7. **Implied content limit:** The implied content must be concise and not complicated; the reference standard should not exceed 20 characters.

- **Limits:** As described in this section's prose.


### Soothe (Comfort)

```yaml ability
id: visionary-seq-07-soothe-comfort
name: Soothe (Comfort)
pathway: visionary
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target within 10 meters.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- control
text: 'Helps Beyonders on the verge of losing control regain sanity and escape danger.
  Cost: 2 points of Spirituality Use: 1 Casting Action Targeting and range: Choose
  1 target within 10 meters. Effect (choose/apply as appropriate): Clear a creatures
  emotional/crazy symptoms. The target gains 1 point of temporary Sanity / Rationality
  for 1 hour; it cannot be stacked. It reappears later. Whenever there is a Beyonder
  beside you whose Sanity / Rationality returns to 0, as long as you still have the
  action of casting spells, you are allowed to try to soothe them. Let a Beyonder
  about to lose control regain sanity:'
```




Helps Beyonders on the verge of losing control regain sanity and escape danger.

- **Cost:** 2 points of **Spirituality**
- **Use:** 1 **Casting Action**
- **Targeting and range:** Choose 1 target within 10 meters.
- **Effect (choose/apply as appropriate):**
  1. Clear a creature’s emotional/crazy symptoms. The target gains 1 point of temporary Sanity / Rationality for 1 hour; it cannot be stacked. It reappears later.
     > **GM Note:** Soothe can only temporarily suppress mental illness. A real solution requires [[id:alias-psychological-guidance|Psychological Guidance]]; use guidance to gradually adjust the target’s mentality/viewpoint so things develop in a better direction. The GM decides whether the disease is truly cured.
  2. Whenever there is a Beyonder beside you whose Sanity / Rationality returns to 0, as long as you still have the action of casting spells, you are allowed to try to soothe them.
- **Let a Beyonder about to lose control regain sanity:**
  - Make 1 Mental Guidance appraisal. Initial Difficulty Value is 40; for each sequence level you have, the Difficulty Value is -5.
    - **Clarification:** Reduce Difficulty Value by 5 for each Sequence level above 9 you have (Sequence 8 = -5, Sequence 7 = -10, etc.).
  - Each time the target is larger than you by 1 character, the identification Difficulty Value is +15. If greater than 2 characters, “big success” is ignored.
    - **Clarification:** Add +15 Difficulty Value for each Sequence the target is higher than you. If the target is 2+ Sequences higher, **Big Success** is ignored.
  - There is only one chance. If the identification fails, the target is completely out of control.

- **Effect:** Soothe (Comfort) resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Mind Reading

```yaml ability
id: visionary-seq-07-mind-reading
name: Mind Reading
pathway: visionary
sequence: 7
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- utility
text: 'You place the target in a semi-hypnotic state through candlelight, pure dew,
  and other media, and communicate directly with their mental body. Setup / Use: Prepare
  the environment with media such as candles/hydrosols. 1 Free Action: tint your pupils
  gold. Choose a target who is looking at the candle (or smelling the pure dew) in
  front of you and is looking at you. The target usually must be voluntary; they enter
  a trance. Trance State: A target in Trance State answers all your questions truthfully
  and cannot lie. This has no effect on a target who can [[Stay Awake in Dream]].'
```




You place the target in a semi-hypnotic state through candlelight, pure dew, and other media, and communicate directly with their mental body.

- **Setup / Use:**
  - Prepare the environment with media such as candles/hydrosols.
  - 1 **Free Action**: tint your pupils gold.
  - Choose a target who is looking at the candle (or smelling the pure dew) in front of you and is looking at you. The target usually must be voluntary; they enter a trance.
- **Trance State:**
  - A target in **Trance State** answers all your questions truthfully and cannot lie.
  - This has no effect on a target who can [[Stay Awake in Dream]].
  - If a question is vague and too broad, then if it is answered, it means the other party has the willingness to inform.
    - **Clarification:** Vague questions yield only a general intent or summary, not detailed specifics.

- **Effect:** Mind Reading resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
