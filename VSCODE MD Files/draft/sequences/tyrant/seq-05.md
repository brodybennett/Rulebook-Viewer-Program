---
title: 'Sequence 5: Ocean Songster'
id: tyrant-seq-05
tags:
- pathway:tyrant
- sequence:5
---





# Tyrant Pathway: Sequence 5

## Ocean Songster

A **Ocean Singer** possesses shallow mastery over lightning, greatly enhanced underwater capability, and the power to influence others through song. Depending on personal disposition, their singing may interfere with a target’s **Spirit Body**, shock foes like thunder, or provoke rage through discordant sound.

> **Lore:** Ocean Singers are said to harmonize with the sea itself, their voices carrying both calm and catastrophe beneath the waves.

---

## Advancement

### Advancement Ritual

- **Ritual:** Consume the potion while inside the stomach of an **Obnish**.

### Advancement Function

After consuming the potion:

- You hear the voices of all creatures across the surrounding sea area.
- The stomach of the **Obnish** blocks and blurs these voices, preventing loss of control during advancement.
- Invisible sound waves continuously burst within your body, causing minor tearing to the **Spirit Body**.
- The mucus lining of the **Obnish** reflects these sound waves back inward, gradually sanding and stabilizing them, similar to material refined in a furnace.
- You involuntarily emit sound during this process.

---

## Extraordinary Abilities

### Attribute Gain

- **Strength** +1  
- **Constitution** +1  
- **Agility (DEX)** +1  
- **Intuition (INT)** +1  
- **Will** +1  
- **Piloting**, **Swimming**, and **Diving** may now be advanced to **Master** level.

---

### Closeness to Marine Life

```yaml ability
id: tyrant-seq-05-closeness-to-marine-life
name: Closeness to Marine Life
pathway: tyrant
sequence: 5
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: sustained
scaling: []
tags:
- ritual
text: You may spiritually communicate with aquatic creatures. Communication allows
  normal conversation. Non-hostile aquatic creatures generally maintain a friendly
  attitude toward you. --
```




- You may spiritually communicate with aquatic creatures.
- Communication allows normal conversation.
- Non-hostile aquatic creatures generally maintain a friendly attitude toward you.

---

- **Effect:** Closeness to Marine Life resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Lightning Mastery

```yaml ability
id: tyrant-seq-05-lightning-mastery
name: Lightning Mastery
pathway: tyrant
sequence: 5
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: physical_defense
range: line of sight
target: 1 creature within line of sight
duration: instant
scaling: []
tags:
- ritual
- control
- defense
- offense
text: 'You gain superficial control over lightning. #### Lightning Strike Cost: 3
  Spirituality Use: 1 Casting Action Target: 1 creature within line of sight Check:
  d20 + 15 Disaster bonus vs. Physical Defense Limits: Ignores Agility (DEX) and Dodge
  Effect:'
```




You gain superficial control over lightning.

#### Lightning Strike

- **Cost:** 3 Spirituality  
- **Use:** 1 Casting Action  
- **Target:** 1 creature within line of sight  
- **Check:** d20 + 15 Disaster bonus vs. Physical Defense  
- **Limits:** Ignores Agility (DEX) and Dodge  
- **Effect:**  
  - Speed is considered lightning-fast.  
  - Deals 3d10 Lightning damage.

**On Hit:**
- Target must immediately pass a Physical Examination (Difficulty 20) or be **Paralyzed**, unable to take movement or attack actions for 1 round.

**On Miss:**
- Lightning disperses into countless electric arcs.
- Creatures within 1 meter that are significantly conductive or **Wet** must still make a Physical Examination or suffer the paralysis effect.

#### Lightning Restraint

- **Dark Creatures:** +1d6 damage  
- **Corrupted Creatures:** +2d6 damage  
- **Undead Creatures:** +3d6 damage  

---

### Thunderous Voice

```yaml ability
id: tyrant-seq-05-thunderous-voice
name: Thunderous Voice
pathway: tyrant
sequence: 5
type: active
action: swift
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- buff
- offense
text: 'Cost: 1 Spirituality per sentence Use: 1 Swift Action Effect: Your voice combines
  with lightning power. Vocal transmission range increases to 5 kilometers. --'
```




- **Cost:** 1 Spirituality per sentence  
- **Use:** 1 Swift Action  
- **Effect:**  
  - Your voice combines with lightning power.
  - Vocal transmission range increases to 5 kilometers.

---

- **Limits:** As described in this section's prose.


### Arrow of Thunder and Lightning

```yaml ability
id: tyrant-seq-05-arrow-of-thunder-and-lightning
name: Arrow of Thunder and Lightning
pathway: tyrant
sequence: 5
type: active
action: swift
cost:
  spirituality: 3
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- offense
text: 'Your hair defies natural law, standing on end and entwined with lightning.
  Cost: 3 Spirituality Use: 1 Attack Action Requirement: Typically used with a bow
  and arrow Choose one of the following modes: Lightning Attachment Additional Cost:
  1 Swift Action Effect:'
```




Your hair defies natural law, standing on end and entwined with lightning.

- **Cost:** 3 Spirituality  
- **Use:** 1 Attack Action  
- **Requirement:** Typically used with a bow and arrow  
- Choose one of the following modes:

1. **Lightning Attachment**
   - Additional Cost: 1 Swift Action  
   - Effect:
     - Lightning from your hair coils around the arrow.
     - Arrow gains +1d6 Lightning damage.
     - Applies Lightning restraint and paralysis effects (misses excluded).

2. **Thunder Attachment**
   - Builds on **Lightning Attachment**.
   - Effect:
     - A bolt of lightning overlays the fired arrow.
     - Arrow becomes pure Lightning damage.
     - Speed is considered lightning.
     - All Lightning effects apply (restraint applies only once).

3. **Extended Application**
   - **Cost:** 1 Spirituality, 1 Swift Action  
   - Effect:
     - Apply **Lightning Attachment** to fists or firearms.
     - May be used in combos, but only one attack in the combo may gain lightning or wind blade effects.

> **Lore:** When Thunder Attachment is used, the lightning-clad arrow resembles a storm cloud gathering midair before striking with unavoidable speed.

**Special Notes:**
- Lightning arrows may critically strike.
- Thunder Attachment may be used with firearms but cannot be combined with other effects.

---

- **Effect:** Arrow of Thunder and Lightning resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Singing

```yaml ability
id: tyrant-seq-05-singing
name: Singing
pathway: tyrant
sequence: 5
type: active
action: free
cost:
  spirituality: 3
roll: null
opposed_by: none
range: 100 meters
target: All creatures within range
duration: sustained
scaling: []
tags:
- ritual
text: 'You may influence creatures through continuous singing. Effects depend on your
  Singing proficiency. Cost: 3 Spirituality per round Use: 1 Free Action (continuous)
  Range: 100 meters Target: All creatures within range This ability does not require
  identification. #### Untrained Effect:'
```




You may influence creatures through continuous singing. Effects depend on your Singing proficiency.

- **Cost:** 3 Spirituality per round  
- **Use:** 1 Free Action (continuous)  
- **Range:** 100 meters  
- **Target:** All creatures within range  

This ability does not require identification.

#### Untrained

- Effect:
  - Chaotic, unpleasant singing enrages enemies.
  - Each round, affected creatures lose 0/1 Sanity / Rationality.
  - All attacks must prioritize the singer.
  - If performing a critical action, a creature may resist with a Will check (Difficulty 20).
- After singing ends, only residual aftereffects remain; rage dissipates.

#### Trained–Proficient

- Effect:
  - Singing simulates thunder and inspires awe.
  - All affected creatures remain in a state of awe until singing ends.

#### Advanced–Master

You interfere directly with a target’s **Spirit Body** using beautiful song. Choose one effect:

**Stunning (Charisma (CHA)):**
- Designate a target.
- Target enters a trance and is **Charmed** by you.
- All maintained abilities (except yours) immediately end.
- Effect lasts up to 1 round; repeated attempts reapply the duration.

Options:
1. **Special Charisma (CHA)**
   - Target must use its Movement Action each round to approach you.
   - Target will not attack you first.
   - Each round, target may resist with a Will check (Difficulty 15).

2. **Partial Resistance**
   - Even on a successful resistance, target is still considered Charmed by you.
   - Suffers –4 to personal skill and attribute checks.
   - Cannot attack you first.

**Enhanced Burst:**
- While singing:
  - Skill and attribute checks gain +2.
  - Damage increases by +1d6.

**Special Rule:**
- For targets of higher than 1 character tier, effect and difficulty are halved.

> **GM Note:** A Beyonder with higher Singing proficiency may intentionally use lower-level Singing effects. Characters with innate musical talent may still require training to sing in incomplete five-tone scales.

- **Effect:** Singing resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
