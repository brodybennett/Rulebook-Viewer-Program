---
title: 'Sequence 9: Corpse Collector'
id: death-seq-09
tags:
- pathway:death
- sequence:9
---






# Death Pathway: Sequence 9

## Corpse Collector

- See also: Death

> **Lore:** It was called the "Phoenix" approach in ancient times. The mythical creature form was originally a phoenix, but now it is a feathered snake, corresponding to the Tarot card "Reaper". A unique bird-shaped ornament made of gold.

### Overview

- You possess certain corpse-like characteristics:
  - You appear gloomy.
  - Your body temperature is low.
  - These traits help you avoid being attacked by ignorant undead.
- You have **Spirit Vision** and can directly see some evil spirits.
- You understand the traits and weaknesses of many undead creatures (see **Knowledge of the Dead**).

## Advancement

### Auxiliary Materials

- **Auxiliary Materials:** Air-dried adult black-spotted frogs

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Constitution +1, Agility (DEX) +1, Intuition (INT) +1
- You are trained in a new skill: **Knowledge of the Dead**.

### Corpse-Like Traits

```yaml ability
id: death-seq-09-corpse-like-traits
name: Corpse-Like Traits
pathway: death
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
- debuff
- defense
text: 'You gain 5 points of resistance to cold, poison, and curse. Ordinary undead
  (ghosts, zombies, etc.) will mistake you for the same kind. This does not include
  undead with outstanding intelligence (such as evil spirits formed by extraordinary
  people). This does not include an undead creature transformed into by an Extraordinary.
  Your appearance changes: You become quite gloomy, with a lower body temperature,
  whiter skin, and certain corpse characteristics. This may have some benefits for
  your appearance, but it is a bit unrealistic already looming.'
```





- You gain **5** points of resistance to cold, poison, and curse.
- Ordinary undead (ghosts, zombies, etc.) will mistake you for the same kind.
  - This does **not** include undead with outstanding intelligence (such as evil spirits formed by extraordinary people).
  - This does **not** include an undead creature transformed into by an Extraordinary.
- Your appearance changes:
  - You become quite gloomy, with a lower body temperature, whiter skin, and certain corpse characteristics.
  - This may have some benefits for your appearance, but it is a bit unrealistic already looming.

- **Effect:** Corpse-Like Traits resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Knowledge of the Dead

```yaml ability
id: death-seq-09-knowledge-of-the-dead
name: Knowledge of the Dead
pathway: death
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
conditions:
- dead
tags:
- detection
text: '*Knowledge of the Dead: You know the traits and weaknesses of many undead creatures.
  #### Using Knowledge of the Dead for Corpse Identification Knowledge of the Dead
  can replace [[Biology]] for corpse identification. It is regarded as a subdivision
  skill of Biology. Whenever you use Knowledge of the Dead on a corpse, you can quickly
  understand rough information such as: Approximate cause of death Weapon of death
  Time of death'
```





**Knowledge of the Dead:** You know the traits and weaknesses of many undead creatures.

> **GM Note:** This is a clarification: in potion ascension, you are trained in this skill; normally, Knowledge of the Dead is related to education.

#### Using Knowledge of the Dead for Corpse Identification

- Knowledge of the Dead can replace [[Biology]] for corpse identification.
  - It is regarded as a subdivision skill of Biology.
- Whenever you use Knowledge of the Dead on a corpse, you can quickly understand rough information such as:
  - Approximate cause of death
  - Weapon of death
  - Time of death
  - Whether the cause of death involves extraordinary things

#### Detailed Autopsy Identification

To learn more detailed information, you must spend at least **2 hours** to conduct a detailed autopsy and make an identification.

- **Autopsy Identification Difficulties (Knowledge of the Dead):**
  - **Difficulty Value 15:** You know the general cause of death of the corpse, the weapon of death, the time of death, and whether the cause of death involves extraordinary things.
    - Difficulty Value 15 is the difficulty of quick autopsy.
    - If you are doing a quick autopsy on a corpse, you can only reach Difficulty Value 15 at most.
  - **Difficulty Value 20:** You know the exact cause of death of the corpse, the specific type of weapon, the specific time of death, and the type of Extraordinary power involved (such as sacred, dark, fallen, undead, flame).
  - **Difficulty Value 25:** You have reverse engineered the treatment the corpse suffered before death, whether it was disguised as suicide, whether it was still tortured after death, whether it experienced a beating and fighting before death.
    - This can only restore information directly related to the corpse.
  - **Difficulty Value 30:** You have confirmed the general living conditions of the corpse, what kind of person it was in life (staying at home all year round, living too slack, etc.), whether it has been taking drugs for a long time, whether it has undergone some training, etc.
  - **Great success:** On the basis of the existing benefits, you can roughly restore the death scene of the corpse, you can substitute the perspective of the dead in your mind, and recognize the general picture of the corpse being devastated before it was alive.
    - If you do not grasp the clues, the picture will be quite abstract.
  - **Catastrophic failure:** Your autopsy went terribly wrong, and some clues to the corpse were permanently lost due to your mishandling.

- **More autopsies (Difficulty Value 25):** The collector may want to specifically confirm some specific information about the corpse (such as what the corpse ate within 2 days before its death, and what drugs it may have taken). Difficulty Value 25 is used as a general treatment.

- **Special:**
  - Higher Difficulty Value includes the benefits of lower Difficulty Value.
  - If you perform a **2-hour** autopsy, no matter what the identification result is, you can get at least Difficulty Value **20** information.
  - You can re-identify by repeating the autopsy, which consumes **2 hours** again.

##### Autopsy Penalties for Aged or Mutilated Corpses

- If the dead body has been dead for a prolonged period of time or has been severely mutilated:
  1. Corpse dead for more than **1 week** or beyond recognition: autopsy identification **-2** unfavorable.
  2. Corpse dead for more than **1 month** or internal organs completely destroyed: autopsy identification **-4** unfavorable.
  3. The corpse has been dead for more than **half a year** or half of its limbs are missing: autopsy identification **-6** unfavorable.
  4. The corpse has been dead for more than **several years** or there is only a layer of skin/bones left: autopsy identification **-8** unfavorable, the highest Difficulty Value can only reach **20**, and the Great success is still valid.
     - In the above special circumstances, if the limbs are incomplete and the internal organs are missing, the cadaver may not be able to obtain the corresponding information (for example, gastrointestinal related loss may cause the cadaver to be unable to obtain information about what the corpse has eaten), but it can still be found out that it is taking medicine.

#### Improving Knowledge of the Dead

- Whenever you conduct a **2-hour** autopsy on a corpse or undead creature (the type cannot be repeated), your Knowledge of the Dead will increase by **1 level**.
  - A type of corpse or undead creature can only be upgraded once.
  - From training to proficiency, to advanced, to mastery, you need to learn **2, 3, 4** times.
- For the time being, it can only be upgraded to mastery.
- When creating a character who has not just been promoted, growth skills gain **2x Intuition (INT)** points from the potion.

#### Using Knowledge of the Dead Against Undead Creatures

- When you make any [[Attack Roll]] against an undead creature, Knowledge of the Dead translates into an additional attack roll bonus.
  - **Note:** You must have dissected an undead creature for which you gain the Knowledge of the Dead bonus, or know the corresponding information.
- Example:
  - Original: rd20+dexterity+shooting
  - With Knowledge of the Dead: rd20+dexterity+shooting+knowledge of the dead
- If the Corpse Collector's shot is untrained, then the apparent reason for the hit is based on anticipation of the undead's habits.
- **Special:** When using Knowledge of the Dead to attack, the corpse collector can also perform a [[Vital Blow]] against an undead creature that is not vital, but the undead creature is still immune to the corresponding damage.
  - Example: Even if you use Knowledge of the Dead to shoot bullets, the spirit body is still immune to physical damage, unless you use [[Enchanted Bullets]].

- **Effect:** Knowledge of the Dead resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Vision

```yaml ability
id: death-seq-09-vision
name: Vision
pathway: death
sequence: 9
status: adapted
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Vision is an upkeep toggle; check_roll maps Spiritual Intuition checks while vision is active.
scaling: []
conditions:
- dead
tags:
- ritual
- detection
- healing
text: 'You gain Vision, but it is not as effective for you as your own inspiration.
  Use: 1 free action. Cost: Consuming 1 spirituality point per round. Effect: You
  activate vision, and your vision gains the following benefits: Etheric body: You
  can directly see the health status of the target through the color of the aura,
  directly find out where the other party''s body is uncomfortable, where there is
  a problem, specific to a certain organ, and you can directly see the soul of the
  dead. For more details, see [[Spirit Body Field of View]]. Spiritual body: You can
  confirm whether an object/creature has spirituality, which cannot identify extraordinary
  people. Mental body: You can see whether the o...'
```





You gain **Vision**, but it is not as effective for you as your own inspiration.
- **Use:** 1 free action.
- **Cost:** Consuming 1 **spirituality point** per round.
- **Effect:** You activate vision, and your vision gains the following benefits:


  1. **Etheric body:** You can directly see the health status of the target through the color of the aura, directly find out where the other party's body is uncomfortable, where there is a problem, specific to a certain organ, and you can directly see the soul of the dead.
     - For more details, see [[Spirit Body Field of View]].
  2. **Spiritual body:** You can confirm whether an object/creature has spirituality, which cannot identify extraordinary people.
  3. **Mental body:** You can see whether the other party is thinking, but only so, and you cannot get more detailed information.
  4. **Astral body:** You cannot see the astral body.
  5. When in the state of spiritual vision, your [[Spiritual Intuition Test]] **+1 is beneficial**.

- **Notes:**
  - Creatures that are dead are usually dull in color and cannot be identified.
  - Spiritual materials are usually spiritual, but you cannot determine the corresponding Pathway.
  - The color seen by the spirit vision allows you to see each other in the dark, but you can only see the existence of color, and it is still possible to get lost in the dark.
  - Unlike dead creatures, undead creatures have deep black spirituality color instead of no.
  - As spiritual vision, it belongs to a basic ability of extraordinary people and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.


### Spirit Vision

```yaml ability
id: death-seq-09-spirit-vision
name: Spirit Vision
pathway: death
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
conditions:
- invisible
tags:
- ritual
- detection
text: 'You naturally have Spirit Vision and can directly see some evil spirits. You
  dont need to turn on Spirit Vision; you can also directly use normal vision to find
  spirit creatures. This does not include the advanced invisibility of resentful souls.
  This does not include information creatures. Information creatures are not a kind
  of spirit. When you use 1 Vision to confirm the body of the deceased, your autopsy
  identification +2 is beneficial. Sequence 8: You can discover wraiths in advanced
  invisibility, as well as other hard-to-find spirit creatures. (This is just an explanation;
  it belongs to the same effect as spiritual vision.)'
```





You naturally have **Spirit Vision** and can directly see some evil spirits.

1. You don’t need to turn on Spirit Vision; you can also directly use normal vision to find spirit creatures.
   - This does not include the advanced invisibility of resentful souls.
   - This does not include information creatures. Information creatures are not a kind of spirit.
2. When you use 1 Vision to confirm the body of the deceased, your autopsy identification **+2** is beneficial.
3. **Sequence 8:** You can discover wraiths in advanced invisibility, as well as other hard-to-find spirit creatures.
   - (This is just an explanation; it belongs to the same effect as spiritual vision.)

- **Effect:** Spirit Vision resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
