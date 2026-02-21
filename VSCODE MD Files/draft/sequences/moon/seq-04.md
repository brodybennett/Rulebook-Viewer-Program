---
title: 'Sequence 4: Spirit Alchemist'
id: moon-seq-04
tags:
- pathway:moon
- sequence:4
---






# Moon Pathway: Sequence 4

## Spirit Alchemist

> **Lore:** **Witch King**s can easily live to a thousand years old and are among the long-lived demigods, but they will inevitably enter irreversible old age and decline afterward.
>
> **Lore:** They are outstanding individuals who control the power of darkness, the moon, strangeness, and other fields, surpassing powerhouses of the same kind. They are proficient in various spells in the moon and dark realms, and can arrange rituals that directly borrow the power of the "moon" by relying on natural interaction methods-this is terrifying.
>
> **Lore:** They have a strong physique, terrifying speed, regeneration, and self-healing speed beyond imagination, but they are closer to the caster.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** Under the illumination of the full moon, borrow power from the moon through rituals to research unique and powerful magic in the moon domain or dark domain. (unofficial ceremony)

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Constitution +2, Agility (DEX) +2, Strength +1, Willpower (WIL) +1; your [[Occultism]] goes up by one level.

### Moon Paper Man

```yaml ability
id: moon-seq-04-moon-paper-man
name: Moon Paper Man
pathway: moon
sequence: 4
status: canonical
type: active
action: free
cost:
  spirituality: 1
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: No roll required; each figurine expends 1 spirituality to absorb one listed effect.
scaling: []
tags:
- ritual
- divination
- debuff
- defense
- offense
text: 'Cost: Free action; 1 point of spirituality per use. [[Spirituality]] Free Action
  Use: Use a paper man/paper doll (a moon paper figurine) as a Stand-in to resist
  damage you take. [[Stand-in]] Effect: The moon paper figurine wards off one of the
  following that targets you: disease, wound, curse, attack, prophecy, or gaze. Limits:
  Production requires a unique process in the moon domain. The number of moon paper
  figurines you have equals your amoon knowledgea level. [[Lunar Knowledge]] If your
  moon knowledge level is a Master, you can carry up to 5 moon paper figurines at
  the same time, plus 1 training-only figurine in addition to the active ones. Area
  damage and multiple Stand-ins: [[Area Da...'
```





- **Cost:** **Free action**; 1 point of **spirituality** per use. [[Spirituality]] Free Action
- **Use:** Use a paper man/paper doll (a moon paper figurine) as a **Stand-in** to resist damage you take. [[Stand-in]]
- **Effect:** The moon paper figurine wards off one of the following that targets you: disease, wound, curse, attack, prophecy, or gaze.
- **Limits:**
  - Production requires a unique process in the moon domain.
  - The number of moon paper figurines you have equals your "moon knowledge" level. [[Lunar Knowledge]]
- If your moon knowledge level is a Master, you can carry up to 5 moon paper figurines at the same time, plus **1 training-only figurine** in addition to the active ones.
  - **Area damage and multiple Stand-ins:** [[Area Damage]]
    - Area damage can consume multiple Stand-ins. When suffering area damage, at least two Stand-ins must be consumed to completely avoid the damage; consuming only one Stand-in causes you to suffer half the damage.
    - Specific area damage (examples: meteorite of fate, lightning storm of the tyrant, dark control of the bishop of fear) requires at least three Stand-ins to completely avoid it. [[Meteorite of Fate]] [[id:alias-tyrant|Tyrant]] [[Lightning Storm]] [[Bishop of Fear]] [[Dark Control]]
    - If the source of the area damage is one level lower than yours, the number of Stand-ins you need is -1; otherwise, +1 on the original basis.
    - This +1 also applies to specifically marked area skills, and cannot be reduced to 0; a minimum of 1 Stand-in is still needed.
- **Special:** The moon paper figurine can be given to another person to use once if necessary.
  - Each person can only get one piece per day.
  - The paper figurine expires after one year.

> **GM Note:** The paper figurines of the Fool's Path are ordinary paper figurines in essence, so they can only be used by extraordinary people of the Fool with extraordinary abilities and are not considered extraordinary items. [[Fool]] [[Extraordinary Item]]
>
> **GM Note:** The moon paper figurine is imbued with the spirituality of the moon domain and is a time-sensitive extraordinary item, so it can be used by others.

### Dark Gaze

```yaml ability
id: moon-seq-04-dark-gaze
name: Dark Gaze
pathway: moon
sequence: 4
status: canonical
type: active
action: free
cost: {}
roll: null
opposed_by: willpower_defense
range: One target within line of sight.
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
- debuff
- defense
- offense
text: 'Cost: Casting Action; 3 points of spirituality. Casting Action Targeting and
  range: One target within line of sight. Effect: Use your own naked eyes as a substitute
  for others, affecting the target within your line of sight. Mysteriously attack
  the opponentaTMs Willpower Defense; then the target establishes contact with you,
  which is regarded as entering a Substitute State. [[Substitute State]] This is a
  temporary curse that can be dispelled; it can also be dispelled automatically when
  leaving the battlefield. [[Dispel]] In the Substitute State (called aavatar statea
  in the RAW): The avatar state is a stronger variant of the substitute state. Obscuration'
```





- **Cost:** **Casting Action**; 3 points of **spirituality**. Casting Action
- **Targeting and range:** One target within line of sight.
- **Effect:**
  - Use your own naked eyes as a substitute for others, affecting the target within your line of sight.
  - Mysteriously attack the opponent's Willpower Defense; then the target establishes contact with you, which is regarded as entering a **Substitute State**. [[Substitute State]]
  - This is a temporary curse that can be dispelled; it can also be dispelled automatically when leaving the battlefield. [[Dispel]]
- **In the Substitute State (called "avatar state" in the RAW):** The avatar state is a stronger variant of the substitute state.
  - **Obscuration**
    - **Use:** Free action; continued obscuration costs you an action each turn.
    - **Effect:** The obscured target and creatures interacting with it treat each other as blind. Unless they have other ways to locate position, both sides remain disadvantaged. [[Blind]]
  - **Crushing**
    - **Use:** **Attack Action.** Attack Action
    - **Effect (self):** You crush one of your eyeballs, taking 5d6 damage instantly.
    - **Effect (ongoing self):** You continue to lose 1 action and unlimited free actions each turn until the eyeball is restored, or the eyeball restores itself after the battle.
      - If both of your eyes are crushed, you are continuously blinded and have only 1 action and 1 free action per round.
      - For the Witch King, the crushed eyeball must be fully regenerated after an encounter, and can only be regenerated after the encounter.
    - **Effect (foe):** Your foe immediately suffers: your normal attack damage +4d6+5 **Hard Damage** (ignores any normal means of armor, doubles, and damage reduction). [[Hard Damage]] [[Armor]] [[Doubles]] [[Damage Reduction]]

- **Limits:** As described in this section's prose.


### Moon Rituals

```yaml ability
id: moon-seq-04-moon-rituals
name: Moon Rituals
pathway: moon
sequence: 4
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
text: 'Cost: 10 spirituality points; 5-minute ritual process. [[Ritual]] Use: Must
  be performed under moonlight; only once every 24 hours. Effect: You directly borrow
  power from the amoon.a This is a ritual magic that can only be mastered by a Witch
  King. When the ritual is completed, the Witch KingaTMs all attributes +1. At the
  same time, [[Lunar Knowledge]] gains an additional skill level: This does not affect
  the identification of Lunar Knowledge. All abilities that calculate benefits based
  on the number of Lunar Knowledge levels calculate one more skill level, and gain
  one extra benefit.'
```





- **Cost:** 10 **spirituality** points; 5-minute ritual process. [[Ritual]]
- **Use:** Must be performed under moonlight; only once every 24 hours.
- **Effect:**
  - You directly borrow power from the "moon." This is a ritual magic that can only be mastered by a Witch King.
  - When the ritual is completed, the Witch King's all attributes +1.
  - At the same time, [[Lunar Knowledge]] gains an additional skill level:
    - This does not affect the identification of Lunar Knowledge.
    - All abilities that calculate benefits based on the number of Lunar Knowledge levels calculate one more skill level, and gain one extra benefit.
  - This benefit lasts for one hour.
- **Example:** In this state, the moon double gains an extra double because of the extra skill level. [[Moon Double]]
- **Sequence 3 note:** Change to an extra level of knowledge for two months. [[id:alias-sequence-3|Sequence 3]]

- **Limits:** As described in this section's prose.


### Illusionary Bat Swarm

```yaml ability
id: moon-seq-04-illusionary-bat-swarm
name: Illusionary Bat Swarm
pathway: moon
sequence: 4
status: canonical
type: active
action: free
cost: {}
roll: 1d20 + @attr.str + @skill.fighting
opposed_by: physical_defense
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.str + @skill.fighting
  damage_roll: 1d3 + @attr.str
  heal_roll: 1d6
  effect_roll: 2d6
  notes: Check/damage/heal map batization life-suck attacks; effect_roll maps the emergency 2d6 recovery when reduced to 0 HP.
scaling:
- when: batization_with_spirituality
  changes:
    damage_roll: 3d6 + @attr.str
    effect_note: Spirituality-fueled batization increases damage and allows potion creation.
tags:
- mobility
- offense
text: 'Cost: Free action. Effect: Your body disintegrates and collapses into a group
  of vampire bats between reality and illusion; you gain the ability to fly. [[Flight]]
  Each bat has 1 hit point; the swarm''s total hit points equal your current hit points
  when this form is activated. Hit Points Your movement speed is multiplied by 2.
  [[Movement Speed]] In this state, unless all bats are killed, you can regroup; this
  state is immune to Hard Damage. The swarm is considered as a whole: The bats formed
  cannot act alone.'
```





- **Cost:** **Free action.**
- **Effect:**
  - Your body disintegrates and collapses into a group of vampire bats between reality and illusion; you gain the ability to fly. [[Flight]]
  - Each bat has **1 hit point**; the swarm's total hit points equal your current hit points when this form is activated. Hit Points
  - Your movement speed is multiplied by 2. [[Movement Speed]]
  - In this state, unless all bats are killed, you can regroup; this state is immune to **Hard Damage**.
  - The swarm is considered as a whole:
    - The bats formed cannot act alone.
    - Their minds are synchronized with you; you do not gain extra actions from this.
    - There is no difference between single-target and area-of-effect damage.
- **Special:**
  - You may separate only one or a small number of bats from your body and order them to do simple tasks instead of you (e.g., delivering letters, finding items, transporting goods).
  - In normal form, once per day, when your hit points become 0, you immediately recover 2d6 hit points, then immediately convert the remaining hit points into a swarm of bats and flee in all directions. If the heart is pierced to death, this cannot be recovered.
- **Sequence 3 note:** Part of your bat can answer prayers in your place. [[Answer Prayers]] [[id:alias-sequence-3|Sequence 3]]

- **Special judgment on "batization":**
  - In bat state, you cannot use the [[Claws of Corrosion]] or perform normal fighting attacks, but you can still use other spells.
  - Fighting is changed to life sucking; this is divided into non-consumption of spirituality and consumption of spirituality. [[Fighting]]
  - **Does not consume spirituality:**
    - You turn into a bat and rush to wrap the opponent.
    - The Casting Action is changed to an Attack Action.
    - Test: fighting against physical defense. [[Physical Defense]]
    - Damage: curse damage equal to 1d3 + Strength damage dice. [[Curse Damage]]
    - Healing: recover 1d6 hit points.
    - This method cannot produce additional potions; you only gain the benefits of dealing damage and restoring hit points. [[Potions]]
  - **Consumption of spirituality (two types):**
    1. You do not pounce to use melee attacks; instead, you summon black mist from a distance to form additional bats. These bats cause normal life-sucking effects, using the Casting Action like the original ability.
    2. You pounce and use a close-range attack (still an Attack Action), tested as fighting against physical defense:
       - Damage: 3d6 + Strength damage dice of curse damage.
       - Healing: restore 1d6 blood volume.
       - This creates additional potions, which can be taken immediately when bat-formed or temporarily kept in an empty bottle when transformed back into human form (only one can be kept at most). [[Empty Bottle]]

> **Lore:** In expression, you can have yourself rush out from the depths of darkness in the form of a bat swarm, immediately envelop a target, accompanied by the sound of flapping wings and the scream of the target, swallow the target alive, and turn it into a mummified corpse within three seconds; after you recover your human form, you can wipe the corners of your mouth as if you have had a full meal.

> **GM Note:** At this stage, the Witch King of Sequence 4 is already considered a leader in the field of darkness and moon magic, but because the original book does not have more dark magic, the extension of dark and moon magic is left to the actual **GM** and **Player** to draw up by themselves. To put it simply, extraordinary people can draw up some dark magic by themselves and execute it after the **GM** approves it; it should not be too strong or too weak. You can refer to the original dark or moon magic for creation. As a standard, no more than three kinds of original dark magic are recommended; otherwise, it may cause uncontrollable variables, and the content and ideas should be concise and clear. [[Dark Magic]] [[Moon Magic]]

- **Limits:** As described in this section's prose.
