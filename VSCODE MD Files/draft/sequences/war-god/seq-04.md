---
title: 'Sequence 4: Demon Hunter'
id: war-god-seq-04
tags:
- pathway:war-god
- sequence:4
---






# Twilight Giant Pathway: Sequence 4

## Demon Hunter

- Sensitive to traces of evil, depravity, and pollution.
- Can cover up one’s own actions and intentions, making targets that can foresee danger unable to detect you.
- A nemesis of demons; skilled at discovering the weaknesses of different monsters.
- Skilled at identifying the uses of various materials and, in a unique meditation mode, formulating and producing miraculous potions, holy ointments, essential oils, and special marks—then restraining the target by taking, smearing, or using these items.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Unilaterally kills an evil, depraved, powerful creature that is heavily tainted, and resolves the root cause of the event so related events do not occur again. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength +2, agility +1, constitution +2, will +2.

### Detect Evil

```yaml ability
id: war-god-seq-04-detect-evil
name: Detect Evil
pathway: war-god
sequence: 4
status: canonical
type: active
action: free
cost: {}
roll: 1d20 + @attr.int + @skill.investigation
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.investigation
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: "Difficulty Value 15 Intuition + Spot check; apply Avoidance of Scrying penalty if present. Use Investigation for the roll token."
scaling: []
tags:
- detection
text: 'Use: Free Action Check: Difficulty Value 15 Intuition + [[Spot]] check. Effect:
  Look for signs of evil, corruption, and contamination; detect evil creatures currently
  within the scene or that have been in the area within the last 24 hours. Limits/Modifiers:
  If a target has the [[Avoidance of Scrying]] trait, apply its penalty to this check.'
```





- **Use:** **Free Action**
- **Check:** **Difficulty Value 15** Intuition + [[Spot]] check.
- **Effect:** Look for signs of evil, corruption, and contamination; detect evil creatures currently within the scene or that have been in the area within the last 24 hours.
- **Limits/Modifiers:** If a target has the [[Avoidance of Scrying]] trait, apply its penalty to this check.

- **Limits:** As described in this section's prose.


### Demon Hunt Ritual

```yaml ability
id: war-god-seq-04-demon-hunt-ritual
name: Demon Hunt Ritual
pathway: war-god
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 4
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
  notes: "No roll; attack identifications of 18/19/20 count as big success after the ritual."
scaling: []
tags:
- ritual
- offense
text: 'Use: Perform a ritual where you hunt demons. Time: 10 minutes. Cost: 4 [[Spirituality]].
  Requirements: Find the traces of demons and understand the types of demons. Effect:
  After the ceremony takes effect, your attack Identification checks of 18, 19, or
  20 are considered a [[Big Success]].'
```





- **Use:** Perform a ritual where you hunt demons.
- **Time:** 10 minutes.
- **Cost:** 4 [[Spirituality]].
- **Requirements:** Find the traces of demons and understand the types of demons.
- **Effect:** After the ceremony takes effect, your attack Identification checks of 18, 19, or 20 are considered a [[Big Success]].

- **Limits:** As described in this section's prose.


### Mind Barrier

```yaml ability
id: war-god-seq-04-mind-barrier
name: Mind Barrier
pathway: war-god
sequence: 4
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
- stealth
text: 'Effect: Conceal your intentions. You can surprise creatures that would not
  otherwise be surprised. A demons danger perception no longer applies to you.'
```





- **Effect:** Conceal your intentions.
  - You can surprise creatures that would not otherwise be surprised.
  - A demon’s danger perception no longer applies to you.

- **Limits:** As described in this section's prose.


### Spiritual Disturbance

```yaml ability
id: war-god-seq-04-spiritual-disturbance
name: Spiritual Disturbance
pathway: war-god
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: "Target makes an Intuition check at -5; on failure treat as Big Failure."
scaling: []
tags:
- ritual
text: 'Effect: The target makes an Intuition check at -5; on failure, treat the result
  as a Big Failure.'
```





- **Effect:** The target makes an Intuition check at -5; on failure, treat the result as a Big Failure.

- **Limits:** As described in this section's prose.


### Material Identification

```yaml ability
id: war-god-seq-04-material-identification
name: Material Identification
pathway: war-god
sequence: 4
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: 1d20
  notes: "Craft time is 1d20 minutes; healing potion restores 2d6 health, purification potion deals 3d6 to wraiths and grants 1d3 sanity armor; marks add listed bonus dice."
scaling: []
tags:
- detection
text: 'Effect: Identify the uses of various materials and prepare corresponding magical
  potions, holy ointments, essential oils, and special marks. Time: 1d20 minutes.
  Check: Difficulty Value 20 Intuition check. Limits: Create up to five magical items
  per day. Storage/Duration: Unless otherwise specified, magical potions can only
  be stored or effective for 24 hours. Heres a list of the magical items you can craft:
  Holy Anointing Use: Full Round to apply.'
```





- **Effect:** Identify the uses of various materials and prepare corresponding magical potions, holy ointments, essential oils, and special marks.
- **Time:** 1d20 minutes.
- **Check:** **Difficulty Value 20** Intuition check.
- **Limits:** Create up to five magical items per day.
- **Storage/Duration:** Unless otherwise specified, magical potions can only be stored or effective for 24 hours.

Here’s a list of the magical items you can craft:

- **Holy Anointing**
  - **Use:** **Full Round** to apply.
  - **Effect:** The applier gains 5 **cold resistance** and 5 **curse resistance** for 24 hours.
  - **Limits:** Can only take effect twice.
  - **Additional Effect:** If the curse/cold/poison’s Difficulty Value is within 5 points of your Intuition score, you may choose to suppress or cure it.

- **Essential Oil**
  - **Use:** 1 **Round**.
  - **Effect:** The diffused aroma repels dark, corrupted, and undead creatures below **Sequence 7**; on a failed resistance, they must leave the area and cannot enter while the aroma persists.
  - **Additional Uses:** Refreshes the mind so users can continue to act for a period of time when they are tired.
  - **Additional Uses:** Can be dripped on teammates to distinguish friend from foe through the unique aroma.

- **Choking Potion**
  - **Use:** An action other than a **Free Action**.
  - **Aftereffects:** After taking it, you will not be able to breathe air, but you can breathe freely underwater.

- **Mark of Purification**
  - **Use:** An action other than a **Free Action**; attaches to a weapon or object.
  - **Effect:** The next 3 attacks are converted to **holy damage**.
  - **Bonus Damage:** +2d6 against corrupted and dark creatures; +3d6 against undead.

- **Mark of Lightning**
  - **Use:** An action other than a **Free Action**; attaches to a weapon or object.
  - **Effect:** Deals an extra 1d10 **lightning damage** for the next 2 hits.
  - **Bonus Damage:** An extra 3d6 damage to undead.

- **Frozen Mark**
  - **Use:** An action other than a **Free Action**; attaches to a weapon or object.
  - **Effect:** The subsequent three attacks cause **cold damage**.
  - **Aftereffects:** Muscles tremble and frost condenses; the target’s next skill check is at -4 disadvantage.

- **Mark of the Curse**
  - **Use:** An action other than a **Free Action**; attaches to a weapon or item.
  - **Effect:** The damage of the next three attacks is converted into **curse damage**.
  - **Additional Effect:** When applying the mark, specify a category or set of targets that the curse damage will not affect; all other targets are affected normally.

- **Healing Potion**
  - **Effect:** Restores 2d6 health.

- **Purification Potion**
  - **Effect:** Immediately heals all poisons and minor diseases, as well as curses.
  - **Effect:** Causes 3d6 damage to the [[Wraiths]] in the body.
  - **Effect:** Provides 1d3 [[Sanity / Rationality Armor]] (this does not stack with other Sanity / Rationality Armor sources; it can stack only for targets with the Visionary).

> **GM Note:** Other special item effects require approval by the GM.

> **GM Note:** Under special circumstances, you can refer to the [[Potions Professor]] list of medicines for making new medicines. However, the Twilight Giant pathway is not a Sequence Pathway suitable for research, so the development of new medicines should be greatly restricted.

- **Imprint Form Variation:** You can craft a resistance imprint instead of a mark; it grants 10 points of resistance to the corresponding damage/condition type (holy, lightning, cold, or curse). This cannot be superimposed.

### God of War

```yaml ability
id: war-god-seq-04-god-of-war
name: God of War
pathway: war-god
sequence: 4
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
conditions:
- fear
tags:
- healing
- debuff
- defense
text: 'Trigger: Whenever you fall into [[Madness]]. Effect: Temporarily consume 3
  points of Will Cap to continue fighting in a normal state. Limits: This does not
  affect your Willpower Defense. Failure Condition: If your [[Sanity / Rationality]]
  reaches a negative value, you immediately lose the will to fight and cannot continue
  fighting. Recovery: The lost Will Cap can be restored after an hour. Status Interaction:
  You no longer suffer negative effects from blindness, deafness, fear, anger, etc.,
  including negative emotions bestowed by the [[Black Emperor]], and will not suffer
  impairmentsalthough these negative states still exist (e.g., you are still theoretically
  blind or deaf), you can still...'
```





- **Trigger:** Whenever you fall into [[Madness]].
- **Effect:** Temporarily consume 3 points of **Will Cap** to continue fighting in a normal state.
- **Limits:** This does not affect your **Willpower Defense**.
- **Failure Condition:** If your [[Sanity / Rationality]] reaches a negative value, you immediately lose the will to fight and cannot continue fighting.
- **Recovery:** The lost Will Cap can be restored after an hour.
- **Status Interaction:** You no longer suffer negative effects from blindness, deafness, fear, anger, etc., including negative emotions bestowed by the [[Black Emperor]], and will not suffer impairments—although these negative states still exist (e.g., you are still theoretically blind or deaf), you can still act normally through rich combat experience.
- **Limits:** This does not affect [[Dreaming]]; you will be awakened as usual if you are dreamed.
- **Special:** If the enemy that triggers these effects is of a higher Sequence than you, or is an Visionary Extraordinary of the same Sequence, you only suffer the enemy’s related Identification penalty; you do not lose actions or become unable to act.

- **Sequence 3 Update:** The lost upper limit of will is restored after half an hour.
