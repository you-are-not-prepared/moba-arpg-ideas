# Hero kit rework

**Status:** idea, to discuss (2026-10-25). Nothing here is built yet.

## Summary

Five ideas that belong together. They move heroes from a fixed MOBA kit (passive + locked ultimate) to **a hero identity plus the player's build**, which fits the ARPG side of the game better.

1. **Signature spell.** Heroes start with their passive and **one basic spell**, instead of passive + ultimate.
2. **Choose your ultimate.** The **first ascension** gives a choice between **several ultimates**.
3. **Shape your ultimate.** The **second and third ascensions** modify the chosen ultimate.
4. **Damage types.** The six types from [spell affinity](../spell-affinity/): Fire, Frost, Nature, Lightning, Physical, Air.
5. **Ascension points.** The ultimate rank-up points (levels 6/11/16) become **ascension points**, gained at the same levels.

## How it works today

- **Ultimate:** each hero has a passive and one ultimate, locked into R. It's ranked up at levels 6/11/16 with skill points.
- **Q/W/E:** the shop sells spells and mods for these slots. At levels 1–5 a hero has only their passive and whatever they bought.
- **Ascension:** at levels 6/11/18 the player picks talents. Level 6 picks a path (A builds on the passive, B on the ultimate, C is a hybrid), and 11 and 18 offer two talents from that path. Most talents are flat stats ("+150 max health", "+1s ultimate duration").

## The ideas

### 1. Signature spell
Every hero starts with one basic spell that fits them: Ilsa a frost bolt, Oren a fiery strike, Corvin a lightning bolt.

- **Why:** a recognisable playstyle from minute one. Today levels 1–5 feel the same for every hero.
- **Fits damage types:** the signature spell carries the hero's base damage type and colours.

### 2. Choose your ultimate (first ascension)
At the first ascension the player picks one of several ultimates. That choice is the hero's path: the next two ascensions follow it.

- **Why:** more replayability and real build decisions, while the hero keeps its identity (all options fit the hero).
- **Fits what exists:** paths A/B/C already lean this way, so each path would become one ultimate. Today's ultimates (Skybreaker Arrow, Aegis Wall, Glacial Prison…) become one of each hero's options.
- **Cost:** about 2–3 ultimates per hero, so ~30 for 10 heroes. The reusable spell types (`ZoneSpell`, `LeapSpell`, storm and timed buffs) make many of them mostly new numbers and visuals on an existing type.

### 3. Shape your ultimate (second and third ascensions)
The later ascensions change how the chosen ultimate works, e.g. "Glacial Prison also shatters for damage when it ends" or "Blazing Leap leaves a burning trail".

- **Why:** fixes the weakest part of today's talents. Flat stats ("+1s duration") are bland; changing how the ultimate behaves is a real choice.
- **How:** ultimate talents can work like built-in mods, using the same modifier system as Volley/Fork/Searing.

### 4. Damage types
The six damage types from [spell affinity](../spell-affinity/), each hero with affinities toward some of them, spells taking the hero's damage type and look, and conversion mods.

- **The biggest change of the five.** Every spell, mod, item and hero touches it.
- **Phasing:**
  1. types and hero affinities, as numbers only;
  2. spell look per hero (colours, projectile shape);
  3. conversion mods.

### 5. Ascension points instead of ultimate points
The skill points spent on ultimate ranks at 6/11/16 become ascension points at the same levels.

- **Why:** if ascensions shape the ultimate, separate ultimate ranks are redundant.
- **Side effects:**
  - The ultimate's power curve then comes only from ascensions.
  - The 3 freed skill points would push basic spells to max rank sooner, so the level and skill-point curve needs a look.
  - Ascension picks are at 6/11/18 today, so the third pick would move from 18 to 16 (to be settled).

## Suggested order

1. **Damage types first:** spells, mods, items and heroes all depend on them, and 20 spells and 30 mods are planned. Building those before damage types exist means revisiting all of them.
2. **Then the kit rework, as one change:** ideas 1, 2, 3 and 5 only make sense together.
3. **Then the content:** new spells, mods and heroes, built once for the final system.

## Open questions

1. **Signature spell:** locked to its slot, or a normal spell the player can move, mod or replace? (Leaning: normal but free, to respect build freedom.)
2. **Ultimates:** unique per hero, or a shared pool with hero-specific options mixed in?
3. **How many choices:** 2 or 3 ultimates per hero?
4. **Resistances:** does each damage type map to armour vs magic resist, or do all six get their own resistance?
5. **Bots:** how do they choose their ultimate? Random, by hero, or by what the team needs?
6. **Levels:** do ascension picks happen at 6/11/16 or 6/11/18?
7. **Existing heroes:** do their current ascension trees get rewritten, or kept for path flavour?

## What it touches in the game

- **Hero definitions:** a signature spell instead of a locked ultimate; ultimate options per path.
- **Ascension:** the first pick sets the ultimate; later picks are ultimate modifiers instead of only stats.
- **Ultimate ranks and skill points:** `AbilityCaster.RequiredLevel`, the level curve, the HUD's level-up buttons.
- **Champion select and tooltips:** show the ultimate options per hero.
- **Bots:** picking an ultimate.
- **Match history:** record the chosen ultimate in builds.
