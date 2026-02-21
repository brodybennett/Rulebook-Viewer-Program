---
title: 'Sequence 3: High Summoner'
id: moon-seq-03
tags:
- pathway:moon
- sequence:3
---






# Moon Pathway: Sequence 3

## High Summoner

> **Lore:** With the influence of the moon on the [[Spirit World]], the Summoner Master summons powerful creatures from its depths to help them. If the summoner’s “popularity” is good enough, they can even sign a [[Contract]] with [[Angels]] and summon them directly.  
> Occasionally, uncontrollable changes occur during a Summoner Master’s summoning, causing strange creatures that do not come from the Spirit World—and have not signed a contract—to descend into reality. Rumors say this points to a boundless, dark universe. Some Summoner Masters died because of these mutations; others gained powerful abilities or items different from the twenty-two sequences.  
> In addition to summoning, Summoner Masters are also outstanding magic masters in moon and dark realms.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** In a full moon or blood moon, the reality and the Spirit World in a certain area are completely blended together, and countless powerful beings from the depths of the Spirit World are subdued alone, and the Spirit World and reality are separated again, but an entrance of interweaving between reality and the Spirit World is left behind. In the dividing line of the two worlds—being in the real world and the spirit world at the same time—take the [[Potion]] under the illumination of the full moon. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2, **Will** +1, and your **Occultism** increases by 1 level.

### Gate of Summoning

```yaml ability
id: moon-seq-03-gate-of-summoning
name: Gate of Summoning
pathway: moon
sequence: 3
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
- mobility
text: 'The Gate of Summoning opens an illusory door to the depths of the Spirit World
  so you can contract a creature into service. Cost: Consume 5 points of Spirituality.
  [[Spirituality]] Use: Through a Casting Action, open the illusory door leading to
  the depths of the Spirit World, sign a contract with the creature, and let it come
  to the real world to serve. Casting Action Limits: Only one per Encounter. *Summoned
  creature determination Use a Lucky Appraisal to determine the type of creature to
  be summoned. [[Lucky Appraisal]] For ease of calculation, its panel is equal to
  the summoner itself. When the difficulty is full, a +1 gain will be obtained based
  on the knowledge level of each month....'
```





The **Gate of Summoning** opens an illusory door to the depths of the Spirit World so you can contract a creature into service.

- **Cost:** Consume 5 points of **Spirituality**. [[Spirituality]]
- **Use:** Through a **Casting Action**, open the illusory door leading to the depths of the Spirit World, sign a contract with the creature, and let it come to the real world to serve. Casting Action
- **Limits:** Only one per Encounter.

**Summoned creature determination**
- Use a **Lucky Appraisal** to determine the type of creature to be summoned. [[Lucky Appraisal]]
- For ease of calculation, its panel is equal to the summoner itself.
- When the difficulty is full, a +1 gain will be obtained based on the knowledge level of each month. GM decides the exact trigger and scope.

**Difficulty outcomes**
- **Difficulty 10:** Spirit World creatures that are one Sequence weaker than themselves.
- **Difficulty 15:** Spirit World creatures of the same Sequence level as oneself.
- **Difficulty 20:** Spirit World creatures with the same Sequence level as yourself, but slightly stronger (all skill identification extra +4, damage +3).
- **Difficulty 25:** A Spirit World creature with a Sequence higher than itself will start to be out of control after five rounds.

**Great success**
- The Spirit World creatures chosen one Sequence higher than oneself will be in a controllable state for the entire encounter, and +10 Vitality on this basis.
- At this time, the second Lucky Appraisal is performed. If the difficulty is higher than 15, the Alien Pathway will be summoned. (GM draws themselves, not necessarily higher or lower than their own Sequence level; the Alien Pathway will usually directly be an alien creature, not a Spirit World creature.)

**Big failure**
- Summon a high-path spirit creature that attacks indiscriminately; pass a Difficulty 15 Lucky Appraisal again to judge whether it is stronger than the summoner, and conduct a third Difficulty 20 Lucky Appraisal to determine whether it is an Alien Pathway, or aliens. (GM self-made; big failure summons are usually extremely dangerous enemies.)

**Arrival timing, blockage, and retries**
- If the Sequence level of the summoned creature is higher than the Sequence level of the holder, it needs to arrive at the scene after the end of the current round after being summoned, and this process may cause the summoning to be blocked.
- A failed summoning is not considered to have consumed a use opportunity; the summoner can re-summon to allow that existence to arrive at the scene.

**Summoning Gate statistics and interactions**
- The **Summoning Gate**’s Vitality is regarded as half of the Summoner Master’s Vitality.
- The Summoning Gate enjoys the Summoner Master’s life recovery and its weaknesses, and it gains the same restraint bonuses against undead that the summoner has.
- If the summoner themself is not Sequence 3, then the Summoning Gate’s Vitality defaults to 40, and it enjoys the same [[Defense Value]] as the summoner themself.
- If half of the life value of the summoner in Sequence 3 is less than 40, the door’s life value will be processed as 40 by default.

**Defense Value inheritance and item scaling**
- The Defense Value inherited by the Summoning Gate is the base value of the summoner themself.
- If it is improved through [[Extraordinary Items]], a similar effect needs to be exerted on the Summoning Gate in order for it to obtain the corresponding bonus.
- Unless the addition of this item itself includes the Gate of Summoning, or the improvement obtained is the improvement of one’s own personality or the level of spellcasting, the Gate of Summoning can also be strengthened accordingly.

**Targeting and empowerment**
- A summoning portal is considered a friendly target unless the summoned being is malicious.
- Summoning Gates can be empowered by other empowerment spells.

**Sequence 2 notes**
- **Sequence 2:** Spirit World creatures that are stronger than themselves; their Sequence level will be limited by the current Pathway (for example, if there is Sequence 0, there is no Sequence 1).
- As a compensation, the relevant rewards can be exchanged for the existence of mixed pathways, and an extra +1 for the number of times the Gate of Summoning can be used; it can only be +1 at most, or a Spirit World creature that can be perfectly controlled.
- Except for the Big failure and the Alien Pathway, all Spirit World creatures summoned at the second level of the Sequence will be controllable until the end of the encounter.

- **Effect:** Gate of Summoning resolves using its yaml ability block and section prose.
