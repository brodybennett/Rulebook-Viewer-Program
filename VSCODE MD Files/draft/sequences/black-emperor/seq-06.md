---
title: 'Sequence 6: Baron of Corruption'
id: black-emperor-seq-06
tags:
- pathway:black-emperor
- sequence:6
---






# Black Emperor Pathway: Sequence 6

> **Lore:** It appears to obey rules, but actually distorts them-constantly absorbing the power of order to serve itself.

- **Distortion:** By distorting a target's language, actions, and intentions, you construct an order beneficial to yourself, restricting or influencing the opponent.
- **Corrosion:** You can make the hearts of people within 10 meters become darker and greedier, making irrational choices more likely.

## Baron of Corruption

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Constitution +1; Intuition (INT) +1; your Law and Deceit skill goes up by one level.
- At the same time, your Sequence 9 [[Rapid Improvement]] upper limit has reached [[Erudition]].

### Distortion

```yaml ability
id: black-emperor-seq-06-distortion
name: Distortion
pathway: black-emperor
sequence: 6
status: canonical
type: active
action: swift
cost:
  spirituality: 3
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
text: 'Cost: 3 spirituality points Use: 1 Swift Action Limits: once per round Effect:
  By distorting the meaning of the targetaTMs words, actions, and intentions, you
  construct an order beneficial to you. Choose one of the following benefits to take
  effect: Distorted Language: You distort the message sent by any creature through
  speech or text, modifying it into a similar meaning. The similar meaning distorted
  by you becomes an actual rule, and extraordinary effects appear according to that
  meaning. Example: If you distort ano one else can get in and outa to ano one can
  get in or out,a this place is really inaccessible. Behavior Distortion: Usage and
  effect are the same as in Distorted Language,...'
```





- **Cost:** 3 **spirituality points**
- **Use:** 1 Swift Action
- **Limits:** once per round
- **Effect:** By distorting the meaning of the target's words, actions, and intentions, you construct an order beneficial to you. Choose one of the following benefits to take effect:

1. **Distorted Language:** You distort the message sent by any creature through speech or text, modifying it into a similar meaning. The similar meaning distorted by you becomes an actual rule, and extraordinary effects appear according to that meaning.
   - Example: If you distort "no one else can get in and out" to "no one can get in or out," this place is really inaccessible.
2. **Behavior Distortion:** Usage and effect are the same as in Distorted Language, except you distort the meaning of other people's behavior instead of their language.
   - Example: Running away is a kind of behavior; you can distort "running away" into "running in circles in place" when that behavior is executed.
   - Example note: Escaping and escaping in circles in place are both escapes, but escaping in circles in place obviously cannot achieve the real purpose of escaping.
   - **Special:** (Behavior Distortion only) The behavior of an object is also regarded as behavior. For example, you can distort a bullet from hitting you to hit the beer bottle next to you; distort the object blocking you to block the soil next to you; or [[Twisted Melee Attack]].
3. **Distorted Intentions:** You distort intentions existing in other people's minds into similar meanings (for example, distorting the intention of intercepting separately into separate actions). The distorted intentions disappear after 1 minute once the target perceives something wrong.

- **Further clarification on Distortion:**
  1. The essence of Distortion can be understood as an evolved version of [[Distortion Guidance]]. Compared with Sequence 9's Distortion Guidance, Sequence 6's Distortion constructs a practical and inviolable mystical rule.
  2. For example, closing a door can become a sealed room-isolating internal and external sounds and making it impossible to get out-changing "prohibit others from entering and exiting" into "prohibit anyone from entering and exiting," from a simple guide into a truly mystical effect (approximate law).
  3. As long as the meaning is similar, even rules with mystic meaning can produce effects (for example, sound isolation from outside). This is extremely powerful and a major development.
  - It is up to the **GM** to decide whether a "similar meaning" twist makes sense based on the rules above.
  - **Special:** In some cases, one twisting ability can affect multiple targets (for example, multiple targets performing the same action; multiple targets having the same intention; or multiple attacks selecting the same target). In this case, 1 warp affects all the same targets.

- **To get rid of the distortion effect:**
  1. **Distorted Language:** To get rid of distorted language, you must first take action to violate the distorted rules, and then choose your own arbitrary method to fight against the Corrupted Baron's "law bonus + inspiration + will" as the **Difficulty Value**.
     - Example: To break a "blocked room," use brute force to break through: you need to reach the door and use strength identification to fight; or use an extraordinary ability and the corresponding skill to fight. Because the distorted rules already exist objectively, attacking the distorter is meaningless.
     - If the distorted language is spoken by someone other than the Corrupted Baron, then among the above three attributes that determine the Difficulty Value, the will attribute changes to the will of the language owner. Only when the language owner tries to break the rules can you only use the will test to break through (and you still need to start by taking actions to violate the rules).
  2. **Distorted Behavior:** The effect of distorted behavior lasts for 1 round. You can try to break through once per round, but because the master of the behavior is yourself (as in the "language owner" case of Distorted Language), the attributes and breakthrough identification depend on your own will.
     - **Special:** If you distort an object (such as a bullet), the one who fired it cannot determine the will of the bullet. The distorted subject is not a living thing, so you cannot break through unless you can control the bullet.
  3. **Distorted Intentions:** Distorted behavior makes the distorted target noticeably aware it is doing something it does not want to do; distorted intention makes it difficult for the distorted target to perceive this.
     - Unless the distorted intention is reminded by others or the target obtains information, it cannot be actively broken through within 1 minute.
     - Premise: the corresponding intentions do exist. In some cases, a [[Psychological Appraisal]] check (Difficulty Value 20) may be required to confirm others' intentions. If the Corrupted Baron can confirm the intentions of the other party, this is not necessary.

### Corrosion

```yaml ability
id: black-emperor-seq-06-corrosion
name: Corrosion
pathway: black-emperor
sequence: 6
status: canonical
type: toggle
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: indiscriminately affects all creatures within 10 meters of you as the center.
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling:
- when: maintained_for_additional_minutes
  changes:
    effect_note: Corrosion continues to trigger every minute while upkeep is paid.
tags:
- ritual
text: 'Use: 1 Swift Action Cost: 1 spirituality point per minute Targeting and range:
  indiscriminately affects all creatures within 10 meters of you as the center. Effect:
  Active: Triggered every 1 minute. You choose the current behavior and intention
  of a creature in range and distort it into a similar meaning that develops in the
  direction of darkness, greed, and conspiracy. Passive: When a creature stays in
  the range for 1 minute, it takes effect. Whenever they notice someone or something
  they care about (such as coveted [[Extraordinary Items]] or people they want to
  hunt), they immediately suffer an Active effect; greed appears, and self-assertion.
  Example: Compared with violence and coercio...'
```





- **Use:** 1 Swift Action
- **Cost:** 1 **spirituality point** per minute
- **Targeting and range:** indiscriminately affects all creatures within 10 meters of you as the center.
- **Effect:**
  1. **Active:** Triggered every 1 minute. You choose the current behavior and intention of a creature in range and distort it into a similar meaning that develops in the direction of darkness, greed, and conspiracy.
  2. **Passive:** When a creature stays in the range for 1 minute, it takes effect. Whenever they notice someone or something they care about (such as coveted [[Extraordinary Items]] or people they want to hunt), they immediately suffer an Active effect; greed appears, and self-assertion.

> **GM Note:** Because distortion channeling is essentially twisting to a similar meaning, even if it becomes dark and greedy, the corrupted creature will not deviate too much from its own nature. When the passive effect affects teammates, the distortion should be decided by the GM.

- Example: Compared with violence and coercion, euphemistic and gentle people are more likely to spend money beyond their ability to do things recklessly (closer to mutilating themselves or defrauding), while violent people are more likely to achieve all this through violence.

- **Limits:** As described in this section's prose.


### Multiple Targets

```yaml ability
id: black-emperor-seq-06-multiple-targets
name: Multiple Targets
pathway: black-emperor
sequence: 6
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: self
duration: persistent
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Target-side Spiritual Intuition checks are mapped for detecting distortion at application time.
scaling:
- when: distorted_behavior_mode
  changes:
    effect_note: Distorted behavior duration is reduced to 1 round.
- when: target_sequence_higher_than_1
  changes:
    effect_note: Corruption effect resolves at Warp Channeling strength.
tags:
- ritual
- detection
- mobility
text: 'Distorted Language: It can affect multiple targets. At the moment of distortion,
  each target can use a successful [[Spiritual Intuition]] identification to notice
  the rule change and roughly identify which rule is wrong. Detection does not remove
  the distortion; removal still follows the Distorted Language breakthrough procedure
  above. Distorted Behavior: Distorted behavior can only be in effect for 1 round
  instead of 1 minute. Distortion Intent: The moment you are distorted, you can immediately
  detect something is wrong with a successful [[Spiritual Intuition]] check. Corruption:
  The effect on targets higher than Sequence 1 is equal to Warp Channeling. (For Spiritual
  Intuition, see [[Spe...'
```





- **Distorted Language:** It can affect multiple targets. At the moment of distortion, each target can use a successful [[Spiritual Intuition]] identification to notice the rule change and roughly identify which rule is wrong. Detection does not remove the distortion; removal still follows the Distorted Language breakthrough procedure above.
- **Distorted Behavior:** Distorted behavior can only be in effect for 1 round instead of 1 minute.
- **Distortion Intent:** The moment you are distorted, you can immediately detect something is wrong with a successful [[Spiritual Intuition]] check.
- **Corruption:** The effect on targets higher than Sequence 1 is equal to Warp Channeling.

- (For Spiritual Intuition, see [[Special Actions]].)

- **Effect:** Multiple Targets resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
