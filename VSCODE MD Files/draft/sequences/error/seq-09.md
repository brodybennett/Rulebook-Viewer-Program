---
title: 'Sequence 9: Marauder'
id: error-seq-09
tags:
- pathway:error
- sequence:9
---






# Error Pathway: Sequence 9

## Marauder

> **Lore:** Not a thief, but a thief-a fraudster. The dream is to steal people's hearts, steal spells, cheat rules, and cheat fate, and all of this starts with stealing things from others. It is difficult to distinguish these extraordinary people from ordinary thieves. Maybe they are more powerful in their methods, and their purpose of stealing property is not for enjoyment or survival, but more like fulfilling a mission.

- See also: The Error Path Pathway

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
- You can skillfully master observation and stealing skills.

1. Whenever you perform a challenging, non-repetitive stealing behavior and the stealing is successful, you can choose the Detection skill to increase by 1 level. The things you steal must be valuable to the owner.
2. Still, bullying doesn't count. Stealing from beings weaker than you isn't challenging. A thief's dream is to steal hearts, steal spells, cheat rules, and cheat fate. Stealing is more like fulfilling a mission.
3. It takes 2, 3, and 4 trainings to advance from training to proficient, proficient to advanced, and advanced to mastery, respectively.
4. When directly creating a character with a higher Sequence, the growth-skill increase from the potion is doubled to make up for the gap in growth.

### Agile Hands

```yaml ability
id: error-seq-09-agile-hands
name: Agile Hands
pathway: error
sequence: 9
status: canonical
type: active
action: full-round
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- buff
- offense
text: 'The stability and dexterity of your wrists and fingers are enhanced, which
  is the essence of power. Effect: Once per round, you can use a free action Free
  Action to perform an action that uses a skill at Mastery tier. This action is usually
  an attack/Casting Action. If it is a Full-Round Action [[Full-Round Action]], it
  is changed to an attack/Casting Action. Whenever you make an identification Identification
  related to the flexibility and stability of your fingers and wrists, your identification
  +2 is beneficial. You can better learn skills related to the flexibility and stability
  of your fingers and wrists. Whenever you learn this aspect, as long as the knowledge
  is true and effective,...'
```





The stability and dexterity of your wrists and fingers are enhanced, which is the essence of power.

- **Effect:**
  1. Once per round, you can use a **free action** Free Action to perform an action that uses a skill at **Mastery** tier. This action is usually an attack/Casting Action. If it is a **Full-Round Action** [[Full-Round Action]], it is changed to an attack/Casting Action.
  2. Whenever you make an **identification** Identification related to the flexibility and stability of your fingers and wrists, your identification +2 is beneficial.
  3. You can better learn skills related to the flexibility and stability of your fingers and wrists. Whenever you learn this aspect, as long as the knowledge is true and effective, and the learning time exceeds 2 hours, your corresponding skills will increase by 1 grade.
- **Limits:**
  4. You can only study once per day; skill progression uses 2/3/4 trainings for training -> proficient -> advanced -> mastery.

**Skills related to the flexibility and stability of fingers and wrists:**
- Fighting (hand-to-hand combat)
- Shooting
- Skillful hands
- Locksmithing
- Other skills (same category)

**This generally does not include:**
- Grappling
- Grappling (giant weapons)
- Shooting (rifles)
- Etc.

### Excellent Observation

```yaml ability
id: error-seq-09-excellent-observation
name: Excellent Observation
pathway: error
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: 10m
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- detection
text: 'Your observation and inspiration are more unique. Effect: You can sense valuables
  within 10 meters from you as the center, and you can distinguish the degree of value
  and the approximate location of the items. This does not include the Extraordinary
  characteristics in the Beyonder, but includes unused Extraordinary characteristics,
  Extraordinary items, etc. [[Beyonder]] Although you can perceive the existence of
  valuables, you canaTMt know what it is unless it is directly exposed to your eyes.
  Otherwise you canaTMt distinguish the shape, form, and whether it is extraordinary;
  you can only judge according to its value. Special: The standard of valuables is
  determined by the society in whic...'
```





Your observation and inspiration are more unique.

- **Effect:**
  1. You can sense valuables within 10 meters from you as the center, and you can distinguish the degree of value and the approximate location of the items. This does not include the Extraordinary characteristics in the **Beyonder**, but includes unused Extraordinary characteristics, Extraordinary items, etc. [[Beyonder]]
  2. Although you can perceive the existence of valuables, you can't know what it is unless it is directly exposed to your eyes. Otherwise you can't distinguish the shape, form, and whether it is extraordinary; you can only judge according to its value.
- **Special:**
  - The standard of valuables is determined by the society in which they live. As long as they are generally considered valuable, they have value.
  - Things like diamonds can be perceived as long as they are recognized by society, but fakes, fakes, and shoddy goods can also be judged come out.
  - (This cannot be recorded or stolen, Player can actively apply for triggers to relieve GM pressure, and will be affected by anti-divination.) [[id:alias-anti-divination|Anti-Divination]]

- **Limits:** As described in this section's prose.


### Steal

```yaml ability
id: error-seq-09-steal
name: Steal
pathway: error
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: designated target(s)
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
- defense
text: 'You can easily steal items from the targetaTMs pocket without being detected.
  Cost: 2 points of spirituality [[Spirituality]] Use: 1 Casting Action Casting Action;
  perform 1 contact stealing behavior. Effect: Skilled against physical defense, when
  stealing items, ignore Agility (DEX) and Dodge in Physical Defense, you steal the
  opponentaTMs items. As long as you touch the items, you can succeed, and usually
  you will not be discovered unless extraordinary means are involved. Not to be discovered
  does not include the discovery of lost items afterwards, as well as the corresponding
  suspicion and investigation; only the process of stealing is not discovered. If
  the stolen item is an Extraordi...'
```





You can easily steal items from the target's pocket without being detected.

- **Cost:** 2 points of **spirituality** [[Spirituality]]
- **Use:** 1 **Casting Action** Casting Action; perform 1 contact stealing behavior.
- **Effect:**
  1. Skilled against physical defense, when stealing items, ignore Agility (DEX) and Dodge in Physical Defense, you steal the opponent's items. As long as you touch the items, you can succeed, and usually you will not be discovered unless extraordinary means are involved.
  2. Not to be discovered does not include the discovery of lost items afterwards, as well as the corresponding suspicion and investigation; only the process of stealing is not discovered.
  3. If the stolen item is an Extraordinary item, choose the one with the highest Sequence level of the item and the owner. For every Sequence level the target is higher than you, your identification is disadvantaged by -2. If the target is two or more Sequences higher, **Big Success** [[Big Success]] is ignored.
  4. If the stolen item has no owner (it is not currently carried or held, and the item that is not on the body is ownerless):
     - If the ownerless item is an ordinary item, the stealing identification is successful by default.
     - If it is an extraordinary item, it requires a **Difficulty Value 15** identification check.

**Sequence scaling:**
- Sequence 8: You no longer need to touch. You can directly transfer objects within 10 meters of your field of vision to your hand. If it is blocked by an object, as long as you can confirm the approximate location of the object, you can also let it come across the barrier to your hands. The Error Path Pathway: Sequence 8
  - Stealing from a distance still requires stealing postures, such as closing five fingers, holding objects virtual, and twisting wrists.
- Sequence 7: Your Steal range is increased to 30 meters. The Error Path Pathway: Sequence 7
- Sequence 6: Your Steal range is increased to 50 meters. The Error Path Pathway: Sequence 6
- Sequence 5: Your stealing range is increased to 100 meters. The Error Path Pathway: Sequence 5

- **Limits:** As described in this section's prose.


### Ritual Mastery

```yaml ability
id: error-seq-09-ritual-mastery
name: Ritual Mastery
pathway: error
sequence: 9
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
  your Occult skill is advanced or not. While holding this ability, you gain access
  to ritual magic, regardless of whether your occult skill is advanced or not. [[Occult
  Skill]] For the ritual magic you can use, refer to [[Common Ritual Magic]]. Limits:
  (This is the effect brought by 1 potion and cannot be stolen or recorded.)'
```





You gain access to ritual magic, able to invoke power from the gods.
- **Effect:** While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.


  - While holding this ability, you gain access to ritual magic, regardless of whether your occult skill is advanced or not. [[Occult Skill]]
  - For the ritual magic you can use, refer to [[Common Ritual Magic]].
- **Limits:**
  - (This is the effect brought by 1 potion and cannot be stolen or recorded.)

### Spiritual Vision

```yaml ability
id: error-seq-09-spiritual-vision
name: Spiritual Vision
pathway: error
sequence: 9
status: adapted
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition + 2
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition + 2
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Vision is an upkeep toggle; check roll maps the +2 Spiritual Intuition benefit while active.
scaling: []
tags:
- ritual
- detection
- healing
- mobility
text: 'You have obtained a more outstanding spiritual vision because of your inspiration.
  Use: 1 free action to activate. Cost: 1 spirituality point per round while active.
  Effect: While active, your vision gains the following benefits: Etheric body: You
  can directly see the health status of the target through the color of the aura,
  directly find out where the other partyaTMs body is uncomfortable, where there is
  a problem, and when it comes to a certain organ, you can see the inside through
  the unthickened door, confirm the number of people inside. [[Etheric Body]] Spiritual
  body: You can confirm whether an object/creature has spirituality (this cannot identify
  extraordinary people). You can al...'
```





You have obtained a more outstanding spiritual vision because of your inspiration.
- **Use:** 1 **free action** to activate.
- **Cost:** 1 **spirituality point per round** while active.
- **Effect:** While active, your vision gains the following benefits:


  1. **Etheric body:** You can directly see the health status of the target through the color of the aura, directly find out where the other party's body is uncomfortable, where there is a problem, and when it comes to a certain organ, you can see the inside through the unthickened door, confirm the number of people inside. [[Etheric Body]]
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality (this cannot identify extraordinary people). You can also penetrate the door to see the inside, and identify whether there is ritual magic power in it. This can penetrate the spiritual wall. [[Spiritual Body]] [[Spiritual Wall]]
  3. **Mental Body:** You can see the color represented by the other person's emotions, but you can only see a general content. For example, you can know whether the other person is depressed or uneasy. This kind of negative emotion is usually a dark tone. [[Mental Body]]
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your spiritual intuition test +2 is beneficial. [[Spiritual Intuition Test]]
- **Note:**
  - Dead creatures are usually only dull in color and cannot be recognized.
  - Spiritual materials usually have spirituality.
  - The color of the material in the spiritual vision usually represents its corresponding Pathway. This does not mean that you can see the power of a Beyonder Pathway.
  - The color seen by the spirit vision allows you to see each other in the dark, but you can only see the existence of color, and it is still possible to get lost in the dark.
  - Unlike dead creatures, undead creatures have deep black spirituality color instead of no.
  - --Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
