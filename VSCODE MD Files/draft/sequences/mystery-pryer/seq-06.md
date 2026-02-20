---
title: 'Sequence 6: Scrolls Professor'
id: mystery-pryer-seq-06
tags:
- pathway:mystery-pryer
- sequence:6
---





# Hermit Pathway: Sequence 6

## Scrolls Professor

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition +2
- Your [[Occult]] / [[Occult Language]] can be quickly raised to [[Erudition]] (treat Erudition as the standard skill rank).

### Scroll Scribe

```yaml ability
id: mystery-pryer-seq-06-scroll-scribe
name: Scroll Scribe
pathway: mystery-pryer
sequence: 6
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
text: 'You can transcribe magic into scrolls. Cost: 1 piece of [[Parchment]] (consumed).
  Use: Takes 1 minute to conduct a [[Mystery]] with a difficulty of 25; if the Identification
  is successful, the spell is successfully copied into the scroll. Effect: Spells
  transcribed are limited to the effects of: [[Voyeur Spells]] [[Timber Witchcraft]]
  [[Ritual Magic]]'
```




You can transcribe magic into scrolls.

- **Cost:** 1 piece of [[Parchment]] (consumed).
- **Use:** Takes 1 minute to conduct a [[Mystery]] with a difficulty of 25; if the Identification is successful, the spell is successfully copied into the scroll.
- **Effect:**
  1. Spells transcribed are limited to the effects of:
     - [[Voyeur Spells]]
     - [[Timber Witchcraft]]
     - [[Ritual Magic]]
  2. Transcribed spells may have already been strengthened by [[Knowledge Enhancement]]. Casting a spell that has been strengthened by Knowledge Enhancement through the scroll requires only one Casting Action.
  3. **Scroll** ≠ **Record**: because the scroll can transcribe the effects of Ritual Magic, you can pray to the corresponding gods to obtain extraordinary abilities through Ritual Magic. This process is like a spell, and you cannot transcribe the ability of attack actions.
     - [[Record]]
     - [[Attack Actions]]

#### Using a Scroll

1. One Casting Action: consume 3 [[Spirituality]], read the spell, and activate the scroll to release the magic inside. No roll is required; it can be used directly according to the original ability. This differs from a spell and can be roughly understood as a high-level spell.
2. The shelf life of the scroll is 7 days; the effect will not be reduced.
   > **GM Note:** Usually, there will be no [[Demigod Materials]] to make [[Demigod Scrolls]].

- **Limits:** As described in this section's prose.


### Scroll Improvement

```yaml ability
id: mystery-pryer-seq-06-scroll-improvement
name: Scroll Improvement
pathway: mystery-pryer
sequence: 6
type: active
action: cast
cost: {}
roll: null
opposed_by: physical_defense
range: self
target: self
duration: sustained
scaling: []
tags:
- buff
- defense
- offense
text: 'For an ability copied into a scroll by you that has not obtained Knowledge
  Enhancement (but comes from other means), you can apply Knowledge Enhancement to
  it within the scroll. Use: The moment you craft another Pathway ability scroll,
  choose one benefit to add to the embedded ability. Effect (choose one): Originally
  required continuous maintenance: The scroll cannot continuously maintain the effect.
  Instead, make an Occult check against Will defense; on success, apply the corresponding
  effect for 1d2 rounds. [[Occult check]] Willpower Defense > GM Note: Originally,
  mental abilities are against Will defense; physical damage abilities are against
  [[Physical Defense]]; and those affected by...'
```




For an ability copied into a scroll by you that has not obtained Knowledge Enhancement (but comes from other means), you can apply Knowledge Enhancement to it within the scroll.

- **Use:** The moment you craft another Pathway ability scroll, choose one benefit to add to the embedded ability.
- **Effect (choose one):**
  - **Originally required continuous maintenance:** The scroll cannot continuously maintain the effect. Instead, make an **Occult check** against **Will defense**; on success, apply the corresponding effect for **1d2 rounds**.
    - [[Occult check]]
    - Willpower Defense
    - > **GM Note:** Originally, mental abilities are against Will defense; physical damage abilities are against [[Physical Defense]]; and those affected by poisons and diseases are against Physical Defense.
    - > **GM Note:** Example: [[Requiem of the Dark Night]] requires continuous spellcasting maintenance, but an instant-cast [[Mystic Scroll]] cannot do this.
  - **Originally single-target:** Change it to a group effect, affecting all targets within a radius of **10 meters**.
  - **Originally damage-type:** Increase the original damage by **1d10**; the damage type remains the same as the original ability.
  - **Originally manufacturing:** Gain a **+4 bonus** on checks when manufacturing the corresponding product.
  - **Originally, identification was not an ability of occultism:** When you cast the corresponding ability, it is changed to occult identification.

- **At higher Sequences:**
  - **Sequence 5:** You can choose two improved effects instead; the original scroll needs to be re-transcribed.
  - **Sequence 4:** You can select three improved effects instead; the original scroll needs to be re-transcribed.

> **GM Note:** Although the above scroll improvements may seem to make the Scroll Professor more powerful than the original caster, it is not entirely true. For example, the fireball created in the [[Red Priest]]’s [[Manipulation of Flames]] is **2d10** initial damage, which requires continuous compression of the flames to achieve **4d10** or even **5d10** damage.
>
> The Scroll Professor’s scroll can only do one of the effects of creating fireballs or compressing flames at a time. In other words, compared to a Red Priest, the Scroll Professor can only cause **2d10** damage in the end (there may be an additional bonus of **1d10**), while the Red Priest can cause **4d10** or even **5d10** damage.

- **Effect:** Scroll Improvement resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
