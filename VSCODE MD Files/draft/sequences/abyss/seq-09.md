---
title: 'Sequence 9: Criminal'
id: abyss-seq-09
tags:
- pathway:abyss
- sequence:9
---






# Abyss Pathway: Sequence 9

## Criminal

- See also: Abyss

> **Lore:** Also known as the “demon” Pathway, corresponding to the Tarot card “demon”. [[Tarot Card — Demon]]

> **Lore:** Unlike a prisoner, a “Criminal” does not suppress themself or feel restrained; body and mind are under the rule of evil desires. Their conscience has not been completely wiped out, and they are not cruel enough. “Criminals” are described as having a strong body, keen perception, and various criminal abilities—whether using knight swords, daggers, longbows, pistols, rifles, or six-barreled machine guns.

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
- In addition, your fighting-related, weapon-use-related, throwing, and criminal skills can quickly grow to proficiency:
  1. Each time you receive 2 hours of corresponding guidance, or conduct 2 hours of corresponding training yourself, your corresponding skills increase by 1 level. It takes 2 times to be trained to be proficient, and only once per day.
  2. For details about criminal skills, see the same criminal skills of different Sequence 9. Criminal Skills (Sequence 9)

- When creating a character that has not just been promoted, you can use the relevant attributes brought by the potion as inspiration to add points for growth skills.
  - The attributes can only add points to your own related skills.
  - The Intuition (INT) attribute itself can add points to any skills.

### Spirit Vision
```yaml ability
id: abyss-seq-09-spirit-vision
name: Spirit Vision
pathway: abyss
sequence: 9
status: adapted
type: toggle
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted check mapping for interpretation tasks while Spirit Vision is active; activation itself is a toggle.
scaling:
- when: spirit_vision_active
  changes:
    effect_note: Spiritual Intuition tests gain +1 beneficial.
tags:
- ritual
- detection
- divination
- utility
text: 'Use: 1 Free Action to activate. Cost: 1 Spirituality per round. Effect: While
  Spirit Vision is active, you gain the following benefits: You gain Spirit Vision
  through your Intuition (INT). Etheric Body: You can directly see the health status
  of the target through the color of the aura, and directly find out where the other
  partys body is uncomfortable, where there is a problem, and it is specific to a
  certain organ. Spiritual Body: You can confirm whether an object/creature has spirituality,
  which cannot identify extraordinary people. Mental Body: You can confirm whether
  the other person is thinking, but you cannot see more content. Astral Body: You
  cannot see the astral body.'
```





- **Use:** 1 **Free Action** to activate.
- **Cost:** 1 **Spirituality** per round.
- **Effect:** While Spirit Vision is active, you gain the following benefits:


- You gain **Spirit Vision** through your Intuition (INT).
  1. **Etheric Body:** You can directly see the health status of the target through the color of the aura, and directly find out where the other party’s body is uncomfortable, where there is a problem, and it is specific to a certain organ.
  2. **Spiritual Body:** You can confirm whether an object/creature has spirituality, which cannot identify extraordinary people.
  3. **Mental Body:** You can confirm whether the other person is thinking, but you cannot see more content.
  4. **Astral Body:** You cannot see the astral body.
  5. When in the state of Spirit Vision, your [[Spiritual Intuition Test]] gains **+1 beneficial**.

- Notes:
  - Dead creatures are usually only dull in color and cannot be identified.
  - Spiritual materials usually have spirituality.
  - The color of the material in Spirit Vision usually represents its corresponding Pathway. This does not mean that you can directly read a Beyonder's power/Pathway details.
  - The color seen by Spirit Vision allows you to see each other in the dark, but you can only see the existence of color, and it is still possible to get lost in the dark.
  - Unlike dead creatures, undead creatures have deep black spirituality color instead of no color. [[Undead]]
  - Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.


### Perception of Depravity

```yaml ability
id: abyss-seq-09-perception-of-depravity
name: Perception of Depravity
pathway: abyss
sequence: 9
status: adapted
type: passive
action: none
cost: {}
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted appraisal token for contested or ambiguous depravity readings while in Spirit Vision.
scaling: []
tags:
- detection
text: 'You are very sensitive to people who have fallen or are falling, and you can
  see black colors on them from your Spirit Vision. Fall is defined as fallen creatures
  or anyone who has violated public morals, no matter what they are for difficulties.
  Difficulty Value Limits: (Fallen Perception is a supplementary description to Spirit
  Vision, which cannot be recorded or stolen.)'
```





- You are very sensitive to people who have fallen or are falling, and you can see black colors on them from your Spirit Vision.
- **Fall** is defined as fallen creatures or anyone who has violated public morals, no matter what they are for difficulties. Difficulty Value
- **Limits:** (Fallen Perception is a supplementary description to Spirit Vision, which cannot be recorded or stolen.)

> **Lore:** Example: There are actually a full one-sixth of the women in Backlund, the capital of Loen, who have worked as street girls, and there are also current female teachers among them. They are all forced to survive, and they have no choice but to do so in order to survive, but they are still considered depraved. [[Backlund]] [[Loen]]
>
> **Lore:** People from other countries will find that in such a conservative country as Ruen, the capital is full of street girls, and they all meet the requirements of the Sequence 5 ceremony of the abyss pathway. [[Ruen]] Abyss Pathway Sequence 5 Ceremony

- **Effect:** Perception of Depravity resolves using its yaml ability block and section prose.


### Intoxicated

```yaml ability
id: abyss-seq-09-intoxicated
name: Intoxicated
pathway: abyss
sequence: 9
status: adapted
type: reaction
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
  heal_roll: "1"
  effect_roll: null
  notes: Triggered sanity restoration by crime severity; mapped as resource recovery tiers with overcap/ritual caveats in scaling.
scaling:
- when: illegal_killing_or_public_safety_endangerment
  changes:
    heal_roll: 1d2
- when: major_crime_killing_blasting_bank_robbery
  changes:
    heal_roll: 2d2
- when: perfect_crime
  changes:
    effect_note: Add +1 fixed sanity restoration to the rolled result.
- when: ritual_window_repeated_activation_within_3_days
  changes:
    effect_note: Restoration converts to sanity loss during the Sequence 5 ritual condition.
- when: sanity_above_cap_for_72_hours
  changes:
    effect_note: Lose 1 sanity from the over-cap pool every 72 hours.
tags:
- detection
- healing
- offense
text: 'You are addicted to the thrill of crime. Trigger: Whenever you complete a criminal
  action. Effect: You restore a certain amount of [[Sanity / Rationality]] according
  to the degree of the crime: Robbing others, stealing valuables: 1 Illegally killing
  others and endangering public safety: 1d2 Serious crimes such as killing, blasting,
  and robbing banks: 2d2 Perfect Crime: On the basis of any of the above benefits
  +1 fixed value. Conditions for a perfect crime: Any of the above-mentioned crimes
  has not been discovered, and has not been detected by the police or officials in
  the end, and has not spread.'
```





- You are addicted to the thrill of crime.
- **Trigger:** Whenever you complete a criminal action.
- **Effect:** You restore a certain amount of [[Sanity / Rationality]] according to the degree of the crime:
  1. Robbing others, stealing valuables: 1
  2. Illegally killing others and endangering public safety: 1d2
  3. Serious crimes such as killing, blasting, and robbing banks: 2d2
  4. **Perfect Crime:** On the basis of any of the above benefits +1 fixed value.
     - Conditions for a perfect crime: Any of the above-mentioned crimes has not been discovered, and has not been detected by the police or officials in the end, and has not spread.
- **Limits:**
  - Sanity / Rationality points can exceed the upper limit, up to twice your sanity value.
  - Every 3 days (72 hours), the sanity beyond the upper limit will lose 1 point.
  - The sanity consumed beyond the upper limit will not be included in the value leading to madness. [[Madness]]

- **Special:** When dealing with the sanity loss of the Sequence 5 Promotion Ceremony, only the second level of crime is valid, and the third level of crime is invalid.
  - Because every time you kill someone, you must perform a specific ritual: eat the internal organs of the other party after killing.
  - In the ritual state, the second level and above of the Intoxicated ability must be activated at least once every 3 days.
    - Repeated activation within these 3 days will change from restoring sanity to reducing sanity.

> **GM Note:** “Eat the internal organs” is presented as the required ritual component after killing, with the rationale that you must remain rational and not overindulgent during the bloodthirsty process.

### Domination of Evil Desires

```yaml ability
id: abyss-seq-09-domination-of-evil-desires
name: Domination of Evil Desires
pathway: abyss
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
- utility
text: After taking the potion, your personality has changed, and your evil desires
  are more prominent than before. When there is a problem that needs to be solved,
  or an item that you covet, improper thoughts will flash in your mind, making you
  more inclined to solve or obtain it in a form that violates ethics, social order,
  and public good customs.
```





- After taking the potion, your personality has changed, and your evil desires are more prominent than before.
- When there is a problem that needs to be solved, or an item that you covet, improper thoughts will flash in your mind, making you more inclined to solve or obtain it in a form that violates ethics, social order, and public good customs.

> **GM Note:** This is a play-by-play explanation; it will not bring about the effect of identification, but it can be used as an introduction to the plot if necessary.

- **Effect:** Domination of Evil Desires resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Killing Skills

```yaml ability
id: abyss-seq-09-killing-skills
name: Killing Skills
pathway: abyss
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
text: 'Effect: Your critical strike, double strike, proximity shooting, and other
  special action identification gains +2 beneficial, excluding first aid and surprise
  attack. Limits: This does not affect special actions that simply gain benefits.
  Momentum and aiming will not change from +2 to favorable (therefore not becoming
  +4); affects identification only. This improvement cannot be recorded or stolen.'
```





- **Effect:** Your critical strike, double strike, proximity shooting, and other special action identification gains **+2 beneficial**, excluding first aid and surprise attack.
- **Limits:**
  - This does not affect special actions that simply gain benefits.
  - Momentum and aiming will not change from +2 to favorable (therefore not becoming +4); affects identification only.
  - This improvement cannot be recorded or stolen.

> **GM Note:** This is also described as an improvement brought by the potion, listed separately.
