---
title: 'Sequence 9: Hunter'
id: red-priest-seq-09
tags:
- pathway:red-priest
- sequence:9
---





# Red Priest Pathway: Sequence 9

## Hunter

- See also: [[Red Priest]]

> **Lore:** The embodiment of war and pure masculinity, corresponding to the Tarot card “Chariot” ([[Tarot - Chariot]]).

### Acting Rules

- The largest city is also the largest dark jungle.
- Here, everyone has two identities: prey and hunter.
- No matter how weak a hunter is, they are still a hunter—and may hurt powerful prey.
- Observe the environment, be familiar with the environment, and use the environment.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +1, Agility (DEX) +1, Intuition (INT) +1.
- All fighting-related skills increase by 1 level.

### Skill Growth

```yaml ability
id: red-priest-seq-09-skill-growth
name: Skill Growth
pathway: red-priest
sequence: 9
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
- detection
- stealth
- buff
text: 'Guided Training (1/day): Each time you receive at least 2 hours of non-repetitive,
  effective guidance, only once per day, your skills corresponding to the guidance
  content increase by 1 level: Fighting Shooting Tracking Survival Craft Manufacturing
  Stealth Detection'
```




1. **Guided Training (1/day):** Each time you receive at least 2 hours of non-repetitive, effective guidance, **only once per day**, your skills corresponding to the guidance content increase by 1 level:
   - Fighting
   - Shooting
   - Tracking
   - Survival
   - Craft Manufacturing
   - Stealth
   - Detection
   - Throwing
   - Listening  
   This increase **cannot exceed Proficiency**. Proficiency

2. **Hunting Growth:** It takes **2, 3, and 4 times** to be trained to be **Proficiency, Advanced, and Master** respectively.  
   Each time you successfully hunt an enemy stronger than you, it is also regarded as a skill growth. Choose any one of the above skills as the growth skill; apply the growth.

- Note on newly promoted characters and Intuition (INT):
  - It is not that a character who has just been promoted can use the relevant attributes brought by the potion (and corresponding to the skill) as Intuition (INT) to add points to the growth skill.
  - The potion’s own Intuition (INT) attribute can choose any skill to grow, regardless of whether the skill is inspired or not. Intuition

- **Effect:** Skill Growth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Law of the Jungle

```yaml ability
id: red-priest-seq-09-law-of-the-jungle
name: Law of the Jungle
pathway: red-priest
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- utility
text: 'Law of the Jungle: An explanation that your hunting-related skills will be
  used more effectively. Survival (Difficulty Value 20): On a Survival identification
  (Difficulty Value 20), you can judge: Whether the environment is good/bad for your
  survival Food channels Whether food is edible This includes cities. You cant get
  information that lacks clues; each clue is +2 beneficial. Tracking (Difficulty Value
  15): On a Tracking identification (Difficulty Value 15), choose a clue or target.
  As long as the target does not cover up content related to the clue by RP before
  leaving, you can track the targets action path along the way until the clue is disconnected
  due to extraordinary factors. Can...'
```




- **Law of the Jungle:** An explanation that your hunting-related skills will be used more effectively.

1. **Survival (Difficulty Value 20):** On a Survival identification (Difficulty Value 20), you can judge:
   - Whether the environment is good/bad for your survival
   - Food channels
   - Whether food is edible  
   This includes cities. You can’t get information that lacks clues; **each clue is +2 beneficial**.

2. **Tracking (Difficulty Value 15):** On a Tracking identification (Difficulty Value 15), choose a clue or target. As long as the target does not cover up content related to the clue by RP before leaving, you can track the target’s action path along the way until the clue is disconnected due to extraordinary factors.
   - Can be used in lieu of [[Spotting]].
   - Can resist [[Stealth]] checks against invisible/hiding creatures to spot targets, but you must first be aware of their presence.

3. **Listening (Difficulty Value 15):** On a Listening appraisal (Difficulty Value 15), you must know the target’s gait and voice before the appraisal, then choose the target you want to listen to. As long as the gait and sound corresponding to the target appear, you detect it immediately.

4. **Reconnaissance (Difficulty Value 15):** On a Reconnaissance identification (Difficulty Value 15), choose a target within your field of vision. On success, you remember some of their characteristics; the GM tells you what characteristics those are. Until the characteristics are covered or changed, you can recognize the target.

5. **Special Actions:** Special Actions such as [[Critical Strike]], [[Double Hit]], and [[Proximity Shooting]] are **+2 beneficial**, excluding [[First Aid]] / [[Surprise Attack]].
   - Does not affect special actions that simply gain benefits.
   - If a special action requires an Identification check, use **+4** on that Identification check instead of +2.

> **GM Note:** As a hunter, there may be more skill usages; the above content corresponds to ordinary people who are proficient in skills.

- **Effect:** Law of the Jungle resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Trap Making

```yaml ability
id: red-priest-seq-09-trap-making
name: Trap Making
pathway: red-priest
sequence: 9
type: active
action: full-round
cost: {}
roll: null
opposed_by: difficulty_value
range: self
target: self
duration: instant
scaling: []
tags:
- detection
- mobility
text: 'You can place traps in an area. This area must be a relatively small room,
  difficult to move, or another suitable location for traps. Use: As a Full-Round
  Action, you must reach the designated location and set a trap. #### Trap Placement
  Conditions The number of traps depends on your materials, and your materials depend
  on your [[Reputation]]. If your reputation is not Advanced, your trap upper limit
  equals your reputation level 3. If your Reputation is Advanced or higher, multiply
  by 5 (Proficiency does not count as Advanced). When a creature that is not blind
  and can see the surrounding environment is close to the trap, it can use a Difficulty
  Value 25 Detection / Survival / Crafting ch...'
```




- You can place traps in an area. This area must be a relatively small room, difficult to move, or another suitable location for traps.
- **Use:** As a Full-Round Action, you must reach the designated location and set a trap.

#### Trap Placement Conditions

1. The number of traps depends on your materials, and your materials depend on your [[Reputation]]. If your reputation is not Advanced, your trap upper limit equals your reputation level × 3. If your Reputation is Advanced or higher, multiply by 5 (Proficiency does not count as Advanced).

3. When a creature that is not blind and can see the surrounding environment is close to the trap, it can use a **Difficulty Value 25** Detection / Survival / Crafting check to find the trap. If you are in the field or in the ruins, you can use **Difficulty Value 20** Geology and Archeology respectively instead.  
   Detection  
   [[Geology]]  
   [[Archeology]]

4. If the creature is a [[Beast]] or an extraordinary creature (or extraordinary who has lost its mind), detecting the trap fails by default.

- A creature can only trigger **1 trap at the same time** (you cannot let a creature trigger multiple traps at the same time).

#### Trap Types and Resolution

- When you set up traps, you can choose the following:

1. **Triggering traps:** Craft Manufacturing identification is against the target’s [[Physical Defense]] to determine whether the trap works. Restricted traps do not need identification if they are not detected, while damage traps still need identification.

2. If a damage trap is not detected, its Craft Manufacturing identification can ignore the agility and dodge in Physical Defense, and gain the benefits of [[Sneak Attack]] and [[Surprise Attack]]; identification **+2**.

3. The benefits of Surprise Attack and Sneak Attack are invalid for creatures that cannot be surprised or sneak attacked.

#### Restricted Traps

##### Warning Trap

- **Use:** Choose an area; set up warning traps in this area and choose a way for the trap to remind you there is a target (e.g., hang a bell, or a tied wine bottle that falls).
- **Effect:** Once a creature passes through the edge of the area in physical form (where the warning trap is located), the bell or wine bottle immediately reminds you that the trap is triggered.
- **Reset:** Whenever the warning trap is triggered, you must go to where it is placed and use a Full-Round Action to reinstall it before it can be triggered again.

##### Capture Trap

- **Use:** Choose an area with a diameter ranging from **2 meters to 5 meters**; arrange capture traps.
- **Effect:** Once creatures arrive at the location of the capture trap in physical form, they are immediately restrained by you in the specified form (e.g., a net falling from the sky).
- **Breaking Free:**
  - Ordinary animals generally need **1 hour** to break free or cannot break free.
  - An intelligent or extraordinary creature can break free by passing a Strength test of **Difficulty Value 15**.
- **While Captured:** The creature cannot perform any attack or movement actions, but can perform spellcasting or swift/free actions.
- Capture traps can only be triggered once.

#### Injury Traps

##### Hunting Trap

- **Use:** Create a hunting trap no more than **0.5 meters to 1 meter** in diameter.
- **Effect:** Once a creature arrives at the location of the hunting trap in physical form, it immediately causes **2d6** physical damage.
- **Form Examples:** Triggered crossbow arrows, animal traps, and so on.
- **Leg Immobilization:** If the trap is similar to a trap, it is also considered to have delivered a vital blow to the leg; the creature must use an attack or spellcasting action to dismantle the trap, otherwise it cannot move.
- **Triggering Limits:** A creature can only trigger one hunting trap at the same time, but every movement action may cause it to trigger once.
- **Reset:** Each hunting trap must take a Full-Round Action after being triggered to return to its untriggered state.

##### Explosive Trap

- **Use:** Must have one explosive first; each explosive trap can place at most one explosive.
- **Effect:** Once a creature arrives at the location of the explosive trap in physical form and performs an identification equivalent to the above description, the explosive detonates immediately, causing damage equivalent to that of the explosive.
- **Typical Damage:** Generally speaking, an explosive trap can cause **2d6** physical damage and **1d6** fire damage.
- **After Trigger:** Explosive traps cannot be recovered after being triggered. Once the explosion is considered raw material, it is blown into hard-to-collect fragments.

- **Special case (multiple dynamites):** The GM may allow multiple dynamites in a trap; each additional dynamite takes **10 minutes** to consume.
  1. Starting from the second explosive, for each explosive, Crafting **+2 bonus** on identification against Physical Defense.
  2. Every time there are **5 explosives** in total, a **Difficulty Value 20** Crafting appraisal is required, and it takes **10 minutes** to expand the trap.
  3. For blasting behavior of excessive explosives, the GM should properly restrict it—especially except at sea. Explosives are not a product that can be bought casually; sellers are usually wary of users causing trouble and drawing attention to themselves.

- Other reasonable and logical traps are allowed by the GM.

#### Manual Triggering and Self-Safety

- If you choose to trigger the trap manually when placing the trap:
  - Once in a round, only one Swift Action can be triggered at a time.

- You are familiar with your trap arrangement:
  - Unless there is a big failure, or the trap is passive, you will not trigger your own trap involuntarily.
  - You clearly remember the location, principle, and mechanism of your own trap.

#### Sequence Promotion (Trap Making)

- **Sequence 6:** It only takes 1 casting or Attack Action to set up a trap; you can designate a location without the setting process, and it is regarded as a trap immediately there.

- **Special (from now on):** Your traps gain some occult effects, and the damage vectors in the traps can be replaced with your different types of fire.
  1. **Hunting Trap:** Can be turned into fire damage (e.g., hidden rockets shot out when triggered).
  2. **Explosive Trap:** You can directly use your [[Fireball]] or [[Fire Crow]] to replace the bomb. They can also be compressed, but you must pay the spirituality cost of making and compressing them when placing them.
     - When the [[Fire Crow]] is used instead of a bomb, if the Fire Crow is divided into three checks, at least one of the targets of the check must be the triggerer. Fireballs are similar to bombs and explode immediately when triggered.
     - Regardless of the identification of the previous flame type, when used as a trap, they are uniformly replaced with a Crafting identification.
     - This kind of flame storage trap is only effective for **24 hours**; after 24 hours the flame cannot be maintained and disintegrates.  
       [[Spirituality]]

- **Limits:** As described in this section's prose.


### Quick Dodge

```yaml ability
id: red-priest-seq-09-quick-dodge
name: Quick Dodge
pathway: red-priest
sequence: 9
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
- offense
text: 'Quick Dodge: You can dodge firearms. Against firearms (rather than light/lightning-type
  attacks), you retain full Agility (DEX) and Dodge in Physical Defense. When you
  face non-gun-like high-speed attacks, such as the flames of the Red Priest and the
  ice spear of the Witch. [[Red Priest]] [[Witch]] For any attack whose described
  speed does not reach the level of a gun, unless it must be hit, you retain your
  Agility (DEX) and Dodge defenses and also gain an additional dodge bonus. Note:
  When facing firearms, your extra evasion is invalid, but the original full agility
  and evasion defenses are still retained. Sequence scaling:'
```




- **Quick Dodge:** You can dodge firearms.

1. Against firearms (rather than light/lightning-type attacks), you retain full Agility (DEX) and Dodge in Physical Defense.

2. When you face non-gun-like high-speed attacks, such as the flames of the Red Priest and the ice spear of the Witch.  
   [[Red Priest]]  
   [[Witch]]

3. For any attack whose described speed does not reach the level of a gun, unless it must be hit, you retain your Agility (DEX) and Dodge defenses and also gain an additional dodge bonus.

- Note: When facing firearms, your extra evasion is invalid, but the original full agility and evasion defenses are still retained.

- Sequence scaling:
  - **Sequence 9:** Gain a level for additional evasion skills.
  - **Sequence 5:** The extra dodge skill is raised by one level.
  - **Sequence 4:** The extra dodge skill is raised by one level, and you can get extra dodge even in the face of firearms.
  - **Sequence 2:** The extra evasion skill goes up by one level.

- This is the benefit of the potion; it cannot be stolen or recorded.

- **Effect:** Quick Dodge resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spiritual Vision
```yaml ability
id: red-priest-seq-09-spiritual-vision
name: Spiritual Vision
pathway: red-priest
sequence: 9
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
scaling: []
tags:
- ritual
- detection
text: 'Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect:
  You activate Spiritual Vision, and your vision gains the following benefits: You
  gain Spiritual Vision, but it is not as effective for you as your own Intuition
  (INT). Etheric body: You can roughly tell whether the other partys body is good
  or bad through the color of the aura, but you cant get detailed information. Spiritual
  body: You can confirm whether an object/creature has spirituality; this cannot identify
  extraordinary people. Mental body: You can see whether the other party is thinking,
  but only so; you cannot get more detailed information. Astral body: You cannot see
  the astral body.'
```




- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate Spiritual Vision, and your vision gains the following benefits:


- You gain Spiritual Vision, but it is not as effective for you as your own Intuition (INT).

  1. **Etheric body:** You can roughly tell whether the other party’s body is good or bad through the color of the aura, but you can’t get detailed information.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality; this cannot identify extraordinary people.
  3. **Mental body:** You can see whether the other party is thinking, but only so; you cannot get more detailed information.
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your [[Spiritual Intuition]] test **+1 is beneficial**.

- Notes:
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding path.
  - The colors seen by spirit vision allow you to see each other in the dark, but you can only see the existence of colors; it is still possible to get lost in the dark because the colors you can see are limited.
  - You cannot use the colors to distinguish undead biology.

- Spiritual Vision can see some ordinary spirit bodies by default (which have not dissipated for **24 hours**) and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
