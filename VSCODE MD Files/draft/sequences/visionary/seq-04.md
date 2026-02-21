---
title: 'Sequence 4: Manipulator'
id: visionary-seq-04
tags:
- pathway:visionary
- sequence:4
---






# Visionary Pathway: Sequence 4

## Manipulator

> **Lore:** The Manipulator’s core gifts center on **manipulation** and **virtual personalities**, expressed through a corresponding mental body that can resist many influences in the spiritual field. Practitioners are known to invade a target’s [[Consciousness Island]], tamper with the subconscious, read thoughts, and drive targets toward actions without obvious external pressure.

Commonly associated techniques include:
- [[Consciousness Walking]]
- [[Dragon Transformation]]
- [[Mental Deprivation]]
- [[Psychic Storm]]
- [[Spiritual Plague]]
- [[Psychological Invisibility]]

## Advancement

### Auxiliary Materials

- **Primary Material:** The complete brain of an aged psychic dragon, **or** the crystallized heart of a treant mentor.
- **Auxiliary Materials:** 80 ml of the blood of the old psychic dragon; 3 golden leaves of the treant mentor; 1 drop of tears produced by 7 different humans or humanoid creatures due to strong emotions.

### Advancement Ritual

- **Advancement Ritual:** On a specific occasion of at least 10,000 people, consume the potion in the great resonance of their emotions. [[MISSING REF: 7]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Willpower (WIL) +5; Strength +3; Constitution +1; Agility (DEX) +1; Psychological Guidance and Psychological Skills increase by 1 level.

### Multiple Minds

```yaml ability
id: visionary-seq-04-multiple-minds
name: Multiple Minds
pathway: visionary
sequence: 4
status: canonical
type: active
action: attack
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
  effect_roll: "1"
  notes: "No roll; targets may attempt Intuition DV 15 to notice an implanted avatar."
scaling: []
tags:
- ritual
- defense
- offense
text: 'You possess a large number of virtual personalities that help resist attacks
  and each has a corresponding mental body. Passive benefits: You can conduct multiple
  skill appraisals at the same time (e.g., pick a lock while reading a book). In combat,
  you can take an Attack Action and a Spellcasting action respectively. You may use
  a virtual personality as a stand-in to resist influences in the spiritual field.
  This does not resist damage from direct blows to the spirit body (e.g., [[Spiritual
  Puncture]], [[Spiritual Breath]]). You have 13 virtual personalities in Sequence
  4, and 16 after digesting the potion. All values of the virtual personality are
  equal to yours. Note: If all your avatar...'
```





You possess a large number of **virtual personalities** that help resist attacks and each has a corresponding mental body.

- **Passive benefits:**
  - You can conduct multiple skill appraisals at the same time (e.g., pick a lock while reading a book).
  - In combat, you can take an **Attack Action** and a **Spellcasting action** respectively.
  - You may use a virtual personality as a stand-in to resist influences in the spiritual field. This does **not** resist damage from direct blows to the spirit body (e.g., [[Spiritual Puncture]], [[Spiritual Breath]]).
  - You have 13 virtual personalities in Sequence 4, and 16 after digesting the potion.
  - All values of the virtual personality are equal to yours.
- **Note:** If all your avatars are insane or otherwise unusable, you lose the above multiple-action benefits; [[Psychic Strike]] begins to affect you; and avatars that fall into madness cannot continue to be used.

- **Active (implant a virtual personality):** Implant a virtual personality into a creature; you gain:
  - Shared vision with that creature.
  - You may use that creature as a focal point to use: [[Mind Channeling]], [[Stun]], [[id:alias-frenzy|Frenzy]], [[Mind Reading]], [[Psychic Storm]], and [[Dream Manipulation]].
- **Note (detection/counterplay):** Implanting an avatar in an identical target allows the target’s spiritual intuition to attempt an **Intuition (INT) check** (Difficulty Value 15) to perceive it. This may allow the other party to counterattack. If implanting into a target of the same personality, the act must be sufficiently concealed.

- **Sequence 3 (separating identities):**
  - You can separate some identities or virtual personalities you once had and turn them into living people.
  - Even if these identities die, they do not cause the main body to fall.
  - You can separate 3 additional real personalities; beyond this limit, you must use your own virtual personality limit as a substitute.
  - Separated identities and avatars can be endowed with extraordinary characteristics and memories.
  - If an avatar uses your main body to use high-level abilities: all abilities must be prepared as a **Full-Round Action**; passive abilities cannot be used; and all abilities can only be used initially.

- **Effect:** Multiple Minds resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Psychic Breath

```yaml ability
id: visionary-seq-04-psychic-breath
name: Psychic Breath
pathway: visionary
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 6
roll: 1d20 + @attr.int + @skill.psychological_guidance
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychological_guidance
  damage_roll: 5d6
  heal_roll: null
  effect_roll: null
  notes: "Apply -4 disadvantage to the check; damage ignores fire resistance and imposes -4 on the target's next Penetrating Blow That Pierces the Soul check."
scaling: []
tags:
- ritual
- stealth
- defense
- offense
text: 'You breathe out an invisible but searing flame. Cost: 6 points of Spirituality.
  Use: Spellcasting action. Effect: Make a psychological attack against the targets
  Willpower Defense with disadvantage (-4). Area: 10-meter cone. Deal 5d6 fire damage
  with invisible mental fire. This damage cannot be reduced by any kind of fire resistance.'
```





You breathe out an invisible but searing flame.

- **Cost:** 6 points of **Spirituality**.
- **Use:** **Spellcasting action**.
- **Effect:**
  - Make a psychological attack against the target’s Willpower Defense with disadvantage (-4).  
  - **Area:** 10-meter cone.
  - Deal 5d6 fire damage with invisible mental fire.
  - This damage cannot be reduced by any kind of fire resistance.
  - You do not gain the double effect of burning plants and webs.
  - **Psychic Breath** causes enemies to take a -4 penalty on their next check for the [[Penetrating Blow That Pierces the Soul]].

- **Limits:** As described in this section's prose.


### Psychic Storm

```yaml ability
id: visionary-seq-04-psychic-storm
name: Psychic Storm
pathway: visionary
sequence: 4
status: canonical
type: active
action: cast
cost:
  spirituality: 5
roll: 1d20 + @attr.int + @skill.psychological_guidance
opposed_by: willpower_defense
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychological_guidance
  damage_roll: null
  heal_roll: null
  effect_roll: 2d6
  notes: "Mode 1: area 2d6 km, duration 1d6 hours, divination interference 1d3 days. Mode 2: check vs Willpower Defense at -4 disadvantage (-8 if known spectator); on success target makes sanity check 1/1d2 and is stunned."
scaling: []
tags:
- ritual
- stealth
- offense
text: 'You create an invisible wind, forming a psychic storm. This ability can be
  used in two ways. Mode 1: Set off a spiritual storm in the Sea of Collective Subconscious
  Cost: 5 Spirituality. Use: Spellcasting action. Area/Duration: 2d6 kilometers in
  diameter for 1d6 hours. Effect: The mental storm immediately produces one weather
  effect you choose: heavy rain, strong wind, thunder, or sunny day. The storm does
  not appear in reality; it appears in the [[Sea of Collective Subconscious]], but
  affects the corresponding position in reality, sweeping around and repeatedly slapping
  the enemys [[Consciousness Island]].'
```





You create an invisible wind, forming a psychic storm. This ability can be used in two ways.

- **Mode 1: Set off a spiritual storm in the Sea of Collective Subconscious**
  - **Cost:** 5 **Spirituality**.
  - **Use:** **Spellcasting action**.
  - **Area/Duration:** 2d6 kilometers in diameter for 1d6 hours.
  - **Effect:**
    - The mental storm immediately produces one weather effect you choose: heavy rain, strong wind, thunder, or sunny day.
    - The storm does not appear in reality; it appears in the [[Sea of Collective Subconscious]], but affects the corresponding position in reality, sweeping around and repeatedly slapping the enemy’s [[Consciousness Island]].
    - You destroy “[[Divination Interference]]” type abilities of creatures in the area for 1d3 days.
    - Any creature that makes an **Intuition (INT) check** in the storm immediately suffers a [[Sanity / Rationality Attack]] and takes half of the Sanity / Rationality damage.
  - **Extra:** During the storm, any additional sanity protection other than the caster loses 1d3 value per round (does not affect sanity beyond sanity protection). Examples include the [[Black Emperor Sanity / Rationality Shield]] and sanity shields applied to oneself by other Audience channels.

- **Mode 2: Use information flow to wash away the enemy’s spirit**
  - **Cost:** 5 **Spirituality**.
  - **Use:** **Spellcasting action**.
  - **Targeting:** Choose a target or an area.
  - **Check:** Psychological Guidance against Willpower Defense with disadvantage (-4). If you are known to be a [[Spectator]], take an additional -4 disadvantage (total -8).
  - **Effect:**
    - Instill a large amount of information into the target’s mind (meaningless bombardment or meaningful specific information; customized).
    - On a successful Psychological Guidance check: the target must immediately make a [[Sanity / Rationality Check]] (1/1d2) and is [[Stunned]]. The stunned state cannot be stacked.
  - **Note:** If you cram compelling secret or important knowledge into the storm in this mode, the target is drawn to it and gains the knowledge as a result. If you hide in the dark, the target’s detection of the environment also fails by default because their attention is drawn away.
  - **Sequence interaction:** If the target is 1 Sequence lower than you, the special effect of the sanity test is directly replaced by the [[id:alias-frenzy|Frenzy]] effect.

- **Limits:** As described in this section's prose.


### Consciousness Walking

```yaml ability
id: visionary-seq-04-consciousness-walking
name: Consciousness Walking
pathway: visionary
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
  effect_roll: "1"
  notes: "No roll; travel effect."
scaling: []
tags:
- ritual
- offense
text: 'Allows your consciousness and spiritual body to swim in the [[Sea of Collective
  Subconscious]], but it cannot bring your physical body into it. Sequence 3: You
  can bring in your physical body by transforming it into an [[Incorporeal Body]];
  in this state you cannot receive physical damage, nor can you cause physical damage.
  For details about the Sea of Collective Subconscious and Consciousness Islands,
  see [[Chapter Twelve: Special Regions]].'
```





Allows your consciousness and spiritual body to swim in the [[Sea of Collective Subconscious]], but it cannot bring your physical body into it.

- **Sequence 3:** You can bring in your physical body by transforming it into an [[Incorporeal Body]]; in this state you cannot receive physical damage, nor can you cause physical damage.
- For details about the Sea of Collective Subconscious and Consciousness Islands, see [[Chapter Twelve: Special Regions]].

- **Effect:** Consciousness Walking resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Accurate Grasp

```yaml ability
id: visionary-seq-04-accurate-grasp
name: Accurate Grasp
pathway: visionary
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
  notes: "No roll; consumes an avatar to redirect a discovered attack to the phantom."
scaling: []
tags:
- divination
- control
- offense
text: You can precisely control your own psychology and spirit; premonition-like abilities
  no longer work on you. This is an explanation, not a transcendent ability; demigods
  of the Spectator path can already do this on their own, so this ability cannot be
  stolen or recorded. From now on, premonition-type abilities have no effect on you
  (e.g., fast immediate action, or any kind of extra-action ability with a high success
  in the description). If an attack against you is successful, you cannot gain the
  benefits of fast intuitive action. If you gain an extra action of fast intuitive
  action through others, the target of that extra action cannot be you. The thiefs
  swift hand grand success effect is...
```





You can precisely control your own psychology and spirit; premonition-like abilities no longer work on you.

- This is an explanation, not a transcendent ability; demigods of the Spectator path can already do this on their own, so this ability cannot be stolen or recorded.
- From now on, premonition-type abilities have no effect on you (e.g., fast immediate action, or any kind of extra-action ability with a high success in the description).
- If an attack against you is successful, you cannot gain the benefits of fast intuitive action.
- If you gain an extra action of fast intuitive action through others, the target of that extra action cannot be you.
- The thief’s swift hand grand success effect is also a quick intuitive action.

- **Effect:** Accurate Grasp resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Psychic Stealth

```yaml ability
id: visionary-seq-04-psychic-stealth
name: Psychic Stealth
pathway: visionary
sequence: 4
status: canonical
type: active
action: swift
cost:
  spirituality: 3
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: "Sanity check is 0/1 (treat as 1d2-1); target must also make Will DV 20 each round; Psychoanalysis DV 20 to relieve."
scaling: []
tags:
- stealth
- offense
text: 'Your psychic cloaking advances further. Use: 1 Swift Action, once per round,
  only available during the instant of [[Psychological Invisibility]] exposure. Effect:
  While psychologically invisible, you consume an avatar to create a phantom beside
  you that shares the objects affected by psychological invisibility. Only for the
  moment when the psychic cloak is discovered and attacked, attacks on you (except
  area attacks) are directed at the phantom instead. The phantom takes no real damageonly
  Sanity / Rationality damageand goes insane. After the ability ends, the avatar returns
  to your body.'
```





Your psychic cloaking advances further.

- **Use:** 1 **Swift Action**, once per round, only available during the instant of [[Psychological Invisibility]] exposure.
- **Effect:** While psychologically invisible, you consume an avatar to create a phantom beside you that shares the objects affected by psychological invisibility. Only for the moment when the psychic cloak is discovered and attacked, attacks on you (except area attacks) are directed at the phantom instead.
- The phantom takes no real damage—only Sanity / Rationality damage—and goes insane. After the ability ends, the avatar returns to your body.

- **Limits:** As described in this section's prose.


### Psychic Plague

```yaml ability
id: visionary-seq-04-psychic-plague
name: Psychic Plague
pathway: visionary
sequence: 4
status: canonical
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- healing
text: 'Quietly plant seeds of Contagious Madness in the targets mental island. Cost:
  3 points of Spirituality. Use: Swift Action, once per round. Effect: Plant a spiritual
  plague seed in the targets spiritual island. After detonation, the resulting madness
  can spread through the [[Spiritual Body Thread]]. Maturation: Seeds require two
  rounds to mature, then detonate on their own. On detonation: The detonated creature
  is immediately regarded as being in a state of mental plague. Ongoing effect (each
  round, until mental healing is obtained): The target makes a [[Sanity / Rationality
  Check]] (0/1).'
```





Quietly plant seeds of “Contagious Madness” in the target’s mental island.

- **Cost:** 3 points of **Spirituality**.
- **Use:** **Swift Action**, once per round.
- **Effect:** Plant a “spiritual plague seed” in the target’s spiritual island. After detonation, the resulting madness can spread through the [[Spiritual Body Thread]].

- **Maturation:** Seeds require two rounds to mature, then detonate on their own.
- **On detonation:** The detonated creature is immediately regarded as being in a state of mental plague.
  > **Lore:** The condition presents as extreme mood volatility (manic spikes and depressive crashes), including profound hopelessness and self-destructive thoughts.

- **Ongoing effect (each round, until mental healing is obtained):**
  - The target makes a [[Sanity / Rationality Check]] (0/1).
  - The target must also make a Will check (Difficulty Value 20). On failure, it cannot perform any actions other than **Swift**/**Free** actions.
  - Even if it passes the Will check, the next round still requires another sanity check and Will check.
  - The symptom can be relieved by a [[Psychoanalysis]] check (Difficulty Value 20). Psychoanalysis is a **Free action** once per round.
- **Insanity rules:** This is considered a form of insanity; the affected target has disadvantage on checks, and other creatures have advantage on checks against the affected target.

- **Contagion and timing:**
  - The symptoms are contagious; as long as there are spectators or other affected creatures around, the duration does not enter the countdown.  
  - **Base duration:** Once no other affected creature is within line of sight, the plague’s remaining duration becomes 10 minutes.
  - Each round, the afflicted creature uses a **Free action** to spread the plague, randomly spreading a biological plague seed within line of sight. The seed takes effect after two rounds and cannot be controlled.
  - Spread can also occur via the Spiritual Body Thread; you do not need line of sight to spread through that thread.
  - Seeds planted on the [[Secret Puppet]] do not take effect on the Secret Puppet after detonation, but they can still spread.

- **Audience interaction:**
  - For a target in the mental plague state, the Audience can ignore whether the target is in [[Shock]], directly detonate emotions, and use a Spellcasting action to use [[Madness]] on them.

- **Evasion, mitigation, and counters:**
  - The mental plague cannot be evaded by a substitute.
  - Half of its influence can be offset through the virtual personality: instead of being limited to only swift/free actions, the target may take 1 normal action per round (but still loses one action that round).
  - It can be evaded in advance by [[Teleportation]] or swapping positions, provided the target is aware of it.
  - With a specific shelter, it can only delay maturity time by 2 rounds, and the impact is halved.

- **Limits:** As described in this section's prose.
