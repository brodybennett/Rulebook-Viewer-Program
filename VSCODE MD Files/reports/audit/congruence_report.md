# Congruence Audit Report

- Generated (UTC): `2026-02-21T21:09:17+00:00`
- Repo: `C:\Users\dan\Desktop\Personal\Projects\LoTM Rulebook\VSCODE MD Files`
- Content root: `draft`
- Markdown files scanned: **263**

## Summary

- High: **6**
- Medium: **25**
- Low: **103**

- High details:
  - Definition drift terms: **1**
  - Mechanic field drift blocks: **5**
- Medium details:
  - Heading collisions: **25**
- Low details:
  - `[[UNCLEAR: ...]]` markers: **0**
  - `[[LINK LATER: ...]]` markers: **0**
  - Unreferenced heading collisions: **103**

## High Severity

### Definition Drift (`**Term:** ...`)

#### Term: `Pathway` (5 occurrences, 3 variants)

- Variant (x3): `Earth Pathway.` (sample: `draft/sequences/earth/seq-02.md:18`)
- Variant (x1): `Visionary.` (sample: `draft/sequences/visionary/seq-03.md:18`)
- Variant (x1): `[[Red Priest]].` (sample: `draft/sequences/red-priest/seq-01.md:16`)
- Locations:
  - `draft/sequences/earth/seq-02.md:18` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/earth/seq-03.md:16` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/earth/seq-07.md:16` - `**Pathway:** Earth Pathway.`
  - `draft/sequences/red-priest/seq-01.md:16` - `**Pathway:** [[Red Priest]].`
  - `draft/sequences/visionary/seq-03.md:18` - `**Pathway:** Visionary.`

### Mechanic Field Drift (repeated heading blocks)

#### Block Title: `Spiritual Vision` (11 occurrences)

- Field `**Cost:**` -> conflicting values + missing field in some blocks (10/11 blocks have this field)
  - Variant (x9): `1 **spirituality point per round** while active.` (sample: `draft/sequences/apprentice/seq-09.md:173`)
  - Variant (x1): `Consuming 1 **spirituality point** per round.` (sample: `draft/sequences/red-priest/seq-09.md:374`)
- Field `**Use:**` -> conflicting values + missing field in some blocks (10/11 blocks have this field)
  - Variant (x9): `1 **free action** to activate.` (sample: `draft/sequences/apprentice/seq-09.md:173`)
  - Variant (x1): `1 free action.` (sample: `draft/sequences/red-priest/seq-09.md:374`)
- Field `**Effect:**` -> conflicting values (11/11 blocks have this field)
  - Variant (x9): `While active, your vision gains the following benefits:` (sample: `draft/sequences/apprentice/seq-09.md:173`)
  - Variant (x1): `Spiritual Vision resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.` (sample: `draft/sequences/night/seq-06.md:104`)
  - Variant (x1): `You activate Spiritual Vision, and your vision gains the following benefits:` (sample: `draft/sequences/red-priest/seq-09.md:374`)
- Locations:
  - `draft/sequences/apprentice/seq-09.md:173` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/earth/seq-09.md:384` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/error/seq-09.md:274` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/fate/seq-09.md:218` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/fool/seq-09.md:229` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/hanged-man/seq-09.md:109` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/mystery-pryer/seq-09.md:39` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/night/seq-06.md:104` - `### Spiritual Vision` | Cost=<missing>, Use=<missing>, Effect=Spiritual Vision resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.
  - `draft/sequences/reader/seq-09.md:408` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:
  - `draft/sequences/red-priest/seq-09.md:374` - `### Spiritual Vision` | Cost=Consuming 1 **spirituality point** per round., Use=1 free action., Effect=You activate Spiritual Vision, and your vision gains the following benefits:
  - `draft/sequences/visionary/seq-09.md:415` - `### Spiritual Vision` | Cost=1 **spirituality point per round** while active., Use=1 **free action** to activate., Effect=While active, your vision gains the following benefits:

#### Block Title: `Ritual Mastery` (7 occurrences)

- Field `**Effect:**` -> conflicting values (7/7 blocks have this field)
  - Variant (x6): `While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.` (sample: `draft/sequences/apprentice/seq-09.md:128`)
  - Variant (x1): `Ritual Mastery resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.` (sample: `draft/sequences/night/seq-06.md:155`)
- Locations:
  - `draft/sequences/apprentice/seq-09.md:128` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.
  - `draft/sequences/death/seq-07.md:380` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.
  - `draft/sequences/error/seq-09.md:228` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.
  - `draft/sequences/fool/seq-09.md:180` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.
  - `draft/sequences/night/seq-06.md:155` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=Ritual Mastery resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.
  - `draft/sequences/reader/seq-07.md:156` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.
  - `draft/sequences/reader/seq-09.md:96` - `### Ritual Mastery` | Cost=<missing>, Use=<missing>, Effect=While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.

#### Block Title: `Spirit Vision` (6 occurrences)

- Field `**Cost:**` -> missing field in some blocks (5/6 blocks have this field)
  - Variant (x5): `1 **Spirituality** per round.` (sample: `draft/sequences/abyss/seq-09.md:51`)
- Field `**Use:**` -> missing field in some blocks (5/6 blocks have this field)
  - Variant (x5): `1 **Free Action** to activate.` (sample: `draft/sequences/abyss/seq-09.md:51`)
- Field `**Effect:**` -> conflicting values (6/6 blocks have this field)
  - Variant (x5): `While Spirit Vision is active, you gain the following benefits:` (sample: `draft/sequences/abyss/seq-09.md:51`)
  - Variant (x1): `Spirit Vision resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.` (sample: `draft/sequences/death/seq-09.md:271`)
- Locations:
  - `draft/sequences/abyss/seq-09.md:51` - `### Spirit Vision` | Cost=1 **Spirituality** per round., Use=1 **Free Action** to activate., Effect=While Spirit Vision is active, you gain the following benefits:
  - `draft/sequences/death/seq-09.md:271` - `### Spirit Vision` | Cost=<missing>, Use=<missing>, Effect=Spirit Vision resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.
  - `draft/sequences/paragon/seq-09.md:208` - `### Spirit Vision` | Cost=1 **Spirituality** per round., Use=1 **Free Action** to activate., Effect=While Spirit Vision is active, you gain the following benefits:
  - `draft/sequences/sun/seq-09.md:223` - `### Spirit Vision` | Cost=1 **Spirituality** per round., Use=1 **Free Action** to activate., Effect=While Spirit Vision is active, you gain the following benefits:
  - `draft/sequences/tyrant/seq-09.md:279` - `### Spirit Vision` | Cost=1 **Spirituality** per round., Use=1 **Free Action** to activate., Effect=While Spirit Vision is active, you gain the following benefits:
  - `draft/sequences/war-god/seq-09.md:158` - `### Spirit Vision` | Cost=1 **Spirituality** per round., Use=1 **Free Action** to activate., Effect=While Spirit Vision is active, you gain the following benefits:

#### Block Title: `Divine Gaze` (5 occurrences)

- Field `**Effect:**` -> conflicting values (5/5 blocks have this field)
  - Variant (x4): `You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.` (sample: `draft/sequences/apprentice/seq-00.md:127`)
  - Variant (x1): `You can gaze at the surroundings of that creature, and use extraordinary abilities that normally target an area to target that area (normal range limits still apply).` (sample: `draft/sequences/arbiter/seq-00.md:33`)
- Locations:
  - `draft/sequences/apprentice/seq-00.md:127` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/arbiter/seq-00.md:33` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use extraordinary abilities that normally target an area to target that area (normal range limits still apply).
  - `draft/sequences/fool/seq-00.md:39` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/moon/seq-00.md:40` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.
  - `draft/sequences/visionary/seq-00.md:33` - `### Divine Gaze` | Cost=<missing>, Use=When any creature recites your **True Name**., Effect=You can gaze at the surroundings of that creature, and use your extraordinary abilities to target the area at will.

#### Block Title: `Premonition of Danger` (5 occurrences)

- Field `**Use:**` -> missing field in some blocks (2/5 blocks have this field)
  - Variant (x1): `Triggered whenever you are raided, sneak attacked, or something on the scene is about to put a raid or sneak attack into action. [[Raid]] [[Sneak Attack]] - **Use (additional tr...` (sample: `draft/sequences/fool/seq-08.md:57`)
  - Variant (x1): `Triggered whenever you are raided, sneak attacked, or there is something on the scene that is about to put the raid or sneak attack into action. | If 1 damage exceeds half of yo...` (sample: `draft/sequences/error/seq-07.md:47`)
- Field `**Effect:**` -> conflicting values (5/5 blocks have this field)
  - Variant (x2): `Premonition of Danger resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.` (sample: `draft/sequences/apprentice/seq-07.md:208`)
  - Variant (x1): `1) Make an Intuition (INT) appraisal (**Difficulty Value** 15). If you succeed, an idea flashes in your mind immediately, telling you the form of danger. - After you succeed, yo...` (sample: `draft/sequences/error/seq-07.md:47`)
  - Variant (x1): `Premonition of Danger resolves using its yaml ability block and section prose.` (sample: `draft/sequences/fool/seq-08.md:57`)
  - Variant (x1): `You have a keen intuition for danger and can foresee danger beyond your personality. | 1. Whenever you suffer any **Surprised**/**Sneak Attack**, you must perform a **Difficulty...` (sample: `draft/sequences/fate/seq-09.md:147`)
- Locations:
  - `draft/sequences/apprentice/seq-07.md:208` - `### Premonition of Danger` | Cost=<missing>, Use=<missing>, Effect=Premonition of Danger resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.
  - `draft/sequences/error/seq-07.md:47` - `### Premonition of Danger` | Cost=<missing>, Use=Triggered whenever you are raided, sneak attacked, or there is something on the scene that is about to put the raid or sneak attack into action. | If 1 damage exceeds half of yo..., Effect=1) Make an Intuition (INT) appraisal (**Difficulty Value** 15). If you succeed, an idea flashes in your mind immediately, telling you the form of danger. - After you succeed, yo...
  - `draft/sequences/fate/seq-09.md:147` - `### Premonition of Danger` | Cost=<missing>, Use=<missing>, Effect=You have a keen intuition for danger and can foresee danger beyond your personality. | 1. Whenever you suffer any **Surprised**/**Sneak Attack**, you must perform a **Difficulty...
  - `draft/sequences/fool/seq-08.md:57` - `### Premonition of Danger` | Cost=<missing>, Use=Triggered whenever you are raided, sneak attacked, or something on the scene is about to put a raid or sneak attack into action. [[Raid]] [[Sneak Attack]] - **Use (additional tr..., Effect=Premonition of Danger resolves using its yaml ability block and section prose.
  - `draft/sequences/night/seq-09.md:232` - `### Premonition of Danger` | Cost=<missing>, Use=<missing>, Effect=Premonition of Danger resolves using its yaml ability block and section prose. - **Limits:** As described in this section's prose.

## Medium Severity

### Heading Collisions

#### Heading: `Wheel of Fortune` (x2, linked 19x)

- Link references:
  - `draft/advanced-systems/mythical-creature-form.md:116` - `[[Wheel of Fortune]]`
  - `draft/advanced-systems/mythical-creature-form.md:474` - `[[Wheel of Fortune]]`
  - `draft/advanced-systems/mythical-creature-form.md:522` - `[[Wheel of Fortune]]`
  - `draft/core-rules/beyonder-items.md:44` - `[[Wheel of Fortune]]`
  - `draft/core-rules/combat/special-actions.md:401` - `[[Wheel of Fortune]]`
  - `draft/core-rules/skills-professions.md:249` - `[[Wheel of Fortune]]`
  - `draft/lore-reference/names-and-honorific-titles.md:153` - `[[Wheel of Fortune]]`
  - `draft/lore-reference/names-and-honorific-titles.md:158` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-00.md:16` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-00.md:16` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-00.md:21` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-02.md:18` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-02.md:19` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-03.md:18` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-04.md:18` - `[[Wheel of Fortune]]`
  - `draft/sequences/fate/seq-09.md:18` - `[[Wheel of Fortune]]`
  - `draft/sequences/mystery-pryer/seq-04.md:70` - `[[Wheel of Fortune]]`
  - `draft/sequences/mystery-pryer/seq-04.md:86` - `[[Wheel of Fortune]]`
  - `draft/sequences/reader/seq-01.md:33` - `[[Wheel of Fortune]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:934` (h2, `# wheel-of-fortune`) `## Wheel of Fortune`
- `draft/sequences/fate/seq-00.md:19` (h2, `# wheel-of-fortune`) `## Wheel of Fortune`

#### Heading: `Black Emperor` (x2, linked 18x)

- Link references:
  - `draft/advanced-systems/special-regions.md:592` - `[[Black Emperor]]`
  - `draft/core-rules/beyonder-items.md:34` - `[[Black Emperor]]`
  - `draft/lore-reference/names-and-honorific-titles.md:115` - `[[Black Emperor]]`
  - `draft/lore-reference/names-and-honorific-titles.md:185` - `[[Black Emperor]]`
  - `draft/lore-reference/names-and-honorific-titles.md:190` - `[[Black Emperor]]`
  - `draft/lore-reference/names-and-honorific-titles.md:196` - `[[Black Emperor]]`
  - `draft/sequences/apprentice/seq-03.md:65` - `[[Black Emperor]]`
  - `draft/sequences/apprentice/seq-03.md:76` - `[[Black Emperor]]`
  - `draft/sequences/arbiter/seq-03.md:69` - `[[Black Emperor]]`
  - `draft/sequences/arbiter/seq-03.md:84` - `[[Black Emperor]]`
  - `draft/sequences/arbiter/seq-06.md:356` - `[[Black Emperor]]`
  - `draft/sequences/black-emperor/seq-05.md:29` - `[[Black Emperor]]`
  - `draft/sequences/hanged-man/seq-05.md:109` - `[[Black Emperor]]`
  - `draft/sequences/reader/seq-09.md:340` - `[[Black Emperor]]`
  - `draft/sequences/war-god/seq-04.md:333` - `[[Black Emperor]]`
  - `draft/sequences/war-god/seq-04.md:347` - `[[Black Emperor]]`
  - `draft/sequences/war-god/seq-05.md:155` - `[[Black Emperor]]`
  - `draft/sequences/war-god/seq-05.md:166` - `[[Black Emperor]]`
- Heading locations:
- `draft/advanced-systems/bombard-and-killing-beyonders-module.md:348` (h2, `# black-emperor`) `## Black Emperor`
- `draft/sequences/black-emperor/seq-00.md:16` (h2, `# black-emperor`) `## Black Emperor`

#### Heading: `Red Priest` (x2, linked 17x)

- Link references:
  - `draft/core-rules/beyonder-items.md:36` - `[[Red Priest]]`
  - `draft/lore-reference/names-and-honorific-titles.md:138` - `[[Red Priest]]`
  - `draft/lore-reference/names-and-honorific-titles.md:148` - `[[Red Priest]]`
  - `draft/lore-reference/names-and-honorific-titles.md:190` - `[[Red Priest]]`
  - `draft/sequences/hanged-man/seq-06.md:71` - `[[Red Priest]]`
  - `draft/sequences/hanged-man/seq-06.md:81` - `[[Red Priest]]`
  - `draft/sequences/mystery-pryer/seq-06.md:160` - `[[Red Priest]]`
  - `draft/sequences/mystery-pryer/seq-07.md:69` - `[[Red Priest]]`
  - `draft/sequences/mystery-pryer/seq-07.md:84` - `[[Red Priest]]`
  - `draft/sequences/paragon/seq-06.md:278` - `[[Red Priest]]`
  - `draft/sequences/paragon/seq-07.md:138` - `[[Red Priest]]`
  - `draft/sequences/paragon/seq-07.md:152` - `[[Red Priest]]`
  - `draft/sequences/reader/seq-09.md:342` - `[[Red Priest]]`
  - `draft/sequences/red-priest/seq-01.md:16` - `[[Red Priest]]`
  - `draft/sequences/red-priest/seq-09.md:18` - `[[Red Priest]]`
  - `draft/sequences/red-priest/seq-09.md:339` - `[[Red Priest]]`
  - `draft/sequences/red-priest/seq-09.md:355` - `[[Red Priest]]`
- Heading locations:
- `draft/advanced-systems/bombard-and-killing-beyonders-module.md:397` (h2, `# red-priest`) `## Red Priest`
- `draft/sequences/red-priest/seq-00.md:16` (h2, `# red-priest`) `## Red Priest`

#### Heading: `Darkness` (x2, linked 12x)

- Link references:
  - `draft/core-rules/becoming-a-beyonder/madness-and-losing-control.md:100` - `[[Darkness]]`
  - `draft/core-rules/becoming-a-beyonder/spirituality-and-abilities.md:31` - `[[Darkness]]`
  - `draft/core-rules/beyonder-items.md:32` - `[[Darkness]]`
  - `draft/lore-reference/names-and-honorific-titles.md:23` - `[[Darkness]]`
  - `draft/lore-reference/names-and-honorific-titles.md:286` - `[[Darkness]]`
  - `draft/sequences/hanged-man/seq-00.md:22` - `[[Darkness]]`
  - `draft/sequences/night/seq-03.md:63` - `[[Darkness]]`
  - `draft/sequences/night/seq-03.md:76` - `[[Darkness]]`
  - `draft/sequences/night/seq-09.md:22` - `[[Darkness]]`
  - `draft/sequences/reader/seq-09.md:338` - `[[Darkness]]`
  - `draft/sequences/sun/seq-09.md:152` - `[[Darkness]]`
  - `draft/sequences/sun/seq-09.md:165` - `[[Darkness]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:558` (h2, `# darkness`) `## Darkness`
- `draft/sequences/night/seq-00.md:15` (h2, `# darkness`) `## Darkness`

#### Heading: `Hanged Man` (x2, linked 10x)

- Link references:
  - `draft/core-rules/beyonder-items.md:30` - `[[Hanged Man]]`
  - `draft/lore-reference/names-and-honorific-titles.md:74` - `[[Hanged Man]]`
  - `draft/lore-reference/names-and-honorific-titles.md:121` - `[[Hanged Man]]`
  - `draft/lore-reference/names-and-honorific-titles.md:314` - `[[Hanged Man]]`
  - `draft/sequences/abyss/seq-05.md:268` - `[[Hanged Man]]`
  - `draft/sequences/demoness/seq-07.md:658` - `[[Hanged Man]]`
  - `draft/sequences/error/seq-04.md:429` - `[[Hanged Man]]`
  - `draft/sequences/hanged-man/seq-00.md:18` - `[[Hanged Man]]`
  - `draft/sequences/hanged-man/seq-09.md:24` - `[[Hanged Man]]`
  - `draft/sequences/reader/seq-09.md:336` - `[[Hanged Man]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:2666` (h2, `# hanged-man`) `## Hanged Man`
- `draft/sequences/hanged-man/seq-00.md:16` (h2, `# hanged-man`) `## Hanged Man`

#### Heading: `Justiciar` (x3, linked 6x)

- Link references:
  - `draft/advanced-systems/special-regions.md:193` - `[[Justiciar]]`
  - `draft/core-rules/beyonder-items.md:35` - `[[Justiciar]]`
  - `draft/lore-reference/names-and-honorific-titles.md:196` - `[[Justiciar]]`
  - `draft/sequences/black-emperor/seq-04.md:26` - `[[Justiciar]]`
  - `draft/sequences/black-emperor/seq-05.md:27` - `[[Justiciar]]`
  - `draft/sequences/reader/seq-09.md:341` - `[[Justiciar]]`
- Heading locations:
- `draft/advanced-systems/bombard-and-killing-beyonders-module.md:380` (h2, `# justiciar`) `## Justiciar`
- `draft/sequences/arbiter/seq-00.md:18` (h2, `# justiciar`) `## Justiciar`
- `draft/sequences/arbiter/seq-02.md:16` (h2, `# justiciar`) `## Justiciar`

#### Heading: `Puppet` (x2, linked 3x)

- Link references:
  - `draft/sequences/fool/seq-04.md:88` - `[[Puppet]]`
  - `draft/sequences/fool/seq-04.md:100` - `[[Puppet]]`
  - `draft/sequences/moon/seq-01.md:87` - `[[Puppet]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:770` (h2, `# puppet`) `## Puppet`
- `draft/sequences/mutant/seq-05.md:16` (h2, `# puppet`) `## Puppet`

#### Heading: `Stunned` (x2, linked 3x)

- Link references:
  - `draft/core-rules/combat/special-actions.md:273` - `[[Stunned]]`
  - `draft/sequences/arbiter/seq-07.md:161` - `[[Stunned]]`
  - `draft/sequences/visionary/seq-04.md:236` - `[[Stunned]]`
- Heading locations:
- `draft/core-rules/combat/special-conditions.md:104` (h2, `# stunned`) `## Stunned`
- `draft/core-rules/link-target-aliases.md:426` (h2, `# stunned`) `## Stunned`

#### Heading: `Witch` (x2, linked 3x)

- Link references:
  - `draft/sequences/fool/seq-02.md:132` - `[[Witch]]`
  - `draft/sequences/red-priest/seq-09.md:339` - `[[Witch]]`
  - `draft/sequences/red-priest/seq-09.md:356` - `[[Witch]]`
- Heading locations:
- `draft/advanced-systems/bombard-and-killing-beyonders-module.md:422` (h2, `# witch`) `## Witch`
- `draft/sequences/demoness/seq-07.md:18` (h2, `# witch`) `## Witch`

#### Heading: `Worm of Time` (x2, linked 3x)

- Link references:
  - `draft/advanced-systems/mythical-creature-form.md:102` - `[[Worm of Time]]`
  - `draft/sequences/error/seq-02.md:242` - `[[Worm of Time]]`
  - `draft/sequences/fool/seq-02.md:38` - `[[Worm of Time]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:450` (h2, `# worm-of-time`) `## Worm of Time`
- `draft/sequences/error/seq-01.md:18` (h2, `# worm-of-time`) `## Worm of Time`

#### Heading: `Apothecary` (x2, linked 2x)

- Link references:
  - `draft/sequences/mystery-pryer/seq-09.md:242` - `[[Apothecary]]`
  - `draft/sequences/mystery-pryer/seq-09.md:259` - `[[Apothecary]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:1098` (h2, `# apothecary`) `## Apothecary`
- `draft/sequences/moon/seq-09.md:16` (h2, `# apothecary`) `## Apothecary`

#### Heading: `Clown` (x2, linked 2x)

- Link references:
  - `draft/sequences/visionary/seq-08.md:106` - `[[Clown]]`
  - `draft/sequences/visionary/seq-08.md:120` - `[[Clown]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:1542` (h2, `# clown`) `## Clown`
- `draft/sequences/fool/seq-08.md:18` (h2, `# clown`) `## Clown`

#### Heading: `Instigator` (x2, linked 2x)

- Link references:
  - `draft/sequences/visionary/seq-08.md:105` - `[[Instigator]]`
  - `draft/sequences/visionary/seq-08.md:120` - `[[Instigator]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:2914` (h2, `# instigator`) `## Instigator`
- `draft/sequences/demoness/seq-08.md:18` (h2, `# instigator`) `## Instigator`

#### Heading: `Reaper` (x2, linked 2x)

- Link references:
  - `draft/sequences/mutant/seq-05.md:268` - `[[Reaper]]`
  - `draft/sequences/mutant/seq-05.md:283` - `[[Reaper]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:3978` (h2, `# reaper`) `## Reaper`
- `draft/sequences/red-priest/seq-05.md:18` (h2, `# reaper`) `## Reaper`

#### Heading: `Rose Bishop` (x2, linked 2x)

- Link references:
  - `draft/sequences/earth/seq-06.md:171` - `[[Rose Bishop]]`
  - `draft/sequences/hanged-man/seq-09.md:273` - `[[Rose Bishop]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:806` (h2, `# rose-bishop`) `## Rose Bishop`
- `draft/sequences/hanged-man/seq-06.md:16` (h2, `# rose-bishop`) `## Rose Bishop`

#### Heading: `Apocalypse` (x2, linked 1x)

- Link references:
  - `draft/sequences/demoness/seq-01.md:22` - `[[Apocalypse]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:1094` (h2, `# apocalypse`) `## Apocalypse`
- `draft/sequences/demoness/seq-01.md:16` (h2, `# apocalypse`) `## Apocalypse`

#### Heading: `Dying Threshold` (x2, linked 1x)

- Link references:
  - `draft/core-rules/combat/combat-procedure.md:137` - `[[Dying Threshold]]`
- Heading locations:
- `draft/core-rules/combat/special-conditions.md:257` (h4, `# dying-threshold`) `#### Dying Threshold`
- `draft/core-rules/link-target-aliases.md:2102` (h2, `# dying-threshold`) `## Dying Threshold`

#### Heading: `Faceless` (x2, linked 1x)

- Link references:
  - `draft/sequences/hanged-man/seq-06.md:233` - `[[Faceless]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:2290` (h2, `# faceless`) `## Faceless`
- `draft/sequences/fool/seq-06.md:16` (h2, `# faceless`) `## Faceless`

#### Heading: `Gatekeeper` (x2, linked 1x)

- Link references:
  - `draft/sequences/night/seq-05.md:164` - `[[Gatekeeper]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:2534` (h2, `# gatekeeper`) `## Gatekeeper`
- `draft/sequences/death/seq-06.md:18` (h2, `# gatekeeper`) `## Gatekeeper`

#### Heading: `Nightmare` (x2, linked 1x)

- Link references:
  - `draft/sequences/night/seq-03.md:25` - `[[Nightmare]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:3482` (h2, `# nightmare`) `## Nightmare`
- `draft/sequences/night/seq-07.md:21` (h2, `# nightmare`) `## Nightmare`

#### Heading: `Off-Balance` (x2, linked 1x)

- Link references:
  - `draft/core-rules/combat/special-actions.md:255` - `[[Off-Balance]]`
- Heading locations:
- `draft/core-rules/combat/special-actions.md:257` (h3, `# off-balance`) `### Off-Balance`
- `draft/core-rules/combat/special-conditions.md:9` (h2, `# off-balance`) `## Off-Balance`

#### Heading: `Pleasure` (x2, linked 1x)

- Link references:
  - `draft/sequences/demoness/seq-08.md:44` - `[[Pleasure]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:3698` (h2, `# pleasure`) `## Pleasure`
- `draft/sequences/demoness/seq-06.md:18` (h2, `# pleasure`) `## Pleasure`

#### Heading: `Poisoned` (x2, linked 1x)

- Link references:
  - `draft/core-rules/combat/special-actions.md:340` - `[[Poisoned]]`
- Heading locations:
- `draft/core-rules/combat/special-conditions.md:227` (h2, `# poisoned`) `## Poisoned`
- `draft/core-rules/link-target-aliases.md:3714` (h2, `# poisoned`) `## Poisoned`

#### Heading: `Silver Knight` (x2, linked 1x)

- Link references:
  - `draft/advanced-systems/mythical-creature-form.md:418` - `[[Silver Knight]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:4274` (h2, `# silver-knight`) `## Silver Knight`
- `draft/sequences/war-god/seq-03.md:22` (h2, `# silver-knight`) `## Silver Knight`

#### Heading: `Vampire` (x2, linked 1x)

- Link references:
  - `draft/advanced-systems/mythical-creature-form.md:465` - `[[Vampire]]`
- Heading locations:
- `draft/core-rules/link-target-aliases.md:4962` (h2, `# vampire`) `## Vampire`
- `draft/sequences/moon/seq-07.md:16` (h2, `# vampire`) `## Vampire`

## Low Severity

### `[[UNCLEAR: ...]]` Markers

- None found.

### `[[LINK LATER: ...]]` Markers

- None found.

### Unreferenced Heading Collisions

- These collisions currently have no plain `[[Title]]` references, so they are lower-priority unless you plan to link to them by title.
- `Advancement` (x221)
- `Extraordinary Abilities` (x221)
- `Attribute Gain` (x220)
- `Advancement Ritual` (x189)
- `Auxiliary Materials` (x123)
- `Main Materials` (x97)
- `Canon Lore Placeholder` (x28)
- `Mechanics Stub` (x28)
- `Spiritual Vision` (x11)
- `Description` (x10)
- `Acting Rules` (x7)
- `Ritual Mastery` (x7)
- `Spirit Vision` (x7)
- `Vision` (x6)
- `Divine Gaze` (x5)
- `Premonition of Danger` (x5)
- `Sequence abilities` (x5)
- `Sequence abilities (overview)` (x5)
- `Breeding Environment` (x4)
- `Common Items` (x4)
- `Full Moon Curse` (x4)
- `Overview` (x4)
- `Sequence 4` (x4)
- `Abyss` (x3)
- `Acting` (x3)
- `Additional` (x3)
- `Basic Data` (x3)
- `Combat` (x3)
- `Divination` (x3)
- `Habits` (x3)
- `Insight` (x3)
- `Living Environment` (x3)
- `Quick Dodge` (x3)
- `Roleplay` (x3)
- `Sequence 1` (x3)
- `Sequence 2` (x3)
- `Sequence 3` (x3)
- `Taste` (x3)
- `Tyrant` (x3)
- `Visionary` (x3)
- ... +63 more
