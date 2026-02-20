---
title: 'Sequence 7: Witch'
id: demoness-seq-07
tags:
- pathway:demoness
- sequence:7
---





# Demoness Pathway: Sequence 7

> **Lore:** Advancing to Witch reshapes the body toward striking beauty and charm.

## Witch

## Advancement

### Main Materials

- The whole blood of the black abyss demon fish
- The egg of the agate peacock

### Auxiliary Materials

- 80ml of pure water
- 5 drops of golden mandala juice
- Three scales of shadow lizard
- 10 drops of daffodil juice

## Extraordinary Abilities

You gain the following **extraordinary abilities**.

### Attribute Gain

- Strength +1
- Constitution +1
- Agility (DEX) +1
- Intuition (INT) +1
- Charisma +2
- You transform into a female.

### Mysticism Growth and Identity Effects

```yaml ability
id: demoness-seq-07-mysticism-growth-and-identity-effects
name: Mysticism Growth and Identity Effects
pathway: demoness
sequence: 7
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
- divination
text: 1 Your [[Mysticism]] has been included in the rapid growth category of Sequence
  9, and it can be upgraded to proficient at most. 2 If you were originally a male,
  then when you transform into a female, divination, prophecy, etc. that point to
  your original male identity (excluding past occult information) will be invalid
  because of the wrong gender designation, as if you evaporated. Only correct divinations
  that assume you are female and point to your new name (if any) will work.
```




- ① Your [[Mysticism]] has been included in the rapid growth category of Sequence 9, and it can be upgraded to proficient at most.
- ② If you were originally a male, then when you transform into a female, divination, prophecy, etc. that point to your original male identity (excluding past occult information) will be invalid because of the wrong gender designation, as if you “evaporated.”
  - Only correct divinations that assume you are female and point to your new name (if any) will work.

- **Effect:** Mysticism Growth and Identity Effects resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Curse

```yaml ability
id: demoness-seq-07-curse
name: Curse
pathway: demoness
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- debuff
text: 'You can add a curse to the target or perform a curse ceremony through various
  mystical information such as flesh and blood and [[True Name]]. Cost: 3 [[Spirituality]]
  Use: As a Casting Action, choose a target of flesh and blood whose true name you
  know. Effect: 1 If you only know the real name, you need to sacrifice your life
  and cast curse-related ritual magic to complete the curse. If you hold the targets
  flesh and blood, then you can directly curse the target, and this time the curse
  must succeed. 2 After success, the target will fall into a Cursed State. If the
  target is an ordinary person and knows that they are cursed by you, they may also
  fall into a state of fear of you. #### Curs...'
```




You can add a **curse** to the target or perform a curse ceremony through various mystical information such as flesh and blood and [[True Name]].

- **Cost:** 3 [[Spirituality]]
- **Use:** As a Casting Action, choose a target of flesh and blood whose true name you know.
- **Effect:**
  - ① If you only know the real name, you need to sacrifice your life and cast curse-related ritual magic to complete the curse.
  - If you hold the target’s flesh and blood, then you can directly curse the target, and this time the curse must succeed.
  - ② After success, the target will fall into a **Cursed State**. If the target is an ordinary person and knows that they are cursed by you, they may also fall into a state of fear of you.

#### Cursed State

- ① The target in the Cursed State is immediately regarded as having established a mystical connection with you. You can cast an extraordinary ability on the cursed target at any time regardless of distance limits, and this extraordinary ability is bound to be a Great Success.
- ② This extraordinary ability will be converted into curse damage, and this kind of great success can still be saved by a [[Substitute]].
- ③ After the spell is cast, the Cursed State ends immediately. A second degree of curse must be completed by obtaining flesh and blood or performing a ritual, and the flesh and blood used for casting the spell will be consumed.
- ④ There is no point in hoarding flesh and blood, because after the first casting of the spell, the target will know that they are under the curse, and will therefore have enough time to immediately cast the ritual magic to cut off the connection between the flesh and blood.

**Sequence scaling:**

- [[id:alias-sequence-6|Sequence 6]]: With a quick action once in a round, a curse connection can be established through flesh and blood.

- **Limits:** As described in this section's prose.


### Ritual of Curse

```yaml ability
id: demoness-seq-07-ritual-of-curse
name: Ritual of Curse
pathway: demoness
sequence: 7
type: active
action: full-round
cost: {}
roll: null
opposed_by: none
range: The casting range covers a city.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- debuff
text: 'You cast a large area-specific curse through ritual magic. Duration/Upkeep:
  For about 1 week, consume 5 points of [[Spirituality]] every day. Range: The casting
  range covers a city. Rules status: This is essentially [[Ritual Magic]], not a Beyonder
  ability; therefore, even if the Curse ability is lost, the ritual can still be performed.
  Prayed God: The default is Chick, the Primordial Witch. #### Site Setup First select
  an altar area with a radius of 10 meters. Prepare the initial ceremony in 5 minutes.'
```




You cast a large area-specific curse through ritual magic.

- **Duration/Upkeep:** For about 1 week, consume 5 points of [[Spirituality]] every day.
- **Range:** The casting range covers a city.
- **Rules status:** This is essentially [[Ritual Magic]], not a Beyonder ability; therefore, even if the Curse ability is lost, the ritual can still be performed.
- **Prayed God:** The default is Chick, the Primordial Witch.

#### Site Setup

- First select an altar area with a radius of 10 meters.
- Prepare the initial ceremony in 5 minutes.
- Wrap the altar area (10-meter radius) with a [[Spiritual Wall]].
- At the same time, it is best to ensure that the surrounding area within about 10 meters (roughly one house) is silent; the **GM** decides the exact requirement.

#### Procedure

After the initial ceremony is ready, you need to start harvesting human life.

- If you choose animals, usually five animals equals one person, unless you can find something similar to a dire bear.
- Every time you kill a target:
  - The target’s soul will be attracted to the altar’s 10-meter radius, blocked by the spiritual wall, and turned into a [[Ghost]] that wanders within the ceremony’s scope, waiting for the ceremony to start as a sacrifice for the burnt offering.

A ritual requires at least 8 human lives.

- For each additional person beyond 8, the ceremony can be advanced by one day.

Before starting the ceremony:

- You need to use the puppet to write the real name and related information of one or more targets you want to curse in advance.

#### Activation and Effect

- **Use:** Use a Full-Round Action to start the ceremony.
- **Effect:** The targets whose real names you specify—up to the number of sacrifices you have made—will immediately fall into a Cursed State.
- **Range and escape:** The casting range covers a city, and targets within the casting range and not isolated cannot escape.

#### Consequences and Special Cases

- **Note:** The location of the altar where ghosts start to accumulate will have a strong breath of death. There will be continuous cold winds within a radius of 100 meters, and the surrounding temperature will be 5 degrees lower than normal.
- **Special:** If you give up the ritual and remove the spiritual wall, the accumulated ghosts will immediately lose control and start indiscriminately attacking everyone around, or possessing plants to entangle and attack creatures or attack directly, until it becomes difficult to maintain their existence after one hour.
- **Note:** As a kind of ritual magic knowledge, if extraordinary from other paths understand this ritual and have the ability to perform ritual magic, they can also use it, but they also need to pray to the gods with the ability to curse.

- **Limits:** As described in this section's prose.


### Black Flame

```yaml ability
id: demoness-seq-07-black-flame
name: Black Flame
pathway: demoness
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Choose 1 target within 30 meters
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- debuff
- defense
- offense
text: 'You have been favored by the Black Flame. A hot and treacherous black flame
  emerges from your spirituality. From this moment on, you will annihilate ghosts
  and rot creatures. Black Flame spreads like a real flame, but there is no sound
  during the spreading process. It only burns flames with spirituality and life. It
  ignores 5 points of [[Curse Resistance]]. It can be used to deal with the scene:
  burning corpses and traces as if they never existed. When the target has no curse
  resistance and the ignored resistance therefore overflows, the ignored resistance
  is changed to a damage bonus. #### Remote Attack'
```




You have been favored by the **Black Flame**.

- A hot and treacherous black flame emerges from your spirituality. From this moment on, you will annihilate ghosts and rot creatures.
- Black Flame spreads like a real flame, but there is no sound during the spreading process.
- It only burns flames with spirituality and life.
- It ignores 5 points of [[Curse Resistance]].
- It can be used to deal with the scene: burning corpses and traces as if they never existed.

- When the target has no curse resistance and the ignored resistance therefore overflows, the ignored resistance is changed to a damage bonus.

#### Remote Attack

- **Use:** 1 spellcasting action
- **Cost:** 2 [[Spirituality]]
- **Targeting and range:** Choose 1 target within 30 meters
- **Check:** [[Mysticism]] against [[Physical Defense]]
- **Effect:** Deal 3d6 curse damage.

#### Black Flame Circles

- **Use:** 1 Swift Action
- **Limits:** 1 time per round
- **Effect:** You let a group of black flames hover around you in advance. In your next long-range attack, the hovering black flames are regarded as guns when fired, ignoring Agility (DEX) and Dodge in Physical Defense, and the range is increased to 50 meters.

- **Special:** Every 1d6 of Black Flame’s damage can be resolved as a separate identification/attack roll, up to 3 identifications. Overflow damage can be added to a certain identification at your discretion (e.g., first hit is 2d6, follow-up is 1d6), which is a combo.

#### Melee Attack

- **Use:** 1 Attack Action
- **Check:** Changed to fight against [[Physical Defense]]
- **Effect:** Both hands shoot up evil black flames for close-range attacks. Because the black flames penetrate into the body, they ignore armor and deal curse damage of 2d6 + strength damage dice. This can double hit.
- The black flame of the melee attack can also wrap around the weapon, so the melee attack can also increase the damage of the weapon.

#### Covered by Black Flames

- When there are any black flames around your body, you are considered to have 5 points of [[Cold Resistance]].

**Sequence scaling:**

- [[id:alias-sequence-6|Sequence 6]]: Black Flame damage increased by 1d6.
- [[Sequence 5]]: Black Flame damage increased by 1d6.
- [[id:alias-sequence-4|Sequence 4]]: Black Flame damage increases by 2d6, and you can specify which kind of spiritual and life-bearing things the black flame burns.

#### Other Usages / Deepening Usages of Black Flame

- ① Burn off traces of the scene: You can let a crime scene with the dead be accurately burned off the body. The black flame will not make any sound or spread uncontrollably due to wood products; it will only accurately burn off remaining traces—from scorched marks from lightning strikes, to individual stains and bloodstains on clothing, to a single hair on an entire ship.
  - Because the black flame is completely under your control, it is up to you whether it will continue to spread. The process of spreading is still silent, only burning living and spiritual creatures, but not hurting yourself.
  - Starting from Sequence 4, you can also specify to burn a certain life or spiritual existence, so other targets and creatures are not affected even if they touch the black flame.
  - This can be used as an afterthought to make everything seem like it never happened.
- ② Make contact paste: You can burn a strand of your hair with a black flame, leaving a paste-like black thing. Others can smear it on a mirror, and then your spiritual intuition will respond accordingly.
  - On your side, you can wipe a mirror with a black flame; the mirrors on both sides can connect images, allowing real-time communication.

### Frost Mastery

```yaml ability
id: demoness-seq-07-frost-mastery
name: Frost Mastery
pathway: demoness
sequence: 7
type: active
action: attack
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- defense
- offense
text: 'You have gained the favor of ice. Ice can condense on your body surface; places
  you walk are covered with frost; snowflakes float in the air. #### Long-Range Attack
  Use: An Attack Action Cost: 2 [[Spirituality]] Effect: Ice bursts from your palm;
  frost quickly condenses into an ice spear filled with hoarfrost and surrounded by
  cold smoke. Check: Roll against [[Physical Defense]] Damage: 3d6 + strength damage
  dice cold damage Aftereffects: The targets muscles tremble; frost cascades; ice
  crystals condense. The targets next check within 1 round is -2 disadvantageous,
  and has no effect on targets with [[Cold Resistance]].'
```




You have gained the favor of ice. Ice can condense on your body surface; places you walk are covered with frost; snowflakes float in the air.

#### Long-Range Attack

- **Use:** An Attack Action
- **Cost:** 2 [[Spirituality]]
- **Effect:** Ice bursts from your palm; frost quickly condenses into an ice spear filled with hoarfrost and surrounded by cold smoke.
- **Check:** Roll against [[Physical Defense]]
- **Damage:** 3d6 + strength damage dice cold damage
- **Aftereffects:** The target’s muscles tremble; frost cascades; ice crystals condense. The target’s next check within 1 round is -2 disadvantageous, and has no effect on targets with [[Cold Resistance]].
- **Miss:** If it misses, the surrounding environment will also be filled with frost and freeze.

#### Melee Attack

- The ice spear can also be used for melee attack, but because of the lack of potential energy, it changes to cold damage of 1d6 + strength damage dice.

#### Area Attack

- **Use:** A spellcasting action
- **Cost:** 2 [[Spirituality]]
- **Effect:** Create a blizzard; choose an area with a radius of 10 meters.
- **Check:** [[Mysticism]] against [[Physical Defense]]
- **On success:** Deal 2d6 cold damage to all creatures within the range except you.
- **Aftereffects:** Creatures successfully attacked by the blizzard and with no cold resistance suffer a -2 penalty to their next check within 1 round.

- **Note:** Because Black Flame affects things with spirits, it cannot be enchanted on Ice Lances before [[Demigod]].

**Sequence scaling:**

- [[id:alias-sequence-6|Sequence 6]]: Damage increased by 1d6.
- [[Sequence 5]]: Damage increased by 1d6.
- [[id:alias-sequence-4|Sequence 4]]: Damage increased by 2d6.

- **Limits:** As described in this section's prose.


### Mirror Stand-in

```yaml ability
id: demoness-seq-07-mirror-stand-in
name: Mirror Stand-in
pathway: demoness
sequence: 7
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: Choose a mirror within 10 meters.
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
text: 'You use a mirror as your stand-in. Use: 1 Casting Action Cost: Consumes 4 [[Spirituality
  Limit]] Requirement: Prepare a complete mirror (vanity mirror, silver mirror, or
  a large floor-to-ceiling mirror). #### Use a Mirror Use: 1 free action Cost: 2 [[Spirituality]]
  Targeting and range: Choose a mirror within 10 meters.'
```




You use a mirror as your **stand-in**.

- **Use:** 1 Casting Action
- **Cost:** Consumes 4 [[Spirituality Limit]]
- **Requirement:** Prepare a complete mirror (vanity mirror, silver mirror, or a large floor-to-ceiling mirror).

#### Use a Mirror

- **Use:** 1 free action
- **Cost:** 2 [[Spirituality]]
- **Targeting and range:** Choose a mirror within 10 meters.
- **Timing:** 1 second before you are about to be attacked.
- **Effect:** Use the mirror instead of yourself to resist 1 attack or other effects; the effect is completely neutralized.
- **Displacement:** After the stand-in, you reappear up to 8 meters away and cannot pass through walls (an additional displacement effect).
- **Area attacks:** If the displacement does not let you leave the area of effect, you take half damage (rounded up).
- **Limits/conditions:**
  - The stand-in must be used immediately. Because it is an active ability, you must recognize the corresponding threat to use it.
  - Effects that have already taken effect on you cannot be substituted. Example: once the witch’s plague takes effect, the subsequent deterioration cannot be substituted.
  - Special: If the target is higher than your Sequence by 2+, the ability to act freely is too late for the substitute.

#### Anti-Divination

- **Use:** Destroy a mirror.
- **Choose:** A specific mystical piece of information related to you (e.g., “you plan to attack someone next”).
- **Check:** Conduct a [[Mystic Appraisal]] as the Difficulty Value of anti-divination.
- **Effect (on success):** This information is excluded in related divination, spiritual intuition, and prophecy, unless it exceeds the corresponding difficulty.
- **After the mirror is shattered:** Your spirituality limit is restored; your body that was hit becomes a shattered mirror; your figure reappears about one meter away.

#### Special: Mirror/Fragments as a Curse Medium

- **Use:** 1 Casting Action
- **Targeting:** Shine a mirror that you have applied the stand-in effect on, or the fragments of a shattered mirror, to a creature.
- **Check:** [[Mysticism]] against [[Physical Defense]]
- **Effect (on success):** Create a Cursed State, using the mirror or fragments as the medium.
- The curse relationship established this way supports melee attacks and directly grabbing into the mirror to directly attack the cursed target.

- **Limits:** As described in this section's prose.


### Wand Substitution

```yaml ability
id: demoness-seq-07-wand-substitution
name: Wand Substitution
pathway: demoness
sequence: 7
type: active
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
text: 'You craft a wand as a stand-in. Use: About 5 minutes Cost: Consume 3 points
  of [[Spirituality Limit]] Crafting requirement: Crafting a wand requires two [[Credits]]
  levels; proficient and above credits will not be consumed. Materials: You must bring
  your own wood or other raw materials, or directly use a walking stick. Form: The
  wand can be an ordinary black wand, or a gorgeous cane (mastery and above are basically
  the latter). #### Use the Wand Use: A free action'
```




You craft a wand as a **stand-in**.

- **Use:** About 5 minutes
- **Cost:** Consume 3 points of [[Spirituality Limit]]
- **Crafting requirement:** Crafting a wand requires two [[Credits]] levels; proficient and above credits will not be consumed.
- **Materials:** You must bring your own wood or other raw materials, or directly use a walking stick.
- **Form:** The wand can be an ordinary black wand, or a gorgeous cane (mastery and above are basically the latter).

#### Use the Wand

- **Use:** A free action
- **Cost:** 2 [[Spirituality]]
- **Trigger:** When you suffer an attack.
- **Effect:** Gain the equivalent effect of a mirror stand-in; it can also be used for anti-divination.
- **Range condition:** The wand does not have to be carried with you; as long as the wand is within a 10-meter radius of you, it can be used as a stand-in.
- **After resisting:** The wand breaks; your spirituality limit recovers; your body that was hit collapses and is replaced by the broken wand; your figure reappears up to 8 meters aside and cannot pass through walls.

#### Spellcasting While Holding the Wand

- When holding the wand, if you take out the wand and use it to cast spells, your [[Occultism]] will temporarily increase by one level.

- **Limits:** As described in this section's prose.


### Invisibility

```yaml ability
id: demoness-seq-07-invisibility
name: Invisibility
pathway: demoness
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: 1 minute
scaling: []
tags:
- ritual
- divination
- detection
- stealth
text: 'You gain invisibility through special magic powder. #### Hide Face Use: 1 Casting
  Action Cost: 1 [[Spirituality]] Effect: Make the face hazy and blurred. Except for
  the special vision of the [[Eye of Mystery/Fate]], others usually cannot see your
  face clearly. Duration: 1 minute Limits: Personal goals only. #### Hidden Body Shape'
```




You gain **invisibility** through special magic powder.

#### Hide Face

- **Use:** 1 Casting Action
- **Cost:** 1 [[Spirituality]]
- **Effect:** Make the face hazy and blurred. Except for the special vision of the [[Eye of Mystery/Fate]], others usually cannot see your face clearly.
- **Duration:** 1 minute
- **Limits:** Personal goals only.

#### Hidden Body Shape

- **Use:** 1 Casting Action
- **Cost:** 1 [[Spirituality]]
- **Targeting:** Sprinkle fluorescent powder on yourself or others, and chant to achieve invisibility.
- **Duration:** 1 minute
- **Break conditions:** Once you take damage or launch an attack during the stealth process, the stealth is released immediately.
- **Limits:**
  - Invisibility powder cannot be used by other creatures.
  - The maximum amount of powder is equal to your Intuition (INT).
- **Effect:**
  - You immediately disappear into the air and cannot be selected as a target by sight-based abilities.
  - However, the psionic effects of [[Voyeur]], [[Spectator]], and [[Puppet Master]] can still see your existence, and the [[Hanged Man]] may be able to hear your voice.
  - You gain [[Attack Advantage]] against creatures that are unaware of your presence.

**Sequence scaling:**

- [[id:alias-sequence-6|Sequence 6]]: You no longer need to scatter dust. You can make yourself or others invisible through a Swift Action. The others must be within 10 meters of you, and it consumes 1 spirituality point each time.

> **GM Note:** About repeated sneak attacks in battle: If you become invisible again in official battle after a sneak attack, as long as you can make the enemy unable to accurately detect your movements and use this to launch a sneak attack or surprise attack, then the sneak attack in the battle is still valid and may take effect repeatedly. The same goes for other raid or sneak attack operations with similar sequences. See [[Special Actions]] for details, and [[Special State]] for how to see through invisibility.
