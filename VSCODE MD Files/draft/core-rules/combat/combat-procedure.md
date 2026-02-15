---
title: "Combat Procedure"
id: "combat-procedure"
tags: ["core", "chapter-6"]
---

# Combat Procedure

A single combat round is approximately **6 seconds**.

## Surprise Round

1. If one side ambushes the other **and is not discovered**, the ambushing side gains **1 Surprise Round**. Otherwise, skip this step and start at Regular Combat Round.
2. During the Surprise Round, each character on the ambushing side may take **one** of the following: **1 Attack/Cast/Move Action** or **2 Swift Actions**. The ambushed side **cannot take any actions**.
3. If, during the Surprise Round, the ambushing side is not exposed within the target's line of sight **or** its presence is not noticed, the ambushed side suffers the [[LINK LATER: Caught Off Guard | type=condition | hint=surprise penalty]] effect during the Surprise Round.
4. The ambushing side has **Advantage** and the ambushed side has **Disadvantage** only during the Surprise Round. After the actions in Step 2 resolve, the Surprise Round ends. Ongoing sources of Advantage/Disadvantage (such as surrounding/flanking or invisibility) may still apply after the Surprise Round ends. See [[LINK LATER: Advantage / Disadvantage | type=mechanic | hint=roll modifiers]].

## Regular Combat Round

### Initiative

- Each participant rolls initiative using the command: `.ri+Agility (DEX)`.
- The GM enters `.init` (last) to view the combat order.
- You may alternatively sort directly by all creatures' **Agility (DEX)**.
- Clear initiative values with: `.init clr`.

[[UNCLEAR: The text uses "1d20 + Agility (DEX)" once; this appears to mean the same initiative roll as ".ri+Agility (DEX)", but the dice notation is inconsistent.]]

### Actions Per Round

| Action Type | Count |
|---|---:|
| Attack/Cast Action | 1 |
| Swift Action | 3 |
| Move Action | 1 |
| Free Action | Unlimited |

### Action Types

**Attack/Cast Action:** Choose **either** a physical attack (e.g., Fighting, shooting) **or** a Beyonder Ability (a "Cast"). You cannot attack once and cast once in the same round using this allotment.

**Swift Action:** A very fast action (e.g., cycling a bolt-action rifle, snapping your fingers, quickly drawing a small item).

**Free Action:** An action that takes almost no time and can be performed alongside other actions (e.g., speaking). Free actions are unlimited within a round. Beyonder Abilities that require spending Spirituality, or infusing Spirituality, are usually **not** Free actions. Substitute or switching Grazed Souls are exceptions. **Special:** Canceling the use of certain Beyonder Abilities typically costs **1 Free Action**.

**Move Action:** Movement (and certain quick object/limb movements). In one Move Action, you can move up to a distance equal to your movement distance. You cannot "move again" simply because you did not use the full distance.

### Timing and Priority

- Relative speed (fastest to slowest): **Free Actions > Swift Actions > Attack/Cast Actions = Move Actions**.
- **Free Actions** can be used during other people's turns, but **cannot interrupt** other people's actions.
- **Swift Actions** can be used during other people's turns, but **cannot interrupt** other people's actions unless an ability explicitly says it can.
- When using a Swift-action Beyonder Ability during another person's turn, that other person's action resolves its check first, then the Swift action takes effect. They take effect **simultaneously** for outcome timing purposes.

### Full-Round Action

A **Full-Round Action** consumes **1 Attack/Cast Action, 3 Swift Actions, 1 Move Action, and unlimited Free Actions**.

- Once you use a Full-Round Action, you cannot do anything else that round.
- A Full-Round Action does **not** complete immediately. It continues until the **start of your turn in the second round**, and only then is it considered complete.

### Action Conversion

- You may convert **1 Attack/Cast Action -> 2 Swift Actions**.
- You cannot convert Move Actions.
- You cannot convert **2 Swift Actions -> 1 Attack/Cast Action**.
- You may only convert downward; you cannot merge upward.
- No action can be saved into the next round.

### Extra Actions

Some Beyonder Abilities or Beyonder items may grant extra Swift/Attack/Cast/Move Actions. When the number of extra actions reaches a certain magnitude, its benefits are reduced:

1. The upper limit of this magnitude is **1**, regardless of action type.
2. If extra actions provided reach **2** (e.g., 2 extra Cast Actions), the **2nd** Cast Action is **invalid** and cannot be used.
3. **Invalid** actions can be merged into **valid** actions. Example: If you gain **3** extra Cast Actions, the 2nd and 3rd (invalid) Cast Actions can be merged into **1** valid Cast Action, for a total of **2** usable Cast Actions.
4. The **3rd** valid action requires merging **3** invalid actions; the **4th** valid action requires merging **4** invalid actions; and so on.

> **GM Note:** This limit counts only extra actions gained through **external forces** (e.g., Beyonder items, ritual magic). Extra actions from your own Beyonder Abilities or Mythical form are **not** counted for this purpose.

## Opposed Checks When Attacking Others

There is no active Dodge skill check in combat. Dodge is integrated into **Physical Defense**.

### Physical Defense

**Physical Defense = 10 + Armor + Agility (DEX) + Dodge**

To hit a target, the attacker makes the relevant check (e.g., `1d20 + relevant attribute + skill modifier`) and must **exceed** the target's Physical Defense.

- If the check exceeds Physical Defense: the attack hits and deals damage.
- If the check does not exceed Physical Defense: the attack is treated as dodged/blocked and deals **no damage**.

Example: You make a Fighting check: `1d20 + Strength (STR) + skill modifier`. If the opponent's Physical Defense is 24, you hit only if your result **exceeds 24**.

### Firearms and Dodging

Firearms generally cannot be dodged. When facing firearms, the opposed Physical Defense does **not** include Agility (DEX) and Dodge:

**Physical Defense = 10 + Armor**

If you have the **Quick Dodge** skill, you can dodge bullets. When facing firearms, you retain full Physical Defense:

**Physical Defense = 10 + Armor + Agility (DEX) + Dodge**

See [[LINK LATER: Quick Dodge | type=skill | hint=bullet dodging]].

### Other Defenses

Some Beyonder Abilities oppose **Constitution Defense** or **Willpower Defense** instead of Physical Defense. For how these defenses are calculated, see [[LINK LATER: Chapter 3: Attributes | type=rule | hint=defense formulas]]. Such attacks will be marked in the relevant ability text.

## Movement

- **1 Move Action** lets you move a distance equal to your **movement distance**. See [[LINK LATER: Chapter 3: Attributes | type=rule | hint=movement distance]].
- Generally: **movement distance = Strength (STR) + Agility (DEX)**.
- A Move Action can be used during other people's turns, but cannot be banked into the next round.

A Move Action can also represent movement of limbs/objects, such as picking up a potion and drinking it, taking out an item, or grabbing a nearby obstacle to use as a block.

Movement-distance costs (within the same Move Action):

| Action | Cost (movement distance) |
|---|---:|
| Picking up an item on your person | 1 |
| Grabbing or moving something nearby | 2 |

Example: Movement distance 8. You grab a nearby wooden crate (2 movement distance) to use [[LINK LATER: Borrowed-Object Protection | type=mechanic | hint=blocking with objects]]. Remaining movement distance: **8 - 2 = 6**.

## GM Guidance

### Encounter Balance and Rewards

> **GM Note:** Beyonder power comes from Beyonder Characteristics. Aside from special cases (e.g., regions described in [[LINK LATER: Chapter 12: Special Regions | type=location | hint=region effects]]), arranging too many enemies can create excessively large rewards because enemies may drop Beyonder Characteristics. Have enemies behave intelligently: probe, retreat if they cannot win, and avoid making rewards "too cheap."

### Tuning Enemy Stats

> **GM Note:** When arranging enemies, dynamically adjust enemies' Dodge and Fighting values against the PCs' Physical Defense and skill modifiers. Avoid "dance fighting" (no one can hit) and "guaranteed hits" (every strike lands). During session prep, you may do private test checks and aim for roughly a **50/50** hit rate and damage such that it takes **2-3 hits or more** to reach the [[LINK LATER: Dying Threshold | type=mechanic | hint=death threshold]] (except boss fights). Enemy stat assignments must be reasonable for the PCs' Sequences (e.g., don't keep PCs at Sequence 9 while enemies have Physical Defense values that are unrealistically high).

### Use Special Actions

> **GM Note:** Make good use of [[LINK LATER: Special Actions | type=mechanic | hint=combat options]]. They can provide check modifier bonuses, restrict enemies' actions, and more. Skill-based advantages can narrow gaps between low-Sequence and high-Sequence opponents.

## Group Battle Variant

This is an optional ruleset intended to speed up combat when the number of combatants on the same "screen" reaches **4** (including NPCs).

### Setup

- Optional initiative at combat start: roll initiative (as in Initiative) and resolve from highest to lowest, or sort by Agility (DEX).
- Commands: `.ri+Agility (DEX)` to roll; `.init` to view order; `.init clr` to clear.

### Flow

1. The GM briefs the Players on the environment and positions, who and where the enemies are, what is happening, and what actions the enemies are about to take (their intent).
2. All Players then **declare** (roleplay) what they intend to do.
3. The GM resolves outcomes in initiative or Agility (DEX) order, providing feedback from first to last.
4. Checks are rolled **during resolution** (when the action actually occurs in the narration), not during the initial declaration.

### Timing Notes

- Priority is determined by **time required**, not by a separate traditional priority list.
- Under normal circumstances, Free Actions resolve before Swift Actions and Attack Actions; Swift Actions resolve before Attack Actions.
- If an Attack/Cast action is already **in progress**, a Free Action or Swift Action used at that moment may resolve only **simultaneously** with it unless an ability explicitly says it interrupts.

> **GM Note:** The text uses "half-completed Attack Action" as a narrative timing concept but does not define a measurement method for progress. Use the safest faithful reading: if an action has already meaningfully begun resolving, later actions at similar speed occur simultaneously unless a rule/ability explicitly grants interruption.

Additional rules and exceptions (as written):

- An attack made as a Free Action generally cannot interrupt an ongoing Move Action or Attack/Cast Action; at most, it resolves simultaneously and adds damage.
- If two characters simultaneously use Free Actions to attack each other, order is determined by initiative or Agility (DEX). If equal, both Free Actions take effect simultaneously.
- Some control abilities can interrupt an Attack Action currently in progress (Free Actions are difficult to interrupt due to speed). Example: Moon Pathway "Abyss Shackles." The restrained target makes the relevant opposed check to determine whether the attack still succeeds; on failure, the attack for that round is interrupted. Whether the target can still use Free Actions that round depends on the control ability's description. See [[LINK LATER: Abyss Shackles | type=ability | hint=control example]] and [[LINK LATER: Moon Pathway | type=pathway | hint=control abilities]].
- "Agile Hand" exception: an attack or casting action gained through **Agile Hand** is treated as requiring only the time of a Free Action, so it may interrupt an attack in some cases. "Dual Action" (Marauder Pathway) includes one original action plus one attack or move action gained through Agile Hand; only the latter is Free-action time. The original attack/cast remains standard time. See [[LINK LATER: Agile Hand | type=ability | hint=action speed]] and [[LINK LATER: Dual Action | type=ability | hint=paired actions]] and [[LINK LATER: Marauder Pathway | type=pathway | hint=ability source]].
- Extra Attack Actions gained through other means (example given: a Great Success on an Intuition ability) are treated as requiring standard action time and cannot interrupt others' progress. The user may choose to fire all extra actions gained within the time of one standard action, but those extra actions cannot be saved to the next round.

### Handling Confusion

> **GM Note:** If declarations become chaotic, use these handling points:
> 1. All Players must declare at the very start (including "I take no action yet," plus when they intend to act and what preparation they make).
> 2. Declarations can be spoken in initiative or Agility order to keep it orderly, while still treating the round as "declared together."
> 3. Rolls/checks happen during GM resolution, not at declaration.
> 4. GM descriptions should depict the process of combat, not only outcomes.

## Armor Break

Armor is not indestructible. Under certain conditions it can be damaged (a gap appears) rather than completely destroyed.

### Armor Break Conditions

When a creature has **Armor** and **damage reduction**, calculate Armor Break under these conditions:

- **Normal damage (brawl/melee damage, etc.):** If the attack roll exceeds the target's Physical Defense **and** deals **>=10 effective damage**, the Armor is considered damaged. This becomes a Vital Strike location; Vital Striking this part adds **1d6** damage.
- **Firearms/explosive damage** (including other attacks whose speed is treated as firearms): If the attack roll exceeds the target's Physical Defense, it is considered Armor Break. If it does **not** meet the normal-damage **>=10 effective damage** requirement, then Vital Striking this spot ignores Armor and damage reduction but does **not** gain the increased damage benefit.
- **Special:** A zombie's Armor, even when facing firearms/explosive damage, only suffers the **normal damage** effect above.

### Wound Widening

- For each **10** points of effective damage dealt by the above two damage types, the Vital Strike penalty against the corresponding part is **-2**.
- Performing a Vital Strike against this spot does not suffer the target's Armor-area damage reduction effect.

> **Lore:** Light and Lightning usually are not considered Armor Break content because they cannot perform a Vital Strike (they cannot concentrate on a single point). If damage can be designated to strike a specific point (example given: Spear of No Darkness), treat it as a normal damage roll.

### Armor Recovery

**Armor Recovery (Skin Armor):**
- After a Beyonder restores **10 HP**, it no longer suffers the Wound Widening penalty reduction.
- After restoring **20 HP**, it repairs the Armor and damage reduction effects.
- Once HP is fully restored, gain all recovery benefits.

[[UNCLEAR: "Once HP is fully restored, gain all recovery benefits" is redundant with the prior lines and does not specify an additional effect beyond full repair.]]

## HP and Damage Examples

These are reference values and may contain errors (as stated in the source text).

### Creature HP Examples

Ordinary creatures (not including Beyonder creatures):

| Category (examples) | HP |
|---|---|
| Tiny (insects, ants; count as 10 per unit) | Each ten have **1 HP**. |
| Small (rats, birds, a hand, a steak) | **2d2 HP**. |
| Small-medium (cats, dogs; large dogs add **+1d3**) | **7 + 1d3 HP**. |
| Medium (humans, deep ones, a young lion or tiger) | **10 + 2d3 HP**. |
| Medium-large (adult lions, tigers, bears, cattle; meat pigs add **+1d5**) | **20 HP**. |
| Large (giants, large-bodied creatures, Feysacians) | **20 + 2d4 HP**. |
| Huge (size comparable to a ship; 4m or 6m giants; creatures that can destroy ships) | **60 + 10d2 HP**, or more. |

### Vehicle HP Examples

| Vehicle | HP | Physical Defense | Damage Reduction |
|---|---:|---|---|
| Carriage | **30** | **20** (5 Armor, 5 Agility (DEX)) | None |
| Steam Train | **150** | **40** (15 Armor, 15 Agility (DEX)) | **5** physical/fire |
| Airship | **150** | **35** (15 Armor, 10 Agility (DEX)) | **5** physical/fire |
| Small ship | **40** | **20** (5 Armor, 5 Agility (DEX)) | None |
| Medium ship | **60** | **25** (8 Armor, 7 Agility (DEX)) | **5** physical |
| Large ship | **80** | **30** (10 Armor, 10 Agility (DEX)) | **8** physical |
| Ironclad ship | **150** | **40** (15 Armor, 15 Agility (DEX)) | **15** physical/fire |

Special:
- Any ship/airship, when HP is below half (round down), begins sinking or falling.
- Vehicles not in motion do **not** gain Agility (DEX) bonuses to Physical Defense.

### Modern Supplement

| Object | HP | Physical Defense | Damage Reduction |
|---|---:|---|---|
| Car | **40** | **30** (10 Armor, 10 Agility (DEX)) | **5** physical/fire |
| Building | **60** | **35** (25 Armor) | **5** physical/fire |
| Tank | **80** | **40** (25 Armor, 5 Agility (DEX)) | **10** physical/fire |
| Aircraft Carrier | **180** | **45** (25 Armor, 10 Agility (DEX)) | **15** physical/fire |
| Large underground permanent defensive fortification (nuclear-blast level) | **350** | **50** (40 Armor) | **20** physical/fire |

> **GM Note:** The source text notes these calculations may contain many errors. When the gap is clearly too large, do not allow Beyonders to deal effective attacks unless they are demigods or are attacking core parts.

### Damage Examples

- **10d100 fire + 5d100 physical:** center of a nuclear bomb; damage ignores defense and occurs directly.
- **1d50 fire + 10d50 physical:** about 1 km from a nuclear bomb.
- **5d50 physical:** about 4 km from a nuclear bomb.
- **3d10:** a natural lightning strike; about 6 km from a nuclear bomb (burn reference).
- **3d6:** demolition grenade; or being hit by a fast small car/carriage.
- **2d6:** being hit by a not-fast small car/carriage.
- **1d6:** firearm damage (revolver).
- **3d6:** heavy firearm damage (steam rifle).
- **1d10:** strong radiation damage; affects living creatures and precision instruments; once per round.
- **1d8:** medium radiation damage; affects living creatures and precision instruments; once per round.
- **1d6:** weak radiation damage; affects living creatures and precision instruments; once per round.
- **1:** faint radiation damage; affects living creatures and precision instruments; once per round.
- **1:** extremely weak radiation damage; affects living creatures and precision instruments; once per day.

Radiation note (as written): Even after leaving the radiation source, damage may continue for a period due to contaminated radiation dust. Thoroughly rinsing the body with large amounts of clean water may downgrade radiation damage by removing radiation dust.

## Damage Types

- **Physical Damage:** Ordinary physical damage (non-occult). At low Sequence, major obstacles are uncommon except vs cases like wraiths; at higher Sequence, it is often replaced by other damage types.
- **Curse Damage:** Wounds are pitch-black with no blood; flesh may vanish. Suppresses natural HP recovery (not Beyonder healing). HP lost to curse damage usually cannot begin to recover naturally until **half a day** later. Can be purified or expelled early by the Sun Pathway; other healing-type Pathways may also do so. Can affect living targets and objects.
- **Fire Damage:** Doubled against spiderwebs, wood, and vine plants.
- **Cold Damage:** Often causes "Slow"-type effects such as reduced movement speed and/or penalties to the next check. Fire methods may offset cold-environment penalties depending on relative Sequence/level; cold resistance can allow ignoring penalties and speed reductions.
- **Holy Damage:** Concentrated in the Sun Pathway; restrains Darkness, Corruption, and undead. Additional restraining damage is usually limited to the Sun Pathway itself. Holy damage is extremely difficult to reduce; only Sun Pathway vs Sun Pathway may have partial immunity. Sun Pathway talismans require gold.
- **Lightning Damage:** Concentrated in the Storm Pathway. Can, with extremely high priority, ignore the Agility (DEX) and Dodge parts of Physical Defense in situations where Physical Defense is generally very high. Has an additional effect against undead creatures.
- **Mental Damage:** Examples include Spectator (mental strike) and Arbiter (mental pierce). Often targets low **Willpower Defense**, producing a high hit rate. Often includes control effects (e.g., stun, fear) that reduce enemy actions. Can affect undead (as written: undead that can act have spirit bodies and can go mad).
- **Toxin Damage:** Targets **Constitution Defense** (between Physical Defense and Willpower Defense in typical breakthrough difficulty). Common sources include Demoness Pathway and certain Beyonder Abilities; Moon, Earth, and Abyss Pathways can also create toxin damage. Generally hard to apply to golems.

## Defense and Dodge Types

### Damage Reduction

**Damage reduction** reduces damage taken (typically 2-5). It is most effective against **multi-hit** damage.

- Damage reduction applies to multi-hit damage as multiple reductions (one per hit/instance), not once per damage die.
- If a single attack combines multiple dice into one damage instance (e.g., multiple damage types rolled together for one hit), damage reduction is applied **once** to the combined result.
- Damage reduction cannot reduce a damage instance below **1** (you always take at least 1 damage).

Examples (as written):
- Many small hits: If 50 air cannons each deal 1d6 damage and damage reduction is 5, each hit is reduced by 5 (minimum 1).
- One combined instance: A destruction potion dealing 2d6 acid + 2d6 toxin + 2d6 fire is still one attack; reduce only once from the combined result.
- One slash with stacked dice: If damage is 1d5 + 2d12 + 1d8 from a single slash, reduce only once.

### Immunity

**Immunity** is an extreme form of damage reduction: it can completely negate a type of damage, taking **0 HP** loss from that type.

### Damage Resistance

**Damage resistance** reduces damage taken for a specific damage type (e.g., fire resistance, cold resistance, lightning resistance, curse resistance).

- Unlike damage reduction, damage resistance can reduce a damage instance to **0**.
- Damage resistance often includes additional effects:
- Fire resistance: act naturally in certain fire environments.
- Cold resistance: ignore Slow/penalty debuffs from certain cold skills.
- Lightning resistance: may grant immunity to paralysis.
- Curse resistance: may allow ignoring curse-related additional effects (see relevant ability descriptions).

### Extra Dodge

**Extra Dodge** increases Dodge under conditions where an incoming attack is slower than bullet-speed. It is usually an additional effect of **High-Speed Dodge** or **Quick Dodge**.

- Extra Dodge usually does not apply to bullet-speed attacks; it applies when the incoming attack is slower than a bullet.

Example logic (as written):
- Against firearms, Physical Defense may drop to **10 + Armor** because bullets cannot be dodged.
- If you can dodge bullets (Quick Dodge), you retain full Physical Defense (**10 + Armor + Agility (DEX) + Dodge**) even against firearms.
- Against slower attacks (e.g., a fist), Extra Dodge may apply because if you can dodge bullets, you should dodge slower attacks even more easily.

See [[LINK LATER: High-Speed Dodge | type=skill | hint=extra dodge]] and [[LINK LATER: Quick Dodge | type=skill | hint=bullet dodging]].

#### Rise by 1 Dodge Tier

Extra Dodge is often described as "**rise by 1 Dodge tier**":

- If Dodge is **Trained**, treat it as **Proficient** (from +2 to +4).
- If Dodge is **Proficient**, treat it as **Advanced** (from +4 to +5).
- Starting from **Advanced**, skill bonuses increase by **+1 per tier** instead of **+2 per tier**.

#### High-Sequence Notes

- Extra Dodge exists because the incoming attack is not as fast as a bullet, while lightning and light are faster than bullets.
- When facing such attacks, you cannot gain Extra Dodge, and it may be that preserved Agility (DEX) and Dodge bonuses from High-Speed Dodge cannot take effect either.
- At very high Sequence, some Pathways may reach speeds where bullets are "like fists," potentially allowing Extra Dodge even against bullets or lightning; the source text states this is basically limited to angels and would be noted in relevant Sequence upgrade entries.
