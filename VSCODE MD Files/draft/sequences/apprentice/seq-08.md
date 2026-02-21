---
title: 'Sequence 8: Trickmaster'
id: apprentice-seq-08
tags:
- pathway:apprentice
- sequence:8
---






# Door Pathway: Sequence 8

## Trickmaster

- Wields a variety of strange but not powerful spells, including “fog,” “wind,” “flash,” “freeze,” “shock,” and the slippery “fall.”

## Advancement

### Main Materials

- Stomach pouch of the soul eater × 1
- Deep-sea marlin blood × 20 ml

### Auxiliary Materials

- Hornbeam essential oil × 5 ml
- Thread ball grass powder × 10 g
- Blooming red chestnut flower × 1
- Pure water × 80 ml

### Acting Rules

- Focus on the two words “act” and “fool.” “Fool” can also be replaced by “deception.”

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2, **Constitution** +2, **Agility (DEX)** +1.  
  Intuition  
  [[Constitution]]  
  Agility (DEX)

### Performance Recognition

```yaml ability
id: apprentice-seq-08-performance-recognition
name: Performance Recognition
pathway: apprentice
sequence: 8
status: canonical
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- buff
- social
text: 'Each time you perform a performance that is not repeated and is recognized
  by different people (especially strangers), choose one of your Performance/Deception
  skills; it increases by 1 level, up to mastery. [[Performance]] [[Deception]] To
  improve between the following levels, you must meet the above condition this many
  times: Training Proficiency: 2 times Proficiency Advanced level: 3 times Advanced
  level Mastery: 4 times'
```





- Each time you perform a performance that is not repeated and is recognized by different people (especially strangers), choose one of your Performance/Deception skills; it increases by 1 level, up to mastery.  
  [[Performance]]  
  [[Deception]]
- To improve between the following levels, you must meet the above condition this many times:
  - Training → Proficiency: 2 times
  - Proficiency → Advanced level: 3 times
  - Advanced level  Mastery: 4 times

- **Effect:** Performance Recognition resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spells

```yaml ability
id: apprentice-seq-08-spells
name: Spells
pathway: apprentice
sequence: 8
status: adapted
type: active
action: cast
cost:
  spirituality: 1
roll: 1d20 + @attr.cha + @skill.performance
opposed_by: physical_defense
range: varies by trick mode (single target or 10m area centered on caster)
target: designated target(s)
duration: varies by trick mode (instant to 3 rounds; fog 1 round if unsealed)
dice:
  check_roll: 1d20 + @attr.cha + @skill.performance
  damage_roll: 1d6
  heal_roll: null
  effect_roll: 1d3
  notes: Adapted primary check uses Performance; prose also permits Deception or Occultism for many tricks. Effect roll tracks ongoing burn tick where applicable.
scaling:
- when: freezing_technique_mode
  changes:
    cost: {spirituality: 1}
    damage_roll: 1d6
    effect_note: On hit, target without cold resistance takes -2 on next movement/skill/ability checks.
- when: wind_blowing_skill_mode
  changes:
    cost: {spirituality: 2}
    effect_note: Apply up to 6 meters forced movement, reduced by target size.
- when: fall_mode
  changes:
    cost: {spirituality: 2}
    effect_note: On successful check, target becomes Unbalanced until it spends movement to recover.
- when: flash_mode
  changes:
    cost: {spirituality: 1}
    effect_note: Affected targets are blinded for 1 round.
- when: fog_creation_mode
  changes:
    cost: {spirituality: 2}
    effect_note: Create 10m fog zone with targeting penalties for 1 round if environment is unsealed.
- when: electric_shock_mode
  changes:
    cost: {spirituality: 2}
    damage_roll: 1d6
    effect_note: Wet targets may be paralyzed on Constitution DV15 failure; undead take +1d6 lightning damage.
- when: incinerate_mode
  changes:
    cost: {spirituality: 2}
    damage_roll: 1d6
    effect_roll: 1d3
    effect_note: Burned target takes 1d3 fire damage at round start for 3 rounds.
- when: rebound_mode
  changes:
    cost: {spirituality: 1}
    effect_note: Redirect falling or moving target back on original trajectory and can apply Unprepared state.
- when: cantrip_skill_quicken
  changes:
    action: free
    effect_note: Once per round, one cast-action trick can be used as a free action.
tags:
- ritual
- mobility
- defense
- offense
- social
- control
- debuff
text: 'You wield a variety of strange but not powerful spells. #### Freezing Technique
  Use: 1 Casting Action. Casting Action Cost: Consume 1 Spirituality. [[Spirituality]]
  Targeting and range: Choose 1 target. Check: Performance/Deception/Occult vs Physical
  Defense. [[Occult]] [[Physical Defense]] Effect: Rapidly lowers temperature; freezes
  the surface of the targets body, dealing 1d6 cold damage. Aftereffects: Against
  a target without cold resistance, it suffers a -2 penalty on its next movement,
  skill, and ability checks. [[Cold Resistance]]'
```





You wield a variety of strange but not powerful spells.

#### Freezing Technique

- **Use:** 1 **Casting Action**. Casting Action
- **Cost:** Consume 1 **Spirituality**. [[Spirituality]]
- **Targeting and range:** Choose 1 target.
- **Check:** Performance/Deception/Occult vs **Physical Defense**. [[Occult]] [[Physical Defense]]
- **Effect:** Rapidly lowers temperature; freezes the surface of the target’s body, dealing **1d6** cold damage.
- **Aftereffects:** Against a target without cold resistance, it suffers a **-2** penalty on its next movement, skill, and ability checks. [[Cold Resistance]]
- **Special:** You can make a glass of water (or something like that) cool down very quickly.

#### Wind Blowing Skill

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 2 **Spirituality**.
- **Effect:** You make the whistling sound of wind suddenly appear, and all light objects are blown away.
- **Benefit:** The following effect applies.
  - Choose a wind direction within a range of **10 meters** and gain **6 points of forced movement**, forcing creatures in this range to move **6 meters** in the wind’s direction.  
    [[Forced Movement]]
  - For each point of the creature’s size, the forced movement is **-1**, excluding Tiny volume (ants, spider).  
    [[Size/Volume]]
- **Volume notes:** Things other than Tiny volume that can rely on “Volume Reduction Wind” are as follows:  
  [[Volume Reduction Wind]]
  - Small size (gravel, paper book)
  - Small to medium size (cats, dogs)
  - Medium volume (person)
  - Medium to large creatures (adult tigers, bears)
  - Large creatures (giants, demons, warriors)
  - Creatures of very large size (cyclops, monsters that capsize ships)
  - A total of **6** volumes that can reduce the effects of the wind spell.
- **Special:** Any creature that loses balance will receive double the force of forced movement.  
  [[Unbalanced]]
- **Special:** Among them, once the small volume and large volume are affected by the wind, they will lose their balance by default, and thus the forced movement force will be doubled.

#### Fall

- **Use:** 1 spellcasting action. Spellcasting Action
- **Cost:** Consume 2 spiritual points. [[Spirituality]]
- **Targeting and range:** Choose 1 target on the ground.
- **Check:** Performance/Deception/Occult vs **Physical Defense**; ignores armor. [[Armor]]
- **Effect:** If the identification is successful, the opponent immediately falls down and loses balance (becomes **Unbalanced**).
- **Condition: Unbalanced**
  - Unable to move, attack, and cast spells.
  - You must use **1 Movement Action** to get out of the unbalanced state. Movement Action
  - While unbalanced: (Agility (DEX) and dodge in Physical Defense **-2**).
  - Others gain advantages: (skill and attribute identification) **+2**.  
    [[Advantage / Disadvantage]]

#### Flash

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 1 spiritual point.
- **Targeting and range:** Affects all targets looking directly at you within **10 meters** (centered on you).
- **Check:** Performance/Deception/Occult vs **Physical Defense**; ignores armor.
- **Effect:** Blinds affected targets for **1 round**.
- **Condition: Blind**
  [[Blind]]
  - Unless the action targeting other things is an indiscriminate strike, it needs a **Difficulty Value 15** Intuition (INT) test (according to the memory recall direction) to be successfully executed.  
    Difficulty Value  
    [[Indiscriminate Strike]]
  - The detection test is **-8** disadvantageous. Detection  - Others have an advantage over it.

#### Fog Creation

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 2 points of spirituality.
- **Effect:** Create fog covering a range of **10 meters**.
- **Duration:** If the environment is not sealed, the fog dissipates after **1 round**.
- **Fog effects:**
  1) Including you in the fog range, identification of other things as targets is **-4** disadvantageous, excluding indiscriminate strikes.
  2) Looking for something: unless you have prepared in advance, you need to perform a **Difficulty Value 15** detection assessment before performing it (suffering a penalty). In special cases, it may be a listening assessment.  
     [[Listening]]
  3) Any range ability that can have a substantial impact on the material world (storm of light, wind) will dissipate the fog.  
     [[Storm of Light]]
- **Special:** This effect is overridden by blindness, but the check penalty stacks with blindness’ detection penalty.  
  [[blindness]]

#### Electric Shock

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 2 spiritual points.
- **Targeting and range:** Choose 1 target.
- **Check:** Perform/Deceive vs **Physical Defense**; ignores agility and evasion in Physical Defense; treats it as light, lightning.
  [[Evasion]]
- **Effect:** Deal **1d6** lightning damage.
- **Notes:** Although this counts as lightning, you’re not getting thunder; you’re creating electricity “out of thin air.”
- **Special:** Shock can’t make a vital strike. [[Vital Strike]]
- **Special:** If the target is an undead creature, increase the lightning damage by **1d6**.
- **Special:** If the target is wet, you can make a **Constitution** check vs **Difficulty Value 15** to paralyze it.
- **Condition: Paralyzed**
  [[Paralyzed]]
  - Make a physical examination with a **Difficulty Value 15** to get rid of paralysis; otherwise you cannot perform attack and movement actions.
  - It will not return to normal until the end of the target's next turn.

#### Incinerate

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 2 spiritual points.
- **Targeting and range:** Choose 1 target.
- **Check:** Performance/Deception/Occult vs **Physical Defense**.
- **Effect:** Deal **1d6** fire damage.
- **Duration and ongoing damage:** For **3 rounds**, at the beginning of each round, the burned target continues to suffer **1d3** fire damage.

#### Rebound

- **Use:** 1 **Casting Action**.
- **Cost:** Consume 1 spiritual point.
- **Targeting and range:** Choose 1 falling or moving target (such as a ball that has just been thrown).
- **Effect:** It returns on the same trajectory, which may cause a surprise effect.
- **Condition: Unprepared**
  [[Unprepared]]
  - You are in a hurry, unable to dodge, and lose the agility and dodge in Physical Defense against this attack.

#### Other Tricks

- Other tricks that are logical and allowed by the **GM**; the number depends on the GM’s permission, usually no more than your Intuition (INT).
- You need to write their effects in advance, unless you are only temporarily using them in daily or usual performances.
- Pay attention to original tricks: tricks should meet the characteristics of being strange but not powerful.

#### Cantrip Skill

- You can cast your spell-like abilities as a quickened cast.
- **Rules:**
  1) Once per round, you can use a **Free Action** to cast any cantrip that requires a Casting Action. Free Action [[Cantrip]]
  2) If you formulate an unexpected way to use a trick before performing it and use it with performance-style techniques (for example, deliberately asking the enemy what will happen next), making the enemy unable to guess what you are going to do by performing and fooling:
     - If you let the trick happen at a moment others can’t imagine—like a performer and audience—then your trick has the effect of being caught off guard. [[Caught Off Guard]]
     - This can be done with special actions such as delayed action, or real inspiration, but you must do the relevant roleplay. [[Delayed Action]] [[Real Inspiration]]
- **Special:** Cantrips iden

- **Limits:** As described in this section's prose.
