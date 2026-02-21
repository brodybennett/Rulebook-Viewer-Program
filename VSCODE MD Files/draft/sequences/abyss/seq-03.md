---
title: 'Sequence 3: Bloody Archduke'
id: abyss-seq-03
tags:
- pathway:abyss
- sequence:3
---






# Abyss Pathway: Sequence 3

## Bloody Archduke

- **Effect:** On a failed **Willpower Defense**, roll **1d4** to choose one listed outcome; the listener also suffers **1d6** Sanity / Rationality loss.

## Advancement

### Advancement Ritual

- **Advancement Ritual:** (unofficial ceremony) Choose one:
  - Tempt a high-ranking being who knows the danger of the [[id:alias-abyss|Abyss]] to go to the [[Misty Sea]]; have them find the entrance to the [[id:alias-abyss|Abyss]] and take the initiative to fall into the embrace of the dark side of the universe.
  - Go to the [[id:alias-abyss|Abyss]] yourself, making no secret of your inner desire and the dark side for power, and take potions under the severe erosion of the [[id:alias-abyss|Abyss]].

> **GM Note:** The RAW explains the “essence” of this ritual as using words to tempt a high-ranking existence with interests—either tempting another being into madness, or “tempting” yourself (convincing yourself, despite knowing the danger, to pursue promotion and power even at the cost of your own safety and humanity). This is presented as rationale and thematic guidance, not additional mechanics.

- For details about the [[id:alias-abyss|Abyss]], see [[Chapter Twelve: Special Regions]].

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Strength** +2, **Agility (DEX)** +1, **Constitution** +2, **Intuition (INT)** +3.

### Babbling

```yaml ability
id: abyss-seq-03-babbling
name: Babbling
pathway: abyss
sequence: 3
status: canonical
type: active
action: free
cost:
  spirituality: 1
roll: 1d20 + @attr.int
opposed_by: willpower_defense
range: audible range
target: designated listener(s)
duration: 1 minute after the last babble
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: 1d4
  notes: Failed willpower defense also causes 1d6 sanity/rationality loss; additionally, listeners lose 1 sanity/rationality each round while exposure persists.
scaling:
- when: listener_fails_willpower_defense
  changes:
    effect_note: Apply one 1d4 babbling outcome and an additional 1d6 sanity/rationality loss.
- when: listener_continues_hearing_babble
  changes:
    effect_note: Listener loses 1 sanity/rationality per round.
tags:
- ritual
- divination
- defense
text: 'Cost: 1 point of Spirituality. Use: Free action; once per round. Effect: Make
  an Intuition (INT) test against each listener''s Willpower Defense. Effect: Each
  time you utter a raving from the [[id:alias-abyss|Abyss]], the people present who
  hear your raving lose 1 point of Sanity / Rationality per round for 1 minute after
  the last babble. Effect: On a failed Willpower Defense, roll 1d4 to choose one listed
  outcome; the listener also suffers 1d6 Sanity / Rationality loss. Extra: If someone
  establishes contact with you by using occult means such as [[id:alias-divination|Divination]]
  and [[Cursing]], you can negate the influence and reveal the source.'
```





- **Cost:** 1 point of **Spirituality**.
- **Use:** Free action; once per round.
- **Effect:** Make an **Intuition (INT)** test against each listener's **Willpower Defense**.
- **Effect:** Each time you utter a raving from the [[id:alias-abyss|Abyss]], the people present who hear your raving lose 1 point of **Sanity / Rationality** per round for **1 minute** after the last babble.
- **Effect:** On a failed **Willpower Defense**, roll **1d4** to choose one listed outcome; the listener also suffers **1d6** Sanity / Rationality loss.

- **Extra:** If someone establishes contact with you by using occult means such as [[id:alias-divination|Divination]] and [[Cursing]], you can negate the influence and reveal the source.

- **Limits:** As described in this section's prose.


### Whisperer

```yaml ability
id: abyss-seq-03-whisperer
name: Whisperer
pathway: abyss
sequence: 3
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
- utility
text: 'Effect: If a connection is established (GM decides), the Whisperer can transmit
  their voice to the targets ears across a very long distance, causing severe injuries
  rather than guaranteed instant death.'
```





- **Effect:** If a connection is established (GM decides), the Whisperer can transmit their voice to the targets ears across a very long distance, causing severe injuries rather than guaranteed instant death.

- **Limits:** As described in this section's prose.


### Danger Countermeasure

```yaml ability
id: abyss-seq-03-danger-countermeasure
name: Danger Countermeasure
pathway: abyss
sequence: 3
status: adapted
type: active
action: cast
cost: {}
roll: 1d20 + @attr.int
opposed_by: willpower_defense
range: self
target: designated target(s)
duration: instant
dice:
  check_roll: 1d20 + @attr.int
  damage_roll: null
  heal_roll: null
  effect_roll: null
  notes: Adapted mapping for the explicit Intuition versus Willpower defense gate before counter-targeting the danger source.
scaling:
- when: danger_source_successfully_identified
  changes:
    effect_note: You may directly apply an extraordinary ability to the source.
- when: reflected_influence_mode
  changes:
    effect_note: Foreseen influence can be reflected back to its source.
tags:
- detection
- defense
text: 'Effect: Your danger perception range covers a city. Use: If you sense a clear
  source of danger and pass an Intuition (INT) check against the target''s Willpower
  Defense, you can directly use your extraordinary ability on the source. Effect:
  If you foresee the source of danger, you can reverse the influence by reflecting
  the effect back to the source.'
```





- **Effect:** Your danger perception range covers a city.
- **Use:** If you sense a clear source of danger and pass an **Intuition (INT)** check against the target's **Willpower Defense**, you can directly use your extraordinary ability on the source.
- **Effect:** If you foresee the source of danger, you can reverse the influence by reflecting the effect back to the source.

- **Limits:** As described in this section's prose.
