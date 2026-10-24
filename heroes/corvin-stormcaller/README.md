# Corvin, Stormcaller

**Status:** implemented in moba-test (2026-10-24). Numbers and talents are first versions to tune; the talents below are what the game has.

| | |
|---|---|
| Role | Ranged caster: sustained damage |
| Damage type | Lightning (see [spell affinity](../../game-mechanics/spell-affinity/)) |
| Spell colours | Purple / white |
| Base stats | 550 HP · 27 damage · 6 range · 1.1 attacks/s · 6.5 speed · 380 mana |

## Passive: Static Charge
Every **4th spell** he casts is charged: its hits **jump to 1 more enemy** within 5m for **50% damage**.

## Ultimate (R): Thunderhead
A storm cloud follows him for **6s** and strikes a random enemy within **6m** every **0.5s** (60 / 90 / 120 damage by rank, heroes preferred over creeps).

| Rank | Damage per strike | Cooldown | Mana |
|---|---|---|---|
| 1 | 60 | 80s | 100 |
| 2 | 90 | 70s | 100 |
| 3 | 120 | 60s | 100 |

## Playstyle
Spell spam: the more he casts, the more lightning. Pairs naturally with Volley and Fork mods (more hits = more jumps).

## Ascension (levels 6 / 11 / 18)
- **A, Overcharge** (passive, charged every 3rd spell): more lightning.
  - A1 Arc: +1 chain jump. A2 Voltage: +10% spell damage.
  - A3 Chain Reaction: +1 chain jump. A4 Full Charge: charged one more cast sooner.
- **B, Tempest** (ultimate, storm +1s): a longer, more frequent storm.
  - B1 Brewing Storm: storm +2s. B2 Thunderclap: +15% spell damage.
  - B3 Gathering Clouds: ultimate cooldown -20%. B4 Eye of Thunder: ultimate cooldown -25%.
- **C, Conduit** (hybrid, cooldowns -5%): constant casting.
  - C1 Flow: cooldowns -10%. C2 Battery: +150 max mana.
  - C3 Forked Bolt: +1 projectile. C4 Storm Mind: +15% spell damage.

Changed from the proposal: no jump range, strike speed or "two clouds" talents, and no mana on hit (talents can't do those yet). The charged spell isn't marked on the HUD yet.

## How it's built (moba-test)
- **Static Charge:** `StaticCharge` counts casts; a charged projectile spell chains (new `Chain` in `SpellProjectile`) with `LightningBolt` flashes, shown on clients through the game server.
- **Thunderhead:** a new spell type `StormCloudSpell` and timed buff `StormCloud` (a cloud above him, strikes heroes first), synced to clients like Bloodrush.

## Open questions
- Should the cloud prefer heroes, or the closest enemy?
- Is "every 4th spell" readable enough, or should the charged spell glow?
