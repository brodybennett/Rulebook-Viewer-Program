---
title: 'Sequence 7: Spirit Medium'
id: death-seq-07
tags:
- pathway:death
- sequence:7
---






# Death Pathway: Sequence 7

> **Lore:** You master mystical rituals related to spirits. You can directly communicate with natural spirits and wandering dead souls in the real world, use different spirits to realize various magics, and create supernatural phenomena.

> **GM Note:** Spiritism can be used on living creatures, but it carries danger.

## Spirit Medium

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +2
- Your **Occult** skills go up by one level.

### Communicating with the Dead

```yaml ability
id: death-seq-07-communicating-with-the-dead
name: Communicating with the Dead
pathway: death
sequence: 7
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.knowledge
opposed_by: willpower_defense
range: 100m
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: 5d6
  notes: check_roll maps remote spirit-link establishment versus Willpower Defense; effect_roll maps the typical count of nearby spirits available in range.
scaling: []
tags:
- social
text: You can directly communicate with natural spirits and wandering spirits in the
  real world, like ordinary people. If a dead person has appeared in an area, as long
  as their spirit has not been destroyed, you can see them near their death area,
  communicate directly, ask questions, and perform psychic communication. When communicating
  with undead, you may use social skills such as words, persuasion, pleasing, and
  intimidation as usual (including lying). You can also communicate with natural spirits
  that exist naturally and are related to the Spirit World, and learn local clues.
  In general, you can find at least 5d6 natural spirits or undead in an area within
  100 meters. The undead you can co...
```





You can directly communicate with natural spirits and wandering spirits in the real world, like ordinary people.

- If a dead person has appeared in an area, as long as their spirit has not been destroyed, you can see them near their death area, communicate directly, ask questions, and perform **psychic communication**.
- When communicating with undead, you may use social skills such as words, persuasion, pleasing, and intimidation as usual (including lying).
- You can also communicate with natural spirits that exist naturally and are related to the **Spirit World**, and learn local clues. In general, you can find at least 5d6 natural spirits or undead in an area within 100 meters.
- The undead you can communicate with do **not** include living corpses, water ghosts, skeletons, etc. They usually do not have real spirit bodies.
- **Cost/Action:** 1 **Casting Action**, consuming **3 spirituality points**. Without approaching, you can establish a psychic relationship with a spirit within your **field of vision**.
  - **Check:** Intuition (INT) + [[Knowledge of the Dead]] vs its **Willpower Defense**.
  - The connection is established only on a success.

> **GM Note:** "A psychic should actively communicate with all seeing spirits to achieve the effect of informants everywhere."

- **Effect:** Communicating with the Dead resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Psychic Communication with Living People

```yaml ability
id: death-seq-07-psychic-communication-with-living-people
name: Psychic Communication with Living People
pathway: death
sequence: 7
status: adapted
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: Choose 1 **helpless** target.
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: Involuntary communication can inflict sanity and rationality loss of 1/1d2; effect_roll captures the variable loss component.
scaling:
- when: voluntary_target_setup
  changes:
    effect_note: Requires about one minute of essential-oil setup before communication begins.
tags:
- ritual
text: 'A living personaTMs spirit can also be an object of psychic communication.
  There are two ways to communicate with a living personaTMs spirit: Involuntary target
  Cost/Action: 1 Casting Action; no spiritual consumption. Target: Choose 1 helpless
  target. Effect: You establish a psychic relationship and communicate as a normal
  psychic, but everyone can hear the other partyaTMs response. Helplessness may be
  achieved violently, and causes the channeled target to suffer a Sanity / Rationality
  loss of 1/1d2. Voluntary target'
```





A living person's spirit can also be an object of psychic communication.

There are two ways to communicate with a living person's spirit:

1. **Involuntary target**
   - **Cost/Action:** 1 Casting Action; no spiritual consumption.
   - **Target:** Choose 1 **helpless** target.
   - **Effect:** You establish a psychic relationship and communicate as a normal psychic, but everyone can hear the other party's response.
   - Helplessness may be achieved violently, and causes the channeled target to suffer a **Sanity / Rationality** loss of 1/1d2.

2. **Voluntary target**
   - **Duration/Setup:** For about 1 minute, affect the voluntary target.
   - **Materials/Method:** Use essential oils such as [[Amanda]] and [[Spiritual Eye]]; drip a few drops into the candle flame to make the psychic gradually fall into a state of confusion, then start psychic communication.
   - **Effect:** The rest of the effects are the same as involuntary target.
   - The single dose of essential oil is very small (only a few drops), so it will not be completely consumed.
   - Creatures who can wake up in dreams ignore this effect.

> **GM Note:** Psychic insanity targets cause you to suffer the same Sanity / Rationality loss as their source of insanity, possibly causing taint to spread. In this case, the insanity symptom is the same as if you were insane due to the Sanity / Rationality loss of the channeled target.

- **Limits:** As described in this section's prose.


### Spiritualism

```yaml ability
id: death-seq-07-spiritualism
name: Spiritualism
pathway: death
sequence: 7
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
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
- divination
- offense
text: 'You can use different spirits to achieve various magic. #### Danger Premonition
  Effect: The spirit you are currently in will remind you in time when you are about
  to encounter danger. Requirement: As long as there is a spirit body in the current
  area, whenever you are about to encounter a surprise attack/sneak attack, the local
  spirit body or Spirit World will tell you the corresponding information when such
  things are about to happen, so that you immediately know the next time you will
  encounter a surprise attack/sneak attack and its specific form. Passive: If someone
  intends to do harm to you and has already started to do something about it, the
  ubiquitous spirits who can see these will...'
```





You can use different spirits to achieve various magic.

#### Danger Premonition

- **Effect:** The spirit you are currently in will remind you in time when you are about to encounter danger.
- **Requirement:** As long as there is a spirit body in the current area, whenever you are about to encounter a surprise attack/sneak attack, the local spirit body or Spirit World will tell you the corresponding information when such things are about to happen, so that you immediately know the next time you will encounter a surprise attack/sneak attack and its specific form.
- **Passive:** If someone intends to do harm to you and has already started to do something about it, the ubiquitous spirits who can see these will immediately come and tell you about it (maybe through the Spirit World), but you can only get the information they have seen.
  - This generally ignores distance, but events more than one city away are normally only known at **noon** (once per day).

#### Regional Psychic

You can directly obtain information known to spirits within a certain range.

- **Cost/Action:** 1 Casting Action; consume 3 spirituality points.
- **Check:** Make a [[Knowledge of the Dead]] identification to communicate with the local spirit and get the message of this place.
  - When making this check, the relevant attribute is **Intuition (INT)**, not education.

**Results by Difficulty Value:**
- **Difficulty Value 15:** You know what kind of area the local area is, the general environment around it, and what things exist.
  - If you are in the Spirit World, you can use this to know the environment of the corresponding area in reality.
- **Difficulty Value 20:** You know the local customs, landforms, and what kind of clothes and looks the people here.
- **Difficulty Value 25:** You know more detailed information-what happened recently, and the detailed types of things.
- **Difficulty Value 30:** You know more detailed local information and have obtained relevant direct information, such as the location of the deceased.
- **Great success:** You know almost everything about the place, including the degree of danger here, the size of the degree.
- **Big failure:** The spirits gave you wrong information, possibly because events were disguised or their judgment was wrong.
- **Other psychics (Difficulty Value 25):** You specify a certain item of information to obtain, such as whether there is a specific thing here.

**Special:**
- If you ask the same thing within 24 hours, you will get the same result.
- Generally speaking, spirits can only know about what happened in one day on the next day, unless the place you ask is near the scene of the incident.
- Regional psychic covers 100 meters at a time. Spirits in a specific area may know unique information. In a city, if you ask spirits within different 100-meter ranges about the city's status, because the information is general, there is a high probability that you will get the same information.

#### Spiritual Body Assistance

- **Cost/Action:** 1 Casting Action; consumes 3 spirituality points; lasts 5 minutes.
- **Effect:** Summon 1 spirit body to possess you; you gain the following benefits:
  1. Within five minutes, you choose a skill to use at mastery level, even if you have not been trained in that skill. If you find a specific spirit with a higher skill level, you can designate it to possess you and use it with a higher skill level.
  2. **Cost/Action:** 1 **Full-Round Action** without consuming spirituality. With the help of your spirit body, you can reproduce information or a portrait you have seen at an extremely fast speed by writing and painting, provided that your memory is not affected by extraordinary factors.

#### Drive the Dead

You can communicate with and drive natural spirits, undead, and spirit creatures.

- **Cost/Action:** 1 Casting Action; consuming 3 spirituality points.
- **Effect:** You control 1 undead creature that has "awakened" by itself. This kind of undead creature does not have enough wisdom. Natural spirits and spirit bodies with certain wisdom follow the content below:
  1. **Premise:** You communicate with a spirit body. As long as the other party is willing, it will be regarded as a member of the spirit body that you can drive. The calculation represents your spirit strength.
  2. The spirits you can drive include natural spirits, undead, Spirit World creatures, and undead creatures, but you cannot actively summon undead creatures unless it is a "resurrected" living corpse, water ghost, etc., and it should have no owner or the owner is at least 1 rank/Sequence lower than you.
  3. If you drive undead without replenishment, they can act and fight for up to **24 hours**. After that, they can only be channeled and provide fragmented information; they completely dissipate after **72 hours**.
  4. To replenish an undead, allow it to attach itself to a creature to extract its spirituality and body temperature. For every point of spirituality extracted, the duration of the undead increases by 1 minute. Undead generally refers to resentful souls/evil spirits. Shadows do not have the ability to possess.

##### Driven Undead Templates

- **Undead:** spiritual beings transformed from emissaries who have not been properly buried and requiemed.

> **GM Note:** Undead creatures driven by you are not equal to [[Secret Puppets]] and may not necessarily share senses. You can use your thoughts to give them orders within 100 meters without moving, and they will complete the orders even if they leave the range.

**Shadow**
- 15 health
- 15 **Physical Defense** (5 points for agility and dodge)
- 10 Willpower Defense
- 5 points cold and curse resistance
- Ignores poison and physical damage
- **Attack Action:** 1d6 cold damage
- No more abilities; can perform special actions such as grapple.

**Wraith / Evil Spirit**
- 30 health
- 20 Physical Defense (10 points for agility and dodge)
- 10 Willpower Defense
- 10 points cold resistance
- 5 points curse resistance
- Ignores poison and physical damage
- **Attack Action:** 2d6 cold damage
- **Possession:** Has Wraith Possession, but does not include mirror jumping, etc. Its determination is due to the content of [[Alien Pathway - Sequence 5: Wraith]].

> **GM Note:** Different from resentful souls of different species: wild undead do not gain a series of abilities such as "advanced invisibility" because of their level; they can only cause cold damage. They can possess after a certain level; ordinary shadows do not even have the conditions for possession.

##### Living Corpse, Skeleton, Water Ghost

The following undead creatures can only be enslaved by naturally "awakened" individuals, or created by possessing resentful spirits/evil spirits on corpses. When the spirits dissipate, they return to the corpses. The latter cannot affect those who have been taught to requiem corpse.

**Living corpse**
- 15 health
- 15 Physical Defense (5 points for agility and dodge)
- Ignores the ability to resist physical and Will Defenses
- 5 points resistance to cold, curse, and poison
- **Attack:** 1d6 physical damage
- Like a normal person but with multiple rotting corpses
- (Against a Constitution Defense of 15 to do so if there is a disease that can affect a living corpse, such as [[Witch's Plague]].)

**Skeleton**
- 10 health
- 15 Physical Defense (5 points for agility and dodge)
- Ignores the ability to resist physical and Will Defenses
- 5 points cold, curse, and poison resistance
- **Attack:** 1d6 physical damage
- 10 points bluntness physical damage reduction from weapon strikes.

**Water ghost**
- 15 blood volume
- 15 Physical Defense (5 points for agility and dodge)
- Ignores the ability to resist physical and Willpower Defense
- 5 points cold, curse, and poison resistance
- **Attack:** 1d6 physical damage
- A body swelling and drowning "living corpse" in the water; can maintain normal mobility underwater.

##### Special Rules: Characteristics, Containment, and Existence Time

- Undead creatures usually do not have more extraordinary abilities unless they consume extraordinary characteristics.
- The way to consume characteristics of shadows/wraiths/evil spirits is to put them in the body and digest them a little bit. Undead creatures do not need potions because they are half mad.
- Only for spirit bodies: containing a feature can increase the upper limit of existence time, so that it will not dissipate after the existence time is exhausted.
  - For each Sequence level of tolerance, it can exist for 24 more hours.
  - It can exist permanently when reaching a demigod.
- If spiritual materials are contained instead of characteristics, the increase in corresponding existence time will only take effect once.
- Charms/spiritual materials/extraordinary items can still be used for 1 day = 1 minute of existence time.
- Items with extraordinary characteristics must be smashed back into characteristics to be effectively used through containment; otherwise they will suffer negative effects, and the spirit body will also follow the law of transfer path and lose control.
  - Transfer Path

##### Natural Spirits

- **Natural spirit:** a naturally produced spirit body combined with the Spirit World; not transformed from the dead; power comes from the Spirit World.

Natural spirits are different from undead: undead are transformed after the death of living things, while natural spirits are naturally born spirits because of the existence of the Spirit World.

Because the description of natural spirits is lacking, you can create a natural spirit in the following way:

1. Roll 2d10 to determine a natural spirit's blood volume, Physical Defense, and Willpower Defense.
   - The agility and dodge in Physical Defense are the values after Physical Defense -10.
2. Customize the ability of the natural spirit or randomize its ability:
   - Roll 1d2 to randomly generate the following abilities:
     1. **Cost/Action:** 1 Casting Action. **Effect:** Deal 1d6 damage. Roll 1d4 to determine whether it is fire/poison/cold/spiritual damage. This does not mean it can switch its own attributes; you decide what kind of damage this natural spirit can *only* cause.
     2. **Cost/Action:** 1 Casting Action. **Effect:** Restore 1d3 hit points to a living creature (not a dead object).

A more common natural spirit only has the above two abilities. This is the most general template; you may also create a natural spirit with a unique extraordinary ability.

**Examples (more powerful natural spirits):**

**Dread Banshee**
- 50 health
- 25 Physical Defense (agility and dodge 10)
- 20 Willpower Defense
- Appearance: beautiful face, rotten body, huge eagle wings.
- **Attack Action:** Use your Intuition (INT) instead of its check against Physical Defense, dealing 3d6 mental damage. A successfully attacked target:
  - Temporarily -1 Will attribute
  - Is in a state of fear for 1 round.

**Goddess of the Lake**
- 60 health
- 20 Physical Defense (agility and dodge 10)
- 15 Willpower Defense
- Appearance: accompanied by mist-shrouded lake water; central ripples; a beautiful yet illusory figure.
- **Cost/Action:** 1 Casting Action. **Target:** Choose 1 target. **Effect:** Choose one benefit:
  1. Within 1 round, the next skill and attribute appraisal +2 will be beneficial.
  2. For 1 round, one of the three defenses gets a +2 bonus.
  3. Within 1 round, gain 5 points of extra life, or extra spirituality (only one item can be obtained at the same time; cannot be superimposed).
  4. Within 1 round, the mental influence (fear, anger, etc., other than shock) suffered by the target is halved; forced movement is halved (round up) on the first application and completely removed after the second application of the ability. Mental influence includes temporary madness but not other crazy.

> **GM Note:** Other possible natural spirits vary widely (e.g., land stealth, sensory sharing, etc.). More natural spirits are written by you and handed over to the GM for review; it is only logical and approved by your GM.

> **GM Note:** Sensory sharing is a good choice. The sharing range generally covers a city. It can send messages or communicate on your behalf, but the sharing only takes effect for 5 minutes. You can let it reach the corresponding area and then establish contact.

**Special:**
- With the permission of the GM, you can create a natural spirit to drive, or drive 3 ordinary natural spirits, and you can customize its image.
- The unique ability of natural spirits will not be included in your undead army.

- **Limits:** As described in this section's prose.


### Ritual Mastery

```yaml ability
id: death-seq-07-ritual-mastery
name: Ritual Mastery
pathway: death
sequence: 7
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
text: 'You gain access to ritual magic, able to invoke power from the gods. Effect:
  While holding this ability, you gain access to ritual magic, regardless of whether
  your Occult skill is advanced or not. For the ritual magic you can use, refer to
  [[Common Ritual Magic]]. Special: When the ritual you perform is a psychic ritual/spiritual
  ritual/summoning ritual, the Occult identification succeeds by default. Limit: This
  is the effect brought by 1 potion and cannot be stolen or recorded.'
```





You gain access to ritual magic, able to invoke power from the gods.
- **Effect:** While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.


- For the ritual magic you can use, refer to [[Common Ritual Magic]].
- **Special:** When the ritual you perform is a psychic ritual/spiritual ritual/summoning ritual, the Occult identification succeeds by default.
- **Limit:** This is the effect brought by 1 potion and cannot be stolen or recorded.

- **Limits:** As described in this section's prose.


### Undead Army Battle Adjudication

```yaml ability
id: death-seq-07-undead-army-battle-adjudication
name: Undead Army Battle Adjudication
pathway: death
sequence: 7
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
- buff
text: 'Because the Reaper Pathway starts from Sequence 7, and every time a Sequence
  is increased the subordinates you can drive and enslave increase explosively, you
  must decide the judgment method of your undead army in battle. #### When the Undead
  Are Treated as an aArmya As long as the total number of dead people driven by you
  is more than 3, then all the dead people driven by you are considered as a whole.
  You add the blood volume of all your dead people together, but it cannot be added
  together at one time; it needs to be classified and added. Example method: first
  add the Vitality of all living corpses together, then add the Vitality of all shadows
  together. After adding the values of the...'
```





Because the Reaper Pathway starts from Sequence 7, and every time a Sequence is increased the subordinates you can drive and enslave increase explosively, you must decide the judgment method of your undead army in battle.

#### When the Undead Are Treated as an "Army"

1. As long as the total number of dead people driven by you is more than 3, then all the dead people driven by you are considered as a whole.
2. You add the blood volume of all your dead people together, but it cannot be added together at one time; it needs to be classified and added.
3. Example method: first add the Vitality of all living corpses together, then add the Vitality of all shadows together. After adding the values of the dead of the same kind, record their blood volume respectively (e.g., using ".st living corpse (blood volume value)").
4. Decide the priority of your undead army's constituent species (example priority order given in RAW: living corpses 1, skeletons 2, wraith 3, water ghost 4).

#### Official Battle Judgment

1. Once the setting is completed, when battle officially starts and the undead army is attacked, the blood volume of the priority 1 species is used first for judgment and loss.
2. Once the blood volume of the priority 1 classification is cleared, overflow damage is borne by the priority 2 classification, and so on by priority order.
3. Each round, as long as you have more than 3 dead and are judged to be an army, the army can conduct 3 appraisals each round and can attack different targets separately.
   - You may freely choose which of the 3 appraisals are species; the same species can be selected as long as that species still exists.
4. When the total number of the undead army is 10, the damage caused by three identifications increases by 1d6 each time.
   - Example scaling given: shadow damage is 1d6 when total number <10; at 10 it is 2d6; at 20 it is 3d6; at 50 it is 6d6; and so on.
5. The actions of the undead army are independent and do not consume your body's actions.
   - They have 1 attack/Casting Action and 1 movement action.
   - You can spend a **Swift Action** to convert one of these actions into **two** swift actions.
6. All skill and attribute appraisals of the undead army use your Intuition (INT).
   - The identification of the undead army gains a bonus equal to (base bonus / number of its army species) / 2 (round down).

#### Siege

1. As long as the undead army exists, you and your teammates will continue to get the siege effect of siege/flanking-i.e., continue to gain advantage/disadvantage-unless the opponent also has the same number of undead troops.
2. If the enemy has a target higher than you by 1+ Sequence, the undead army can only offset the advantage/disadvantage effect of that target, unless the opponent has basically lost the ability to resist.

#### Area Damage

1. Area damage deducts blood volume from all species classifications of the undead army at the same time.
   - Example: "Yang Yan" of the [[Sun]] demigod-single damage from Yang Yan simultaneously reduces the life value of all classifications (living corpse, shadow, skeleton, etc.).
2. If a single-target attack says "Multiple targets standing together are considered the same target," then that single-target attack's damage to the undead army is doubled, but it is still deducted gradually according to priority 1, 2, and 3 rather than being deducted together.

**Special:**
- Each species block in the undead army can count up to 50 units. If a species exceeds 50, split it into additional blocks; army-mode rules still trigger whenever your total driven undead exceed 3.
- Unless an area attack can cover the whole field, it can only affect one of the undead army at a time by default.

- **Effect:** Undead Army Battle Adjudication resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
