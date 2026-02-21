---
title: 'Sequence 8: Barbarian'
id: abyss-seq-08
tags:
- pathway:abyss
- sequence:8
---






# Abyss Pathway: Sequence 8

## Barbarian

> **Lore:** Known as “Cold-Blooded One” in ancient times, this Beyonder has lost their conscience and grown more inhuman, gaining demonic, magic-like abilities.

- See also: Abyss

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Agility (DEX) +1, Constitution +2, Intuition (INT) +1.
- Your **Mysticism** is added to the **Quick Learning** category of Sequence 9, which can be improved to **Proficiency**.
- The **Sequence 9 potion** skill can be upgraded to **Advanced**.
  - [[Quick Learning]]
  - Sequence 9

### Inhuman Body

```yaml ability
id: abyss-seq-08-inhuman-body
name: Inhuman Body
pathway: abyss
sequence: 8
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.con
opposed_by: difficulty_value
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.con
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted endurance token for edge-case recovery adjudication; core recovery cadence is deterministic and defined by sequence scaling.
scaling:
- when: sequence_8_base
  changes:
    effect_note: Natural health recovery interval is 10 hours (rounded up).
- when: sequence_7
  changes:
    effect_note: Natural health recovery interval becomes 8 hours.
- when: sequence_6
  changes:
    effect_note: Natural health recovery interval becomes 6 hours.
- when: each_higher_promotion
  changes:
    effect_note: Required recovery time is halved, rounded down.
tags:
- ritual
- healing
text: 'Effect: You recover health much faster than others. Natural recovery time:
  The time required for your body to naturally restore life is only 10 hours, rounded
  up. See [[Recovery of Spirituality and Other States]] for details. Sequence scaling:
  Sequence 7: Changed to every 8 hours. Sequence 6: Changed to every 6 hours. Every
  time one level is promoted: the required time is cut in half and rounded down.'
```





- **Effect:** You recover health much faster than others.
- **Natural recovery time:** The time required for your body to naturally restore life is only **10 hours**, **rounded up**. See [[Recovery of Spirituality and Other States]] for details.
- **Sequence scaling:**
  - **Sequence 7:** Changed to every **8 hours**.
  - **Sequence 6:** Changed to every **6 hours**.
  - Every time one level is promoted: the required time is cut in half and **rounded down**.

- **Limits:** As described in this section's prose.


### Dehumanization

```yaml ability
id: abyss-seq-08-dehumanization
name: Dehumanization
pathway: abyss
sequence: 8
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
conditions:
- fear
tags:
- debuff
- social
text: 'Effect: From the moment you are promoted, you are no longer human. You still
  have feelings, but it is difficult to empathize; you will act only for your own
  desires, closer to pure egoism. Only in extreme cases is it close to emotional divinity.
  Play guidance: When playing, pay attention to the annihilation of humanity. Condition
  impact (halved): The effects of Charisma (CHA), Anger, and Fear on you are halved.
  You still have pure bloodthirsty and killing desires; this is not inconsistent with
  the halving of the anger state. Forced/restrictive effects: If these conditions
  have any special effect on you, such as forcing or restricting your actions, you
  can ignore such incidents. Special: T...'
```





- **Effect:** From the moment you are promoted, you are no longer human. You still have feelings, but it is difficult to empathize; you will act only for your own desires, closer to pure egoism. Only in extreme cases is it close to emotional divinity.
- **Play guidance:** When playing, pay attention to the annihilation of humanity.
- **Condition impact (halved):** The effects of **Charisma (CHA)**, **Anger**, and **Fear** on you are **halved**.
  - You still have pure bloodthirsty and killing desires; this is not inconsistent with the halving of the anger state.
- **Forced/restrictive effects:** If these conditions have any special effect on you, such as forcing or restricting your actions, you can ignore such incidents.
- **Special:** Targets one level higher than you have the full effect on you normally.
- *(This is a potion benefit that cannot be recorded or stolen.)*
  - [[Charisma (CHA)]]
  - [[anger]]
  - [[Fear]]

- **Limits:** As described in this section's prose.


### Broken Wings

```yaml ability
id: abyss-seq-08-broken-wings
name: Broken Wings
pathway: abyss
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int
opposed_by: willpower_defense
range: Designate 1 target **within sight**.
target: designated target(s)
duration: 'Lasting until the end of the target''s next action, they gain all of the
  following effects:'
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted directly from the stated Intuition-versus-Willpower Defense test.
scaling:
- when: sequence_4_or_higher_branch
  changes:
    effect_note: One check can apply to multiple targets.
- when: target_is_one_sequence_lower_in_sequence_4_branch
  changes:
    effect_note: Movement and agility can be reduced to zero (dodge remains unaffected).
tags:
- ritual
- mobility
- debuff
- defense
text: 'Cost: 3 Spirituality. Use: 1 Casting Action. Test: Intuition (INT) vs. Willpower
  Defense. Targeting and range: Designate 1 target within sight. Effect: You raise
  your arms horizontally and press down your palms suddenly; the targets body becomes
  heavy and their movement slows, as if the wings used to fly have been broken off.
  Duration: Lasting until the end of the targets next action, they gain all of the
  following effects: Their movement power is halved. Their Agility (DEX) is halved,
  rounded up.'
```





- **Cost:** 3 Spirituality.
- **Use:** 1 Casting Action.
- **Test:** Intuition (INT) vs. Willpower Defense.
- **Targeting and range:** Designate 1 target **within sight**.
- **Effect:** You raise your arms horizontally and press down your palms suddenly; the target’s body becomes heavy and their movement slows, as if the wings used to fly have been broken off.
- **Duration:** Lasting until the end of the target’s next action, they gain all of the following effects:
  - Their movement power is **halved**.
  - Their Agility (DEX) is **halved**, **rounded up**.
  - Their Dodge is **normal** (unchanged), which will affect the value of Physical Defense.
  - They take a **-2 penalty** on skill or ability checks against the Physical Defenses of others.
- **Sequence scaling:**
  - **Sequence 4:** Broken Wings can affect multiple targets at once. One Intuition (INT) Test is against the Willpower Defense of all targets.
    - If the target is one character lower than you, you can make them lose all mobility and agility, but it still does not affect Dodge.

- **Limits:** As described in this section's prose.


### Demonic Spells

```yaml ability
id: abyss-seq-08-demonic-spells
name: Demonic Spells
pathway: abyss
sequence: 8
status: canonical
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: Choose 1 target.
target: designated target(s)
duration: 1 encounter.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- utility
text: 'Effect: You gain more demonic spell-like abilities. Number gained: Divide your
  ontologys current Intuition (INT) by 2 to determine the number of demon-like spells
  you can gain. Additional gains: Potion Completely Digested: Choose another demon-like
  spell to get it. Every time a Sequence or position is promoted: choose 1 more demon-like
  spell to get. When you upgrade the position, you can get 2 more. [[Potion Completely
  Digested]] [[Position]]'
```





- **Effect:** You gain more demonic spell-like abilities.
- **Number gained:** Divide your ontology’s current Intuition (INT) by **2** to determine the number of demon-like spells you can gain.
- **Additional gains:**
  - **Potion Completely Digested:** Choose another demon-like spell to get it.
  - Every time a **Sequence** or **position** is promoted: choose **1** more demon-like spell to get.
  - When you upgrade the **position**, you can get **2** more.
  - [[Potion Completely Digested]]
  - [[Position]]
- Choose the corresponding quantity from the following demonic spells:

- **Bad Words Hurt People**
  - **Cost:** 1 Spirituality.
  - **Use:** 1 Swift Action; **1 time per round**.
  - **Test:** Intuition (INT) vs. Willpower Defense.
  - **Targeting and range:** Choose 1 target.
  - **Effect:** Before casting, you need to RP out insults, bad words, and curses on the target, causing **1d4 curse damage**.
  - **Sequence scaling:**
    - **Sequence 7:** When it is a big success, swearing and hurting people causes a deterrent effect lasting **1 round**, and the damage caused is **doubled**.
- **Limits:** This restriction is **per target** and does not share a pool with other abilities.

- **Create Poison Flame**
  - **Cost:** 2 Spirituality.
  - **Use:** 1 Casting Action.
  - **Test:** Occult vs. Physical Defense.
  - **Targeting and range:** Choose 1 target.
  - **Effect:** A red-green flame rises from your palm; you spew out this flame, causing **2d6 poison** and **1d6 fire** damage.
  - **Special:**
    - This ability doubles the damage to plants, spider webs, and silk hair.
    - A target who successfully loses hit points from poison damage begins to suffer **1 point of poison damage each round** until they clear the poison with a **15th Difficulty Value Medicine** check.
  - **Sequence scaling:**
    - **Sequence 7:** The poisonous fire can ascend into a poisonous gas wrapped in green fire; multiple targets can be selected within **10 meters**.

- **Magma Attachment**
  - **Cost:** 2 Spirituality.
  - **Use:** 1 Casting Action.
  - **Duration:** 1 encounter.
  - **Effect:** Your skin splits into web-like lines and hidden magma appears in the gaps; the fissures begin to shimmer, but it’s not enough to illuminate.
    - You gain **Fire Resistance 5** and **Cold Resistance 5**.
    - Your unarmed melee attacks deal **+1d6 fire damage**.
  - **Sequence scaling:**
    - **Sequence 7:** It can be changed to attach **1d6 fire damage** to a melee weapon, and the damage can be added to the rest of the fire-type abilities to increase the heat of other fire-type abilities.

- **Danger Premonition**
  - **Trigger:** When you are about to encounter a surprise attack or sneak attack.
  - **Use:** Immediately use Intuition (INT) to conduct a **Difficulty Value 25** spiritual intuition appraisal.
  - **Effect (on success):** The opponent cannot gain the advantages brought by the surprise round and surprise attack, and the spiritual intuition will be triggered steadily at this time.
  - **Sequence scaling:**
    - **Sequence 7:** Changed to **Difficulty Value 20** Intuition (INT) identification, and you can tell whether the enemy is a fallen person or a fallen creature.
  - [[Surprise Round]]
  - [[Spiritual Intuition]]

- **Create Fireballs**
  - **Cost:** 1 Spirituality.
  - **Use:** 1 Casting Action.
  - **Test:** Occult vs. Physical Defenses.
  - **Targeting and range:** Choose 1 target.
  - **Effect:** Deal **3d6 fire damage**.
  - **Sequence scaling:**
    - **Sequence 7:** The fireball acquires the properties of brimstone, appears slightly light blue, and creates a small explosion, increases poison damage by **1d6**, and can select two targets standing together.
  - [[Brimstone]]

- **Customized Demon-Like Spell**
  - If you are not satisfied with the above-mentioned demon-like spells, you can get **only one** custom-made demon-like spell that is unique to you.
  - This requires the consent of the **GM** and must be reasonable.
  - It occupies the spell slot.
  - [[Spell Slot]]

> **GM Note:** Explanation about demon-like spells (Abyss Pathway)
>
> - In the Abyss Pathway, different races end up with different images of demons (e.g., goat demons, Cthulhu-like monsters, tentacles, or terrifying creatures like Shan Hai Jing).
> - Human blood is impure; people may be mixed with blood from other regions. The concept of “race” applies beyond humans and animals.
> - You can design a meaningful unique ability based on your character background (for customized demon-like spells).
> - All demon-like spells listed above are lower-level versions of Sequence 6 abilities; custom abilities will also have a more complete body mutation when reaching a higher Sequence. You can design an upgraded version in advance based on this idea.
>
> [[Shan Hai Jing]]
