---
title: 'Sequence 5: Desire Apostle'
id: abyss-seq-05
tags:
- pathway:abyss
- sequence:5
---






# Abyss Pathway: Sequence 5

## Desire Apostle

Capable of exploiting and manipulating emotions and desires, inducing corruption. If an enemy has overly intense mood swings or obvious desires, you can remotely control them, plant seeds, or directly catalyze those emotions—exposing problems, causing gradual degeneration, or triggering emotional loss of control at critical moments.

You can also forcibly impact an enemy’s spirit to make them inevitably feel certain emotions. You can transform into a pitch-black liquid, possess “filthy words” with different effects, and summon a magma sword. [[Filthy Words]] [[Magma Sword]]

- See also: Abyss

## Advancement

### Advancement Ritual

- **Ritual:** Serial killings targeting those who have fallen; minimum **13** people, maximum **49**.
  - The more complete the ritual, the more hopeful you will be promoted.
  - There must be an interval of at least **3 days** between two killings; otherwise it is easy to lose control.
  - The interval must not exceed **9 days**; exceeding this resets the ritual.
- After every murder and every part of the ritual, you eat the victim’s internal organs.
  - From then on, you will always be in a state of violent bloodthirst, wanting to hurt others, until that desire is satisfied again.

- **Ritual Nature (loss of control / sanity):**
  - “Abyss” is extremely easy to lose control from Sequence 6 and loses conventional emotional empathy. [[id:alias-abyss|Abyss]] [[id:alias-sequence-6|Sequence 6]]
  - Only through killing can one regain sanity; this must be offset by the pleasure brought by serial murders and the loss of sanity during promotion.
  - Starting from Sequence 6, the demon’s sanity test must fail; if the promotion to Sequence 5 fails the sanity test, **1d10** sanity will be lost. [[sanity test]] [[Sanity / Rationality]]
- Therefore, the extra intellectual resistance through intoxication and sinking grants **Advantage** on Sanity / Rationality checks during the ritual.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** strength **+1**, agility **+1**, constitution **+2**, inspiration **+2**.

### Control Desires

```yaml ability
id: abyss-seq-05-control-desires
name: Control Desires
pathway: abyss
sequence: 5
status: adapted
type: active
action: cast
cost:
  spirituality: 2
roll: null
opposed_by: none
range: Choose 1 target in your field of vision who is already in an emotional state.
target: designated target(s)
duration: sustained
dice:
  check_roll: null
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Composite emotional-control kit; individual sub-effects use their own listed DV checks and constitution-linked damage conversions.
scaling:
- when: detonate_desire_extreme_emotion
  changes:
    effect_note: Immediate loss equals (20 - target constitution), with remaining value converted to d6 damage dice.
- when: seed_planted
  changes:
    effect_note: Stored emotional state can be remotely treated as catalyzed/detonated later.
tags:
- ritual
- detection
- mobility
- control
text: 'You exploit and manipulate emotions and desires, inducing corruption. ####
  Catalyze Emotions Cost: 2 spirituality points. [[Spirituality]] Use: 1 Casting Action.
  Targeting and range: Choose 1 target in your field of vision who is already in an
  emotional state. Limits: Disguised emotion cannot be catalyzed. Uncatalyzed emotions
  can be calmed after 1 round by meditating as a casting/Move Action.'
```





You exploit and manipulate emotions and desires, inducing corruption.

#### Catalyze Emotions

- **Cost:** 2 spirituality points. [[Spirituality]]
- **Use:** 1 Casting Action.
- **Targeting and range:** Choose 1 target in your field of vision who is already in an emotional state.
- **Limits:**
  - Disguised emotion cannot be catalyzed.
  - Uncatalyzed emotions can be calmed after **1 round** by meditating as a casting/Move Action.
- **Effect:** You intensify an existing emotion (e.g., weak anxiety becomes extreme; slight vigilance becomes nervous), producing the corresponding state below.

**Catalyzed outcomes (examples and defined states):**

- **Vigilance behavior in progress → Nervous state**
  - The original vigilance becomes nervous; subjective perception seems to slow down, entering nervousness, lasting until the danger disappears or the target reaches a safe zone.
  - **Nervous state:** Investigative and Listening identification **-4** is unfavorable, and **1, 2, and 3** of these two identifications are all big failures.

- **Expressing a desire to escape → Fear state**
  - The original thoughts are transformed into substance, and the target enters fear.
  - **Fear state:**
    - The movement action can only escape in the direction opposite to any one source of fear.
    - If the source of fear is not found, move in a direction considered safe.
    - Skill assessment related to the source of fear is **-4** disadvantageous until reaching a safe area, or until a **Difficulty Value 15** psychological guidance or **Difficulty Value 20** social identification cancels this effect. [[id:alias-psychological-guidance|Psychological Guidance]] [[Social Identification]]
  - **Special:** Strategic retreats cannot be catalyzed, and retreats are not considered a form of escape.

- **Showing anxiety and timidity → Fear state (no forced opposite-direction movement)**
  - Enters fear, but is not subject to the forced movement effect of fleeing opposite a fear source.

- **Showing hostility (not vigilance) → Rage / Angry state**
  - Hostility is catalyzed; the target immediately attacks the source of hostility, entering rage.
  - **Angry state:**
    - Skill identification **-4** disadvantageous.
    - Melee attack damage **+1d6**.
    - Continue to chase or attack the source of anger until the source of anger or the target dies, faints, or the person in anger is given **Difficulty Value 15** psychological guidance.
    - If the source of anger is things that are important to you, the state clears after causing damage once.

- **Hormonal coveting of another’s body/beauty → Charisma (CHA) state**
  - Love is catalyzed; the target enters fascination with the coveted person.
  - **Charisma (CHA) state:**
    - Obey the source of the charm, unless important things or people are involved.
    - When hostile, attack other people first.
    - Try to help them when talking.
    - Each resistance to this effect requires **Difficulty Value 20** willpower.
    - Ends when desire is satisfied, or is dispelled after **Difficulty Value 15** psychological guidance.

- **Admiration due to another’s charisma → Fascination (admiration variant)**
  - Admiration is catalyzed; the target falls into fascination for the admired.
  - **Difference from Charisma (CHA) state:**
    - Only makes the admired person beneficial to social identification **+4**.
    - When hostile, attack others first.
    - “Talking as much as possible to help talk” can only be removed by **Difficulty Value 15** psychological guidance.

- **Coveting another’s finances → Greedy state**
  - Coveting is catalyzed; the target falls into greed.
  - **Greedy state:**
    - Detection and identification can only target things related to the item.
    - Immediately conduct a **Difficulty Value 15** will identification; if the behavior does not meet its moral standards, then it can be identified twice.
    - On failure, the target acts to obtain the item (can be obtained in a legitimate way).
    - If discovered, reprimanded, or blocked, only the effect of detection and identification remains until the chance of obtaining the target is lost, and the greedy state is lifted.

- **Contempt for something/someone → Arrogant state**
  - Contempt is catalyzed into arrogance.
  - **Arrogant state:**
    - Until the underestimated target has caused a dangerous result, it cannot be severely attacked and can only be dealt with using the lowest strength.
    - Released after a **Difficulty Value 20** social identification or **Difficulty Value 15** psychological guidance by others.

**Other reasonable, appropriate catalyzed emotions (as allowed by the GM):**

- **Jealousy state:**
  - Scouting and identification can only choose the source of jealousy.
  - If it does not violate interests, the movement action must move to the jealousy target.
  - Lifted after the jealousy source is caused material, mental, or interest damage and the other party is indeed frustrated by it, or after a **Difficulty Value 15** social identification or psychological guidance is performed.

- **Lazy state:**
  - The first action requires a **Difficulty Value 10** will.
  - After falling into a sleep state, it takes a **-5** disadvantage to wake up.
  - Natural sleep also requires a **Difficulty Value 15** will to wake up (maybe consciousness is awake but the mind is difficult to act).

- **Hunger state:**
  - The target wants to eat uncontrollably until lifted after being full.
  - If you do not eat in each round, you lose an action.
  - Each time you perform a **Difficulty Value 15** will, you can counteract this effect and act normally.

- **Desire state:**
  - Make a **Difficulty Value 15** will test; otherwise, you will take action towards the thing you desire.
  - Unlike greed, this may be a compliment, satisfaction, or approval.
  - Dismisses when the source of desire is gained, the chance to obtain the source of desire is lost, or a **Difficulty Value 15** Social or Mental Channel check is made. [[Mental Channel]]
  - If the GM can’t define an effect for special catalyzed scenarios, it can be treated as desire state (includes desire to eat, evil thoughts, and desire to do good).

#### Detonate Desire

- **Cost:** 2 spirituality points.
- **Use:** 1 Casting Action.
- **Targeting and range:** Choose 1 target within your field of vision who is in an emotional state; then choose a corresponding benefit to take effect.
- **Effect:**
  - After the detonated emotion is over, the original corresponding emotional state is cleared until it is catalyzed again.
- **Special:**
  - No matter which desire is detonated, the detonated person continues to lose an action within one encounter, is extremely weak, cannot be superimposed, and any effect that needs to be maintained all the time (such as marionette or wraith possession) will terminate on the spot. [[Marionette]] [[Wraith Possession]]
  - If you detonate desire under extreme emotions (not merely catalyzed emotions), this usage is considered a desire explosion.

- **Effect:** The target of the explosion will immediately lose **(20 - target constitution)**; the remaining value becomes the number of **1d6** damage dice.

- **Effect:** The target of the explosion will immediately lose **(20 - target constitution)**; the remaining value becomes the number of **1d6** damage dice.
- Desire explosion usually cannot be replaced; if fatal, it may explode the brain and be dismembered by emotions.

> **GM Note:** Example given: a creature under extreme hormonal charm that is exploded by desire may burst into flames, suffer sudden heart compression, intense flushing/sweating, loss of mind, myocardial infarction, cerebral hemorrhage, and die on the spot.

- **Extreme emotions requirement:** Extreme emotions cannot be achieved through purely catalyzed emotions; certain conditions must be met (listed below).

##### Emotional detonation list (and extreme conditions)

1. **Nervousness (detonated):**
   - A non-existent enemy appears in the target’s eyes; any thing (including items) in the selected scene is regarded as an enemy, but teammates are not included unless suspected to be part of the enemy.
    - After the emotion is detonated, the target performs an action consistent with the emotion; the **GM** chooses the action.
   - *(Extreme allergy: The source of danger has not been found while continuing to cause harm to oneself; the person cannot reach a safe zone for a long time; teammates disappear one by one; helpless, or unable to provide effective help—this is considered extreme.)*

2. **Fear state (detonated):**
   - The target leaves the source of fear at all costs.
   - You, as the Player, make it take an action that meets the reason of “fleeing from the source of fear,” even letting them attack once to stop teammates ahead.
   - *(Extreme fear: Entering a bloodbath without effective reinforcements, no suitable means to get out of trouble, and incapable of suppressing/balancing the fear source with one’s advantage.)*

3. **Anger state (detonated):**
   - The target abandons reason to destroy the source of anger at all costs, even if about to die.
   - Only **Difficulty Value 25** psychological guidance can calm them; otherwise they do not stop until the source dies/faints, or self-death/fainting.
   - *(Extreme anger: Unable to damage the anger source; the source keeps provoking; no means to deal with it; no timely persuasion or psychological guidance identification to suppress anger.)*

4. **Hormone Charisma (CHA) (detonated):**
   - The target abandons reason to obtain the charm source.
   - You, as the Player, make them immediately take an action that meets hormonal charm.
   - Note: best not to make other Players feel uncomfortable.
   - *(Extreme hormones: The moment when the charm and the charmed are engaged in behavior violating social customs and reaches the maximum 18, it is considered extreme.)*

5. **Charisma (CHA) of personality (detonated):**
   - The target does whatever it takes to gain the favor of the charm source.
   - You, as the Player, make them perform an action that would be favored by the charm source in their perception; no matter how crazy, they cannot recognize it as something that will arouse disgust.
   - *(Extreme longing: Continuously recognized by the charm source through heart-straightening events beyond usual imagination—e.g., a girl crushing on a prince is repeatedly confessed to and promised marriage.)*

6. **Greedy state (detonated):**
   - The target abandons reason to get what they want; you, as the Player, make them immediately act to get the item even if it damages their image.
   - *(Extreme greed: Continues to have no way to get it but learns more benefits; fantasizes happy ending; decides to abandon moral ethics/personality standards to seize the moment.)*

7. **Arrogant state (detonated):**
   - For **1 full round**, no matter how serious the despised target does, the arrogant target cannot take action against it.
   - *(Extreme arrogance: The despised target hasn’t shown effective harm but keeps appearing; is gradually recognized by everyone except oneself; the arrogant can’t bear being regarded as contemptuous in person.)*

8. **Jealousy state (detonated):**
   - The goal is to destroy the envied person at all costs; you, as the Player, make it happen once immediately.
   - In their cognition, it strips the envied person’s glamorous appearance, destroys life, and pulls them to the same or lower level.
   - *(Extreme jealousy: Cannot punish the jealousy source; desired things are taken away; status/skills are learned and replaced; rationality is abandoned.)*

9. **Lazy state (detonated):**
   - For **1 full round**, the target performs no actions no matter what they witness (not limited to one specific target).
   - *(Extreme laziness: Any important matter can be resolved without involving oneself while still gaining considerable benefits; too comfortable to return to previous life.)*

10. **Hunger state (detonated):**
   - The target immediately loses control due to excessive hunger, even if full.
   - Must perform at least one Attack Action in each round to eat within **two rounds**.
   - If there is no food in the scene, they will eat people; the creature devours items, dealing **1d6** physical damage per item to it.
   - Cannibals prioritize choosing people other than teammates; under this condition, you can choose a target to be devoured as a Player.
   - *(Extreme hunger: Sudden lack of food to the limit of the human body, and suddenly witnessing the most favorite and most desired food.)*

11. **Desire state (detonated):**
   - You, as the Player, immediately make them perform an action that will give them the desired thing, no matter how crazy.
   - *(Extreme desire: Can’t get it for a long time and can’t forget it; breaks moral code and intends to damage everything—even important things—to obtain it.)*

#### Degenerate Seeds

- **Cost:** 2 spirituality points.
- **Use:** 1 Casting Action.
- **Targeting and range:** Choose 1 target within your line of sight who must already be in an emotional state.
- **Effect:**
  - After casting, you clear an emotional state you specify; it no longer has any effect.
  - The cleared emotional state becomes a potential emotional seed hidden in the target’s soul, and the target enters a depraved latent state.
- **Depraved latent state:** One or more latent emotional seeds exist in the soul, equivalent to a mental illness with an infinite incubation period. As long as the Apostle of Desire wants to, they can treat it as a catalyzed detonation of desire at any time; the detonation corresponds to the original emotional state.
- **Special:** Extraordinary people who can enter the spiritual island through the spectator path can clear the seed, and the separated and fallen thoughts of the Hanged Man path can also clear the seed. Visionary [[Spiritual Island]] [[Hanged Man]] [[Separated and Fallen Thoughts]]

### Sense of Depravity

```yaml ability
id: abyss-seq-05-sense-of-depravity
name: Sense of Depravity
pathway: abyss
sequence: 5
status: canonical
type: active
action: cast
cost: {}
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
  notes: No explicit dice expression in source text.
scaling: []
tags:
- detection
- control
- debuff
text: 'You perceive a desire to approach depravity in those around you. Special: This
  is a bonus effect brought by the potion; it cannot be recorded or stolen. Benefits:
  When holding the perception of corruption, you can perceive emotional states within
  a radius of 100 meters, tell what kind of person it probably comes from, and how
  strong the emotion is. This can be a perceived emotion as a state of fascination,
  fear, etc., or simply uneasiness that has not yet had an actual effect. As long
  as the emotion is perceived by you, even if the target is not within your field
  of vision, you can remotely: use your desire to control it, catalyze the emotion,'
```





You perceive a desire to approach depravity in those around you.

- **Special:** This is a bonus effect brought by the potion; it cannot be recorded or stolen.
- **Benefits:**
  - When holding the perception of corruption, you can perceive emotional states within a radius of **100 meters**, tell what kind of person it probably comes from, and how strong the emotion is.
    - This can be a perceived emotion as a state of fascination, fear, etc., or simply uneasiness that has not yet had an actual effect.
  - As long as the emotion is perceived by you, even if the target is not within your field of vision, you can remotely:
    - use your desire to control it,
    - catalyze the emotion,
    - detonate it, or
    - plant the seed.
  - If multiple creatures within your perception range are caught in the same common emotional state, your desire control can affect all of them at once—catalyzing or detonating their common emotions together, including fallen seeds of the same emotions.

- **Effect:** Sense of Depravity resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.


### Incarnation of Desire

```yaml ability
id: abyss-seq-05-incarnation-of-desire
name: Incarnation of Desire
pathway: abyss
sequence: 5
status: adapted
type: active
action: swift
cost:
  spirituality: 2
roll: 1d20 + @attr.dex + @skill.stealth
opposed_by: difficulty_value
range: self
target: self
duration: sustained
dice:
  check_roll: 1d20 + @attr.dex + @skill.stealth
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted roll mapping for stealth/mobility resolution while transformed; grapple mental-shock branch follows Horn of Arrogance rules.
scaling:
- when: transformed_liquid_state
  changes:
    check_bonus: 8
    effect_note: Gain fluid-body movement options and lose armor/reduction benefits.
- when: target_sequence_higher
  changes:
    effect_note: Effect fails.
tags:
- ritual
- stealth
- mobility
- control
text: 'You transform your body into an illusory, viscous black liquid of various emotions
  and desires. Cost: 2 spirituality points. Use: As a Swift Action, once per round.
  Effect: You collapse into a viscous black liquid whose shape you control. Benefits:
  Your movement remains the same, but you are treated as a fluid. You gain a +8 bonus
  on Stealth checks; you can seep through floors, into walls, into tiny crevices,
  and even flow down ceilings. Limits:'
```





You transform your body into an illusory, viscous black liquid of various emotions and desires.

- **Cost:** 2 spirituality points.
- **Use:** As a Swift Action, once per round.
- **Effect:** You collapse into a viscous black liquid whose shape you control.
- **Benefits:**
  - Your movement remains the same, but you are treated as a fluid.
  - You gain a **+8** bonus on Stealth checks; you can seep through floors, into walls, into tiny crevices, and even flow down ceilings.
- **Limits:**
  - You cannot use any supernatural abilities in this state.
  - Whether you enter this state in demon form or human form, you lose all your armor, resistance, and reduction.
  - All non-spiritual damage you receive is halved.
- **Limits:** If the target has a higher **Sequence level** than you, this effect fails.
- **Perception effect:**
  - Any creature that sees you witnesses a combination of fear, anger, greed, jealousy, hunger, lust, etc.; seeing you head-on leads to abnormal perception. [[Abnormal Perception]]
- **Special action:** You can grapple; each round, the grappled target is given a mental shock effect equal to that of the horn of arrogance. [[Horn of Arrogance]]
