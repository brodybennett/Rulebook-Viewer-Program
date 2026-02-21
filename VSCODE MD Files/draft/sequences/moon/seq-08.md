---
title: 'Sequence 8: Beast Tamer'
id: moon-seq-08
tags:
- pathway:moon
- sequence:8
---






# Moon Pathway: Sequence 8

> **Lore:** Domesticate and use living animals, including extraordinary creatures; greatly improve physical fitness.

## Beast Tamer

## Advancement

### Auxiliary Materials

- **Main Material:** [[Medulla Crystal of the Spring of Elves]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +2.
- Your animal taming uses Sequence 9 rapid growth rules: cap at **Proficient**, and each non-repeating tame counts as 1 growth.

### Animal Senses

```yaml ability
id: moon-seq-08-animal-senses
name: Animal Senses
pathway: moon
sequence: 8
status: canonical
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.cha + @skill.animal_handling
opposed_by: willpower_defense
range: Choose 1 animal / extraordinary creature / insect (even mosquito) within 20
  meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.animal_handling
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Taming check is opposed by the target's Willpower Defense.
scaling: []
tags:
- ritual
- detection
- defense
text: 'Cost: 3 [[Spirituality]] Use: 1 Casting Action Targeting and range: Choose
  1 animal / extraordinary creature / insect (even mosquito) within 20 meters. Check:
  Tame the beast against its Willpower Defense Effect: If you succeed, you share the
  senses with it and gain the effects below for 5 minutes. Limits: The following effects
  cannot be more than 100 meters away from the animal. It can complete the instructions
  even if it is more than 100 meters away.'
```





- **Cost:** 3 [[Spirituality]]
- **Use:** 1 Casting Action
- **Targeting and range:** Choose 1 animal / extraordinary creature / insect (even mosquito) within 20 meters.
- **Check:** Tame the beast against its Willpower Defense
- **Effect:** If you succeed, you share the senses with it and gain the effects below for 5 minutes.
- **Limits:**
  - The following effects cannot be more than 100 meters away from the animal.
  - It can complete the instructions even if it is more than 100 meters away.

#### Effects

1. **Communicating animals:** You can let you understand each other directly without words, and let it act instead of you.
2. **Share the senses:** Directly see what it sees/hears. Even if the other party’s vision (such as mosquitoes) works differently from humans, the picture in front of you can be recombined into a scene that you understand, which may lead you to share [[Sanity / Rationality Loss]].
3. **Drive animals:** In battle, the actions of animals are independent of you, and you can maintain inspired animals equal to your **Intuition (INT)**; they share senses at the same time.
   - Non-intelligent animals can usually be regarded as your subordinates directly after the successful identification of animal taming, and provide you with benefits. [[Animal Taming Identification]]
4. **Auxiliary Potion:** When you share the senses with an intelligent animal:
   - A common animal imposes a **-4 penalty** to the target’s [[Sanity / Rationality Loss Identification]].
   - Only when your Sequence level is greater than it, the **animal** receives a -2 benefit when it is promoted.
   - If the creature’s Pathway is the same as yours, gain an additional -2 benefit.
   - You can also get this benefit if you are 1 Sequence higher than it.

#### Special

- Extraordinary creatures that already have intelligence and have not been domesticated by you (animals after taking potions): if they are not higher than your Sequence, when you intend to domesticate them, they will fall into a state of fear of you, feeling as if encountered a natural enemy.
- A creature that has been fully domesticated by you, even if you lose this ability, will still obey your orders.
  - However, animals without intelligence may cause you to no longer be able to give instructions to it.

### Domesticated Animal Examples

```yaml ability
id: moon-seq-08-domesticated-animal-examples
name: Domesticated Animal Examples
pathway: moon
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
  effect_roll: 2d2
  notes: Effect roll maps example vitality for rats/birds; other sizes use the scaling table.
scaling:
- when: cat_or_dog
  changes:
    effect_roll: 1d3
    effect_note: Vitality is 7 + 1d3.
- when: young_lion_tiger_large_dog
  changes:
    effect_roll: 2d3
    effect_note: Vitality is 10 + 2d3.
- when: adult_lion_tiger_bear_bull
  changes:
    effect_roll: 1d5
    effect_note: Vitality is 20 + 1d5.
- when: large_creature
  changes:
    effect_roll: 2d4
    effect_note: Vitality is 20 + 2d4.
- when: very_large_creature
  changes:
    effect_roll: 10d2
    effect_note: Vitality is 60 + 10d2 (or more).
tags:
- defense
- offense
text: '#### List of regular animals that may be domesticated Bugs/ants: By default,
  they die when they are hit. Only fast-moving bugs can calculate physical defense
  against (such as mosquitoes), with 10 points of physical defense (10 agility), and
  fast dodge. Faced with range/psychic damage, they will die directly by default.
  Rats/birds: 2d2 Vitality. 5 points in Three Defenses (both attributes are 2).'
```





> **GM Note:** Defaults for regular animals that may be domesticated.

#### List of regular animals that may be domesticated

1. **Bugs/ants:**
   - By default, they die when they are hit.
   - Only fast-moving bugs can calculate physical defense against (such as mosquitoes), with 10 points of physical defense (10 agility), and fast dodge.
   - Faced with range/psychic damage, they will die directly by default.
2. **Rats/birds:**
   - 2d2 Vitality.
   - 5 points in Three Defenses (both attributes are 2).
3. **Cat/Dog:**
   - 7+1d3 Vitality.
   - 8 points in Three Defenses (all attributes are 3).
4. **Young lion/tiger/large dog:**
   - 10+2d3 Vitality.
   - 15 Three Defenses (all attributes are 5).
5. **Adult lion/tiger/bear/bull:**
   - 20 Vitality.
   - 18 Three Defenses (both attributes are 8).

#### Domestication conditions

- Non-intelligent / [[Semi-crazy]] creatures can be domesticated by you for a long time by default.
- Other creatures must be voluntary if you want to domesticate them for a long time.

#### Long-term domesticated animal character cards

- If the **Player** is willing, it can be a long-term domesticated animal character card.
- The attributes refer to the list above, or you can draw up your own.
- The Vitality above determines the basic Vitality of the creature.
- The Three Defenses except the attributes determine the basic defense of the species.
- If the above attributes have more than 6 points, it means that its upper limit of attributes is higher than that of human beings.
- Turning a creature into a character card may cause the attributes to be inferior to the above simple calculation, but it means that it truly becomes a character.
- In the case that the basic defense/life does not match that of humans:
  - You can fill in the corresponding data in the extra life/defense of the character card with additional values,
  - or negative values to dynamically adjust.

> **GM Note:** More creatures can be referenced in the [[Injury/Vitality Volume Example]]. The value is determined by the GM. Animal trainers who want to patrol bears/lions and other dangerous creatures need the consent of the GM, and raising such creatures requires at least a [[Credit Rating]] order.

- **Effect:** Domesticated Animal Examples resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
