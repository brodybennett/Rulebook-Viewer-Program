---
title: 'Sequence 5: Reaper'
id: red-priest-seq-05
tags:
- pathway:red-priest
- sequence:5
---





# Red Priest Pathway: Sequence 5

> **Lore:** A Reaper is skilled at finding a prey’s weakness and launching an absolutely fatal attack, with extremely strong offensive power.

## Reaper

## Advancement

### Advancement Ritual

- **Ritual:** Swear to resist in a fierce battle against your weakness—both material weakness and spiritual weakness—then take the potion. *(Unofficial ceremony.)*
- **During the ceremony:** The potion causes the **Extraordinary** to suffer both spiritual and material tortures. Their vital points as a living creature are torn in that moment; blood spurts as if the body is nearly torn apart, and the internal organs also suffer damage.
- **Requirement:** The **Extraordinary** must obtain strong enough willpower before this; otherwise, even if the body is reliable, they will eventually collapse and lose control after losing consciousness. [[Lose Control]]
- **After the promotion:** Although the injury is barely bearable, the better the **Extraordinary** maintains physical condition at the end of the ceremony, the easier it is to be promoted. Otherwise, even if they resist mentally, the **Extraordinary** will still fall down immediately after the promotion is completed, and may die due to physiological reasons.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +1, Agility (DEX) +1, Willpower (WIL) +2.
- All your Sequence 9 skills can quickly grow to **Master**. [[Master]]
- [[Mysticism]] can be upgraded to **Erudition**. [[Erudition]]

### Spot Weaknesses

```yaml ability
id: red-priest-seq-05-spot-weaknesses
name: Spot Weaknesses
pathway: red-priest
sequence: 5
type: active
action: free
cost: {}
roll: null
opposed_by: difficulty_value
range: Choose 1 target within your [[Field of Vision]].
target: designated target(s)
duration: sustained
scaling: []
tags:
- ritual
- detection
- debuff
- defense
text: 'Cost: None (does not consume Spirituality). [[Spirituality]] Use: 1 Free Action.
  Free Action Limits: 1 time per Round. Round Targeting and range: Choose 1 target
  within your [[Field of Vision]]. Test: Perform a [[Detection test]] with Difficulty
  Value 20. Difficulty Value Effect: If the identification is successful, you immediately
  know the opponents weakness from a tactical point of view (e.g., darkness/corruption/undead
  creatures fear the sacred; plants fear poison; stone giants fear ice and fire).
  This does not mean you know the opponents creature type. At the same time, you learn
  which of the opponents existing [[Resistance]] is the lowest. You do not know the
  specific resistance valu...'
```




> **Lore:** You are good at spotting the weaknesses of your prey.

- **Cost:** None (does not consume **Spirituality**). [[Spirituality]]
- **Use:** 1 **Free Action**. Free Action
- **Limits:** 1 time per **Round**. Round
- **Targeting and range:** Choose 1 target within your [[Field of Vision]].
- **Test:** Perform a [[Detection test]] with **Difficulty Value** 20. Difficulty Value
- **Effect:**
  1. If the identification is successful, you immediately know the opponent’s weakness from a tactical point of view (e.g., darkness/corruption/undead creatures fear the sacred; plants fear poison; stone giants fear ice and fire). This does not mean you know the opponent’s creature type.
  2. At the same time, you learn which of the opponent’s existing [[Resistance]] is the lowest. You do not know the specific resistance value—only which resistance is lowest (i.e., which attack is most effective).

### Harvest

```yaml ability
id: red-priest-seq-05-harvest
name: Harvest
pathway: red-priest
sequence: 5
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- buff
- offense
text: '#### Weakness Attack Cost: 2 points of Spirituality. Use: 1 attack/casting/Swift
  Action that causes damage. Swift Action Effect: The various colors of the targets
  body immediately appear in your eyes. The position representing the weakness is
  pale. This attack is -8 disadvantageous, and the damage caused is increased by 3d6.
  [[Disadvantageous]] This is a Vital Blow, which cannot be superimposed with other
  Vital Blows. [[Vital Blow]] The weakness from this mystical point of view is not
  necessarily the internal organs and other locations. #### Fatal Attack Cost: 4 points
  of Spirituality.'
```




> **Lore:** You discover the opponent’s weakness from the perspective of mysticism, and use this to launch a very powerful attack.

#### Weakness Attack

- **Cost:** 2 points of **Spirituality**.
- **Use:** 1 attack/casting/Swift Action that causes damage. Swift Action
- **Effect:** The various colors of the target’s body immediately appear in your eyes.
  1. The position representing the weakness is pale. This attack is **-8 disadvantageous**, and the damage caused is increased by 3d6. [[Disadvantageous]]
  2. This is a **Vital Blow**, which cannot be superimposed with other **Vital Blows**. [[Vital Blow]] The weakness from this mystical point of view is not necessarily the internal organs and other locations.

> **GM Note:** Example: The weakness of the resentful soul may not be in the head, but a little above the Adam’s apple.

#### Fatal Attack

- **Cost:** 4 points of **Spirituality**.
- **Use:** 1 attack/casting/Swift Action that causes damage.
- **Effect:** The eyes will also appear in color.
  1. This strike has the effect of **Weak Point Attack** by default. [[Weak Point Attack]] As long as it hits the opponent, no matter where it hits (even if it is armor), it is considered to cause a weak point attack.  
     (So as long as your attack Identification roll exceeds the target’s Agility (DEX) + Dodge, even if it does not penetrate the armor, it can still cause 3d6 default damage.) Agility (DEX) Dodge [[Armor Penetration]]
     - But because the real damage does not penetrate, no matter how much damage you could have caused, it is only 3d6 at this time.
  2. On the basis of 1, you are considered to have performed a real **Critical Strike** special action, but this critical strike also only has a -8 disadvantage, and the effects of the **Vital Strike** special action can be superimposed with the weak point attack. [[Critical Strike special action]] [[Vital Strike special action]]

> **GM Note:** Example: The initial attack that will cause 1d6+2d6 damage can add +3d6 damage due to the weak point, but if it does not penetrate the armor while hitting the opponent, the 1d6+2d6 damage is invalid—only 3d6.  
> (If the armor is penetrated, the vital blow effect of internal organs will be superimposed, causing 1d6+2d6+3d6+3d6 damage.)


#### Carnage (Slaughter)

> **Lore:** You change your damage to area kills.

- **Trigger/requirement:** This is based on Weakness Attack/Fatal Attack. When you perform either of these attacks, if you give [[Doubled aura]], it can cause a more lethal effect.
- **Effect:**
  1. Weak point attack: change to consume 4 **Spirituality**, and your single-target attack is changed to attack within 10 meters in front of you.
  2. Fatal attack: instead of consuming 12 **Spirituality**, on the basis of 1, the attack has the effect of Fatal Attack.
- (The main effect of Slaughter is to change single-target damage to group damage. If the ability you originally cast is group damage, then you must use Slaughter to enjoy the benefits of weak point/fatal attack; otherwise the ranged damage will not enjoy the harvest effect.)

- **Limits:** As described in this section's prose.
