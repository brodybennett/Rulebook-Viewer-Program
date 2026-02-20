---
title: 'Sequence 9: Apprentice'
id: apprentice-seq-09
tags:
- pathway:apprentice
- sequence:9
---





# Door Pathway: Sequence 9

## Apprentice

> **Lore:** Corresponds to the material gem, and to the Tarot card “Magician.” This is the beginning of a mage genre, pursuing the footsteps of freedom.

## Advancement

### Main Materials

- **Main Materials:** TBD.

### Auxiliary Materials

- **Auxiliary Materials:** TBD.

### Advancement Ritual

- **Advancement Ritual:** TBD.

## Extraordinary Abilities

### Attribute Gain

- **Attribute Gain:** **Intuition (INT)** +2.
- **Skill Increase:** Your **Locksmith** skill increases by 1 level.
- **Occult Training (Guidance):**
  - Each time you receive **effective**, **authentic**, and **non-repetitive** occult guidance that lasts at least **2 hours**, your **Occult** level increases by **1 level**.
  - You must gain this benefit **2 times** to reach **Proficiency**, **3 times** to reach **Advanced**, and **4 times** to reach **Mastery**.
  - **Limit:** This learning is limited to **1 time per day**.
  - **Cap:** This cannot increase the skill level beyond your tutor or book.
- **Character Creation (Higher Sequence Start):** When directly creating a character with a higher **Sequence**, the growth-skill increase is determined by the GM (typically based on the potion's Intuition (INT)) to make up for the gap in growth.

### Open the Door

```yaml ability
id: apprentice-seq-09-open-the-door
name: Open the Door
pathway: apprentice
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: difficulty_value
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
- mobility
text: 'Use: 1 Casting Action. Cost: 2 spirituality points. Effect: Choose one of the
  following effects: 1) Open a lock You can open any lock that does not have extraordinary
  power. For a lock that has extraordinary power but is not higher than your Sequence
  level, you can attempt to open it with an Intuition (INT) + Locksmith test at Difficulty
  Value 20. In special cases, it may be against the identification of the person who
  locked the lock. 2) Create a passage through a barrier'
```




- **Use:** 1 **Casting Action**.
- **Cost:** 2 **spirituality points**.
- **Effect:** Choose one of the following effects:

1) **Open a lock**
   - You can open any lock that does not have extraordinary power.
   - For a lock that has extraordinary power but is not higher than your **Sequence level**, you can attempt to open it with an **Intuition (INT) + Locksmith** test at **Difficulty Value 20**.
   - In special cases, it may be against the identification of the person who locked the lock.

2) **Create a passage through a barrier**
   - Without using the main entrance, without opening a lock, or where there is no door, you press your hand on a wall (or other barrier) **not more than 1 meter thick** to create a vague blue door.
   - Only you can pass through it, like a curtain of water, going straight through the barrier.
   - **Special:** This effect is equivalent to [[Through the Wall]].
     - Eliminating the door is a **free action**.
     - The blue door will not appear if you go through the wall alone.

3) **Create a peephole door**
   - **Use:** 1 **free action**.
   - **Cost:** 1 **spirituality point**.
   - You create an eye-sized door for peeping. You must touch the wall or other barrier.
- You can only make smaller doors, not large enough for a carriage.

- **At Sequence 7:** You can bring other creatures to go through the wall together.

- **Limits:** As described in this section's prose.


### Ritual Mastery
```yaml ability
id: apprentice-seq-09-ritual-mastery
name: Ritual Mastery
pathway: apprentice
sequence: 9
type: active
action: cast
cost: {}
roll: null
opposed_by: none
range: self
target: self
duration: instant
scaling: []
tags:
- ritual
text: 'Effect: While holding this ability, you gain access to ritual magic, regardless
  of whether your Occult skill is advanced or not. While holding this ability, you
  gain access to ritual magic regardless of whether your Occult skill is advanced
  or not. For the ritual magic you can use, refer to [[Common Ritual Magic]]. Special:
  This is the effect brought by 1 potion and cannot be stolen or recorded.'
```




- **Effect:** While holding this ability, you gain access to ritual magic, regardless of whether your Occult skill is advanced or not.


- While holding this ability, you gain access to ritual magic regardless of whether your **Occult** skill is advanced or not.
- For the ritual magic you can use, refer to [[Common Ritual Magic]].
- **Special:** This is the effect brought by 1 potion and cannot be stolen or recorded.

- **Limits:** As described in this section's prose.


### Spiritual Vision
```yaml ability
id: apprentice-seq-09-spiritual-vision
name: Spiritual Vision
pathway: apprentice
sequence: 9
type: toggle
action: free
cost: {}
roll: null
opposed_by: none
range: self
target: designated target(s)
duration: sustained
scaling: []
tags:
- ritual
- detection
- healing
- mobility
text: 'Use: 1 free action to activate. Cost: 1 spirituality point per round while
  active. Effect: While active, your vision gains the following benefits: 1) Etheric
  Body You can directly see the targets health status through the color of the aura.
  You can directly find where the other partys body is uncomfortable/has a problem.
  When it comes to a certain organ, you can see the inside through a not-thick door.
  You can confirm the number of people inside by seeing through the door.'
```




- **Use:** 1 **free action** to activate.
- **Cost:** 1 **spirituality point per round** while active.
- **Effect:** While active, your vision gains the following benefits:


1) **Etheric Body**
   - You can directly see the target’s health status through the color of the aura.
   - You can directly find where the other party’s body is uncomfortable/has a problem.
   - When it comes to a certain organ, you can see the inside through a not-thick door.
   - You can confirm the number of people inside by seeing through the door.

2) **Spiritual Body**
   - You can confirm whether an object/creature has spirituality.
   - This cannot identify extraordinary people.
   - You can penetrate a door to see the inside.
   - You can identify whether there is ritual magic power in it.
   - You can penetrate the spiritual wall.

3) **Mental Body**
   - You can see the color represented by the other person’s emotions, but only general content (e.g., depressed vs. uneasy).
   - Negative emotion is usually a dark tone.

4) **Astral Body**
   - You cannot see the astral body.

5) **Spiritual Intuition**
   - While in the state of spiritual vision, you gain **+2** to **Spiritual Intuition** tests.

- **Notes:**
  - Dead creatures are usually only dull in color and cannot be recognized.
  - Spiritual materials usually have spirituality.
  - The color of a material in spiritual vision usually represents its corresponding **Pathway**; this does not mean you can see the power of a **Beyonder** Pathway.
  - The color seen by spirit vision allows you to see each other in the dark, but you can only see the existence of color; it is still possible to get lost in the dark.
  - Unlike dead creatures, undead creatures have deep black spirituality color instead of none.
  - Spirit Vision can see some ordinary spirit bodies by default, which have not dissipated for 24 hours, and cannot be recorded or stolen.

- **Limits:** As described in this section's prose.
