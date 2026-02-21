---
title: 'Sequence 8: Folk of Rage'
id: tyrant-seq-08
tags:
- pathway:tyrant
- sequence:8
---






# Tyrant Pathway: Sequence 8

> **Lore:** Known as the “Storm Guard” in ancient times. When angered, they can unleash attacks beyond normal limits. [[Storm Guard]]

## Folk of Rage

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Strength +1; Constitution +1; Agility (DEX) +1.

- **Enter Rage:** As a Free Action, you may begin charging for 1 Round; you can act normally during that round. At the end of the round, attempt to enter **Rage** with a Will Test (Difficulty Value 20).

  - **Alcohol Bonus:** If you have consumed [[Alcohol]], your Will Test to enter Rage gains +1 benefit; if you consumed [[Spirits]], it gains +2 benefit.

  - **Delayed Test:** If you do not make the Will Test in the first round of charging, you may try again in the second round at Difficulty Value 15; the third round succeeds by default.

  - **Anger Target:** Before you start charging, choose an **Anger Target**. After you enter Rage, all your attacks must first attack the source of anger. When the target’s companion tries to block you, you can attack that companion.

  - **Low Vitality:** If your [[Vitality]] is less than half, the Difficulty Value to enter Rage against your chosen **Anger Target** is halved (round down).

### Rage State

```yaml ability
id: tyrant-seq-08-rage-state
name: Rage State
pathway: tyrant
sequence: 8
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
- utility
text: Rage State ability details are retained in section prose.
```





- **Use:** You gain **Rage State** when you successfully enter Rage (see Attribute Gain).

- **Effect:**
  - This benefit is brought by a [[Potion]]; it cannot be stolen or recorded.
  - In Rage State, the effect changes to: Skill and Attribute identification is only **-2 disadvantageous**.
  - Strength +2; Constitution +2; Agility (DEX) +2.

- **Duration:** Rage State ends only after the source of anger dies/faints, or after you die/faint.  
  [[Unconscious]]

- **Behavior and Limits:**
  1) **Chasing the Enemy:** Even if the enemy escapes, you must first try to catch up.
  2) **Cancel Rage:** At the beginning of each round, you may attempt to quell Rage with a Will Test (Difficulty Value 15). If you do so, the alcohol advantage becomes disadvantageous.  
     Only your teammates can attempt to cancel your Rage State with a 1-action [[id:alias-psychological-guidance|Psychological Guidance]] or appropriate [[Social Skills]] check against your [[Physical Defense]]; on success, Rage ends.
  3) **Important Things:** If your rage would damage an ally or a personally important possession (declared by you at the start of the scene), your rage is immediately cleared.
  4) **Fast Dodge:** While in Rage State, you retain full [[Physical Defense]] against [[Guns]] (rather than losing Agility (DEX)/Dodge as against light/lightning-speed attacks), and gain an extra level of Dodge.

- **Limits:** As described in this section's prose.


### Furious Strike

```yaml ability
id: tyrant-seq-08-furious-strike
name: Furious Strike
pathway: tyrant
sequence: 8
status: canonical
type: active
action: attack
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
dice:
  check_roll: null
  damage_roll: 1d6
  heal_roll: null
  effect_roll: "1"
  notes: Adds +1d6 damage while in Rage State; can be invoked via full-round action without entering rage.
scaling: []
tags:
- ritual
- control
- offense
text: 'Cost: 1 Attack Action. No [[Spiritual Energy]] required. Use: Only usable while
  in Rage State. Effect: You punch forward. This attack adds +1d6 extra damage; the
  damage type is the same as the original. [[Damage Types]] Limits and Options: 1)
  Furious Strike cannot be combined with combo actions (e.g., double-hit style combos);
  you do not have enough spare energy to converge your strength. 2) If you use a [[Full-Round
  Action]] to restrain your breath and squeeze your anger, you can directly use Furious
  Strike. For that attack only, you gain the Rage bonuses (+2 Strength/Constitution/Agility
  (DEX) and the reduced -2 disadvantage), but you do not enter Rage State.'
```





- **Cost:** 1 Attack Action. No [[Spiritual Energy]] required.

- **Use:** Only usable while in **Rage State**.

- **Effect:** You punch forward. This attack adds **+1d6** extra damage; the damage type is the same as the original.  
  [[Damage Types]]

- **Limits and Options:**
  1) Furious Strike cannot be combined with combo actions (e.g., double-hit style combos); you do not have enough spare energy to converge your strength.
  2) If you use a [[Full-Round Action]] to restrain your breath and squeeze your anger, you can directly use Furious Strike. For that attack only, you gain the Rage bonuses (+2 Strength/Constitution/Agility (DEX) and the reduced -2 disadvantage), but you do not enter Rage State.

> **Lore:** Your muscles swell—strong enough to burst an enemy’s head at the end, or break the iron lock of a stone gate.

- **Limits:** As described in this section's prose.
