# Ilsa, Frostwarden

**Status:** implemented in moba-arpg-game (2026-10-24). Numbers and talents are first versions to tune; the talents below are what the game has.

| | |
|---|---|
| Role | Ranged mage: control |
| Damage type | Frost (see [spell affinity](../../game-mechanics/spell-affinity/)) |
| Spell colours | Blue / white |
| Base stats | 540 HP · 26 damage · 6 range · 1.0 attacks/s · 6.4 speed · 400 mana |

## Passive: Chilling Touch
Her spell hits slow enemies by **20% for 1.5s**. Slowed enemies take **10% more spell damage** (from anyone).

## Ultimate (R): Glacial Prison
Marks a circle (radius 3.5m, cast range 9m). After **0.75s** every enemy inside is **frozen (stunned) for 1.5s**. The circle then stays as a **slowing field (30%) for 3s**.

| Rank | Freeze | Cooldown | Mana |
|---|---|---|---|
| 1 | 1.5s | 90s | 100 |
| 2 | 1.75s | 80s | 100 |
| 3 | 2s | 70s | 100 |

## Playstyle
Controls fights from range: slows whoever she hits, then locks a group down for her team. Weak when caught alone.

## Ascension (levels 6 / 11 / 18)
- **A, Deep Freeze** (passive, slows +5%): stronger, longer slows.
  - A1 Frostbite: slows +10%. A2 Lingering Frost: slows last 1s longer.
  - A3 Shatter: +20% spell damage. A4 Permafrost: slows +10%.
- **B, Winter's Grasp** (ultimate, ice field +1s): a stronger prison.
  - B1 Deep Ice: freeze +0.5s. B2 Cold Snap: ultimate cooldown -15%.
  - B3 Endless Winter: ice field +2s. B4 Glacial Age: ultimate cooldown -25%.
- **C, Glacier Walker** (hybrid, +5% move speed): kiting.
  - C1 Frost Armour: +150 max health. C2 Hailstorm: +1 projectile.
  - C3 Arctic Mind: cooldowns -10%. C4 Glacier Heart: +150 max mana.

Changed from the proposal: the 10% bonus applies to all of her damage against slowed enemies (not spell damage from anyone); no "slowed 3 times → frozen"; no prison radius talent.

## How it's built (moba-arpg-game)
- **Slow:** a new status `Slow` (like stun and burn), synced to game-server clients and shown as an icy border on health bars.
- **Chilling Touch:** `SpellHitPassive` reacts to her spell hits (new `SpellEvents.Hit`).
- **Glacial Prison:** a new reusable spell type `ZoneSpell` with `GroundZone` (warning ring, freeze, slowing field), shown on clients through the game server.

## Open questions
- Does the 10% damage bonus on slowed targets apply to everyone's spells, or only hers?
- Should the freeze warning be visible to enemies (fair) or only to her team?
