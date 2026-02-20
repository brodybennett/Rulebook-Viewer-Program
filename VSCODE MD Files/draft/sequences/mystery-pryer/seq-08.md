---
title: 'Sequence 8: Meister of Weaponry'
id: mystery-pryer-seq-08
tags:
- pathway:mystery-pryer
- sequence:8
---





# Hermit Pathway: Sequence 8

## Meister of Weaponry

> **Lore:** Seeking the secret behind things, fighting is also a kind of things.

- See also: Scholar Pathway

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +2, Agility (DEX) +1, Intuition (INT) +1.
- **Skill growth:** Your fighting-related / dodge / throwing skills are included in the “rapid growth category” of your Sequence 9, up to **Proficient**.

Additionally, you gain the following benefits:

1. **Special action identification bonus:** Your critical strike / double strike / proximity shooting and other special action identification +2 is beneficial, excluding first aid / surprise attack, and does not affect special actions that simply gain benefits, such as gaining momentum and aiming. The +2 bonus does not stack beyond +4 total. It only affects identification.  
   - [[Special Action Identification]]
   - [[Critical Strike]]
   - [[Double Strike]]
   - [[Proximity Shooting]]
   - [[First Aid]]
   - [[Surprise Attack]]
   - [[Gaining Momentum]]
   - [[Aiming]]
2. **Feint and close-range firearm substitution:**
   - When you perform a [[Feint]], you can use fighting identification instead of performance / deceit identification, no matter whether fighting is **Proficient** or not.
   - When using a firearm, if the target is less than 5 meters away from you, shooting can be changed to fighting identification, but the related attribute is Agility (DEX).

### Combat Magic

```yaml ability
id: mystery-pryer-seq-08-combat-magic
name: Combat Magic
pathway: mystery-pryer
sequence: 8
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- utility
text: Combat Magic ability details are defined in the source markdown.
```




- **Effect:** Combat Magic resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Armor of Knowledge

```yaml ability
id: mystery-pryer-seq-08-armor-of-knowledge
name: Armor of Knowledge
pathway: mystery-pryer
sequence: 8
type: active
action: swift
cost: {}
roll: null
opposed_by: physical_defense
range: Self
target: designated target(s)
duration: 1 round
scaling: []
tags:
- ritual
- defense
text: 'Cost: 2 [[Spirituality]] Use: Swift Action Effect: Intangible, undecipherable
  knowledge protects you from harm. You gain Armor of Knowledge for 1 round. Targeting
  and range: Self Duration: 1 round Limits: Your physical defense gains Armor equal
  to (max(Education, Intuition (INT)) + Occult) / 3, rounded down. [[Physical Defense]]
  [[Armor]]'
```




- **Cost:** 2 [[Spirituality]]
- **Use:** **Swift Action**
- **Effect:** Intangible, undecipherable knowledge protects you from harm. You gain Armor of Knowledge for 1 round.
- **Targeting and range:** Self
- **Duration:** 1 round
- **Limits:** Your **physical defense** gains Armor equal to ⌊(max(Education, Intuition (INT)) + Occult) / 3⌋, rounded down.  
  - [[Physical Defense]]
  - [[Armor]]

### Invisible Servant

```yaml ability
id: mystery-pryer-seq-08-invisible-servant
name: Invisible Servant
pathway: mystery-pryer
sequence: 8
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: Disappears after 24 hours.
scaling: []
tags:
- ritual
- stealth
text: 'Cost: 3 [[Spirituality]] Use: Casting Action; you need to pinch your lips and
  whistle. Effect: You create an invisible servant. It can pass through small gaps
  and can do relatively simple things, such as moving goods, picking locks, etc. Limits:
  The servant has 12 Vitality (every 1 point of Intuition (INT), life value +1). [[Vitality]]
  Duration: Disappears after 24 hours.'
```




- **Cost:** 3 [[Spirituality]]
- **Use:** **Casting Action**; you need to pinch your lips and whistle.
- **Effect:** You create an invisible servant. It can pass through small gaps and can do relatively simple things, such as moving goods, picking locks, etc.
- **Limits:** The servant has 12 Vitality (every 1 point of Intuition (INT), life value +1).  
  - [[Vitality]]
- **Duration:** Disappears after 24 hours.

### Fist of Fighting

```yaml ability
id: mystery-pryer-seq-08-fist-of-fighting
name: Fist of Fighting
pathway: mystery-pryer
sequence: 8
type: active
action: attack
cost: {}
roll: null
opposed_by: physical_defense
range: Against a target (range not specified).
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- defense
- offense
text: 'Cost: 2 [[Spirituality]] Use: Casting Action or Attack Action Effect: Extremely
  bright light gathers beside you, forming a fist. Targeting and range: Against a
  target (range not specified). Effect (mechanics): Use Intuition (INT) instead of
  Strength to make a combat check against the targets physical defense. Use Intuition
  (INT) instead of Strength to gain a Strength damage bonus. Limits: The bonus you
  get can only be equal to a maximum of 10 Strength.'
```




- **Cost:** 2 [[Spirituality]]
- **Use:** **Casting Action** or **Attack Action**
- **Effect:** Extremely bright light gathers beside you, forming a fist.
- **Targeting and range:** Against a target (range not specified).
- **Effect (mechanics):**
  - Use Intuition (INT) instead of Strength to make a **combat check** against the target’s **physical defense**.
  - Use Intuition (INT) instead of Strength to gain a Strength damage bonus.
- **Limits:** The bonus you get can only be equal to a maximum of 10 Strength.  
  - [[Combat Check]]
  - [[Damage Bonus]]

### The Palm of Counterattack

```yaml ability
id: mystery-pryer-seq-08-the-palm-of-counterattack
name: The Palm of Counterattack
pathway: mystery-pryer
sequence: 8
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: 1 round
scaling: []
tags:
- ritual
- offense
text: 'Cost: 2 [[Spirituality]] Use: Swift Action Duration: 1 round Trigger: When
  you receive a melee attack, no matter what state you are in. Effect: You can counterattack
  the source of the attack.'
```




- **Cost:** 2 [[Spirituality]]
- **Use:** **Swift Action**
- **Duration:** 1 round
- **Trigger:** When you receive a melee attack, no matter what state you are in.
- **Effect:** You can counterattack the source of the attack.

- **Limits:** As described in this section's prose.


### Acceleration

```yaml ability
id: mystery-pryer-seq-08-acceleration
name: Acceleration
pathway: mystery-pryer
sequence: 8
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: 1 round
scaling: []
tags:
- ritual
- mobility
text: 'Cost: 2 [[Spirituality]] Use: Swift Action Duration: 1 round Effect: Your thinking
  becomes faster and your movement speed becomes faster. Effect (mechanics): You gain
  a movement bonus equal to your Intuition (INT) divided by 2. You gain Fast Dodge
  (defined below). [[Movement Bonus]]'
```




- **Cost:** 2 [[Spirituality]]
- **Use:** **Swift Action**
- **Duration:** 1 round
- **Effect:** Your thinking becomes faster and your movement speed becomes faster.
- **Effect (mechanics):**
  - You gain a movement bonus equal to your Intuition (INT) divided by 2.
  - You gain **Fast Dodge** (defined below).  
    - [[Movement Bonus]]

- **Limits:** As described in this section's prose.


### Fast Dodge

```yaml ability
id: mystery-pryer-seq-08-fast-dodge
name: Fast Dodge
pathway: mystery-pryer
sequence: 8
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: self
duration: instant
scaling: []
tags:
- defense
text: 'Effect: You retain full physical defense against guns (light / lightning bypass
  this), and gain 1 extra level of dodge. Reference: (For extra dodge, see Defense
  and Dodge Types) [[Defense and Dodge Types]]'
```




- **Effect:** You retain full **physical defense** against guns (light / lightning bypass this), and gain 1 extra level of dodge.  
- **Reference:** (For extra dodge, see “Defense and Dodge Types”)  
  - [[Defense and Dodge Types]]

- **Limits:** As described in this section's prose.
