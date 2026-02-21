---
title: 'Sequence 9: Planter'
id: earth-seq-09
tags:
- pathway:earth
- sequence:9
---






# Mother Pathway: Sequence 9

## Planter

- See also: [[Mother]]
- **Pathway trait:** Earth is a purely feminine **Pathway**. At the beginning of Earth Pathway: Sequence 2, you become female.
- You can distinguish different seeds and have high strength.
- You can tell the time of day and are good at predicting the weather.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** [[Strength]] +2, [[Constitution]] +2, Agility (DEX) +1, Intuition +1.
- > **GM Note:** You can better learn the knowledge of planting.

### Planting Growth

```yaml ability
id: earth-seq-09-planting-growth
name: Planting Growth
pathway: earth
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
text: Every time you receive at least 2 hours of real, non-repetitive related guidance,
  choose [[Agriculture]] or [[Botany]]; the chosen skill increases by 1 level. Botany
  can be promoted up to Proficient at most. Agriculture can be rapidly promoted up
  to Proficient at most. From training to proficiency, to advanced, to mastery, you
  need to learn 2, 3, 4 times; this section caps growth at Proficient. Successfully
  cultivating a seed through the stage of flowering and fruiting is also regarded
  as a growth. Cultivating duplicate seeds does not improve growth. When creating
  a character who has not just been promoted, growth skills gain 2x Intuition (INT)
  points from the potion.
```





- Every time you receive at least **2 hours** of real, non-repetitive related guidance, choose [[Agriculture]] or [[Botany]]; the chosen skill increases by **1 level**.
  - Botany can be promoted up to Proficient at most.
  - Agriculture can be rapidly promoted up to Proficient at most.
  - From training to proficiency, to advanced, to mastery, you need to learn **2, 3, 4** times; this section caps growth at **Proficient**.
- Successfully cultivating a seed through the stage of flowering and fruiting is also regarded as a growth.
- Cultivating duplicate seeds does not improve growth.
- When creating a character who has not just been promoted, growth skills gain **2x Intuition (INT)** points from the potion.

- **Effect:** Planting Growth resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Identify Seeds

```yaml ability
id: earth-seq-09-identify-seeds
name: Identify Seeds
pathway: earth
sequence: 9
status: adapted
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: One seed within your field of vision.
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d3
  notes: Effect roll maps crop growth/harvest tables; specific crop timings and yields are captured in scaling.
scaling:
- when: vegetable_food_growth
  changes:
    effect_roll: 1d2
    effect_note: Vegetable crops mature in 1 + 1d2 weeks.
- when: tree_plant_growth
  changes:
    effect_roll: 1d3
    effect_note: Tree plants mature in 2 + 1d3 years.
- when: beverage_raw_material_growth
  changes:
    effect_roll: 1d4
    effect_note: Beverage raw materials mature in 1 + 1d4 years.
- when: energy_crop_growth
  changes:
    effect_roll: 1d5
    effect_note: Energy crops mature in 2 + 1d5 months.
- when: landscaping_growth
  changes:
    effect_roll: 1d3
    effect_note: Landscaping plants mature in 1d3 months.
- when: spice_medicinal_growth
  changes:
    effect_roll: 1d3
    effect_note: Spices/medicinal plants mature in 1d3 months.
- when: restoration_herb_growth
  changes:
    effect_roll: 1d3
    effect_note: Restoration herbs mature in 1d3 weeks.
- when: analgesic_herb_growth
  changes:
    effect_roll: 1d3
    effect_note: Analgesic herbs mature in 1d3 weeks.
- when: spiritual_fruit_growth
  changes:
    effect_roll: 1d2
    effect_note: Spiritual fruits mature in 1d2 months.
- when: fragrant_flower_growth
  changes:
    effect_roll: 1d3
    effect_note: Fragrant flowers mature in 1d3 weeks.
- when: spiritual_material_growth
  changes:
    effect_roll: 1d3
    effect_note: Spiritual medicinal materials mature in 1d3 weeks.
- when: ordinary_crop_harvest_yield
  changes:
    effect_roll: 4d6
    effect_note: Ordinary harvest yields 4d6 (reroll results below 5).
- when: extraordinary_crop_harvest_yield
  changes:
    effect_roll: 3d6
    effect_note: Extraordinary crops yield 3d6 and wither after 1 week.
tags:
- ritual
- detection
text: 'Use: 1 Casting Action Casting Action. Cost: None (does not consume [[Spirituality]]).
  Targeting and range: One seed within your field of vision. Effect: Immediately learn
  the seeds type and state, the result of planting it, and what needs attention when
  planting (temperature, weather, soil, etc.). With precise identification, you can
  plant many strange plants that are difficult for ordinary people, improving your
  life. #### Plants You Can Grow 1) Ordinary crops: Crops that do not possess extraordinary
  power and belong to the field of ordinary things. Vegetable food: Harvest after
  1 + 1d2 weeks (e.g., corn, tomato, potato); no need to worry about food sources.'
```





- **Use:** 1 **Casting Action** Casting Action.
- **Cost:** None (does not consume [[Spirituality]]).
- **Targeting and range:** One seed within your field of vision.
- **Effect:** Immediately learn the seed’s type and state, the result of planting it, and what needs attention when planting (temperature, weather, soil, etc.).
- With precise identification, you can plant many strange plants that are difficult for ordinary people, improving your life.

#### Plants You Can Grow

1) **Ordinary crops:** Crops that do not possess extraordinary power and belong to the field of ordinary things.
- **Vegetable food:** Harvest after **1 + 1d2 weeks** (e.g., corn, tomato, potato); no need to worry about food sources.
- **Tree plants:** Bear fruit after **2 + 1d3 years** (e.g., citrus, peaches, pears, strawberries), ranging from once a year to multiple times a year.
- **Beverage raw materials:** Result after **1 + 1d4 years** (e.g., tea, coffee, cocoa, sugar cane); can be used to make drinks.
- **Fiber plants:** Harvest after **2 + 1d3 months** (e.g., cotton, hemp, flax, bamboo); can be used to make fibers.
- **Energy crops:** Harvest after **2 + 1d5 months** (e.g., wood, fuel charcoal, biogas, biofuel, corn, sugar beets); can be used for wine making, then for making alcohol, or for fuel.
- **Landscaping plants:** Mature after **1d3 months** (e.g., roses, sunflowers, spider plants, flowers, potted plants, lawns, shrubs).
- **Spices/medicinal plants:** Mature after **1d3 months** (e.g., mint, rosemary, ginseng and other medicinal materials); can be used in Pharmacist Pathway: Sequence 9.

**Harvest (ordinary crops):** Whenever any of the above plants mature:
- A single plant yields **4d6** lumber/fruit harvest; reroll if the result is **less than 5**.
  - Lumber refers to the calculated amount after cutting.
- Because different plants produce different numbers of seeds, it is defaulted that as long as you have planted a crop once, you can plant it regardless of seed count.
  - You cannot exceed **ten times** the original number unless you can indeed provide **hundreds of seeds**.
- > **GM Note:** Other common crops allowed by the **GM**, and self-created hybrid species.

2) **Extraordinary crops:** Crops with a certain extraordinary effect; they only have very basic spirituality.
- **Restoration Herbs:** Harvest after **1d3 weeks**. After being used for [[Medical identification]], restore **1d3 Vitality** immediately. Can only be used **once every 24 hours**.
- **Analgesic herbs:** Harvest after **1d3 weeks**. Provide partial analgesia on a smeared area, or short-term analgesia for the whole body. Within **5 minutes**, the corresponding part-of-body/whole-body [[Physical fitness identification]] is successful by default; therefore you will not be able to detect injuries with the help of pain perception.
- **Spiritual Fruits:** Harvest after **1d2 months**. Vegetables whose appearance is not much different from ordinary crops; can be used to maintain physical fitness. After eating this kind of fruit for **3 months**, your initial physical fitness **+1** (up to **2 points**), and cannot exceed the initial **6 points**.
  - **Special:** Different types of fruits can also improve strength/charisma/agility, and only one type can be eaten at the same time.
- **Fragrant flowers and plants:** Grow completely after **1d3 weeks**. Spread fragrance within **100 meters** and grant **1 extra** [[Sanity / Rationality point]] in the area; it can be deducted and not included in the [[Crazy value]]. After **24 hours**, the extra sanity point is recovered.
- **Spiritual medicinal materials:** Growth completes after **1d3 weeks**. Can be used for the regular medicinal materials required by the Moon Pathway: Sequence 6 potion professor.

**Harvest (extraordinary crops):**
- Each extraordinary crop yields a corresponding harvest of **3d6**.
- The extraordinary crop gradually withers after **1 week**.
- > **GM Note:** Other extraordinary crops allowed by the **GM**. The names above are general examples (like “energy crops” as a broad category); there are more subdivisions, and you can also create poisonous extraordinary crops.

#### Starting Crops (Not Just Promoted)

- If a cultivator has not just been promoted:
  - Choose crops equal to your number of Intuition before [[Joining the regiment]]; you are regarded as having harvested the corresponding results.
  - Crops equal to **five times** your Intuition (INT) are deemed to have been planted; you must select the location of the field.
- To expand this upper limit, you must increase your [[Reputation Level]].
  - For every level of reputation higher than [[Advanced level]], the two benefits above are doubled.
- > **GM Note:** This essentially determines whether you have a place as large as a manor for farming.

#### Rejuvenation Judgment of Spiritual Fruit

Obtain the recuperation benefits of the corresponding spiritual fruit according to the digestion degree of the [[Extraordinary cultivator potion]] (if you insist on taking it):

- [[Potion digestion progress]] **5:** Choose **1** spiritual fruit; increase the attribute **+1**.
- Potion digestion progress **10:** Choose **2** spiritual fruits; increase the attribute **+1**.
- Potion digestion progress **15:** Choose **3** spiritual fruits; increase the attribute **+1**.
- The potion is completely digested: Choose **4** spiritual fruits; increase the attribute **+1**.
- Higher-order Extraordinary: By default, you have obtained all the recuperation benefits of the spiritual fruit.
- **Special:** If the Extraordinary reaches the corresponding digestion progress without knowing how to act, the number of benefits is doubled.

- **Limits:** As described in this section's prose.


### Telling the Time of Day

```yaml ability
id: earth-seq-09-telling-the-time-of-day
name: Telling the Time of Day
pathway: earth
sequence: 9
status: adapted
type: active
action: cast
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: 1d3
  notes: Effect roll maps the per-day seasonal forecast table.
scaling:
- when: additional_day_forecast
  changes:
    effect_roll: 1d3
    effect_note: Each extra day costs 1 additional spirituality and adds one more 1d3 roll (max 7 days).
tags:
- ritual
text: 'Use: 1 Casting Action Casting Action. Cost: 1 spirituality point [[Spirituality]]
  for the initial prediction (1 day). Each additional day costs 1 spirituality point
  and adds 1 additional 1d3 roll. Limits: Forecast at most 7 days. Effect: For each
  day predicted, roll 1d3 and interpret the result by the current season. #### Spring
  (1d3) Sunny day: Warm and sunny; plants do not need additional treatment, and creatures
  can survive comfortably. Spring rain: Rainy and humid, suitable for plant growth.
  If organisms do not have sufficient protection, they suffer severe cold effects
  after being exposed to rain for 1 hour. Cold current: Sudden cold current may cause
  adverse effects on plants; insuf...'
```





- **Use:** 1 **Casting Action** Casting Action.
- **Cost:** **1 spirituality point** [[Spirituality]] for the initial prediction (1 day). Each additional day costs **1 spirituality point** and adds **1** additional **1d3** roll.
- **Limits:** Forecast at most **7 days**.
- **Effect:** For each day predicted, roll **1d3** and interpret the result by the current season.

#### Spring (1d3)

1. **Sunny day:** Warm and sunny; plants do not need additional treatment, and creatures can survive comfortably.
2. **Spring rain:** Rainy and humid, suitable for plant growth. If organisms do not have sufficient protection, they suffer severe cold effects after being exposed to rain for **1 hour**.
3. **Cold current:** Sudden cold current may cause adverse effects on plants; insufficient clothing results in severe cold effects.

#### Summer (1d3)

1. **Hot:** Hot and dry; you need to irrigate the soil of your plants adequately. Not enough coolness results in the hot effect.
2. **Rainy and muggy:** High humidity and high temperature may cause diseases and insect pests. Not enough coolness results in the hot effect.
3. **Thunderstorm:** May cause floods and other disasters that affect crops; lack of coolness results in heat.

#### Autumn (1d3)

1. **Rainy:** Suitable temperature and sufficient precipitation; suitable for the growth of some plants. Insufficient clothing can obtain severe cold effect.
2. **Sunny day:** Warm and sunny; plants do not need additional treatment, and creatures can survive comfortably.
3. **Early frost:** Low temperature and frost may cause frost damage to some plants; insufficient clothing results in severe cold effects.

#### Winter (1d3)

1. **Heavy snow:** May affect transportation and harvesting, cause freezing damage to crops; insufficient clothing results in severe cold effects.
2. **Severe cold:** Low temperature may cause freezing damage to some plants; insufficient clothing can obtain severe cold effects.
3. **Dry, cold and sunny:** May lead to drought in the soil; requires sufficient irrigation; insufficient clothing results in severe cold effects.

#### Crop Care Under Weather

- If you leave your plants alone for **24 hours** in any of these severe weather results (**heavy snow**, **thunderstorm**, **severe cold**), then to provide them with shelter you must succeed on a **lucky check** [[Lucky check]] of **Difficulty Value 20** Difficulty Value; otherwise they die.
- If you are in any of the above moderately severe weather (except the severe weather listed above), and you have not taken care of your plants for **24 hours**, you must take care of them for **1 hour** in the next **24 hours**, without identification.
- **Nursing:** Late care of the previous bullet causes crops to reduce yield by **1d6**. Crops wither after **3** yield reductions or **48 hours** without nursing (whichever comes first).

### Severe Cold and Hot Effect

```yaml ability
id: earth-seq-09-severe-cold-and-hot-effect
name: Severe Cold and Hot Effect
pathway: earth
sequence: 9
status: adapted
type: passive
action: none
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: persistent
dice:
  check_roll: null
  damage_roll: 1d3
  heal_roll: null
  effect_roll: null
  notes: Damage roll maps severe-cold exposure damage that begins after 12 hours.
scaling:
- when: hot_exposure_6_hours
  changes:
    effect_note: Hot exposure causes fainting after 6 hours without sufficient cooling.
damage_types:
- cold
tags:
- defense
- offense
text: 'Severe cold: Biological skills and attribute evaluations that are not well-preserved
  are disadvantaged at -2, and agility and evasion in mobility and physical defense
  continue to be -2. If you stay in a severe cold environment for 12 hours, you start
  to suffer 1d3 cold damage each round. Hot: Biological skills and attribute appraisals
  that do not have sufficient cooling are disadvantaged at -2, and agility and dodge
  in mobility and physical defense last at -2. If you stay in a hot environment for
  6 hours, you faint due to heat stroke. Cold has no effect on creatures with [[Cold
  Resistance]], and heat has no effect on creatures with [[Fire Resistance]]. Special:
  The identified weather does...'
```





- **Severe cold:** Biological skills and attribute evaluations that are not well-preserved are disadvantaged at **-2**, and agility and evasion in mobility and physical defense continue to be **-2**. If you stay in a severe cold environment for **12 hours**, you start to suffer **1d3** cold damage each round.
- **Hot:** Biological skills and attribute appraisals that do not have sufficient cooling are disadvantaged at **-2**, and agility and dodge in mobility and physical defense last at **-2**. If you stay in a hot environment for **6 hours**, you faint due to heat stroke.
- Cold has no effect on creatures with [[Cold Resistance]], and heat has no effect on creatures with [[Fire Resistance]].
- **Special:** The identified weather does not necessarily happen. Weather-related Extraordinary abilities can change the result; because they generally take effect immediately, it is difficult to predict them in advance, but it may be predictable in places with a certain distance from the source of the extraordinary ability.
- > **GM Note:** These effects are usually easy to avoid, but this does not include homeless/homeless people; they will most likely die overnight.

- **Effect:** Severe Cold and Hot Effect resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Spiritual Vision
```yaml ability
id: earth-seq-09-spiritual-vision
name: Spiritual Vision
pathway: earth
sequence: 9
status: canonical
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
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
text: 'Use: 1 free action to activate. Cost: 1 spirituality point per round while
  active. Effect: While active, your vision gains the following benefits: Etheric
  body: See through the targets aura field to locate physical defects, down to organs
  in detail. Spiritual body: Confirm whether an object/creature is spiritual; this
  cannot identify extraordinary people. Mental Body: Confirm whether a creature is
  thinking; you cannot obtain more detailed information. Astral body: You cannot see
  the astral body. Sequence 8: If you use Spiritual Vision to determine the cause
  of a creature, you gain +2 to [[Medical identification]] of the symptom. Earth Pathway:
  Sequence 8'
```





- **Use:** 1 **free action** to activate.
- **Cost:** 1 **spirituality point per round** while active.
- **Effect:** While active, your vision gains the following benefits:


  1. **Etheric body:** See through the target’s aura field to locate physical defects, down to organs in detail.
  2. **Spiritual body:** Confirm whether an object/creature is spiritual; this cannot identify extraordinary people.
  3. **Mental Body:** Confirm whether a creature is thinking; you cannot obtain more detailed information.
  4. **Astral body:** You cannot see the astral body.

- **Sequence 8:** If you use Spiritual Vision to determine the cause of a creature, you gain **+2** to [[Medical identification]] of the symptom. Earth Pathway: Sequence 8

> **GM Note:** Dead creatures are usually only dull in color and cannot be identified. Spiritual materials usually have spirituality; the color seen in Spiritual Vision usually represents its corresponding Pathway, but this does not mean you can see the power of a Beyonder. The color lets you see each other in the dark, but you can only see the existence of color and may still get lost. Unlike dead creatures, undead creatures have deep black spirituality color instead of no color.

- Spiritual Vision can see some ordinary spirit bodies by default; those that have not dissipated for **1 day**.
- Ordinary spirit bodies seen this way cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
