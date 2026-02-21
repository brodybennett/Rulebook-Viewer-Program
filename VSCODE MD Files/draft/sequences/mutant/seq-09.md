---
title: 'Sequence 9: Prisoner'
id: mutant-seq-09
tags:
- pathway:mutant
- sequence:9
---






# Chained Pathway: Sequence 9

> **Lore:** The Mutant Pathway represents unbridled desire, corresponding to the Tarot card [[Temperance]].
>
> **Lore:** Extraordinary people of this Pathway are also called heterogeneous. They are transformed into various monsters due to the negative effects brought about by Extraordinary characteristics. An instinctive, distorted, and suppressed bloodthirsty desire hides in their hearts. If they do not control themselves and vent desire wantonly, they become increasingly ruthless until their minds are completely distorted.

## Prisoner

> **Lore:** “The mind is the prisoner of the body, and the body is the prisoner of the world.” This refers to bound madness and suppressed desires. It not only refers to a person locked in a prison, but also a repressed person whose spirituality and desires are bound by reason, body, and the world.
>
> **Lore:** Extraordinary people in this Sequence are physically strong and sensitive, often showing a silent appearance and a crazy heart at the same time. They have mastered many criminal skills and are good at killing people with any item they can get at hand.

> **GM Note:** Extraordinary people in this Sequence often have a silent appearance and a crazy heart at the same time.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

> **GM Note:** Some abilities below are restricted to specific factions/schools as noted in each ability.

### Attribute Gain

- **Attribute Gain:** strength +1, constitution +2, inspiration +1, will +2, education +1.
- In addition, your fighting related/weapon use related/throwing/criminal skills can quickly grow to proficiency:
  1. Each time you receive 2 hours of corresponding guidance, or conduct 2 hours of corresponding training yourself, your corresponding skills increase by 1 level. You need to be trained twice to become proficient. Only once a day.
  2. When creating a character that has not just been promoted, you can use the relevant attributes brought by the potion as inspiration to add points for growth skills. The attributes can only add points to your own related skills, and the inspiration attribute itself can add points to any skills.

Crime-related skills usually include:

- Power related: Climb, Swim, Intimidate, Jump
- Educational: Demolition, Law, Archaeology, Trades, Geology, Biology, Pharmacy (poisons only), Chemistry (explosives only)
- Agility (DEX)-related: Stealth, Hands-on, Locksmithing, Tracking, Driving (including subdivisions)
- Intuition (INT) related: listening, investigation, mechanical maintenance, psychology, craft manufacturing
- Charisma (CHA) related: disguise, deceit, fast talk, pleasing, psychological guidance (hypnosis only)

What they have in common are the preconditions for crimes or a criminal action.

(The above skills are limited to a certain use. If you use an inspiration and train it for real, then the use can become complete again)

### Crazy Hidden

```yaml ability
id: mutant-seq-09-crazy-hidden
name: Crazy Hidden
pathway: mutant
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
- buff
- offense
text: 'Effect: Critical Strike/Double Strike/Proximity Shot and other special action
  identification +2 is beneficial. Exclusions: Excluding first aid/surprise attack.
  Limits: Does not affect special actions that simply gain benefits, such as gaining
  momentum and aiming. This bonus can stack up to +4 total. Notes: It only affects
  identification. GM Note: This is also a description of the improvement brought by
  the potion, which cannot be recorded or stolen, but is just listed separately.'
```





- **Effect:** Critical Strike/Double Strike/Proximity Shot and other special action identification +2 is beneficial.
- **Exclusions:** Excluding first aid/surprise attack.
- **Limits:** Does not affect special actions that simply gain benefits, such as gaining momentum and aiming.
  - This bonus can stack up to +4 total.
- **Notes:** It only affects identification.
- **GM Note:** This is also a description of the improvement brought by the potion, which cannot be recorded or stolen, but is just listed separately.

### Restrain Your Desires and Gain Momentum

```yaml ability
id: mutant-seq-09-restrain-your-desires-and-gain-momentum
name: Restrain Your Desires and Gain Momentum
pathway: mutant
sequence: 9
status: canonical
type: active
action: cast
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
conditions:
- fear
tags:
- control
- debuff
text: 'Prerequisite: This can only be obtained by the [[Temperance faction]] of the
  [[xenopath]]. Effect: You will not be affected by emotional states such as anger,
  fear, charm, etc., but you are still considered to have these emotional states.
  For example, you are considered to be in a state of anger, but you will not get
  any benefits and disadvantages from the state of anger. In addition, when you fall
  into a state of madness, as long as you do not lose control, you can maintain normal
  actions, excluding the [[id:alias-full-moon-curse|full moon curse]] and [[uncertain
  madness]]. Uncertain madness will not force you to act, but will make you lose 1
  action continuously to suppress. Special: The...'
```





- **Prerequisite:** This can only be obtained by the [[Temperance faction]] of the [[xenopath]].
- **Effect:**
  1. You will not be affected by emotional states such as anger, fear, charm, etc., but you are still considered to have these emotional states. For example, you are considered to be in a state of anger, but you will not get any benefits and disadvantages from the state of anger.
  2. In addition, when you fall into a state of madness, as long as you do not lose control, you can maintain normal actions, excluding the [[id:alias-full-moon-curse|full moon curse]] and [[uncertain madness]]. Uncertain madness will not force you to act, but will make you lose 1 action continuously to suppress.
- **Special:** The emotional impact of a person at least 1 **Sequence** higher than you is only halved, rounded up.

> **GM Note:** You will be more focused in normal times. Unless there are extraordinary factors, you should not be distracted at critical times, but you can still see what is the source of attracting others' attention, which does not mean that you are dull.

- **Limits:** As described in this section's prose.


### Sexual Behavior

```yaml ability
id: mutant-seq-09-sexual-behavior
name: Sexual Behavior
pathway: mutant
sequence: 9
status: canonical
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.psychological_guidance
opposed_by: difficulty_value
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.int + @skill.psychological_guidance
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Psychological guidance DV 20 can end the berserk state or allow retreat.
scaling: []
damage_types:
- mental
tags:
- offense
text: 'Prerequisite: This can only be obtained by the heterosexual pathway. Effect:
  Unless there are special circumstances, your insane state defaults to violent tendencies,
  which is regarded as a kind of anger without effects. After falling into a state
  of insanity, you must use your freedom, spellcasting, and attack to deal with your
  enemies or vent. Unless your remaining Vitality < your total Vitality divided by
  4, or you or someone else has passed the Difficulty Value 20 psychological guidance
  test with 1 spellcasting, otherwise you cannot retreat, nor can you save your teammates,
  and you cannot show mercy. Special: Once you suffer mental damage, you will fall
  into madness, unless the enemy...'
```





- **Prerequisite:** This can only be obtained by the heterosexual pathway.
- **Effect:**
  1. Unless there are special circumstances, your insane state defaults to violent tendencies, which is regarded as a kind of anger without effects. After falling into a state of insanity, you must use your freedom, spellcasting, and attack to deal with your enemies or vent.
  2. Unless your remaining Vitality < your total Vitality divided by 4, or you or someone else has passed the Difficulty Value 20 psychological guidance test with 1 spellcasting, otherwise you cannot retreat, nor can you save your teammates, and you cannot show mercy.
- **Special:** Once you suffer mental damage, you will fall into madness, unless the enemy is 2 ranks or 1 rank higher than you.
- **Benefit:** No matter how much sanity you lose, you won't go into [[indeterminate madness]].

> **GM Note:** You should not suppress your desires in normal times, and do it immediately when you have the idea of action, but this does not mean that you are a fool. When facing things that threaten your life, you will still try your best repress yourself.

- **Limits:** As described in this section's prose.


### Favor of the Starry Sky

```yaml ability
id: mutant-seq-09-favor-of-the-starry-sky
name: Favor of the Starry Sky
pathway: mutant
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
- divination
- control
- buff
text: 'Prerequisite: Only Extraordinary people who belong to the [[Rose School of
  Thought]] are available. Setting Constraint: The module timeline should be the period
  when the [[Fifth Epoch]] Rose School split, when the [[Indulgence School]] dominated
  and the [[Temperance School]] fled. Effect: By default, your divination appraisal
  can only reach the minimum success level, and a big success can only increase the
  success level by 1. Death: If you die, the psychic cannot obtain direct and effective
  information from you. Special: Your whereabouts will therefore be under the stable
  control of the Rose School of Thought. This does not mean what you are doing specifically,
  and you can be immediately...'
```





- **Prerequisite:** Only Extraordinary people who belong to the [[Rose School of Thought]] are available.
- **Setting Constraint:** The module timeline should be the period when the [[Fifth Epoch]] Rose School split, when the [[Indulgence School]] dominated and the [[Temperance School]] fled.
- **Effect:** By default, your divination appraisal can only reach the minimum success level, and a big success can only increase the success level by 1.
- **Death:** If you die, the psychic cannot obtain direct and effective information from you.

- **Special:** Your whereabouts will therefore be under the stable control of the Rose School of Thought. This does not mean what you are doing specifically, and you can be immediately informed of any difficulties you encounter. This is derived from the power of the alien high-ranking person or the starry sky.
- This influence even includes your Extraordinary characteristics after death: it will also be tracked by the Rose School, and it cannot be used for divination formulas or other information directly related to the Rose School; general divination functions are not restricted by this clause.
- This bondage can be broken in special ways, but once you break free, it means that you have betrayed the School of the Rose.
- Some Temperance Schools who escaped from the Rose School of Thought have mastered the method of releasing this bondage. Angels who have not mastered the method can only reduce the impact. If it is a Beyonder characteristic, it can be smashed repeatedly until it has almost no impact, but it is also unable to divination formulas and information.

- **Limits:** As described in this section's prose.


### Vision
```yaml ability
id: mutant-seq-09-vision
name: Vision
pathway: mutant
sequence: 9
status: canonical
type: active
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: "1"
  notes: While active, spiritual intuition checks gain +1.
scaling: []
tags:
- ritual
- detection
- healing
text: 'Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect:
  You activate vision, and your vision gains the following benefits: Etheric body:
  You can directly see the health status of the target through the color of the aura,
  and directly find out where the other party''s body is uncomfortable, where there
  is a problem, and it is specific to a certain organ. Spiritual body: You can confirm
  whether an object/creature has spirituality, which cannot identify extraordinary
  people. Mental Body: You can confirm whether the other person is thinking, but you
  cannot see more content. Astral body: You cannot see the astral body. When in the
  state of spiritual vision, your spiritual in...'
```





- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate vision, and your vision gains the following benefits:


  1. **Etheric body:** You can directly see the health status of the target through the color of the aura, and directly find out where the other party's body is uncomfortable, where there is a problem, and it is specific to a certain organ.
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality, which cannot identify extraordinary people.
  3. **Mental Body:** You can confirm whether the other person is thinking, but you cannot see more content.
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your spiritual intuition test +1 is beneficial.

Note:

- Dead creatures are usually only dull in color and cannot be identified.
- Spiritual materials usually have spirituality.
- The color of the material in the spiritual vision usually represents its corresponding path. This does not mean that you can see the power of a Beyonder.
- The color seen by the spirit vision allows you to see each other in the dark, but you can only see the existence of color, and it is still possible to get lost in the dark.
- Unlike dead creatures, undead creatures have deep black spirituality color instead of no color.

- Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
