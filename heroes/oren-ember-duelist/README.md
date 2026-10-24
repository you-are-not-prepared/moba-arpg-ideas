# Oren, Ember Duelist

**Status:** implemented in moba-test (2026-10-24). Numbers and talents are first versions to tune; the talents below are what the game has.

| | |
|---|---|
| Role | Melee bruiser: dive and duel |
| Damage type | Fire (see [spell affinity](../../game-mechanics/spell-affinity/)) |
| Spell colours | Red / orange / yellow |
| Base stats | 680 HP · 35 damage · 1 range (melee) · 1.15 attacks/s · 6.6 speed · 300 mana |

## Passive: Kindled Blade
Each basic attack builds **Heat** (up to 5 stacks, each **+4% attack speed**, lost after 3s without attacking). At 5 stacks his next attack **bursts**: **50 fire damage** around the target (2.5m) and a **3s burn**, then Heat resets.

## Ultimate (R): Blazing Leap
Leaps up to **6m** to a point, dealing **150 / 225 / 300** damage around where he lands (3m) and burning enemies. For **5s** afterwards his attacks burn.

| Rank | Landing damage | Cooldown | Mana |
|---|---|---|---|
| 1 | 150 | 70s | 100 |
| 2 | 225 | 60s | 100 |
| 3 | 300 | 50s | 100 |

## Playstyle
Dives onto a target, sticks to it and wins long fights as Heat builds up. A second melee hero next to Torvald (tank) and Nyx (assassin).

## Ascension (levels 6 / 11 / 18)
- **A, Wildfire** (passive, +25 Heat burst damage): bigger bursts.
  - A1 Flashpoint: +25 burst damage. A2 Stoke: +10% attack speed.
  - A3 Inferno: +50 burst damage. A4 Forge Heart: +200 max health.
- **B, Meteor** (ultimate, burning attacks +2s): leap more often, burn longer.
  - B1 Quick Ignition: ultimate cooldown -20%. B2 Scorch: +15% spell damage (the landing).
  - B3 Afterburn: burning attacks +3s. B4 Second Wind: ultimate cooldown -25%.
- **C, Phoenix** (hybrid, +150 max health): a sturdier fighter.
  - C1 Searing Edge: +15 attack damage. C2 Ember Stride: +8% move speed.
  - C3 Rebirth: +30 max health per level. C4 Sunfire: +25 attack damage.

Changed from the proposal to fit what talents can do today: no burst radius, no healing from burns, no "Heat on kill"; the leap can't go over rocks (it lands on walkable ground).

## How it's built (moba-test)
- **Kindled Blade:** `KindledBlade` counts hits through a new `Attacker.Hit` event; the burst uses the fire explosion.
- **Blazing Leap:** a new spell type `LeapSpell` and movement `Leap` (an arc; the agent is warped on landing; orders wait until it lands), then the timed buff `BurningBlades`. On the game server the arc reaches clients through the position sync.

## Open questions
- Can he leap over walls (rocks), or only along walkable ground?
- Heat on attacking creeps too, or only heroes?
