---
title: 'Sequence 7: Serial Killer'
id: abyss-seq-07
tags:
- pathway:abyss
- sequence:7
---





# Abyss Pathway: Sequence 7

## Serial Killer

> **Lore:** You have mastered many forms of demon-worship knowledge and ritual, and you like to please demons through special serial killings. Given enough time, you can summon demonic projections from the depths. You can effectively interfere with divination and channeling. [[id:alias-divination|Divination]] [[Channeling]]

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1, Agility (DEX) +2, Constitution +2, Intuition (INT) +2.
- Your Occult can be quickly promoted to proficient.

### Nether Disturbance

```yaml ability
id: abyss-seq-07-nether-disturbance
name: Nether Disturbance
pathway: abyss
sequence: 7
type: active
action: cast
cost: {}
roll: null
opposed_by: difficulty_value
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- divination
- offense
text: 'Whenever you kill a sentient being, if you make its body into a demon-pleasing
  artwork and draw the ritual symbol corresponding to the demon, you gain the following
  benefits: Choose 1 item of specific mystic information related to you (for example:
  you plan to attack someone next). Make a Mysticism check against the Anti-Divination
  Difficulty Value; this is a mystic identification. [[id:alias-anti-divination|Anti-Divination]]
  [[Mystic Identification]] After success, this information will be excluded in related
  divination, spiritual intuition, and prophecy unless the corresponding difficulty
  is exceeded. A spirit body arranged in advance by a psychic can still provide effective
  information.'
```




Whenever you kill a sentient being, if you make its body into a demon-pleasing artwork and draw the ritual symbol corresponding to the demon, you gain the following benefits:

1. Choose **1** item of specific mystic information related to you (for example: you plan to attack someone next). Make a **Mysticism** check against the **Anti-Divination** Difficulty Value; this is a mystic identification. [[id:alias-anti-divination|Anti-Divination]] [[Mystic Identification]]
2. After success, this information will be excluded in related divination, spiritual intuition, and prophecy unless the corresponding difficulty is exceeded. A spirit body arranged in advance by a psychic can still provide effective information.

- **Effect:** Nether Disturbance resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Demon Burnt Offering

```yaml ability
id: abyss-seq-07-demon-burnt-offering
name: Demon Burnt Offering
pathway: abyss
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
- ritual
text: 'You have mastered knowledge and rituals related to demons. You can use sacrifices
  to please demons and gain benefits. This is essentially a special ritual magic.
  For the most basic process, see [[Common Ritual Magic]]. You can pray to a high-ranking
  person of the abyss path for a response; treat this as a prayer aligned with the
  Abyss. Abyss [[Dark Side of the Universe]] Special: Unlike righteous gods, the ritual
  magic of the abyss will not be responded to unconditionally; sacrifices must be
  made to be favored. *Pleasing Ritual The basis of all demon-worshiping rituals:
  you donaTMt expect anything in return, only to please the demon. Process: Based
  on general ritual magic, after confirmin...'
```




You have mastered knowledge and rituals related to demons. You can use sacrifices to please demons and gain benefits.

- This is essentially a special ritual magic.
- For the most basic process, see [[Common Ritual Magic]].
- You can pray to a high-ranking person of the abyss path for a response; treat this as a prayer aligned with the Abyss. Abyss [[Dark Side of the Universe]]
- **Special:** Unlike righteous gods, the ritual magic of the abyss will not be responded to unconditionally; sacrifices must be made to be favored.

**Pleasing Ritual**

The basis of all demon-worshiping rituals: you donâ€™t expect anything in return, only to please the demon.

- **Process:** Based on general ritual magic, after confirming the current area is watched by demons, bring an intelligent creature to the ritual site and perform the most brutal â€œartâ€ under the gaze of demons to please them.
- **Benefit:** Pleasing rituals bring no benefits, and the demon will not take the body or soul of its victims, but you gain the demonâ€™s favor.
- **Sanity / Rationality:** Completion of â€œArtâ€ performed within the Pleasing Ritual causes you to instantly restore **1** additional sanity, based on intoxication. [[Sanity / Rationality]] [[Intoxication]]
- **Follow-up:** Within **three days**, your next prayer will definitely be answered by this demon if you pre-pay the required sacrifices within that window; that next prayer requires no additional sacrifices.
- **Flexibility:** You can change the pleasing ceremony into other ceremonies on the spot to pray for an immediate response.

> **GM Note:** After a pleasing ceremony is over, there will usually be an extremely horrified scene.

**Gift Ritual**

Demons who show interest and pleasure in you will give you special benefits.

- **Cost:** Sacrifice of at least **2** intelligent creatures.
- **Effect:** The demon will open a mottled and reddish bestowal door to you, or give you power directly.
- In your prayer, you state the benefits you want and choose **one** of the following effects to take effect:

  - **A dangerous reminder:** A piece of parchment tells you who is threatening you and the corresponding information in mystical words. Usually only the most threatening person is named, because the demon also wants to admire your struggle.
  - **The devil's information:** Information the Extraordinary did not know; if not, the GM decides whether it instead provides guidance about what you should do next.
  - **Knowledge of a crime:** Among the attack and crime skills obtained in Sequence 9, choose a skill to increase by **one level**; it cannot exceed the advanced level. The devil bestows the corresponding knowledge into your mind through ravings.
    - Each acceptance of this knowledge requires a **Sanity / Rationality roll**: 1/1d2. [[Sanity / Rationality Roll]]
  - **A grant of power:** A demon-like spell of the Extraordinary, as a lower version of the [[id:alias-sequence-6|Sequence 6]] ability, which can be upgraded to the Sequence 6 level within **24 hours**.
    - To gain this benefit, you require an immediate **Sanity / Rationality check**: 1/1d3. [[Sanity / Rationality Check]]

- **Other requests:** The rest are in line with ritual magic and mentioned in the prayer (such as anti-divination, clearing curses, and cutting off the mystic connection between your own flesh and blood in the hands of others). In line with the most common ritual magic in [[Common Ritual Magic]], each response also requires at least **one** sacrifice. [[Curses]]

**Projection Ritual**

The demon you please decides to help you solve a difficult problem with its own hands.

- **Cost:** Sacrifices of at least **3** intelligent creatures.
- **Summoning effect:** The candles on the altar suddenly rise and turn into heat waves, forming a huge demon projection to fight for you within the scope of the ritual magic. [[Demon Projection]]
- **Persistence:** Demon projections have no health, but disappear once the altar of ritual magic is broken.
- **Protection model:** The demon projection protects the altar. You must pay **spirituality**, and the spirituality paid is treated as the damage the demonic projection can withstand while protecting the altar. [[Spirituality]]
  - For each intelligent creature sacrificed, the altar can withstand **+10** damage.
  - Once cumulative damage suffered exceeds the total the altar can withstand, the demon projection disappears immediately, and the ritual magic is also damaged.
- **Defenses while protecting the altar:** When protecting the altar, the projection is considered as a whole with the altar:
  - Physical Defense: **15**
  - Will defense: **15**
  - No additional effects modify Physical Defense beyond the fixed value above.
  - Damage reduction: **5**
  - Fire resistance: **5**
  - Cold resistance: **5**
  - Immunity to toxins/poison.
- **Rank/pressure:** The person projected by the demon is considered a demigod (saint) and thus receives the benefit of [[Extra: Person Suppression]]. [[id:alias-demigod|Demigod]]

- **Limits:** As described in this section's prose.
