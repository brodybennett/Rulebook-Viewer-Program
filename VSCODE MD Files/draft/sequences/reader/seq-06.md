---
title: 'Sequence 6: Polymath'
id: reader-seq-06
tags:
- pathway:reader
- sequence:6
---






# White Tower Pathway: Sequence 6

## Polymath

**Polymath** is the ability to recognize, observe, remember, and imitate what you have witnessed.

- Unlike the [[Recorder]], the [[Educational Scholar]] imitates by learning and analyzing the principles behind extraordinary abilities.
- There is no limit to how many times you can use this, but your imitation cannot reach the original ability’s full power.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +2.
- Your [[Potion Skills]] can be quickly upgraded to [[Erudition]].
- If you have reached the upper limit of Erudition, you can be upgraded to [[Master]].

### Analysis

```yaml ability
id: reader-seq-06-analysis
name: Analysis
pathway: reader
sequence: 6
status: canonical
type: active
action: free
cost: {}
roll: 1d20 + @attr.edu + @skill.knowledge
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.edu + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Extraordinary Knowledge Identification DV 20; +5 DV per sequence level above you. Apply -1 per Sanity/Rationality loss during analysis; if loss would drop you below 1, still resolve and gain +2 on the check.
scaling: []
tags:
- ritual
text: 'Cost: 2 Spirituality ([[Spirituality]]). Use: Free Action ([[Actions]]). Whenever
  you recognize the use of an extraordinary ability, you may immediately conduct a
  corresponding [[Extraordinary Knowledge Identification]]. Check: Initial Difficulty
  20. For each Sequence level this ability is higher than yours: Difficulty +5. Requirements:
  Some passives or abilities are difficult to recognize or observe, and may require
  the Beyonder to explain it to you. Aftereffects: When you lose Sanity / Rationality
  ([[Sanity / Rationality]]) while analyzing an ability: for every 1 Sanity / Rationality
  lost, apply -1 to the Analysis check. If the Sanity / Rationality loss would reduce
  you below 1, you sti...'
```





- **Cost:** 2 **Spirituality** ([[Spirituality]]).
- **Use:** **Free Action** ([[Actions]]). Whenever you recognize the use of an extraordinary ability, you may immediately conduct a corresponding [[Extraordinary Knowledge Identification]].
- **Check:** Initial Difficulty 20.
  - For each Sequence level this ability is higher than yours: Difficulty +5.
- **Requirements:** Some passives or abilities are difficult to recognize or observe, and may require the Beyonder to explain it to you.
- **Aftereffects:** When you lose **Sanity / Rationality** ([[Sanity / Rationality]]) while analyzing an ability: for every 1 Sanity / Rationality lost, apply **-1** to the Analysis check. If the Sanity / Rationality loss would reduce you below 1, you still complete the Analysis and gain **+2** on the Analysis result.
  - Sanity / Rationality loss from Analysis does not affect other abilities.
  > **Lore:** “Practice” is closer to experience than “theory.”
- **Effect (On Success):**
  - You reveal the specific effects of the extraordinary ability, including strengths and weaknesses.
  - Targets **2 or more Sequences higher** than you can only be partially analyzed and cannot be simulated, but they still enjoy the second benefit.
  - From the next time onwards, when you are hit by this extraordinary ability, you gain 4 points of **Deflection Defense** ([[Deflection Defense]]), **or** a +4 advantage in [[Countermeasures]], [[Awakening]], etc. checks.
  - This ability is included in the range of abilities that can be simulated by you, and you can write this ability into your [[Character Card]].
- **Special:** When creating a higher-sequence reader character card, it can be regarded as having as many extraordinary knowledge bonuses as there are corresponding resolved abilities.
  - Example: a certain path knowledge of +8 means that most abilities can be selected.
  - Generally, such benefits obtained when creating a character cannot exceed your own Sequence limit.

- **Effect:** Analysis resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.



### Simulation

```yaml ability
id: reader-seq-06-simulation
name: Simulation
pathway: reader
sequence: 6
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.edu + @skill.knowledge
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.edu + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: First simulation per ability requires DV 30 Extraordinary Knowledge appraisal; reduce DV by 5 per +5 Analysis margin. Each use also requires DV 20 knowledge appraisal; apply higher-sequence DV increases as with Analysis.
scaling: []
tags:
- ritual
- buff
text: 'Cost: 1 corresponding action consumes the corresponding spirituality. Use:
  Choose 1 ability that you have analyzed to simulate. Check (First Simulation per
  ability): The first simulation of a given ability requires a corresponding [[Extraordinary
  Knowledge Appraisal]] with Difficulty 30. Every time the Analysis appraisal is 5
  higher than the required difficulty, reduce the required Simulation difficulty by
  5. If the simulated ability is higher than the Sequence or character, the Difficulty
  increases as with Analysis. Effect: When using the simulated ability, no matter
  what the original ability is identified with, you can only change to the corresponding
  Knowledge identification.'
```





- **Cost:** 1 corresponding action consumes the corresponding spirituality.
- **Use:** Choose 1 ability that you have analyzed to simulate.
- **Check (First Simulation per ability):**
  - The first simulation of a given ability requires a corresponding [[Extraordinary Knowledge Appraisal]] with Difficulty 30.
  - Every time the Analysis appraisal is 5 higher than the required difficulty, reduce the required Simulation difficulty by 5.
  - If the simulated ability is higher than the Sequence or character, the Difficulty increases as with Analysis.
- **Effect:**
  - When using the simulated ability, no matter what the original ability is identified with, you can only change to the corresponding Knowledge identification.
  - After the first simulation is successful, this ability can be used permanently. If it fails, the simulation can be repeated until it succeeds.
  - There will inevitably be a gap between the simulated ability and the original version; the size of the gap depends on your Path Knowledge level.
- **Limits (Gaps from the original ability):**
  1. Swift/free-action abilities can only be cast with the action of casting or attacking. Casting/attacking/moving/full-round actions remain unchanged.
  2. Area abilities become single-target abilities. Single-target abilities change to require physical contact to take effect.
     - If you use the ability on yourself, you must remain in contact with yourself the entire time.
  3. Duration downgrades:
     - “Forever” → 24 hours
     - “Hours” → 5 minutes
     - “5 minutes” → 1 minute
     - “1 minute” → 3 rounds
     - “Rounds” → 1 round
     - “1 turn” → only takes effect for a moment
     - (Only affects abilities that explicitly mark duration; e.g., “paper double” is usually used instantly and is not affected.)
  4. Each time you use the simulated ability, you need a Difficulty 20 Knowledge appraisal.
     - Like Analysis, the Difficulty increases (as applicable).
     - If you fail, the action is not returned.
  5. Halving + doubling rules:
     - The effect is halved; damage is halved; number of uses is halved.
     - If you fall into a dream, you will wake up.
     - Identification requirements for inspiration are halved.
     - Negative effects remain the same and are rounded up; they will not be reduced to nothing.
     - Double the cost or Difficulty.
     - (Halving interaction: a substitute can offset only half once; it can be completely offset by consuming it twice in a row.)
- **Special (Passive abilities):** If the simulation is a passive ability, it requires 1 Casting Action to cast. To keep the passive ability lasting like the original version, you must pay 1 Casting Action continuously.
- **Path Knowledge thresholds (which gaps apply):**
  - Proficiency in Pathway knowledge and below: suffer all of 1–5.
  - Path knowledge advancement: suffer 2–5.
  - Path Knowledge Mastery: suffer 3–5, but do not suffer 4 for abilities not higher than your **Sequence** or **Personality**.
  - Path knowledge and erudition: suffer 4–5, but abilities not higher than your **Sequence** or **Personality** do not suffer 4.
  - Path to Master of Knowledge: suffer only 5.
  - If the simulated ability's Sequence is lower than yours or its Personality is lower than yours: no disadvantages, but Path Knowledge must be at least Erudition.

- **Special Simulation Situations:**
- **Note:** “Lose spellcasting actions” means you must spend **1 spellcasting action each round** to maintain the effect.
- **Note:** "Lose spellcasting actions" means you must spend 1 spellcasting action each round to maintain the effect.
  1. [[Secret Puppet]]: After successful [[Marionette]], you need to continue to lose spellcasting actions to manipulate it.
     - If you suffer from gap (4), the secret puppet will be very stuck during operation (like a weird puppet show / frame drop), and each action of the secret puppet during battle needs to be identified by gap (4).
  2. [[Herding]]: After successful grazing, you must continue to lose spellcasting actions to maintain it. Otherwise, due to extraordinary characteristics entering the body, immediately undergo a [[Promotion Appraisal]], and may become a Beyonder of the Jumping Pathway.
  3. [[Recording]]: After successfully recording, you must continue to lose spellcasting actions to maintain the record; otherwise, the recording ability will disappear.
  4. [[Faceless Man]]: Since the corresponding ability is a permanent physical change, there is no need to maintain it with ongoing action loss after completing the disguise.
  5. [[Stealing Ability]]: Under gap (5), the stealing ability is only half effective (rounded up), and the stolen person only has half the ability left (rounded down).
  6. [[Wronged Soul Transformation]]: Under gap (5), high-level invisible ones still exist, but if there are Beyonders in the same area who pass any Difficulty 20 inspiration, even if the purpose is not to find you, they can notice you through spirituality or using [[id:alias-spiritual-vision|Spiritual Vision]] at that moment.
  7. [[Arouse Undead Creatures]]: Undead creatures can continue to exist after being awakened, but to obey you when they are in front of you, you need to continue to lose the breath of magic to simulate death to suppress them.
     - They do not need to obey your orders when not in front of you.
     - Under gap (5), the value of the undead creature is halved (rounded up); it looks dull like a corpse; this does not affect use.
  8. [[Craftsman-made Extraordinary Items]]: If the identification fails during the first simulation and while suffering from gap (4), the characteristics are also considered incorporated.
     - The effects of produced extraordinary items are random; benefits are only 1d2; disadvantages remain the same.
  9. [[Accumulate Luck]]: Accumulated luck also needs continuous loss and casting to maintain.
  10. [[Malicious Perception]]: As a passive ability, it also needs continuous loss to maintain.
  11. [[Flesh Magic]]: As long as the flesh and blood stacked into the body is adjusted properly, it is regarded as part of the body and does not need to be maintained.
  12. [[Traveler's Gate]]: Quick flash can only guarantee complete physical defense; you will still lose agility and dodge in physical defense in the face of light, lightning, and area attacks.

> **GM Note:** More special simulations are decided by the **GM**. As long as an ability does not gain benefits permanently like grazing, secret puppet, and recording, or the benefit has nothing to do with extraordinary results (such as faceless man), then there is no need to continue to maintain it.
> **GM Note:** A common point of the above abilities is that most of them have certain permanent passive effects.

- **Limits:** As described in this section's prose.
