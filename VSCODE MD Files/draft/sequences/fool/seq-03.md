---
title: 'Sequence 3: Scholar of Yore'
id: fool-seq-03
tags:
- pathway:fool
- sequence:3
---






# Fool Pathway: Sequence 3

## Scholar of Yore

> **Lore:** Scholars from antiquity who study antiquity-witnessing fate, influencing the present, and never reversing the past.

### Help from History

You can seek help from history in two ways:

- **Borrow strength from your past self:** Each use lasts **5 minutes**.
- **Summon images from the pores of history:** You can summon images of **people** or **objects**.
  - The more detailed and true your understanding of the relevant history and subject, the greater the probability of success and the longer the duration.
  - When summoning people or objects of a higher **Sequence** than your own, the projection manifests only part of the power and characteristics.

Limits for images summoned from the pores of history:

- **Simultaneous limit:** You can maintain **up to 3** historical images at the same time, including those summoned by **marionettes** [[Marionette]].
- **Maximum duration:** A summoned image can last **up to 1/4 hour**.

### Paper Doll Substitute Additions

In addition to transferring diseases, wounds, curses, attacks, prophecies, and gazing, **paper doll substitute** [[paper doll substitute]] can also transfer a certain part of the paper doll to the target:

- The transferred part runs like a real one before it is found to be fake.

Additional parameters and related effects:

- **Initial control time:** 2 seconds.
- **Then:** transformed into a puppet for 10 seconds.
- **Control range:** 500 meters.
- **Marionette driven; position exchange limit:** 5 kilometers. [[position exchange]]
- **"Flame jump" distance:** 5 kilometers. [[flame jump]]
- There is a certain limit to the difference in body size.
- Simulated organs may be useful or just for display.
- Create fog and lower the temperature.

## Advancement

### Main Materials

- A pair of eyes of Fulgrim's dog (also known as the Guardian of Origin Castle) [[Fulgrim's dog]] [[Origin Castle]]
- A flocculated heart of the Mist Demon Wolf [[Mist Demon Wolf]]

### Auxiliary Materials

- 100 ml of Fulgrim's dog's blood [[Fulgrim's dog's blood]]
- 30 g of hoarfrost crystals from Mist Demon Wolf [[hoarfrost crystals]]
- A large number of real ancient historical records [[ancient historical records]]

### Advancement Ritual

- Completely divorced from reality for at least three hundred years.
- Take potions after you have become history and do not belong to the current era.

### Playing the Code

- Scholars from Antiquity and the Study of Antiquity
  1. From ancient times and research ancient times.
  2. Can research things from history.
  3. Witness fate, influence the present, and cannot reverse the past.

## Extraordinary Abilities

### Attribute Gain

- **Intuition (INT)** Intuition +1
- **Education** [[Education]] +2
- **History skill** [[History skill]] increased by 1 skill level

### Summon Historical Images

```yaml ability
id: fool-seq-03-summon-historical-images
name: Summon Historical Images
pathway: fool
sequence: 3
status: adapted
type: active
action: swift
cost:
  spirituality: 2
roll: 1d20 + @attr.edu + @skill.knowledge
opposed_by: difficulty_value
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.edu + @skill.knowledge
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted mapping for the explicit historical appraisal check; additional costs and DV shifts are applied per mode/familiarity.
scaling:
- when: baseline_historical_appraisal
  changes:
    dv: 20
- when: summoning_extraordinary_item
  changes:
    additional_cost: 1
- when: summoning_extraordinary_creature
  changes:
    additional_cost: 3
- when: summoned_extraordinary_creature_uses_ability
  changes:
    additional_cost: 2
- when: history_is_familiar
  changes:
    effect_note: Difficulty Value is reduced (repeatedly summoned items can drop to around DV 10).
- when: history_is_unfamiliar
  changes:
    effect_note: Difficulty Value increases.
- when: potion_fully_digested
  changes:
    effect_note: Total summon/scene limit increases by 2.
- when: sequence <= 2
  changes:
    effect_note: Total summon/scene limit becomes 9, with only 3 angel-level summons.
tags:
- ritual
- stealth
- summon
- utility
text: 'Use: Once per round; Swift Action. Cost: Consume 2 points of Spirituality [[Spirituality]].
  Check: Perform a historical appraisal [[historical appraisal]] with Difficulty Value
  Difficulty Value 20. Effect (on success): Summon up to 1 of the following from history:
  Items you once owned, or Humans you knew. Additional usage modes and actions: Fog
  of history: You may enter the fog of history [[fog of history]] that you know and
  hide in a historical scene you once knew. In reality, it is difficult to find your
  body without similar means.'
```





- **Use:** Once per round; **Swift Action**.
- **Cost:** Consume 2 points of **Spirituality** [[Spirituality]].
- **Check:** Perform a **historical appraisal** [[historical appraisal]] with **Difficulty Value** Difficulty Value 20.
- **Effect (on success):** Summon up to 1 of the following from history:
  - Items you once owned, or
  - Humans you knew.

Additional usage modes and actions:

- **Fog of history:** You may enter the **fog of history** [[fog of history]] that you know and hide in a historical scene you once knew. In reality, it is difficult to find your body without similar means.
- **False existence via self-projection:** You can enter the **historical projection** [[historical projection]] of yourself that you summoned in the fog of history, make it your substitute in reality, become a "false" existence, and gain your consciousness.
- **Entering the fog of history:** **Move Action**.
- **Dismissing the historical projection:** **free action**.

Costs and difficulty adjustments (as stated):

- Summoning ordinary objects requires almost no consumption of Spirituality.
- If you want to summon extraordinary items, you need 1 Spirituality point.
- To summon extraordinary creatures, you need at least 3 Spirituality points.
- When a summoned extraordinary creature uses extraordinary abilities, treat **2 Spirituality** as the base additional cost; stronger abilities may require more at GM discretion.

Difficulty modifications by familiarity:

- A certain piece of history that you are not familiar with will add to the Difficulty Value.
- The history you are familiar with will reduce the Difficulty Value.
- Example: the Difficulty Value of items you summon repeatedly can be reduced to 10.

Operational limitations and risks:

- The Spirituality used by historical projection consumes your own Spirituality, including the summoned characters.
- Summoned characters have no intelligence and no dialogue-only instinct. Combat is fought only through instinct or your manipulation.
- If you communicate with the owner of the historical projection in advance and make arrangements in advance, then they can feel the historical projection after you summon it, resonate with it, and then manipulate the historical projection to join the battle and fight on behalf of you.
  - In other words, especially angel-level existence, when you summon the historical projection, they can perceive that the historical projection is summoned. [[Angel-Level]]
- The object you summon should not be your enemy-at least, they cannot be your enemy in the period you summoned-because the historical projection relies only on instinctive actions. If you do not control it (or at the moment you come out), its instinct may attack you, potentially causing you to be backstabbed by your own projection.
- The maintenance time of historical projection is limited. If you use it to summon food, it will disappear after you eat it.
- The historical projection can't play the full ability. When the historical projection is identified:
  - Total identification is -4.
  - Damage caused each time is -4 (calculated according to the number of times damage is caused; if an attack is 1d4+2d10, there is more than one damage die, but as long as it is a single attack that only hits once, rather than several hits, the damage reduction takes effect only once).
- The historical projection cannot exert the effect of full ability, and it is still effective when the historical projection has obtained the consciousness of the ontology. [[Ontology]]
- If someone summons your historical projection, you can also participate in the battle in a similar way (by resonating/manipulating through it), but your will may also be captured through the historical projection.
  - Across the historical projection can usually halve the **sanity blow** [[sanity blow]] you suffer, but it also means that if you do not enter the fog of history to hide in advance, your body may be in danger because your will has entered the historical projection.
- **Warning:** If you enter the hole of your historical image and are cut off from your ontology, it is almost predictable that your ontology will inevitably lose control.

Progress notes (as written):

- **Completely digested potion:** Increase your total summon/scene limit by 2.

- **Master of Miracles** [[Master of Miracles]]: Your total summon/scene limit becomes 9, and you can summon familiar scenes, but there are still only three summons at the angel level.

- **Effect:** Summon Historical Images resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Restoring Your Self

```yaml ability
id: fool-seq-03-restoring-your-self
name: Restoring Your Self
pathway: fool
sequence: 3
status: adapted
type: active
action: swift
cost:
  spirituality: 15
roll: 1d20 + @attr.int + @skill.occultism
opposed_by: difficulty_value
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.occultism
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted check model for disruption-sensitive scenes; successful resolution restores the user to full health as stated in prose.
scaling:
- when: successful_resolution
  changes:
    effect_note: Health returns to maximum.
tags:
- ritual
- healing
text: 'Use: Once per round; Swift Action. Cost: 15 Spirituality points. Effect: Your
  health returns to maximum.'
```





- **Use:** Once per round; **Swift Action**.
- **Cost:** 15 Spirituality points.
- **Effect:** Your health returns to maximum.

- **Limits:** As described in this section's prose.


### Paper Doll Stand

```yaml ability
id: fool-seq-03-paper-doll-stand
name: Paper Doll Stand
pathway: fool
sequence: 3
status: adapted
type: active
action: swift
cost:
  spirituality: 8
roll: 1d20 + @attr.cha + @skill.deception
opposed_by: difficulty_value
range: self
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.cha + @skill.deception
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted to model the false-vitality deception pressure; target-side truth checks and awareness collapse are handled by the listed DV branch.
scaling:
- when: target_discerns_truth_with_intuition_dv_15
  changes:
    effect_note: False restored Vitality disappears instantly.
- when: target_is_told_or_realizes_truth
  changes:
    effect_note: False restored Vitality disappears instantly.
tags:
- ritual
- healing
- mobility
- offense
text: 'Use: Once per round; Swift Action. Cost: 8 Spirituality points, and a paper
  figure [[paper figure]]. Effect: You can keep a physically disabled creature moving.
  You instantly restore a creatureaTMs full hit points and remove any disadvantage
  it has from critical attacks. Limit/Truth check: The restored hit points are false
  if the target becomes aware (told or realizes), or discerns the truth with a Difficulty
  Value 15 Intuition (INT) check; then these restored Vitality disappear instantly.'
```





- **Use:** Once per round; **Swift Action**.
- **Cost:** 8 Spirituality points, and a paper figure [[paper figure]].
- **Effect:** You can keep a physically disabled creature moving. You instantly restore a creature's full hit points and remove any disadvantage it has from critical attacks.
- **Limit/Truth check:** The restored hit points are false if the target becomes aware (told or realizes), or discerns the truth with a Difficulty Value 15 Intuition (INT) check; then these restored Vitality disappear instantly.

- **Limits:** As described in this section's prose.


### Fog Creation

```yaml ability
id: fool-seq-03-fog-creation
name: Fog Creation
pathway: fool
sequence: 3
status: canonical
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: Usually only 100 meters in radius.
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
text: 'Use: spellcasting action. Cost: Does not need to consume Spirituality. Effect:
  Fill a certain area around you with gray mist (fog from history). The fog can make
  people hallucinate to a certain extent; most content comes from the past, but usually
  cannot have effective effects. Range: Usually only 100 meters in radius. It can
  block the vision and spiritual vision [[id:alias-spiritual-vision|spiritual vision]]
  of demigods [[Demigod]] and below in the area. From the demigod stage, one can use
  spiritual vision to see through the fog. Only the spirit vision of the Wheel of
  Fortune pathway can still exert its normal effect in this fog, barely identifying
  the target.'
```





- **Use:** **spellcasting action**.
- **Cost:** Does not need to consume Spirituality.
- **Effect:** Fill a certain area around you with gray mist (fog from history).
  - The fog can make people hallucinate to a certain extent; most content comes from the past, but usually cannot have effective effects.
  - **Range:** Usually only 100 meters in radius.
  - It can block the vision and spiritual vision [[id:alias-spiritual-vision|spiritual vision]] of demigods [[Demigod]] and below in the area.
  - From the demigod stage, one can use spiritual vision to see through the fog.
  - Only the spirit vision of the Wheel of Fortune pathway can still exert its normal effect in this fog, barely identifying the target.
  - It can reduce the surrounding temperature and extinguish flames to a certain extent.

> **GM Note:** Other than the effects listed above, this is described as having no more uses and being a non-core skill.

- **Sequence 2 note:** The range of the fog is increased to a radius of one kilometer. [[id:alias-sequence-2|Sequence 2]]

- **Limits:** As described in this section's prose.
