# Thessa, Windrunner

**Status:** implemented in moba-arpg-game (2026-10-24). Numbers and talents are first versions to tune; the talents below are what the game has.

| | |
|---|---|
| Role | Ranged skirmisher: hit and run |
| Damage type | Air (see [spell affinity](../../game-mechanics/spell-affinity/)) |
| Spell colours | Light grey / teal |
| Base stats | 550 HP · 30 damage · 6 range · 1.2 attacks/s · 6.8 speed · 320 mana |

## Passive: Tailwind
Each spell she casts gives **25% move speed for 2s** (casting again refreshes it).

## Ultimate (R): Eye of the Storm
For **6 / 7 / 8s** her spells **cost no mana** and have **50% shorter cooldowns**.

| Rank | Duration | Cooldown | Mana |
|---|---|---|---|
| 1 | 6s | 80s | 0 |
| 2 | 7s | 70s | 0 |
| 3 | 8s | 60s | 0 |

## Playstyle
Cast, reposition, cast again. Strong with fast, cheap spells; the ultimate turns a fight into a spell storm.

## Ascension (levels 6 / 11 / 18)
- **A, Gale** (passive, +0.5s Tailwind): a stronger, longer Tailwind.
  - A1 Jet Stream: +10% Tailwind speed. A2 Updraft: +1s Tailwind.
  - A3 Slipstream: +20% attack speed during Tailwind. A4 Second Gust: +1.5s Tailwind.
- **B, Hurricane** (ultimate, +1s storm): a longer storm.
  - B1 Eye Widens: +2s storm. B2 Charged Air: +15% spell damage.
  - B3 Ceaseless: cooldowns -10%. B4 Calm Before: ultimate cooldown -25%.
- **C, Skirmisher** (hybrid, +10% attack speed): hit and run.
  - C1 Quickdraw: +15% attack speed. C2 Light Feet: +10% move speed.
  - C3 Crosswind: +1 projectile on projectile spells. C4 Windward: cooldowns -10%.

Changed from the first proposal to fit what talents can do today: A4 (was "every 3rd spell doubles Tailwind"), B2 (was "60% shorter cooldowns during the storm"), B3 (was "+15% spell damage during the storm").

## How it's built (moba-arpg-game)
- **Tailwind:** `TailwindPassive` listens for spell casts; new talent stats `tailwindSpeed`, `tailwindDuration`, `tailwindAttackSpeed`.
- **Eye of the Storm:** a new spell type `SpellStormSpell` and timed buff `SpellStorm` (temporary cooldown and mana multipliers on the caster, teal ground ring), synced to game-server clients like Bloodrush.
- **Decided:** the storm doesn't reset cooldowns already running; Tailwind stacks with other speed buffs.

## Open questions
- Does Eye of the Storm also reset the cooldowns that are running when it starts?
- Should Tailwind stack with Bloodrush-style speed buffs?
