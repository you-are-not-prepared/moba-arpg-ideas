# Maela, Grovekeeper

**Status:** implemented in moba-test (2026-10-24). Numbers and talents are first versions to tune; the talents below are what the game has.

| | |
|---|---|
| Role | Support: healing |
| Damage type | Nature (see [spell affinity](../../game-mechanics/spell-affinity/)) |
| Spell colours | Green / gold |
| Base stats | 580 HP · 25 damage · 5.5 range · 1.0 attacks/s · 6.5 speed · 420 mana |

## Passive: Verdant Bond
When her spells hit enemies, the **nearest allied hero** (within 8m, not herself) is **healed for 15% of the damage dealt**.

## Ultimate (R): Sanctuary
A grove (radius 5m, cast range 8m) for **6s**. Allies inside heal **4% of max health per second** and move **20% faster**; enemies inside are **slowed by 20%**.

| Rank | Healing / s | Cooldown | Mana |
|---|---|---|---|
| 1 | 4% | 100s | 120 |
| 2 | 5% | 90s | 120 |
| 3 | 6% | 80s | 120 |

## Playstyle
The first real support: keeps a lane partner or the whole team alive, and turns team fights with Sanctuary. Damage spells are how she heals, so she still fights.

## Ascension (levels 6 / 11 / 18)
- **A, Lifebloom** (passive, +5% healing): stronger healing.
  - A1 Deep Roots: +10% healing. A2 Wildgrowth: +10% spell damage (so more healing).
  - A3 Full Bloom: +10% healing. A4 Barkskin: +200 max health.
- **B, Sacred Grove** (ultimate, grove +1s): a longer, more frequent grove.
  - B1 Old Growth: grove +2s. B2 Quick Sprouts: ultimate cooldown -15%.
  - B3 Seasons: cooldowns -10%. B4 Evergreen: ultimate cooldown -25%.
- **C, Warden of the Wild** (hybrid, +150 max health): a sturdy support.
  - C1 Thorns: +10 attack damage. C2 Swiftwood: +8% move speed.
  - C3 Sap: +150 max mana. C4 Ironbark: +25 max health per level.

Changed from the proposal: no healing of two allies, no shield, no damaging grove (talents can't do those yet). The grove heals allied heroes only, not creeps.

## How it's built (moba-test)
- **Verdant Bond:** `SpellHitPassive` (shared with Ilsa) heals the nearest allied hero when her spells hit.
- **Sanctuary:** the same `ZoneSpell` as Ilsa's prison, set up as a healing, speeding grove that slows enemies.
- No healing pop-ups yet (health bars show it).

## Open questions
- Should healing be shown to everyone (pop-ups over allies) or only to her?
- Does Sanctuary heal creeps too?
