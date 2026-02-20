---
title: 'Sequence 7: Interrogator'
id: arbiter-seq-07
tags:
- pathway:arbiter
- sequence:7
---





# Justiciar Pathway: Sequence 7

- You become proficient with various weapons and an expert in blasting.

## Interrogator

## Advancement

### Auxiliary Materials

- Horn of the flashing black snake ×1 [[Flashing Black Snake Horn]]
- Dust of the spirit of the lake ×1 [[Spirit of the Lake Dust]]

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength +1, constitution +2, agility +1

- Whenever you successfully interrogate a creature and obtain a key, non-repetitive piece of information, choose **one** of the following to increase by 1 level: intimidate / speak / please / persuade.  
  - The number of growth times and the upper limit are equal to the reputation growth of Sequence 9. Sequence 9 Reputation Growth

### Weapon Proficiency

```yaml ability
id: arbiter-seq-07-weapon-proficiency
name: Weapon Proficiency
pathway: arbiter
sequence: 7
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- detection
- offense
text: 'Effect: While you have this ability, your skills in using various weapons are
  treated as mastery (in terms of skills). [[Skill Mastery]] Limits: This does not
  include identification of spellcasting such as occultism / inspiration. [[Occultism]]
  Intuition This does include fighting (including subdivision) / throwing / shooting
  (including subdivision) / blasting / cannon, etc. [[Fighting]] [[Throwing]] [[Shooting]]
  [[Blasting]] [[Cannon]] Progression: Each time you practice at least 2 hours of
  the corresponding skill training, your ability can rise to the corresponding level.
  The growth rate and number of times are equal to skill fighting. [[Fighting Skill
  Growth]] Notes: This is a passive...'
```




- **Effect:** While you have this ability, your skills in using various weapons are treated as mastery (in terms of skills). [[Skill Mastery]]
- **Limits:**
  1. This does **not** include identification of spellcasting such as occultism / inspiration. [[Occultism]] Intuition
  2. This **does** include fighting (including subdivision) / throwing / shooting (including subdivision) / blasting / cannon, etc. [[Fighting]] [[Throwing]] [[Shooting]] [[Blasting]] [[Cannon]]
- **Progression:**
  1. Each time you practice at least 2 hours of the corresponding skill training, your ability can rise to the corresponding level.
  2. The growth rate and number of times are equal to skill fighting. [[Fighting Skill Growth]]
- **Notes:** This is a passive ability that cannot be recorded, but can be stolen. [[Ability Recording]] [[Ability Theft]]

### Spirit Piercing

```yaml ability
id: arbiter-seq-07-spirit-piercing
name: Spirit Piercing
pathway: arbiter
sequence: 7
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: Select 1 target within your field of vision. [[Field of Vision]]
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- debuff
- offense
text: 'Treat this as psychic damage to the spirit body (GM-defined). Preparation (Fear)
  Use: 1 Swift Action Swift Action Cost: Does not consume spirituality. [[Spirituality]]
  Targeting and range: Select 1 target within your field of vision. [[Field of Vision]]
  Effect: This is a preparation state for mental puncture. During the maintenance
  period, no other extraordinary abilities can be used. [[id:alias-extraordinary-abilities|Extraordinary
  Abilities]]'
```




> **Lore:** This is a means to directly attack the spirit body, bringing coercion at the spirit-body level—gathering spirit, piercing the target’s spirit body, and directly attacking their spirit.

> **Lore:** Manifestation form: two lightning bolts suddenly light up in your eyes; the enemy will scream, and the spirit will be pierced by a sharp knife.

Treat this as **psychic damage** to the spirit body (GM-defined).

1. **Preparation (Fear)**
   - **Use:** 1 **Swift Action** Swift Action
   - **Cost:** Does not consume spirituality. [[Spirituality]]
   - **Targeting and range:** Select 1 target within your field of vision. [[Field of Vision]]
   - **Effect:**
     - This is a preparation state for mental puncture.
     - During the maintenance period, no other extraordinary abilities can be used. [[id:alias-extraordinary-abilities|Extraordinary Abilities]]
     - The target gains a **Fear** state, and it does not have the effect of forced movement. [[Fear]] [[Forced Movement]]
   - **Special (rank):** This halves the effect on targets higher than your rank, and has no effect on targets higher than a rank. [[Rank]]

2. **Pierce (Damage + Stun)**
   - **Use:** 1 **Swift Action** Swift Action
   - **Frequency:** 1 time per round Round
   - **Cost:** Consumes 3 spirituality points. [[Spirituality]]
   - **Targeting and range:** Choose 1 target within your field of vision. [[Field of Vision]]
   - **Check:** inspiration + charisma against physical defense; ignores armor. Intuition [[Charisma]] [[Physical Defense]] [[Armor]]
   - **Effect (on success):** Deal 1d6 mental damage and apply a **Stunned** state. [[Mental Damage]] [[Stunned]]
   - **Interaction with (1):** The use of (2) does not need to consume 1 more Swift Action due to (1), but therefore (2) will not cause the fear effect.

Whether step (2) requires step (1) to be active is GM-defined.

- **Limits:** As described in this section's prose.


### Whip of Pain

```yaml ability
id: arbiter-seq-07-whip-of-pain
name: Whip of Pain
pathway: arbiter
sequence: 7
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: Choose 1 target within your field of vision. [[Field of Vision]]
target: designated target(s)
duration: instant
scaling: []
tags:
- ritual
- detection
- debuff
text: 'Ready State (Fear) Use: 1 Swift Action Swift Action Cost: Does not consume
  spirituality. [[Spirituality]] Targeting and range: Choose 1 target within your
  field of vision. [[Field of Vision]] Effect: You enter a ready state. During the
  maintenance period, you cannot use other extraordinary abilities. [[id:alias-extraordinary-abilities|Extraordinary
  Abilities]] Endow the target with a Fear state. [[Fear]]'
```




> **Lore:** The target feels as if electric currents are passing through their minds, forming thorny whips that constantly beat the soul.

1. **Ready State (Fear)**
   - **Use:** 1 **Swift Action** Swift Action
   - **Cost:** Does not consume spirituality. [[Spirituality]]
   - **Targeting and range:** Choose 1 target within your field of vision. [[Field of Vision]]
   - **Effect:**
     - You enter a ready state.
     - During the maintenance period, you cannot use other extraordinary abilities. [[id:alias-extraordinary-abilities|Extraordinary Abilities]]
     - Endow the target with a **Fear** state. [[Fear]]
     - The target clearly feels that the whip formed by the electric current is located in the mind.
   - **Special (sequence/level restriction):** Only for targets lower than your sequence level or level: their movement is halved due to trembling and knees becoming soft. Sequence Level [[id:alias-movement|Movement]]
   - **Other:** The rest of the determination is the same as that of mental piercing, and the target affected by this ability will continue to feel the pain and the lifting of the invisible whip. [[Mental Piercing]]

2. **Cast / Accompany Weapon**
   - **Use:** 1 **spellcasting**/**Attack Action** Spellcasting Action Attack Action
   - **Cost:** Consuming 2 spirituality. [[Spirituality]]
   - **Modes:**
     - **Cast alone (spellcasting action):**
       - **Check:** inspiration + intimidation check against physical defense; ignores armor. Intuition [[Intimidation]] [[Physical Defense]] [[Armor]]
       - **Effect (on success):** Cause 1d6 mental damage. [[Mental Damage]]
       - **After damage:** The target’s movement is halved for 1 round, rounded up. [[id:alias-movement|Movement]] Round
       - Other creatures gain **disadvantage** against them; this cannot be superimposed. [[Advantage / Disadvantage]]

     - **Accompanying weapon (attacking action):**
       - Perform the confrontation identification corresponding to the weapon, and cause corresponding damage. [[Confrontation Identification]]
       - It can only be a melee weapon. [[Melee Weapon]]
       - The accompanying weapon effect should not be an extraordinary ability produced by a Casting Action. [[id:alias-extraordinary-abilities|Extraordinary Abilities]]
       - Range note: casting alone is a long-range effect, and accompanying weapon is a melee effect. [[Range Bands]]
       - If you use it as an accompanying weapon, you only need the confrontation identification corresponding to the weapon to produce the two effects of the weapon itself and the Whip of Pain at the same time.
       - **Resolution vs physical defense:**
         - When the result of the identification > physical defense (including armor), the two effects will be produced at the same time. [[Physical Defense (Including Armor)]]
         - When the result of the identification > physical defense (excluding armor), only the Whip of Pain effect will be produced. [[Physical Defense (Excluding Armor)]]

- **Limits:** As described in this section's prose.
