---
title: 'Sequence 3: Mentor of Deceit'
id: error-seq-03
tags:
- pathway:error
- sequence:3
---






# Error Pathway: Sequence 3

## Mentor of Deceit

> **Lore:** It is the deepening of the scammer, capable of defrauding the natural rules.

## Advancement

### Advancement Ritual

- **Ritual:** Create a grand phenomenon that would not normally occur, and have at least a few thousand people witness and believe it. The more people are deceived, the better the effect.
> **GM Note:** The RAW labels this as an "unofficial ceremony."

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Intuition (INT) +1; Agility (DEX) +1; your Deception increases by 1 skill level.

### Rules of Deceit

```yaml ability
id: error-seq-03-rules-of-deceit
name: Rules of Deceit
pathway: error
sequence: 3
status: adapted
type: active
action: cast
cost:
  spirituality: 3
roll: 1d20 + @attr.cha + @skill.deception
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: 1d20 + @attr.cha + @skill.deception
  damage_roll: null
  heal_roll: null
  effect_roll: 1d2
  notes: Deception check initiates the fraud rule; effect roll captures the explicit 1d2-hour extension option.
scaling:
- when: extend_encounter_to_hours
  changes:
    effect_roll: 1d2
tags:
- ritual
- social
text: 'Cost: 3 spirituality points. Use: One spellcasting action; make a Deception
  check. Effect: You deceive supernatural powers and the laws of nature to defraud
  the laws of nature. This ability can do the following: Write into Instinct: Write
  one thing that is often done into instinct (at most one). This ability needs to
  be used in advance, and it will take effect for one encounter. Choose one thing
  you do often, or a remarkable ability that you use often, and write it into your
  instinct. When you suffer from shock, frenzy, madness, and other abilities that
  affect your actions mentally, the abilities written into your instinct can ignore
  these effects and be used normally. Example: If you now...'
```





- **Cost:** 3 spirituality points.
- **Use:** One spellcasting action; make a Deception check.
- **Effect:** You deceive supernatural powers and the laws of nature to defraud the laws of nature. This ability can do the following:
  - **Write into Instinct:** Write one thing that is often done into instinct (at most one). This ability needs to be used in advance, and it will take effect for one encounter.
    - Choose one thing you do often, or a remarkable ability that you use often, and write it into your instinct.
    - When you suffer from shock, frenzy, madness, and other abilities that affect your actions mentally, the abilities written into your instinct can ignore these effects and be used normally.
    - Example: If you now have two spellcasting actions, and you can only use one spellcasting action because of shock, then the spellcasting action you lost at this time can still be used, but it can only be used on the thing written into your instinct.
  - **Create a False Resurrection Point:** If you need to be resurrected and the original resurrection point cannot be used, you can choose a place with your fresh body tissue (the body tissue must be properly preserved) and change it to your new resurrection point. [[Resurrection Point]]
  - **Extend the Duration of an Effect:** You change:
    - an instantaneous effect to one round,
    - an effect that lasts one round to three rounds,
    - an effect that lasts three rounds or more to an encounter,
    - an encounter to 1d2 hours,
    - 1d2 hours to half a day,
    - half a day to one day,
    - one day to one week,
    - one week to half a month,
    - half a month to one month,
    - one month to half a year,
    - half a year to one year,
    - one year to five years...
    - (By analogy, an effect can only be cheated once.)
  - **Shorten the Duration of an Effect:** Reverse the judgment of the above effect; the effect that can only last for one round will end on the spot. An effect can only be cheated once.
  - **Connect Two Portals with the Same Principle:** You can connect two portals with the same principle and treat them as intercommunicating gates.
    - It must be two portals with the same principle (example: two Apprentice Sequence 9 doors to the Spirit World). [[Door]] [[Spirit World]]
    - The entrance and exit of the hidden space of Door pathway Sequence 4 is also regarded as a kind of portal. [[Hidden Space]]
    - You must clearly know the specific locations of the two portals.
    - It is obviously not feasible to try to obtain an extraordinary item of Apprentice Sequence 9 and then run around the world, because you have no idea where so many Apprentice Sequence 9s in the world will open the door and where you will go again.
    - It is possible to make a temporary portal with two Apprentice Sequence 9s, as long as you can confirm their location and the location has not changed.
    - If one party disconnects during the transfer, the transfer will fail and you will stay where you are.
    - Based on the above principles, you cannot affect the position of a flame jump of an Extraordinary in the Fool pathway, or carry out a teleportation flame jump with a flame jumping item, because you have no way of judging where an Extraordinary in the Fool pathway will jump in the next second. [[Flame Jump]]
    - If you steal their thoughts, they will also forget what they wanted to do just now, and it is likely to make a different jump position choice because of this.
    - Because this is too instant and random, usually the ability of the decryption scholar is too late to decrypt the result of the jump position, so usually you can't consider doing this. [[Decryption Scholar]]
  - **Increase the Success Level of a Skill Identification:** Only for skills that have already been successful.
    - Example: If a skill that reaches Difficulty Value 15 is counted as a normal success, and Difficulty Value 20 is counted as a hard success, then when this identification is thrown to 15, you perform a fraud rule, turning it into 20 successes.
    - Because the increase is a first-level success level, this cannot be simply understood as final value +5. Example: If a skill rolls 17, it is still in the range of 15-20 and has not yet reached 20. Do a rule cheat at this point and it will only turn 20 (i.e., +3 in that example), to the next level of success, instead of +5.
    - Every 5 values is a success level. Although in the example of "Chapter 2: Judgment" in the rule book, the success level is only 30, there are success levels higher than 30: 35, 40, 45. When any authentication value reaches one of the intervals, the fraud rule can make it just reach the next interval (example: 38 becomes 40). [[Success Level]] [[Chapter 2: Judgment]]
    - This can only cheat successful things: it cannot change a failed check to a success, nor change a successful check to a failure. Any fraud has to have an almost equally high correlation, so the similarity between "failure" and "success" isn't that great.
    - The definition of "success" is:
      - In attack identification, the identification exceeds the opponent's defense Difficulty Value. [[Attack Identification]] [[Defense Difficulty Value]]
      - In divination identification, it has reached the minimum value that divination can give a divination result (then it will be considered successful). [[Divination Identification]]
    - This ability doesn't change the base value of 1d20, only the final check, so it doesn't affect critical success or critical failure. [[Critical Success]] [[Critical Failure]]
  - **Lower the Success Level of the First-Level Skill Appraisal:** Same as above: it can only reduce failure severity; it cannot change success into a failure, and it does not affect the 1d20 base.

- **Aftereffects:** Fraud rules are a temporary ability, but the results achieved during the process of fraud rules will not be restored after the rules return to normal (example: resurrection through a false resurrection point will not be "bounced back" after restoration).
> **Lore:** The essence of this law is: "existence is reasonable".

- **Limits:** As described in this section's prose.


## GM Notes

> **GM Note:** The fraud rules themselves are not without restrictions and have clear logic. In general, the things being cheated are usually highly related to each other, or there must be something "exactly the same" in them (not merely similar). This principle is common to most of the fraud rule uses described above.
>
> **GM Note:** Examples from the original book:
> - Klein could only be resurrected in his real body at that time, but the real body was guarded by Amon, so he used fraud rules to resurrect elsewhere; the "false body" treated by the law was a bottle of Klein's own fresh blood (properly preserved), considered "exactly the same" at the core for fraud-rule purposes.
> - Amon connected entrances of two Doorway hidden spaces separated by great distance by treating their principles as "exactly the same," achieving teleportation via connected hidden spaces.
>
> **GM Note:** Player adjudication guidance drawn from the RAW: Players can conduct fraud based on the above principle. The things that are cheated must have a "strong correlation," otherwise the fraud rules cannot be established.

> **GM Note:** Other fraud rules that can be achieved through extraordinary power at the Sequence 2 level (RAW reference list):
>
> - Turn one's avatar into the main body:
>   - Prepare a clone of the same level as yourself (if you are a Sequence 2, your clone is at least a Sequence 2, because only Sequence 2 has the ability to steal fate and transfer fate).
>   - Let this double steal your identity, steal your consciousness, steal your destiny, and steal your self-knowledge.
>   - Only on the basis of such a strong connection can an avatar be considered "completely consistent" with you in terms of rules.
>   - On this basis, perform a fraud rule so the clone becomes your main body.
>   [[Fate Trojan Horse]]
>
> - Transferring other people's spiritual body threads to oneself:
>   - The RAW notes there is no definite evidence, but argues it is supported by passages involving Amon and a "transfer" (an exchange), where the user's own spiritual body thread is lost while the other party's remains.
>   - The RAW suggests this may involve transferring part of fate between oneself and a clone using the Sequence 2 Destiny Trojan Horse ability, then using fraud rules to affect only the astral thread rather than the whole body.
>   - The RAW notes this may be a compound application of Fate Trojan Horse and fraud rules, or it may be done by Fate Trojan Horse alone.
>   [[Spiritual Body Thread]] [[Astral Thread]] [[Destiny Trojan Horse]]
>
> **GM Note:** The RAW also references "Miracle Master of the Fool's Path Sequence 2" and "judges" as examples of the broader world-law principle that what has already happened and results already achieved are not pursued or undone. [[Miracle Master]] [[Judge]]
