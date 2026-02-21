---
title: 'Sequence 5: Druid'
id: earth-seq-05
tags:
- pathway:earth
- sequence:5
---






# Mother Pathway: Sequence 5

You can absorb nutrients and oxygen from the soil, and master earth-like spells.

## Druid

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Master the living habits and physical structure of a variety of ordinary animals and three extraordinary creatures.
  - As an integral part of the ritual, you must write down your accumulated knowledge and experience.

> **Lore:** Image of Extraordinary Characteristics: a group of brown "soil" with roots and hidden "vessels."

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +2, Constitution +2, Agility (DEX) +1, Intuition (INT) +1, Biology +1 skill rank.
- Gain 10 poison resistance.
- Biology and Botany can be quickly improved to **Mastery**.

### **Drain the Earth**

```yaml ability
id: earth-seq-05-drain-the-earth
name: '**Drain the Earth**'
pathway: earth
sequence: 5
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: null
opposed_by: none
range: Touch a point in the soil within 10 meters.
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: 1d6
  effect_roll: "1"
  notes: Heal roll maps the active vitality restoration; effect roll captures the passive 1 vitality per round recovery.
scaling:
- when: passive_breathing_and_regen
  changes:
    effect_note: Passive breathing underground and 1 vitality recovered per round.
- when: mature_plants_present
  changes:
    heal_roll: 3d6
    effect_note: Active restore gains +2d6 vitality when mature plants are present.
tags:
- ritual
text: 'You can extract nutrients and oxygen from the earth. Passive (no action stated):
  You can maintain normal breathing in the ground. Recover 1 Vitality every round.
  Active: Use: 1 Casting Action. Cost: 3 spirituality points. [[Spirituality]] Targeting
  and range: Touch a point in the soil within 10 meters.'
```





You can extract nutrients and oxygen from the earth.

- **Passive (no action stated):**
  - You can maintain normal breathing in the ground.
  - Recover 1 Vitality every round.

- **Active:**
  - **Use:** 1 Casting Action.
  - **Cost:** 3 spirituality points. [[Spirituality]]
- **Targeting and range:** Touch a point in the soil within 10 meters.
  - **Effect:** Recover 1d6 Vitality.
    - If the land has mature plants, recover an additional 2d6 Vitality (deducted from the life of the plant). [[Plant Life / Plant Vitality]]

- **Limits:** As described in this section's prose.


### **Subterranean Sneaking**

```yaml ability
id: earth-seq-05-subterranean-sneaking
name: '**Subterranean Sneaking**'
pathway: earth
sequence: 5
status: adapted
type: active
action: move
cost:
  spirituality: 3
roll: 1d20 + @attr.dex + @skill.stealth
opposed_by: none
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.dex + @skill.stealth
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Stealth check only applies when an opponent actively searches; default underground stealth succeeds unless discovered.
scaling:
- when: each_additional_round_underground
  changes:
    upkeep_cost: {spirituality: 1}
    effect_note: Remaining underground costs 1 spirituality per additional round.
- when: opponent_scouting_check
  changes:
    effect_note: Opponents can contest with Scouting vs your Stealth at +4.
tags:
- ritual
- detection
- stealth
- mobility
text: 'The ground under your feet suddenly softens and turns into a aswamp,a and you
  sink in. Use: 1 movement action. Cost: 3 spirituality points. [[Spirituality]] Effect:
  You enter the ground and can move underground with normal movement power. Each additional
  round you stay underground costs 1 additional spirituality point. Your Stealth test
  underground is successful by default, provided the other party has not found you.
  Otherwise, the other party can use Scouting against your Stealth (with a +4 bonus)
  to find your position. [[Stealth]]'
```





The ground under your feet suddenly softens and turns into a "swamp," and you sink in.

- **Use:** 1 movement action.
- **Cost:** 3 spirituality points. [[Spirituality]]
- **Effect:** You enter the ground and can move underground with normal movement power.

1. Each additional round you stay underground costs 1 additional spirituality point.
   - Your Stealth test underground is successful by default, provided the other party has not found you.
- Otherwise, the other party can use Scouting against your Stealth (with a +4 bonus) to find your position.  
   [[Stealth]]  
   [[Scouting]]
2. You are immune to lightning damage in the ground.
   - If you use underground stealth when lightning comes, you can make a resistance check; on a success, you suffer only half the damage (rounded up).
3. You cannot perform actions other than moving/free actions while underground, unless you use 1 free action to end your underground stealth (you remain underground but are no longer hidden).

- **Limits:** As described in this section's prose.


### **Create Vines**

```yaml ability
id: earth-seq-05-create-vines
name: '**Create Vines**'
pathway: earth
sequence: 5
status: adapted
type: active
action: free
cost:
  spirituality: 3
roll: 1d20 + @attr.str + @skill.biology
opposed_by: physical_defense
range: 1 target within 5 meters.
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.str + @skill.biology
  damage_roll: 1d6
  heal_roll: null
  effect_roll: null
  notes: Baseline maps the vine whip option; ground-piercing and multi-hit options are in scaling.
scaling:
- when: vine_whip_second_hit
  changes:
    check_penalty: -4
- when: vine_whip_third_hit
  changes:
    check_penalty: -6
- when: ground_piercing_vines_mode
  changes:
    action: cast
    range: Choose 1 target within 50 meters.
    check_roll: 1d20 + @attr.int + @skill.biology
    damage_roll: 5d6
    effect_note: Ground-piercing vines erupt from below and can seed Harvest on success.
tags:
- ritual
- defense
- offense
text: 'You create vines out of thin air, causing them to pierce the ground and attack
  enemies. #### Option 1: Vine Whip Use: 1 Attack Action. Cost: 3 spirituality points.
  [[Spirituality]] Effect: Create a vine and treat it as a long whip. Dispelling:
  1 free action dispels it. Targeting and range: 1 target within 5 meters. Check:
  Strength + Biology (Defense) against physical defense.'
```





You create vines out of thin air, causing them to pierce the ground and attack enemies.

#### Option 1: Vine Whip

- **Use:** 1 Attack Action.
- **Cost:** 3 spirituality points. [[Spirituality]]
- **Effect:** Create a vine and treat it as a long whip.
  - **Dispelling:** 1 free action dispels it.
  - **Targeting and range:** 1 target within 5 meters.
- **Check:** Strength + Biology (Defense) against physical defense.  
    [[Physical Defense]]  
    [[Biology (Defense)]]
- **Damage:** 1d6 + half Strength (STR) damage bonus (round up) (physical harm).

- **Special:**
  - The vine can hit 3 times in one Attack Action, split into three identifications:
    - Second hit: -4 disadvantage.
    - Third hit: -6 disadvantage.
- If you suffer more than 10 points of fire damage, the vine is destroyed and the effect ends.

#### Option 2: Ground-Piercing Vines

- **Use:** 1 Casting Action.
- **Cost:** 3 spirituality points. [[Spirituality]]
- **Targeting and range:** Choose 1 target within 50 meters.
- **Effect:** Press your hand to the ground; vines pierce up from the enemy's feet and grow wildly.
  - **Check:** Intuition (INT) + Biology against physical defense. Intuition [[Biology]] [[Physical Defense]]
  - **Damage:** 5d6 physical damage.

- **Special:**
  - The vine created by the Casting Action is regarded as a seed of the harvest ability, which can attack the enemy by itself in the next step.  
    [[Harvest Ability]]

- **Limits:** As described in this section's prose.


### **Toxic Fog**

```yaml ability
id: earth-seq-05-toxic-fog
name: '**Toxic Fog**'
pathway: earth
sequence: 5
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.int + @skill.biology
opposed_by: physical_defense
range: Affects all creatures/plants within a 50-meter cone in front of you.
target: designated target(s)
duration: Fog persists in confined spaces; dissipates after 2 rounds in non-confined
  spaces.
dice:
  check_roll: 1d20 + @attr.int + @skill.biology
  damage_roll: 2d6
  heal_roll: null
  effect_roll: null
  notes: Check roll maps Intuition + Biology vs Physical Defense; damage roll maps poison damage.
scaling:
- when: fog_persists_into_next_round
  changes:
    effect_note: You may re-check each round to deal damage again without additional cost.
tags:
- ritual
- debuff
- defense
- offense
text: 'You cause puffs of yellow-green poisonous gas to spread; creatures who smell
  it start coughing. Use: 1 Casting Action. Cost: 3 spirituality points. [[Spirituality]]
  Targeting and range: Affects all creatures/plants within a 50-meter cone in front
  of you. Check: Intuition (INT) + Biology against physical defense. Intuition [[Biology]]
  [[Physical Defense]] Damage: 2d6 poison damage. Duration: Fog persists in confined
  spaces; dissipates after 2 rounds in non-confined spaces. If the fog persists, at
  the start of each next round you can make another check to cause damage without
  any action.'
```





You cause puffs of yellow-green poisonous gas to spread; creatures who smell it start coughing.

- **Use:** 1 Casting Action.
- **Cost:** 3 spirituality points. [[Spirituality]]
- **Targeting and range:** Affects all creatures/plants within a 50-meter cone in front of you.
- **Check:** Intuition (INT) + Biology against physical defense. Intuition [[Biology]] [[Physical Defense]]
- **Damage:** 2d6 poison damage.
- **Duration:** Fog persists in confined spaces; dissipates after 2 rounds in non-confined spaces.

1. If the fog persists, at the start of each next round you can make another check to cause damage without any action.
2. Creatures below your level (Sequence 9-7) that suffer 1 Toxic Fog damage suffer 1 poisonous effect, and roll 1d5 random poison to be generated; the toxins are random and not necessarily the same each time.  
   [[Poisonous Effect]]  
   [[Random Poison Table (d5)]]
   - Special: Creatures at the same level as yours (Sequence 6-5) receive the effect after suffering 2 damages.
   - Targets higher than you by 1+ Sequence are invalid.

> **GM Note:** When the poisonous mist dissipates, the corresponding effect will be quickly relieved; the lost action is caused by an uncontrollable cough.

- **Effect:** **Toxic Fog** resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### **Incarnation of Animals**

```yaml ability
id: earth-seq-05-incarnation-of-animals
name: '**Incarnation of Animals**'
pathway: earth
sequence: 5
status: canonical
type: active
action: swift
cost:
  spirituality: 6
roll: null
opposed_by: none
range: self
target: self
duration: 5 minutes.
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No explicit dice expression in source text.
scaling: []
tags:
- ritual
text: 'You incarnate as an animal (e.g., a giant bear). Use: 1 Swift Action. Cost:
  3 spirituality points. [[Spirit Points vs Spirituality]] Duration: 5 minutes. Effect:
  Choose one of the following forms: Dire Bear Life limit +10.'
```





You incarnate as an animal (e.g., a giant bear).

- **Use:** 1 Swift Action.
- **Cost:** 3 spirituality points.  
  [[Spirit Points vs Spirituality]]
- **Duration:** 5 minutes.
- **Effect:** Choose one of the following forms:

1. **Dire Bear**
   - Life limit +10.
   - Regarded as a large-scale creature.
   - Strength +2, Constitution +2, Agility (DEX) +1.
   - Gain 3 points of hair armor.
   - Additionally suffer 1d6 fire damage when you transform (once).
2. **Cheetah**
   - Life limit +5.
   - Regarded as a medium-to-large creature.
   - Strength +1, Constitution +2, Agility (DEX) +2.
   - Gain low-light night vision: it works in dim/low light but not in complete darkness.
3. **Coyote**
   - Life limit +5.
   - Strength +1, Constitution +1, Agility (DEX) +1.
   - Gain Extraordinary Sense of Smell (refer to Moon Sequence 7). [[Moon Pathway: Sequence 7]]
   - Gain low-light night vision: it works in dim/low light but not in complete darkness.
4. **Giant Eagle**
   - Life limit +5.
   - Strength +1, Constitution +1, Agility (DEX) +1.
   - Flight speed equals your Mobility.
   - Gain night vision ability.
   - Maximum spotting distance increases to 1 kilometer in clear conditions.
5. **Cats/Dogs**
   - Upper limit of Vitality -5 (the lost Vitality is recovered when the ability is canceled).
   - Regarded as a small and medium-sized creature.
   - Strength -1, Constitution -1, Agility (DEX) +1.
   - Cats gain night vision.
   - Dogs gain Extraordinary Sense of Smell.
   - Special breeds (GM-approved extraordinary breeds) do not reduce Strength and Constitution.

#### Incarnation of Extraordinary Creatures (Partial)

Because extraordinary creatures are half-mad, you can only incarnate part of their limbs; lose 1 Sanity / Rationality for minor incarnations and 1d3 Sanity / Rationality for major ones.  
[[Sanity / Rationality]]

1. **Murloc**
   - Your skin grows phantom scales; your appearance becomes half murloc.
   - Gain 3 points of damage reduction.
   - You are immune to grapple/tackle effects, except for **Clown Precise Control**.  
     [[Clown Precise Control]]
   - Swimming and diving identification gains a **+4 bonus**.  
     [[Swimming and Diving]]

- Because the extraordinary creatures studied by Druids differ during promotion, only the most common murlocs are listed as an example.
- Druids can program 3 more extraordinary creatures by themselves (according to the promotion ceremony); each new extraordinary creature requires 1 week of research to obtain. [[Promotion Ceremony]]
- Druids can also write ordinary, GM-approved creature templates; the data (stat block) must be written in advance.
- The upper limit of extraordinary creatures for high-Sequence Druids (GM decides the threshold) can be changed to be equal to their Intuition (INT), but the ability still needs to be written in advance.

- **Limits:** As described in this section's prose.


### **Biocatalysis**

```yaml ability
id: earth-seq-05-biocatalysis
name: '**Biocatalysis**'
pathway: earth
sequence: 5
status: canonical
type: reaction
action: cast
cost:
  spirituality: 6
roll: null
opposed_by: none
range: All creatures within 50 meters (not limited to plants).
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
text: 'You catalyze the growth of certain organisms, including growth and metabolic
  processes in the body. Use: 1 Casting Action. Cost: 3 spirituality points. [[Spirituality]]
  Targeting and range: All creatures within 50 meters (not limited to plants). Effect:
  Targets gain the catalysis of growth and rate, speeding up function reaction rates.
  The catalytic ability can achieve the following effects: Catalyzed Hair The creatureaTMs
  hair grows wildly and is regarded as an independent aplanta manipulated by you.'
```





You catalyze the growth of certain organisms, including growth and metabolic processes in the body.

- **Use:** 1 Casting Action.
- **Cost:** 3 spirituality points. [[Spirituality]]
- **Targeting and range:** All creatures within 50 meters (not limited to plants).
- **Effect:** Targets gain the catalysis of growth and “rate,” speeding up function reaction rates.

The catalytic ability can achieve the following effects:

1. **Catalyzed Hair**
   - The creature's hair grows wildly and is regarded as an independent "plant" manipulated by you.
   - Every round, use your Intuition (INT) + Biology to fight against the physical defenses of all affected creatures.
     - On success, they are grappled by their own hair.
     - Creatures without hair are instead affected via substitutes (e.g., nose hairs) that grow wildly.
    - Dealing 5 total damage to the **hair** (not the creature) removes the effect.
2. **Catalyzed Injury**
   - Affects targets who:
     - have suffered poison damage but have not received medical treatment, and
     - have Vitality less than half (rounded up) and have not received medical treatment.
   - You catalyze their injuries; they suffer 2d6 of the same type of damage.
3. **Catalyzed Recovery**
   - If the target suffers external damage but still has more than half of their health, **or** the injury has received medical treatment, you catalyze recovery.
   - The target recovers half of their Constitution if untreated, or their full Constitution if treated.
   - See "Spirituality and Other Status Recovery" for details.  
     [[Spirituality and Other Status Recovery]]
    - If you choose Catalyzed Recovery, it does not also trigger Catalyzed Injury even if its conditions are met.
4. **Catalyzed Reaction**
   - You catalyze a creature's chemical reaction rate when combined with a certain type of thing.
   - This ability is not calculated in detail; while you hold this ability, the time required for your biological experiment should be the minimum value.
    - Moon Pathway pharmaceuticals take a minimum of **3 minutes** to finish.  
     Moon Pathway Pharmaceuticals
5. **Catalyzing Extraordinary Characteristics**
   - For creatures that are producing Extraordinary Characteristics, the time to produce Extraordinary Characteristics is halved (rounded down).  
     [[Extraordinary Characteristics]]
6. **Catalytic Metabolism**
   - Within 5 minutes, the creature either:
     - excretes toxins in its body (if it is not medically treated first, this becomes a Catalyzed Injury), or
     - digests what it has eaten.
    - This is invalid for non-biological or otherwise non-metabolizable substances.
7. **Catalyzing Extraordinary Abilities**
   - Reduce the time required for a certain Extraordinary ability being cast:
     - Swift Action -> free action
     - casting/Attack Action -> Swift Action
     - Full-Round Action -> casting/Attack Action
    - Special: When faced with manipulation by the puppet master's spiritual body string, this can only reduce the casting time by **one step** on the action-time ladder (full-round -> casting/attack -> swift -> free).  
     [[Puppet Master Spiritual Body String]]
8. **Catalytic Progress**
   - If an ability has manipulation level and poison level progress, after you use Biocatalysis on the affected target, the caster of that ability can immediately make another corresponding attack test to deepen the progress.  
     [[Progress Tracks (Manipulation/Poison)]]
9. **Catalytic Death**
   - Affects plants that died naturally and have not completely decayed; they regain vitality.

- Other logical, GM-approved uses of catalytic abilities are allowed, provided they do not accelerate physical action speed.

- **Limits:** As described in this section's prose.
