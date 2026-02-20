---
title: "Chapter 3: Attributes"
id: "chapter-3-attributes"
tags: ["core", "chapter-3"]
---

# Chapter 3: Attributes

## Attribute Generation

Attributes represent your fundamental physical, mental, and social capability.

Choose one method:

- **Roll:** For each Attribute, roll **2d3** to determine its value.
- **Point-Buy:** You have **32 points** to increase Attributes, but no Attribute may be lower than **2**.
Point-buy: start with **8,7,6,5,4,3** (assign to attributes) or use a GM-defined point-buy table.

## Attribute Rating Scale

Attribute values generally mean:

- **0:** You do not have this ability.
- **1:** Far below a normal person.
- **2:** Below average.
- **3:** Normal human level.
- **4:** Far above average.
- **5:** A very formidable person.
- **6:** The limit of humanity.

## Attribute List

Attributes are:

- Charisma (CHA)
- Strength (STR)
- Luck
- Agility (DEX)
- Constitution (CON)
- Willpower (WIL)
- Intuition (INT)
- Education

## Using Attributes in Checks

When you make the corresponding check, add the corresponding Attribute to your Skill check (see [[Chapter 2: Checks]] and [[Making a Check]]).

- **General form:** `1d20 + Skill + Attribute`

**Example:** When checking Fighting, if you have **4** points in Fighting and **5** points in Strength (STR), your check is:  
`1d20 + Fighting + Strength (STR)`

## Changing Attributes

Attributes generally do not change, except by consuming potions (see [[Potions and Advancement]]). Only in extremely rare and precious circumstances can they change to some extent.

## Derived Statistics

### Spirituality

Spirituality is a resource used for skill consumption.

- **Initial Spirituality:** `initial Willpower (WIL) + initial Intuition (INT)`
- **Sequence Spirituality Gain:** Each Sequence level provides Spirituality equal to your **final Intuition (INT)** value.

A commonly used calculation is:

- `(initial WIL + initial INT) + (number of Sequences you have advanced) x (your current/final INT)`

**Important calculation rule (as written):** later increases to Intuition use your **final Intuition value** for the Sequence-based portion of the calculation.

**Example:**
- Ordinary person: initial WIL **4** and initial INT **6** -> Initial Spirituality **10**.
- Become a Sequence 9 Beyonder; the potion gives **+1 INT**, so INT becomes **7** -> Spirituality is `(4 + 6) + (1 x 7)`.
- Become a Sequence 8 Beyonder; gain another **+1 INT**, so INT becomes **8** -> Spirituality is `(4 + 6) + (2 x 8)`.

Use the **current Sequence number** as the multiplier (e.g., Sequence 7 -> x7), consistent with the sheet instruction.

**Rank advancement multipliers (Spirituality maximum):**
- At **Sequence 4** and **Sequence 2** and subsequent Rank advancements, your Spirituality maximum is **multiplied by 2**.
- At the **Angel King** stage, you can only increase your existing Spirituality by **half**.
- Upon reaching an **Old One**, multiply by **3**.
- Upon reaching a **Pillar**, multiply by **4**.

At the **Angel King** stage, multiply current Spirituality maximum by **1.5**.

**Spirituality Digestion Increase:**
- For every **5** points of **Digestion %**, your Spirituality maximum **+1**.
- Repeated-Sequence potions do **not** count.

> **GM Note:** If you are using the auto character sheet from the [[Companion Supplemental Rules]], the auto sheet will handle Spirituality and Vitality. Remember to select your current Sequence number in the upper-left corner, or calculations will be affected (example given: Sequence 7 -> select "7"). [[Auto Character Sheet]]

### Sanity / Rationality

Sanity / Rationality is equal to:

- `Willpower (WIL) + 10`

This value is also the Sanity / Rationality maximum. You cannot restore Sanity / Rationality above this maximum (excluding Sanity / Rationality shields and additional Sanity / Rationality).

**Losing Sanity / Rationality:**
- When Sanity / Rationality may be lost, roll **1d20** to oppose the Investigator's **current** Sanity / Rationality.
- If the roll **exceeds** current Sanity / Rationality, they suffer the corresponding Sanity / Rationality damage.

If the roll exceeds current Sanity / Rationality, Sanity / Rationality loss equals the amount exceeded (minimum 1), unless a specific ability lists a different loss.

**Madness thresholds (on a single loss event):**
- Exceeds by **3** or more (including 3): may fall into **temporary madness**.
- Exceeds by **6** or more: fall into **indefinite madness**.
- Sanity / Rationality drops to **0**: fall into **permanent madness**.

### Vitality

Vitality is equal to:

- `Constitution (CON) + 10`

**Sequence advancement:** Each time you advance one Sequence, increase Vitality by an amount equal to your **current Constitution** at the time of advancement, unless otherwise specified by the Sequence (see [[The Beyonder System]]).

**Key distinction from Spirituality (as written):** A potion's increase to Constitution applies **once** when consuming the potion. It does **not** continue to affect prior Sequence contributions after you advance again.

**Practical calculation:**
- Start with `10 + initial CON`, then **add** your Constitution at each Sequence advancement (Sequence 9, then 8, then 7, etc.).

**Example:**
- Ordinary person with CON **4**: Vitality = `10 + 4 = 14`.
- Advance to Sequence 9; potion gives **+2 CON**, so current CON becomes **6** -> Sequence 9 Vitality = `14 + 6`.
- Advance to Sequence 8; potion gives **+1 CON**, so current CON becomes **7** -> Sequence 8 Vitality = `14 + 6 + 7`.

**Vitality Digestion Increase:**
- For every **5** points of **Digestion %**, your Vitality maximum **+1**.
- Repeated-Sequence potions do **not** count.

#### High-Sequence Vitality Calculation

**Demigod-stage multipliers (Vitality maximum):**
- Upon reaching **Sequence 4**, your current Vitality maximum is immediately **multiplied by 2**.  
  (That is, total Vitality accumulated from Sequence 9-4, multiplied by 2.)
- After becoming Sequence 4, at the **Sequence 2** stage, your total Vitality maximum can be **multiplied by 2 again**.
- After that, at **Sequence 0**, it can be **multiplied by 2 again**.
- At the **Angel King** stage, you only gain **half** of the Vitality maximum.
- After Sequence 0, you must reach an **Old One** to increase it again:
  - **Old One:** multiply by **3**
  - **Pillar:** multiply by **4**

At the **Angel King** stage, add **half** of your current Vitality maximum.

**Multipliers to Vitality gained on advancement (starting at Sequence 4):**
- Starting from **Sequence 4**, aside from Vitality doubling, the Vitality you gain each Sequence (equal to your current Constitution) also **doubles**.
- At **Sequence 2**, this changes to **multiply by 3**.
- At **Sequence 0**, **multiply by 4**.

These gain multipliers apply to all subsequent Sequence advancements after reaching that stage.

> **Lore:** Old Ones and Pillars are described as being able to cause galaxy-scale disasters; their Vitality is treated as reference and cannot be used to judge true Vitality.

### Death and Unconsciousness Checks

If your Vitality drops to **0**, you immediately fall **unconscious**.

- Each round, you must make a Constitution (CON) check with **Difficulty Value 10**.
- On a failure, you **die immediately**.

If your Vitality drops **below 0**:

- The amount of negative Vitality you can endure is determined by your Constitution.
- If damage reduces your Vitality below the negative value based on your Constitution, you die on the spot.
- As long as your remaining Vitality is not lower than **-your Constitution**, you are treated as unconscious and continue making checks.

If you take damage while unconscious:

- Make a Constitution (CON) check with **Difficulty Value 10 + (damage taken x 2)** to avoid death.

Stabilizing:

- You may use **one Medicine check** and **one Casting Action** to stabilize the injury; in that case, Constitution checks are no longer required.

## Combat and Action Statistics

### Movement

**Movement:** You may use one Movement action to move a distance equal to:

- `Strength (STR) + Agility (DEX)` meters

Your Movement value represents how many meters you can move in a single move.

### Defense Difficulty

Investigators and all creatures have three types of **Defense Difficulty**:

- **Physical Defense:** `10 + Agility (DEX) + Armor + Dodge + Skills`
- **Willpower Defense:** `10 + Willpower (WIL)`
- **Constitution Defense:** `10 + Constitution (CON)`

Some Beyonder Abilities may provide other bonuses (for example, "Deflection Defense," where an invisible force deflects an opponent's attack). Such bonuses specify the Defense type they affect.

When an action attempts to affect a creature, roll `1d20 + modifiers` against the relevant Defense Difficulty to determine whether the action succeeds (see [[Making a Check]]).

**Example:** If a player wants to use Intimidation against an enemy unit, they roll:  
`1d20 + Intimidation + Strength (STR)`  
to break the target's Willpower Defense.

### Attribute Damage Bonus

Your Attributes grant damage bonuses to certain skills.

**Example:** If a skill's damage is `2d6 + Strength (STR)` damage dice, use the following Strength (STR) damage bonus table:

| Strength (STR) | Damage Bonus |
|---:|:---|
| 0 | -2 |
| 1 | -1 |
| 2 | 0 |
| 3 | 1 |
| 4 | 1d2 |
| 5 | 1d4 |
| 6 | 1d6 |
| 7 | 1d8 |
| 8 | 1d10 |
| 9 | 1d12 |
| 10 | 2d6 |
| 11 | 2d8 |
| 12 | 2d10 |
| 13 | 2d12 |
| 14 | 3d8 |
| 15 | 3d10 |

**Note (as written):** The Strength (STR) bonuses above are treated as the Strength bonuses you can normally obtain through potions. The following are supernatural Strength bonuses; you must possess more powerful Strength to break this limit. Otherwise, you can only reach the damage capability of Strength 15 at most.

| Strength (STR) | Damage Bonus |
|---:|:---|
| 20 | 3d12 |
| 25 | 4d10 |
| 30 | 4d12 |

- If other Attributes have the same characteristic, apply this by analogy.
- Any Strength (STR) value above **30** is treated as **30** as the limit.

### Common Damage Dice and Vitality

Common Damage Dice and Vitality: These damage dice are converted based on how much harm they do to the human body.



## Carrying Items

Some Beyonder Abilities depend on the number of props/items you carry (examples given: a Magician Pathway's matches/paper figurines; a [[Hermit]]'s spellcasting materials). The number of items you carry is subject to quantity limits.

### Item Carry Slots

Determine how many items you can carry:

1. **Theoretical Item Carry Slots:** `Strength (STR) x 2`  
   This is the number of item carry slots you can support by raw strength alone, not counting clothing/backpacks/pockets.
2. **Actual Item Carry Slots:** Determine your number of pockets based on your clothing/backpack.  
   Even if you have sufficient strength, you still need pockets/backpacks with enough capacity to carry supplies normally.
   - **Example:** You have Strength (STR) **3**, so you have **6** theoretical item slots, but you only have **3** pockets. Even if you have 6 item slots, your clothing's pockets/backpack can only support carrying 3 slots' worth of items.
3. **Items Exceeding Carry Max:**  
   If your actual carry slots > theoretical carry slots, and your items are already filling your slots, then for each **1** slot of items exceeding your theoretical item slots:
   - Strength (STR) **-1** (ongoing)
   - Agility (DEX) **-1** (ongoing)  
   This affects Movement and Physical Defense.
4. **Handheld/Worn Items:**  
   Only count against theoretical item slots; they do not take up pocket count. As long as you do not exceed the max of your theoretical item slots, handheld/worn items are allowed as long as the carry position is reasonable.  
   (Examples given: sheaths; a gun holstered on your body; a sword strapped across your back.)

### Pocket Counts by Clothing

- **Impoverished Clothes:** 2 item slots and 2 pockets. (Lower slots are because the clothes are worn out and some pockets can no longer be used.)
- **Ordinary Clothes:** 4 item slots and 2-4 pockets.
- **Formalwear / Performance Tailcoat:** 8 item slots and 4-8 pockets; you may choose 2 hidden pockets.
- **Wizard Robe:** 12 item slots and 8-12 pockets, including 4 hidden pockets.

More clothing:
- Example given: a court long dress is formalwear, but its item slots may differ; decide by discussion with the GM.
- Skirts unique to women generally reduce item slots by 1 tier, even though they still count as formalwear, etc.

The exact pocket count of the above clothing is decided by the **Player** (it can be written on the character sheet). Pocket count does not affect your item slots, because a pocket may be large or small; it may only be useful in special situations.

### Hidden Pocket

**Hidden Pocket:** Items in hidden pockets are not considered valid selectable targets for checks such as Sleight of Hand, etc.

- However, the Error pathway can, by default, use excellent Investigation ability to select objects in your hidden pockets as valid selectable targets.

If you are unconscious and someone searches your body:

- They must proactively request an Investigation check at **Difficulty Value 15** to discover hidden pockets.
- Searching for hidden pockets is **1 Full-Round Action**.
- You do not need a check to search the hidden pockets of your own clothing.

### Backpacks That Provide Extra Item Slots

- **Crossbody Bag:** +2 item slots; may choose 1 hidden pocket. Retrieving an item is **1 Move Action**.
- **Backpack:** +4 item slots; may choose 2 hidden pockets. Retrieving an item is **1 Full-Round Action**.
- **Suitcase:** +6 item slots; may choose 3 hidden pockets. Retrieving an item is **1 Full-Round Action**.
- **Large Suitcase:** +8 item slots; may choose 4 hidden pockets. Retrieving an item is **1 Full-Round Action**.

If you fight while dragging a suitcase:

- Your Skill checks and Attribute checks take a **-2** penalty.

### Reputation Requirements for Different Clothing

- **Impoverished Clothes:** Reputation Untrained-Trained can wear.
- **Ordinary Clothes:** Reputation Trained-Proficient can wear.
- **Formalwear / Performance Tailcoat:** Reputation Proficient-Advanced can wear.
- **Wizard Robe:** Reputation Advanced-Expert can wear.

As written:
- If you are official/military, and you have an appropriate/reasonable/non-personal reason, you may request reimbursement for the clothing purchase to obtain the corresponding clothing when your Reputation does not meet the requirement; or if your profession is thief/criminal type.

### Self/Commissioned Upgrades to Increase Item Slots

If your Crafting skill reaches Proficient, or you commission a suitable person, you may modify the corresponding clothing to add pockets yourself:

- Crafting skill **Proficient:** Difficulty Value 15 Crafting check; add **+2** item slots to one clothing/backpack; may choose **1** hidden pocket
- Crafting skill **Advanced:** Difficulty Value 15 Crafting check; add **+3** item slots to one clothing/backpack; may choose **2** hidden pockets
- Crafting skill **Expert:** Difficulty Value 20 Crafting check; add **+4** item slots to one clothing/backpack; may choose **3** hidden pockets
- Crafting skill **Scholar:** Difficulty Value 25 Crafting check; add **+5** item slots to one clothing/backpack; may choose **4** hidden pockets
- Crafting skill **Master:** Difficulty Value 30 Crafting check; add **+6** item slots to one clothing/backpack; may choose **5** hidden pockets

The number of item slots added to each clothing/backpack cannot stack.

If you commission someone else, determine the tier of tailor/craftsman you can commission:

- Reputation **Untrained:** You almost have no money to commission extra tailoring/craft work; you can only try to find them within the party and commission them.
- Reputation **Trained:** You can commission a tailor/craftsman with Crafting skill **Proficient**
- Reputation **Proficient:** You can commission a tailor/craftsman with Crafting skill **Advanced**
- Reputation **Advanced:** You can commission a tailor/craftsman with Crafting skill **Expert**
- Reputation **Expert:** You can commission a tailor/craftsman with Crafting skill **Scholar/Master**

As written:
- The "craftsman" mentioned here does not mean a craftsman in the Beyonder sense; you must obtain GM approval to commission a Beyonder craftsman.

### Item Slots Occupied by Different Item Sizes

- **Tiny items** (paper figurines / a box of matches / a pen / a candle): **3** items occupy **1** item slot
- **Small items** (mini notebook / a weapon-shaped paper / a tarot deck / a talisman / a necklace): **2** items occupy **1** slot
- **Small-to-medium items** (a knife / a whip / a potion / a bottle of Holy Night Powder / a wallet / a revolver): **1** item occupies **1** slot

From the following sizes onward, items cannot be carried in pockets:

- **Medium items** (swords/knives as a category / rifle / a not-small bottle of liquor): can only be placed in a backpack/suitcase; **1** item occupies **2** slots.
- **Medium-to-large items** (steam rifle / backpack / longbow / sniper rifle): can only be placed in a suitcase; **1** item occupies **3** slots.
- **Large items** (giant weapon / a cannon shell / full plate armor): can only be placed in a large suitcase; **1** item occupies **4** slots.

More items are sized by the GM according to the above standards (some items may be placed by folding, etc.).
