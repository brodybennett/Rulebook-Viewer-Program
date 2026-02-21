---
title: 'Sequence 6: Prometheus'
id: error-seq-06
tags:
- pathway:error
- sequence:6
---






# Error Pathway: Sequence 6

Steal an opponent’s extraordinary ability for a short time and use it.

## Prometheus

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2, **Constitution** +1, **Agility (DEX)** +1
- Your deception, persuasion, speech skills, pleasing mysticism, and clever hands can be quickly upgraded to erudition.

### Ritual Camouflage

```yaml ability
id: error-seq-06-ritual-camouflage
name: Ritual Camouflage
pathway: error
sequence: 6
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
- ritual
text: 'Effect: You can pretend to be a believer of other gods in ritual magic, deceiving
  the gods automatic response. Limits: Although you may pray in ritual magic to gods
  you do not believe in as usual, the god itself can see through your disguise.'
```





- **Effect:** You can pretend to be a believer of other gods in ritual magic, deceiving the gods’ automatic response.
- **Limits:** Although you may pray in ritual magic to gods you do not believe in “as usual,” the god itself can see through your disguise.

### Stealing Tinder

```yaml ability
id: error-seq-06-stealing-tinder
name: Stealing Tinder
pathway: error
sequence: 6
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.occult_identification
opposed_by: difficulty_value
range: Choose 1 **target** within 50 meters
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.occult_identification
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Skill Identification check resolves the base DV 20 theft attempt and its modifiers.
scaling:
- when: sequence_5_or_higher
  changes:
    range: Choose 1 **target** within 100 meters
    effect_note: Range increases to 100 meters at Sequence 5.
- when: target_known_clue
  changes:
    effect_note: Each qualifying clue about the target grants +2 favorable to the identification.
tags:
- ritual
- mobility
- buff
text: 'You put your fingers together, twist your wrist, and briefly steal someone
  elses extraordinary ability for your own use. Use: 1 Casting Action Cost: 3 spirituality
  points Targeting and range: Choose 1 target within 50 meters At [[Sequence 5]],
  stealing range increases to 100 meters. Check: Conduct 1 Skill Identification check.
  Before stealing, choose 1 target active or passive ability you know to steal; otherwise
  the result is completely random. Difficulty Value: Base Difficulty Value 20, modified
  by the following conditions:'
```





You put your fingers together, twist your wrist, and briefly steal someone else’s extraordinary ability for your own use.

- **Use:** 1 **Casting Action**
- **Cost:** 3 **spirituality points**
- **Targeting and range:** Choose 1 **target** within 50 meters
  - At [[Sequence 5]], stealing range increases to 100 meters.
- **Check:** Conduct 1 **Skill Identification** check.
  - Before stealing, choose 1 target active or passive ability you know to steal; otherwise the result is completely random.
- **Difficulty Value:** Base **Difficulty Value** 20, modified by the following conditions:
  - ① The target is higher than you by 1 Sequence: Difficulty Value +5. If the identification fails, you will not be able to obtain any abilities.
  - ② For every character higher than yours: Difficulty Value +5. If the identification fails, you will not be able to obtain any abilities.
  - ③ The target is at the same level as you: the initial Difficulty Value is 20. If the identification fails, you will not be able to obtain any abilities.
  - ④ Every time the target is lower than yours by 1 Sequence: Difficulty Value -5. If the identification fails, a random ability will be obtained.
  - ⑤ The target is lower than you by 1 character: Difficulty Value -5. If the identification fails, a random ability will be obtained.
- **Special:** If you want to steal the ability you specified, the identification result must be higher than the required Difficulty Value by 5 points. Otherwise, the ability will still be random even if the identification is successful.

#### Gaining the Stolen Ability

After successful theft, the stealer and the stolen follow the following rules:

- ① The Fire Thief can use the stolen ability freely for 10 minutes. After 10 minutes, the ability will disappear. It must be 12 hours before the same target can be stolen again, and the original extraordinary ability appraisal is replaced by this skill appraisal.
- ② At the moment when the identification is successful, the stolen person immediately loses the corresponding ability and must wait for 12 hours before recovering.
- ③ As long as the stolen person is still conscious, once they lose their extraordinary ability, they will immediately notice the loss of ability.
- ④ The Fire Thief’s ability can only be stolen from the same target once every 12 hours. This means if there are multiple extraordinary beings present, the Fire Thief can steal the ability multiple times, and multiple extraordinary people do not belong to the same target.
- ⑤ When stealing does not achieve the desired result and needs to obtain abilities randomly, perform 1dX where X is the target's Sequence number. Then check the number of abilities that can be stolen in the corresponding Sequence according to the Sequence level obtained by the die, and then perform random.

#### Additional Bonus

When the Fire Thief steals an ability, the more they know the target, the easier it is to steal what they want; the more ignorant they are, the closer it is to randomness. Every time one of the following conditions is met, the identification of the stolen fire will be +2 favorable:

- ① Know the target’s real name or respected name (it needs to be complete enough; the real name must contain first and last name, unless the person does not have a last name).
- ② Know the real experience of the target (you need to know at least one rough life history; if it is detailed to the point where you can tell almost every detail, then +2 is beneficial).
- ③ Know the Sequence Pathway of the target (you need to know which Pathway the target belongs to; only knowing the knowledge of the corresponding Pathway cannot get this bonus).
- ④ Know the weakness and important things of the target (if the weaknesses and important things in the past are not now, this bonus is +1).

#### Special Stealing Cases

- ① Manipulating the thread of the spiritual body: the [[Master of Puppet]] can no longer continue to be marionetted, but it does not affect them maintaining the progress of manipulating the existing thread of the spiritual body, and manipulating the puppet that has become their secret puppet; but the Fire Thief’s secret puppet will die after being unable to use abilities.
- ② [[Herding]]: The Fire Thief can herd while holding the ability, but after the ability maintenance time is over, if the Fire Thief does not take the initiative to expel the characteristic of grazing, it will immediately trigger a promotion appraisal for the Fire Thief, and may become an extraordinary person of the jump path.
- ③ [[Records]]: Stealing records will only make the recording officer unable to continue recording the ability, and will not affect the recording officer’s ability to release the recorded ability. If the ability in the record is higher than 1 character, it will suffer from [[Extra: Suppression of Personality]] when stealing.  
  Special: Even so, the Fire Thief can still use the recorded ability, and the recorded ability will disappear after the maintenance time.
- ④ [[Simulation]]: Stealing the simulation will only prevent the polymath from simulating the abilities that have not been mastered, and will not affect the capabilities that the polymath has mastered.  
  Special: Unlike a recorder, a Fire Thief who successfully simulates or interprets an ability retains the knowledge, although they may no longer be eligible to cast it.
- ⑤ Transformation ability: You can only steal one of the transformation abilities at a time. For example, you can steal the resentment, but the resentment still retains resentment scream and other abilities; demonization steals part of the demon traits (“semi-demonization”).
- ⑥ [[Flesh Magic]] / [[Faceless Man]]: If flesh magic or transformation can produce permanent physical changes, even if the ability maintenance time disappears, the changes brought about can still be maintained; but the growth and aging of the human body will still affect follow-up.
- ⑦ Strengthening/Buffing/Additional Effects: For example, the sacred contract of the [[Sun]]. This kind of strengthening, or an ability that has been used, can continue to be retained until the time when the ability takes effect is exceeded, even if the maintenance time of your stolen ability has disappeared.

— Other special thefts are decided by the GM according to the above cases.

- **Effect:** Stealing Tinder resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Tinder Vision

```yaml ability
id: error-seq-06-tinder-vision
name: Tinder Vision
pathway: error
sequence: 6
status: canonical
type: active
action: free
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
- ritual
- detection
text: 'You can see the light ball representing extraordinary ability; this is the
  preparation stage for Stealing Tinder. Use: As a free action, or when you are about
  to perform any Stealing Tinder, you trigger Tinder Vision. Effect: 1 You can see
  the light groups represented by extraordinary creatures, extraordinary characteristics,
  and extraordinary items. These light groups represent different extraordinary abilities
  and even spiritual pollution. 2 The process of casting Stealing Tinder is to let
  you see these light clusters, then hold one of these light clusters in your palm.
  You will immediately know the information you have obtained corresponding to the
  extraordinary ability, and use it acc...'
```





You can see the light ball representing extraordinary ability; this is the preparation stage for Stealing Tinder.

- **Use:** As a **free action**, or when you are about to perform any Stealing Tinder, you trigger Tinder Vision.
- **Effect:**
  - ① You can see the light groups represented by extraordinary creatures, extraordinary characteristics, and extraordinary items. These light groups represent different extraordinary abilities and even spiritual pollution.
  - ② The process of casting Stealing Tinder is to let you see these light clusters, then hold one of these light clusters in your palm. You will immediately know the information you have obtained corresponding to the extraordinary ability, and use it accordingly.
  - ③ According to this principle, Stealing Tinder can not only steal from extraordinary people, but also steal from extraordinary items and extraordinary abilities in extraordinary characteristics. It can also be used for 10 minutes and recovered after 12 hours.
  - ④ Mental pollution is also a kind of extraordinary ability. Therefore, you can steal the spiritual pollution in an out-of-control extraordinary characteristic, and you will immediately suffer a corresponding loss of sanity. If this exceeds your tolerance, you will lose control.
  - ⑤ Even if you can see these light clusters, you will not be able to know the corresponding meanings and extraordinary abilities of these light clusters until you thoroughly understand the target. You must make a separate **Identification** check to learn the meanings and abilities of the light clusters.
- **Limits:**
  - Tinder Vision cannot be seen through walls.
  - When stealing spiritual pollution, the corresponding sanity loss is equal to the Sequence level of the spiritual pollution.
  - If a certain spiritual pollution is caused by the existence of a higher level, then it will be changed to the corresponding level of sanity loss.
