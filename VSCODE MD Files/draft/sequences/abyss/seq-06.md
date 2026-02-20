---
title: 'Sequence 6: Devil'
id: abyss-seq-06
tags:
- pathway:abyss
- sequence:6
---





# Abyss Pathway: Sequence 6

## Devil

A **Beyonder** at this **Sequence** can manifest a demon-like form—often growing to nearly 3 meters tall—with major boosts to combat capability and a heightened risk of losing control.

> **Lore:** Different people may imagine demons differently; the appearance described here is only a reference.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Agility (DEX) +1, Constitution +2, Intuition (INT) +1
- **Growth:** Sequence 9 potion skills can be grown to proficiency; mysticism can be grown to erudition.

### Dehumanization

```yaml ability
id: abyss-seq-06-dehumanization
name: Dehumanization
pathway: abyss
sequence: 6
type: active
action: cast
cost:
  sanity: 3
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- debuff
text: 'Effect: Your humanity and emotions have been almost completely wiped out. Effect
  (upgrade): On the basis of Sequence 8 Dehumanization, you will no longer fall into
  states of [[charm]], [[fear]], [[anger]], etc. These states can no longer have any
  effect on you. Sanity / Rationality: Every time you make a [[Sanity / Rationality
  Loss]], the sanity loss check is +4 disadvantageous, and the maximum loss limit
  for the success and failure of the sanity check is doubled. Example: a sanity loss
  of 1d2/1d4 becomes 1d4/1d8. (Sanity / Rationality loss of class 0/1 becomes 1/1d2;
  1/1d3 sanity loss becomes 1d2/1d6, etc.) Special: Emotional states created by one
  person higher than you have half the eff...'
```




- **Effect:** Your humanity and emotions have been almost completely wiped out.
- **Effect (upgrade):** On the basis of Sequence 8 Dehumanization, you will no longer fall into states of [[charm]], [[fear]], [[anger]], etc. These states can no longer have any effect on you.
- **Sanity / Rationality:** Every time you make a [[Sanity / Rationality Loss]], the **sanity loss check** is **+4 disadvantageous**, and the maximum loss limit for the success and failure of the **sanity check** is doubled.  
  - Example: a sanity loss of **1d2/1d4** becomes **1d4/1d8**.  
  - (Sanity / Rationality loss of class **0/1** becomes **1/1d2**; **1/1d3** sanity loss becomes **1d2/1d6**, etc.)
- **Special:** Emotional states created by one person higher than you have half the effect on you, and two persons higher than normal.
- **Limits:** This is a potion benefit that cannot be recorded or stolen.

### Demonization

```yaml ability
id: abyss-seq-06-demonization
name: Demonization
pathway: abyss
sequence: 6
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- control
- offense
text: 'Cost: 1 Swift Action. Sanity / Rationality: Perform an SC (1/1d3). Effect:
  According to your blood, race, and race, you burn your reason and become a demon
  dominated by killing. You immediately take the form of a demon of your race, ethnicity,
  and custom image. This image should be strongly associated with your previously
  custom demon-like spell. You can choose the classic demon image with goat horns,
  or you can choose various grotesque appearances from mythology. These demon images
  represent part of your abilities. For example, some demons may turn into water bodies
  on the basis of being able to control fire, and some may control thunder. Demonized
  state benefits: The demon form will bec...'
```




- **Cost:** 1 Swift Action.
- **Sanity / Rationality:** Perform an **SC (1/1d3)**.
- **Effect:** According to your blood, race, and race, you burn your reason and become a demon dominated by killing. You immediately take the form of a demon of your race, ethnicity, and custom image. This image should be strongly associated with your previously custom demon-like spell.
  - You can choose the classic demon image with goat horns, or you can choose various grotesque appearances from mythology.
  - These demon images represent part of your abilities. For example, some demons may turn into water bodies on the basis of being able to control fire, and some may control thunder.
- **Demonized state benefits:** The demon form will become huge, making you nearly 3 meters tall, and at the same time, you get the following benefits:
  - **Demonized state:** Your strength +2, agility +2, constitution +2, gain 10 extra health, become a [[fallen creature]].
  - At the moment of demonization, you break free from physical and spiritual shackles (e.g., torture, awe, marionette), reducing their damage dice by **one die size**.
  - At the moment of demonization, you break free from physical and spiritual shackles (e.g., torture, awe, marionette), reducing their damage dice by **one die size**.
  - **Size rules:** You are treated as a **Large** creature:
    - With melee damage increased by **1d3** against **Medium** creatures.
    - Attack range halved.
    - **Medium** creatures gain **+2** on attack rolls against you.
- **Ending demonization:** Removing the demonized state requires a Full-Round Action to adjust.
- **Aftereffects:** Ordinary demonization may burst your clothes.

- **Limits:** As described in this section's prose.


### Arrogance: Flaming Horns

```yaml ability
id: abyss-seq-06-arrogance-flaming-horns
name: 'Arrogance: Flaming Horns'
pathway: abyss
sequence: 6
type: active
action: cast
cost:
  spirituality: 4
roll: null
opposed_by: willpower_defense
range: Choose 1 target within the field of vision.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- defense
text: 'Effect: The goat horns on the top of your head are curved and protruding, covered
  with countless mysterious patterns. Limits: The image of the Flaming Horn can be
  customized, but the following content can only be used after reaching [[Sequence
  5]]: Cost: 1 Casting Action; consume 2 spirituality points. Targeting and range:
  Choose 1 target within the field of vision. Check: Intuition (INT) against will
  defense. Effect: You burn the goat horns on your head, and forcefully impact the
  enemy''s spirit. After the identification is successful, based on the content of
  the catalyzed emotion, you give the other party an emotion that has not been catalyzed,
  which lasts until the end of the encounter,...'
```




- **Effect:** The goat horns on the top of your head are curved and protruding, covered with countless mysterious patterns.
- **Limits:** The image of the Flaming Horn can be customized, but the following content can only be used after reaching [[Sequence 5]]:
  - **Cost:** 1 Casting Action; consume 2 spirituality points.
  - **Targeting and range:** Choose 1 target within the field of vision.
  - **Check:** Intuition (INT) against will defense.
  - **Effect:** You burn the goat horns on your head, and forcefully impact the enemy's spirit. After the identification is successful, based on the content of the catalyzed emotion, you give the other party an emotion that has not been catalyzed, which lasts until the end of the encounter, so that the emotion can be catalyzed and detonated later.
    - If the target spends 1 cast/move to meditate, the duration changes to end after your next turn.
    - The specific emotion is decided by the devil himself, but just like the content of the catalyzed emotion, this emotion must be reasonable and in line with the situation. For example, if the target must fight you quickly, then you can make him feel uneasy because he is worried about the arrival of reinforcements.
  - **Special:** If the ability to control desire is lost, the ability will also disappear (this is a branch of controlling desire). [[control desire]]

### Fallen Wings

```yaml ability
id: abyss-seq-06-fallen-wings
name: Fallen Wings
pathway: abyss
sequence: 6
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: physical_defense
range: Each fireball is identified individually, and you can choose different targets
  or all the same targets.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- mobility
- debuff
- defense
- offense
text: 'Effect: There are a pair of bat-like giant wings spread out behind you. The
  image of the wings can be customized, and you can fly in the air at the speed of
  2 times your movement power from now on. Special (Brimstone fireballs): Cost: 1
  Casting Action. Each fireball consumes 1 spirituality point. Effect: Your giant
  wings spread out, creating light blue brimstone fireballs one after another. The
  number of fireballs you can launch at one time is equal to your Intuition (INT).
  Targeting and range: Each fireball is identified individually, and you can choose
  different targets or all the same targets. Check: Occult against physical defense.
  Damage: Each fireball causes 3d6 fire and 1d6 poison...'
```




- **Effect:** There are a pair of bat-like giant wings spread out behind you. The image of the wings can be customized, and you can fly in the air at the speed of 2 times your movement power from now on.
- **Special (Brimstone fireballs):**
  - **Cost:** 1 Casting Action. Each fireball consumes 1 spirituality point.
  - **Effect:** Your giant wings spread out, creating light blue brimstone fireballs one after another. The number of fireballs you can launch at one time is equal to your Intuition (INT).
  - **Targeting and range:** Each fireball is identified individually, and you can choose different targets or all the same targets.
  - **Check:** Occult against physical defense.
  - **Damage:** Each fireball causes **3d6** fire and **1d6** poison damage.
  - **Area/Explosion:** The brimstone fireball will create an explosion, and two mobs standing next to each other are considered the same target.
  - **Limits (same target):** If the same target is identified consecutively, starting from the second fireball, the mysticism assessment will be **-4 disadvantageous**, the third time **-6**, and the fourth fireball will fail by default.
  - **Calculation note:** For ease of calculation, each fireball makes one appraisal against the Physical Defense of its selected targets.

  - (Because the third fireball fails by default, that is, a maximum of 3 identifications can be made, instead of 8–12 identifications.)

- **Limits:** As described in this section's prose.


### Magic Scale Armor

```yaml ability
id: abyss-seq-06-magic-scale-armor
name: Magic Scale Armor
pathway: abyss
sequence: 6
type: active
action: full-round
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- defense
- offense
text: 'Effect: You seem to be wearing a thick and hard armor, and the blood and flesh
  are also extremely elastic and resistant. 1) This is regarded as a kind of skin
  armor. The specific image can be customized, but it usually looks bleak, dark, and
  evil. 2) You gain 5 points of armor and 8 points of damage reduction. If the armor
  is damaged, it can be repaired with 1 Full-Round Action.'
```




- **Effect:** You seem to be wearing a thick and hard armor, and the blood and flesh are also extremely elastic and resistant.
- 1) This is regarded as a kind of skin armor. The specific image can be customized, but it usually looks bleak, dark, and evil.
- 2) You gain **5** points of armor and **8** points of damage reduction. If the armor is damaged, it can be repaired with **1** Full-Round Action.

- **Limits:** As described in this section's prose.


### Body of the Abyss

```yaml ability
id: abyss-seq-06-body-of-the-abyss
name: Body of the Abyss
pathway: abyss
sequence: 6
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
- debuff
- defense
- offense
text: 'Effect: You are immune to most poisons, and you are not afraid of curses and
  flames to a certain extent. Effect: You automatically gain [[magma attachment]].
  You gain 10 poison resistance and 5 curse resistance. Fast dodge: You retain full
  agility and dodge defenses against guns but not light/lightning, but you still cannot
  dodge those extraordinary abilities that cannot be dodged. Extra: When you face
  non-gun-like high-speed attacks, such as [[Red Priest''s Flame]] or [[Witch''s Ice
  Lance]]: For any attack whose described speed does not reach the level of a gun,
  unless it must be hit, not only will you not lose your agility and dodge defense,
  but you will also get an additional dodge bonus...'
```




- **Effect:** You are immune to most poisons, and you are not afraid of curses and flames to a certain extent.
- **Effect:** You automatically gain [[magma attachment]]. You gain **10** poison resistance and **5** curse resistance.
- **Fast dodge:** You retain full agility and dodge defenses against guns but not light/lightning, but you still cannot dodge those extraordinary abilities that cannot be dodged.
- **Extra:** When you face non-gun-like high-speed attacks, such as [[Red Priest's Flame]] or [[Witch's Ice Lance]]:
  - For any attack whose described speed does not reach the level of a gun, unless it must be hit, not only will you not lose your agility and dodge defense, but you will also get an additional dodge bonus.
  - Note: When facing firearms, your extra evasion is invalid, but the original full agility and evasion defenses are still retained.
- **Demonized state:** Gain a rank in the bonus dodge skill.
- **Limits:** (The body of the abyss is an explanation that comes with a demon, which cannot be stolen or recorded, and is just listed separately.)

### Demonic Spells

```yaml ability
id: abyss-seq-06-demonic-spells
name: Demonic Spells
pathway: abyss
sequence: 6
type: active
action: swift
cost: {}
roll: null
opposed_by: willpower_defense
range: Choose a target within a range of 8 meters.
target: designated target(s)
duration: Starting on the second round and maintaining it requires **2** spirituality
  points per round.
scaling: []
tags:
- ritual
- debuff
- defense
- offense
text: 'Your demonic spells are already true demonic spells, and are in part superior
  versions of your former abilities. You get the following demonic spells (all of
  which you now get if you didn''t have their predecessors before). #### The filthy
  word "death" Cost: 1 Swift Action; consume 2 points of spirituality; once per round,
  you can only choose one foul language to use in one round. Targeting and range:
  Choose a target within a range of 8 meters. Check: Intuition (INT) -4 against will
  defense. Damage: On a success, cause 2d6+5 curse damage. This is regarded as a vital
  blow to the heart, and you can get additional damage from the critical blow. ####
  The foul language "slow" Cost: 1 Swift Acti...'
```




Your demonic spells are already true demonic spells, and are in part superior versions of your former abilities. You get the following demonic spells (all of which you now get if you didn't have their predecessors before).

#### The filthy word "death"

- **Cost:** 1 Swift Action; consume 2 points of spirituality; once per round, you can only choose one foul language to use in one round.
- **Targeting and range:** Choose a target within a range of 8 meters.
- **Check:** Intuition (INT) **-4** against will defense.
- **Damage:** On a success, cause **2d6+5** curse damage. This is regarded as a vital blow to the heart, and you can get additional damage from the critical blow.

#### The foul language "slow"

- **Cost:** 1 Swift Action; consume 2 points of spirituality; once per round, you can only choose one foul language to use in one round.
- **Targeting and range:** Within 8 meters of you as the center, regardless of enemy or friend.
- **Check:** Intuition (INT) **-4** is disadvantageous against the will defense of all creatures.
- **Effect:** Resulting in a state of [[Shock]] for 1 round.

#### Foul language "Degenerate"

- **Cost:** 1 Swift Action; consume 2 points of spirituality; once per round, you can only choose one foul language to use in one round.
- **Targeting and range:** Choose an area within 8 meters, and choose a target as the main body.
- **Check:** Intuition (INT) **-4** is disadvantageous against the main body's will defense, and the rest of the targets are against the physical defense. Use the result of one identification to compare the two defenses at the same time. Multiple identifications are not allowed.
- **Effect:** If the check is successful, you deal **3d6** curse damage in an area, ignoring **5** points of curse resistance.
- **Limits/Notes:** (The three filthy words are not the same Extraordinary ability; they can only be recorded and stolen in stages, and "degenerate" into the [[Pollution of the Abyss]].)

#### Manipulate the poisonous flame

- **Cost:** 1 Casting Action; cost 2 spirituality points.
- **Targeting and range:** Choose 1 target.
- **Check:** Occult against physical defenses.
- **Damage:** Deal **2d6** fire and **2d6** poison damage.
- **Aftereffects:** A creature traumatized by poison damage takes **1d6** points of poison damage each round until a Medicine check (Difficulty Value **15**) is made. Difficulty Value
- **Special:** This pair is twice as effective on plants, cobwebs, and silk hair.

#### Toxic steam

- **Limits:** Demonized only; this is the demonized version of Poison Flame.
- **Cost:** 1 spellcasting action; consume 2 spirituality points.
- **Targeting and range:** Selects targets in the current entire area, regardless of enemy or friend.
- **Check:** Mysticism against physical defense.
- **Damage:** Cause **3d6** poison and **1d6** fire damage.
- **Aftereffects:** Beginning each subsequent round, a creature traumatized by poison damage takes **1d6** points of poison damage each round.
  - If the current area is not sealed and the steam does not escape, the poison damage at the beginning of each round is changed to **2d6**.
- **Cleanup:** Cleaning up this toxin requires a 20-difficulty Medicine check (Difficulty Value **20**).

#### Sword of Magma

- **Cost:** 1 Attack Action; consume 3 points of spirituality.
- **Effect:** You are permeated with a depraved breath. You condense a flaming giant sword composed of red magma and light blue flame, with extremely high attack power and shaped like a knife.
- **Damage:** The magma sword deals **3d6+5+strength** damage dice of fire damage.
- **Duration:** Starting on the second round and maintaining it requires **2** spirituality points per round.

#### Malicious perception

- **Effect:** You perceive the harm that can be fatal to you after a short period of time, and you take practical actions, and grasp the specific source of the danger and who it comes from, but you don’t know what to do further details.
- **Range:** For every 1 point of Intuition (INT) you have, the range of malicious perception is 1 km.
- **Timing:** Your Intuition (INT) also represents the time you can detect maliciousness:
  - **6 Intuition (INT):** detect maliciousness within 1 km within 20 minutes, and detect maliciousness beyond 1 km after 24 hours
  - **7 Intuition (INT):** detect malice within 1 km within 15 minutes, and detect malice beyond 1 km after 18 hours
  - **8 Intuition (INT):** detect malice within 1 km within 10 minutes, and detect malice beyond 1 km after 12 hours
  - **9 Intuition (INT):** detect malice within 1 km after 5 minutes, detect malice beyond 1 km after 6 hours
  - **10 Intuition (INT):** detect malice within 1 km after 1 minute, and detect malice beyond 1 km after 4 hours
  - **11 Intuition (INT):** detect malice within 1 km after half a minute, and detect malice beyond 1 km after 2 hours
  - **Higher Intuition (INT):** Immediately detect malice within 1 kilometer, and detect malice beyond 1 kilometer after 1 hour
- **Notes:** (Because malicious perception is a passive skill, it may not be remembered by the host at any time. Extraordinary people can apply to actively trigger it.)  

#### Brimstone Fireball

- **Cost:** 1 Casting Action; consume 1 spirituality point.
- **Targeting and range:** Choose 1 or more targets.
- **Damage:** Each fireball will cause **3d6** fire and **1d6** poison damage.
- **Limits (non-demonized):** Non-demonized state can create up to **3** fireballs; refer to the demonized Fallen Wings for identification.
- **Special:** Two targets standing next to each other are regarded as the same target, and demonizing without this ability will not be able to create brimstone fireballs.

#### Flame Cage

- **Cost:** 1 Swift Action; 1 time per round; consume 2 spiritual points.
- **Effect:** You create a flame cage in the palm of your hand, resisting a long-range attack with a medium that you recognize, which includes the following content:
  - Bullets, air bombs, ice-throwing guns, and musket-throwing guns
  - Excluding beams of light on Path of the Sun, lightning and wind blades on Path of Storms
- **Special:** If this attack is enchanted with a divine power 1 higher than yours, it cannot be blocked.

#### Volcanic eruption

- **Cost:** 1 Full-Round Action.
- **Limits:** Only available in the demonized state.
- **Cost (health):** You expend your health; each 5 hit points counts as **1d10** damage dice.
- **Targeting and range:** All creatures within a 10-meter radius.
- **Check:** **+20** disaster check against physical defense, or half the damage on a failed check.
- **Damage:** Burst inflicting fire damage (based on the health-to-dice conversion above).
- **Special (active volcano):** If you find an active volcano that is about to erupt, you can jump into the crater and use the eruption ability to cause **50** points of fire damage at one time, causing it to erupt immediately (the amount of damage must be caused at one time).
  - This will cause you to suffer half of the damage caused by the volcanic eruption ability, which may cause you to die on the spot.
  - The effect of this will refer to the high-sequence disaster of the Tyrant Path.
- **Sequence 4 note:** Sequence 4: You can cause a volcanic eruption without taking self-damage; you still expend the ability and consume life points.
- **Sequence 4 note:** Sequence 4: You can cause a volcanic eruption without taking self-damage; you still expend the ability and consume life points.

#### Others

- **Effect:** 1 Sequence 6 version of a custom demon-like spell you made before. [[custom demon-like spell]]
- **Notes:**
  - (You can still use incomplete demonic spells before Sequence 6. The order of demonic spells is the same as that of Sequence 8's demon-like spells, so you can tell which ability is the upper version of which demon-like spell.)
  - (If you are a Sequence 7 and strengthening abilities through the sacrificial ceremony: you can only evolve into one of the corrupted words for hurting people; these cannot be suppressed by silence and still take effect. Strengthen the acquired ability)
