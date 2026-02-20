---
title: 'Sequence 6: Notary'
id: sun-seq-06
tags:
- pathway:sun
- sequence:6
---





# Sun Pathway: Sequence 6

## Notary

Notaries specialize in **Notarization**—certifying the authenticity of [[Extraordinary Knowledge]] (including [[Potion Formula]]) and interacting with [[id:alias-extraordinary-ability|Extraordinary Ability]] effects as they are cast. They also excel at binding agreements through **Contracts**.

> **Lore:** Notaries are support-focused Beyonders who “certify” truth and enforce binding terms.

## Advancement

### Auxiliary Materials

- **Main Materials:** Crystal Root of the Tree of the Elders ×1; Tail Feathers of the Kitten ×5
- **Auxiliary Materials:** Radiant Qiling Tree Sap (100 ml); Phnom Penh Sunflower ×1; White Edge Sunflower ×1; Water Fern Juice (drops) ×5

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** Agility (DEX) +1; Intuition (INT) +1; Constitution +2
- **Law:** Included in the category of [[Rapid Improvement]] up to [[Mastery]].

### Notarization

```yaml ability
id: sun-seq-06-notarization
name: Notarization
pathway: sun
sequence: 6
type: active
action: swift
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- buff
text: 'Notarize the authenticity of [[Extraordinary Knowledge]] or the casting of
  an [[id:alias-extraordinary-ability|Extraordinary Ability]]. Cost: 4 [[Spirit Points]]
  Use: 1 Swift Action. Choose one option below each time you use Notarization. ####
  Valid Notarization (Effectiveness) You temporarily improve an extraordinary ability
  you notarize as effective. Use requirement: Speak the keyword effective in the [[Language
  of Mysticism]]. You may add your own prefix (example: God said, it is effective!).
  Timing / limits: When you cast an [[id:alias-extraordinary-ability|Extraordinary
  Ability]], you may use this immediately on that casting.'
```




“Notarize” the authenticity of [[Extraordinary Knowledge]] or the casting of an [[id:alias-extraordinary-ability|Extraordinary Ability]].

- **Cost:** 4 [[Spirit Points]]
- **Use:** 1 Swift Action. Choose **one** option below each time you use Notarization.

#### Valid Notarization (Effectiveness)

You temporarily improve an extraordinary ability you notarize as “effective.”

- **Use requirement:** Speak the keyword **“effective”** in the [[Language of Mysticism]]. You may add your own prefix (example: “God said, it is effective!”).
- **Timing / limits:**
  - When you cast an [[id:alias-extraordinary-ability|Extraordinary Ability]], you may use this immediately on that casting.
  - Notarization can only be used simultaneously with other abilities and only takes effect once.
- **Effect (choose what applies to the notarized ability):**
  1. **Damage-type ability:** Increase the damage by **+1d10**. The damage type is the same as the original [[Damage Type]].
  2. **Effect increase / assistance / change-type ability:** Increase the effect by **half** (rounded down).
  3. **Consumables (e.g., [[Extraordinary Potion]]):** At the moment they are used, they gain benefit (1) or (2) based on their specific effect.
  4. **Manufacturing / detection abilities:** Increase the relevant check result by **+5** (one difficulty tier) for that notarized use, to a maximum effective result of **25**; this does not create an automatic critical success.

#### Invalid Notarization (Invalidation)

You deem a cast extraordinary ability “invalid,” weakening it or forcibly dispersing it.

- **Use requirement:** Speak the keyword **“invalid”** in the [[Language of Mysticism]]. You may add your own prefix (example: “God said, invalid!”).
- **Timing / limits:**
  - When an [[id:alias-extraordinary-ability|Extraordinary Ability]] is cast, you use this immediately.
  - Because “valid” and “invalid” must be used at the moment the ability is cast, it:
    - Cannot affect extraordinary abilities cast in advance, and
    - Cannot affect purely physical actions that are not extraordinary abilities.
- **Effect:**
  1. The invalidated ability is regarded as **not used**; it is invalidated, and any materials/actions consumed are **not returned**.
  2. For two consecutive strikes or multiple strikes that consume the same action, all of them are invalidated together.
  3. **Examples (clarification):**
     - You can invalidate a zombie’s ability to condense frost on its fists, but you cannot invalidate the zombie’s act of charging and punching you.
     - You can negate a magma sword condensed by a demon, but you cannot “condense it in advance” and then negate your later physical cutting action.
- **Special:** Extraordinary abilities cast by targets more than 1 Sequence higher than you only have **half** effect (rounded up) when invalidated.

#### Notarize Extraordinary Knowledge

You notarize whether **1** piece of [[Extraordinary Knowledge]] is true.

- **Requirement:** Whatever Beyonder knowledge is notarized, its specific content must be written down. You notarize based on the written content.
- **Effect:**
  1. **Potion formula:** If the formula content is true (not false), you immediately know it is “effective.”
  2. **Extraordinary information:** You can identify whether a piece of extraordinary information is true or false, but the information must exist objectively and include detailed specifics. If it is only a simple clue (“possible” / not objective fact) without complete details, its authenticity cannot be notarized.
     - Example: “You might be able to obtain a potion recipe somewhere” cannot be notarized.
     - If the source specifies which block, where in the house, and which paper contains an effective, authentic potion formula—and it truly exists—then it can be notarized.

- **Limits:** As described in this section's prose.


### Make a Contract

```yaml ability
id: sun-seq-06-make-a-contract
name: Make a Contract
pathway: sun
sequence: 6
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: instant
scaling: []
tags:
- utility
text: 'Make a Contract. Once you sign and approve it, higher-Sequence powerhouses
  must pay a price to violate it (RAW: Sequence 5 cannot violate it, and even a demigod
  of Sequence 4 pays a big price). Interpretation: automatic forced compliance applies
  to targets not higher than a Notary; higher-Sequence targets may still breach, but
  pay the contract penalty/price. There are two forms: Written Contract: Use parchment
  to write the behaviors both parties must perform (e.g., neither party harms the
  other during a set time; both must help obtain something). Then both parties sign
  the parchment. The signature may be a code name or pseudonym, but the name must
  belong to the signer (including their own...'
```




Make a **Contract**. Once you sign and approve it, higher-Sequence powerhouses must pay a price to violate it (RAW: “Sequence 5 cannot violate it,” and even a “demigod of Sequence 4” pays a big price).  
Interpretation: automatic forced compliance applies to targets **not higher than a Notary**; higher-Sequence targets may still breach, but pay the contract penalty/price.

There are two forms:

1. **Written Contract:** Use parchment to write the behaviors both parties must perform (e.g., neither party harms the other during a set time; both must help obtain something). Then both parties sign the parchment.
   - The signature may be a code name or pseudonym, but the name must belong to the signer (including their own false identity). This does not affect the mysticism “pointing” still being them.
2. **Oral Contract:** The parties sign on parchment, but the terms are stated orally.

**Procedure (both forms):**

- If one party is unwilling to sign, they may press their palm on the parchment instead; esoteric information is absorbed to lock the signer themself.
- Once completed, both parties feel an invisible bondage and subtle connection.
- A contract may also be one-way (e.g., a confidentiality clause) where only one person signs and is affected.

**Execution:**

1. Once the signature is successful, as long as the target is not higher than a Notary, both parties must fulfill the terms. If not, mysticism enforces compliance, ensuring they cannot violate the terms.
2. Optional: Write the breach price into the contract when signing (what must be paid upon breach). This usually only takes effect on sentient beings with **Personality** 2+ and is enforced after a breach.
3. Contracts with more than 2 persons generally have no reliable effect and are mostly formalism.

**Default penalty (if no breach price is written):** The party who violates the terms immediately loses all [[Life Points]], falls into a [[Near-Death]], and this cannot be resisted by a [[Substitute]].

- **Effect:** Make a Contract resolves using its yaml ability block and section prose.
- **Limits:** As described in this section's prose.
