---
title: 'Sequence 5: Marionettist'
id: fool-seq-05
tags:
- pathway:fool
- sequence:5
---






# Fool Pathway: Sequence 5

## Marionettist

You can directly affect a target’s **spiritual body**, **astral body**, **mental body**, and **etheric body** by manipulating the **thread of the spiritual body**, then use the bridge of the **etheric body** to control the opponent’s body.

You control the target like manipulating a puppet, making them slow in thinking, stiff in body, and sluggish in movement. This is forced control and is difficult to resist; the target can basically only rely on the strength of their own spirit body to get rid of it.

> **GM Note:** “Under the demigod, there is almost nothing to worry about.”

As time passes and control deepens, the **Secret Puppet Master** can completely turn the target into their own puppet, hide behind the scenes within a certain distance, and manipulate the opponent to fight. In this way, the puppet can use the original extraordinary ability.

- See also: [[id:alias-fool-pathway|Fool Pathway]]

## Advancement

### Auxiliary Materials

- **Main Materials:** [[Dust of the ancient wraith]], [[core crystal of the six-winged gargoyle]]
- **Auxiliary Materials:** 80ml of spring water from the golden spring of [[Sonia Island]], 10g of bark of the [[dragon tree]], [[remnant spirituality of the ancient wraith]], 1 pair of [[six-winged gargoyle eyes]]

### Advancement Ritual

- **Advancement Ritual:** Consuming the potion to the [[id:alias-mermaid-s-song|mermaid's song]] [2]
- **Function:** The mermaid’s singing is a kind of neutralization and balance, which can help resist the corruption of the magical medicine on the thread of the spirit body.

## Acting Rules

- Each **Secret Puppet** has its own settings; follow its settings while manipulating the **Secret Puppet**.
- Manipulate the **Secret Puppet** behind the scenes to appear in front of the scene.
- Guided by the **Secret Puppet**, manipulate the enemy and put on a puppet show.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +1, **Will** +1.

### Spiritual Thread Vision

```yaml ability
id: fool-seq-05-spiritual-thread-vision
name: Spiritual Thread Vision
pathway: fool
sequence: 5
status: canonical
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: 100m
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Detection utility with no explicit contested check in source text.
scaling:
- when: potion_digestion_progress_10
  changes:
    range: 120m
- when: potion_digestion_progress_15
  changes:
    range: 200m
- when: potion_fully_digested
  changes:
    range: 300m
tags:
- detection
- divination
- utility
text: 'You can use the spiritual thread that exists in creatures with spiritual bodies
  to find hidden targets. Use: As a free action, you open astral thread vision (separate
  from [[clairvoyance]]) and gain the benefits below. Effect: You can see countless
  illusory black lines from each creature with a spirit body, corresponding to different
  limbs, densely packed, extending to infinite heights, reaching the end of the void.
  The lines of the spirit body can be seen through walls and are not blocked by matter.
  These illusory black lines cannot be hidden by [[invisibility]] and other abilities.
  Therefore, by locating the spiritual body line, you can find targets in states such
  as [[advanced invisibi...'
```





You can use the **spiritual thread** that exists in creatures with spiritual bodies to find hidden targets.

- **Use:** As a free action, you open astral thread vision (separate from [[clairvoyance]]) and gain the benefits below.
- **Effect:**
  1. You can see countless illusory black lines from each creature with a spirit body, corresponding to different limbs, densely packed, extending to infinite heights, reaching the end of the void. The lines of the spirit body can be seen through walls and are not blocked by matter.
  2. These illusory black lines cannot be hidden by [[invisibility]] and other abilities. Therefore, by locating the spiritual body line, you can find targets in states such as [[advanced invisibility]], [[shadow hiding]], [[information creature]], etc., excluding [[Psychological Invisibility]].
  3. You can only see spiritual threads within 100 meters. If you trace the source of a spiritual thread within your field of vision, you can see the appearance and location of the owner of the spiritual thread, even if the target is hiding in shadows or invisible.
  4. Plants, gremlins, and undead do not have spiritual body threads, but ghosts, resentful souls, spirit world creatures, and undead creatures transformed from extraordinary people (not dead in essence) do. The **GM** decides edge cases.
- **Note:** Corpses do not have astral threads; the **GM** decides whether recently deceased corpses do.
- **Potion digestion progress:**  
  - Potion digestion progress 10: changed to be able to see the thread of the spirit within 120 meters.  
  - Potion digestion progress 15: changed to be able to see the thread of the spirit within 200 meters.  
  - The potion is completely digested: changed to be able to see the thread of the spirit body within a range of 300 meters.

- **Limits:** As described in this section's prose.


### Manipulate Ethereal Threads

```yaml ability
id: fool-seq-05-manipulate-ethereal-threads
name: Manipulate Ethereal Threads
pathway: fool
sequence: 5
status: adapted
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int + @skill.spiritual_intuition
opposed_by: willpower_defense
range: 5m
target: designated target(s)
duration: sustained
dice:
  check_roll: 1d20 + @attr.int + @skill.spiritual_intuition
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Repeated contested checks build manipulation levels; defender formula in prose includes will and constitution terms.
scaling:
- when: target_tier_plus_2
  changes:
    effect_note: 6 successful checks required per +1 manipulation level.
- when: target_tier_plus_1
  changes:
    effect_note: 5 successful checks required per +1 manipulation level.
- when: target_same_tier
  changes:
    effect_note: 4 successful checks required per +1 manipulation level.
- when: target_tier_minus_1
  changes:
    effect_note: 3 successful checks required per +1 manipulation level.
- when: target_tier_minus_2
  changes:
    effect_note: 2 successful checks required per +1 manipulation level.
- when: target_is_ordinary
  changes:
    effect_note: 1 successful check required per +1 manipulation level.
- when: target_in_bloodbath_state
  changes:
    effect_note: Required successes are reduced by 1.
- when: potion_digestion_progress_10_or_higher
  changes:
    effect_note: Required successes are reduced by 1 across the tier table.
- when: potion_fully_digested
  changes:
    effect_note: Additional automatic successes apply after required-success thresholds are reached as described in prose.
tags:
- ritual
- control
- defense
- hard_control
text: 'You control the targets body by manipulating the targets ethereal threads.
  Use: 1 Casting Action. Choose 1 spiritual thread of a target within 5 meters; you
  start turning creatures into marionettes. Check: Use inspiration identification
  to fight against the targets inspiration + will + constitution halved (rounded up).
  Success deepens manipulation progress, representing the strength of the spirit body
  and part of the physical strength (the thread of manipulating the spirit body can
  only be controlled by the spirit body; body strength resistance). Manipulation progress
  (successes required per +1 manipulation level): 1 Targets 2 levels higher than yours:
  After 6 successful identifications,...'
```





You control the target’s body by manipulating the target’s **ethereal threads**.

- **Use:** 1 Casting Action. Choose 1 spiritual thread of a target within 5 meters; you start turning creatures into marionettes.
- **Check:** Use inspiration identification to fight against the target’s “inspiration + will + constitution halved (rounded up)”. Success deepens manipulation progress, representing the strength of the spirit body and part of the physical strength (the thread of manipulating the spirit body can only be controlled by the spirit body; body strength resistance).
- **Manipulation progress (successes required per +1 manipulation level):**  
  ① Targets 2 levels higher than yours: After 6 successful identifications, the manipulation level increases by 1.  
  ② Targets 1 level higher than yours: After 5 successful identifications, the manipulation level increases by 1.  
  ③ Targets at the same level as you: After 4 successful identifications, the manipulation level increases by 1.  
  ④ Targets lower than 1 level: After 3 successful identifications, the manipulation level increases by 1.  
  ⑤ Targets lower than 2 levels: After 2 successful identifications, the manipulation level increases by 1.  
  ⑥ Ordinary people and ordinary creatures: After 1 successful identification, the manipulation level increases by 1.
- **Special (bloodbath):** For creatures in a [[bloodbath state]], the number of identification successes required is reduced by 1.
- **Potion digestion progress 10, 15, 20:** ①②③④⑤⑥ The number of required successes is reduced by 1; when only 1 remains, add 1 additional identification; after digestion, add 2 additional identifications and all are successful by default.
- **Level note:** Low Sequence (9-8), Middle Sequence (7-5), Saints (4-3), Angels (2-1) are all different levels; ordinary people are a separate level; subdivided there is the “[[King of Angels]]” hierarchy.  
  For details, refer to [[Extra: Personal Suppression]]. Here this is only a separate judgment. Like the content of this chapter, only the middle and low sequences will have the benefits of three defenses +10 when facing demigods.

#### Manipulation States

According to the above rules, targets fall into different manipulation states:

- **Before initial manipulation:** A target less than a demigod can’t detect anything wrong, ignoring [[danger premonition]] and [[spiritual intuition]].
- **Being manipulated by the thread of the spiritual body (descriptive):**
  > **Lore:** “I feel that my thinking has become stagnant, as if surrounded by a thick layer of glass… all my actions have begun to become slow motion… like a high-frequency delay.”  
  > **Lore:** Role-playing example: “What ha

- **Effect:** Manipulate Ethereal Threads resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
