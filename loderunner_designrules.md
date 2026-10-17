# Lode Runner — Level Design Rules

Design rules for levels in `loderunner.py`. They describe what the engine
actually does (there is no jumping, no trap-digging), so they apply to
**every** level — existing or new — not just the one a rule was first
noticed on. Rules are written as engine-independent invariants wherever
possible; concrete numbers (grid size, speeds, columns) are marked as this
engine's current conventions and change with the engine, the principles
do not.

## 1. Level format

*Principle: a level is a fixed-size ASCII grid, one character per tile,
plus spawn points that are legal on that grid.*

- Layout is authored as ASCII rows and converted with `char2tile`:
  `.` empty, `#` bricks, `=` ladder, `-` rope, `o` gold. Keep the
  character alphabet shared by all levels so tools and checks stay generic.
- Every row string has exactly the width the engine expects and there are
  exactly the expected number of rows (currently 26 x 16); layout is
  indexed `layout[y][x]`, top row = 0. Never hard-code the size in a
  checker — read it from the engine constants.
- A level is a dict (`tiles`, `colors`, `size`, `tile_size`, `layout`,
  `player`, `enemies`, `exit_ladder`) appended to `screens`; all levels
  use the same structure so validation can iterate over `screens`.
- Player and enemies spawn on **tile coordinates**. An enemy's spawn tile
  must be walkable at start (solid or ladder directly below it). The
  player may instead spawn in mid-air as an entrance: levels 1 and 2 both
  start the player on row 0 so they drop into the level — the column
  below must then be a clear shaft down to a reachable stand tile, with
  nothing in it the player shouldn't grab (rope, or gold they'd
  auto-collect). Spawning on gold or on an escape-ladder column is legal
  but sloppy — avoid it.

## 2. Tile behaviour (masks)

*Principle: rules follow from the tile masks, so validate against the
masks, not the characters.* Current engine mapping:

| Tile  | Mask                     | Behaviour |
|-------|--------------------------|-----------|
| `#`   | SOLID                    | Blocks movement in all directions. |
| `=`   | STAND + CLIMB            | Can be stood on (walkable floor), climbed up/down, and entered by falling onto it. |
| `-`   | HANG (rope)              | Not solid. Player hangs under it and shuffles sideways; pressing up on a rope turns into down (you cannot climb ropes). |
| `o`   | GOLD                     | Passable; collected on contact when the player passes over it. |
| exit  | STAND + CLIMB + EXIT     | The escape ladder; created dynamically, never in the layout. |

Movement rules that follow from these masks:

- Gravity is continuous: a step into a tile with nothing (SOLID or STAND)
  below becomes a fall. You can walk off ledges, you cannot jump.
- Moving **up** is only possible while overlapping a ladder tile.
- Falling onto a ladder tile lands you on it (ladders are STAND): you can
  drop into the top of a ladder column and keep walking.
- Falling into a ladder column that starts one tile below the floor you are
  walking on is fine; falling down a shaft and expecting to climb back up
  without a ladder is not.

## 3. Connectivity rules

*Principle: reachability is a win condition, fairness is a playability
condition, and geometry must be internally consistent. These hold for any
level in any grid size.*

1. **Every gold pile must be reachable from the player start** using walk,
   fall, ledge-step-off and ladder-climb moves only. This is the hard
   win-condition: without all gold the escape ladder never appears.
2. **Every floor/area needs at least two independent exits** — exits are
   considered independent if an enemy standing between them cannot cut off
   both. A dead-end area is always a sure capture because enemies path
   directly to the player (see §5). This applies especially to areas where
   enemies spawn and to any area the player is *invited* into by gold.
3. **Ladder columns must be continuous through floor slabs.** If a ladder
   crosses a solid row, the gap in that row must be in the *same column*
   as the ladder above and below it. Verify: for every ladder column, no
   brick may sit between the top and bottom tile of that column, and there
   must be no single ladder tile that is not connected to a climbable run
   (an orphan `=` tile next to a column is a misalignment bug).
4. **Every ladder segment must connect two walkable areas** (or a walkable
   area and the escape ladder). A ladder whose top end is capped by bricks
   is decoration at best, a disconnected segment at worst.
5. **A ladder must not start flush against a ceiling you need to pass.**
   The tile above the top ladder tile must be empty or another ladder, and
   the tile above that must be enterable (this leaves room to stand on top
   of the ladder and walk off it).
   *Corollary:* do not run the ladder one tile higher, up into the floor
   layer it serves. Exiting at the top only needs a climbable tile *under*
   the stand tile, so a top tile in the floor layer is never needed — it
   just draws a ladder segment sticking out above the floor (a ladder must
   end at its top slab gap, not one tile past it). Ladders may keep their
   floor-layer tile at the *bottom* end: starting a climb requires the
   stand tile itself to be climbable.
6. **Don't seal gold in a fall-only shaft.** Gold you can fall past but
   never climb back to makes the level unwinnable. Symmetrically: one-way
   routes are fine, but the area they dump into must itself satisfy rule 2.
7. **Avoid symmetry.** A level (or half of it) that is its own mirror
   image is filler: it adds nothing to learn, one enemy can shadow the
   other's threat, and verbatim-repeated slab rows look like copy-paste.
   Stagger the holes between slabs, vary ladder spacing, place gold off
   the mirror line. Two slabs must not be identical rows, and feature
   columns must not sit in perfect mirror pairs around the centre. The
   same applies to rotational symmetry and to repeated whole floor blocks.
8. **No disconnected floors.** The path graph the AI uses is *directed*:
   stepping off a ledge or falling through a hole is a one-way edge, so a
   floor segment that can only be entered by falling into it is
   disconnected for pursuers even though it looks connected on paper.
   Enemies then have no route to a player standing there: they freeze,
   and the area becomes an invincibility camping spot. Every floor
   segment the player can reach must also be reachable *by the enemies*
   from their spawns through two-way links (ladders, walkable junctions).
   Validate this with a directed reachability check, not an undirected
   walk test (see §7).
9. **Every rope segment must bridge at least two floorless cells.** A
   rope whose every cell has solid floor directly beneath it is a fall
   catcher, not a bridge — it adds no traversal choice. At least two
   columns under each rope must be open shafts, so walking the rope and
   dropping from it (or hanging off its ends) lands the player on a
   *different* floor than walking past on the rope would. This also gives
   the rope a real risk/reward: hanging means falling further if you let
   go in the wrong place.
10. **Every rope segment must be reachable from both ends without
    jumping.** The player cannot jump, so a rope is only grabbable from
    *level with it*: a standable or climbable tile must sit directly at
    each end of the run (same row), so the rope can be boarded and left
    in either direction. An open fall path onto an interior rope tile
    (column above it open down to the rope) may serve as extra entry —
   never as a replacement for an end. A rope whose far end dangles over
   a shaft or bare floor turns every metre walked that way into a one-way
   drop the player cannot walk back out of at rope level, and a
    rope with no same-level connection at all is decoration: the player
    under it can look but never grab.
11. **No ladder may ever end in mid-air.** Both ends of every ladder run
   must land on a floor, not on empty space:
   - *Bottom end:* the bottom ladder tile itself must be stood on (solid
     or standable tile directly beneath it). A bottom rung floating over
     a shaft is never entered from below and looks broken; a rope tile
     beneath the bottom rung does not count as support.
   - *Top end:* the tile directly above the top ladder tile must be a
     standable tile — you climb the run to *step off* it, so it has to
     exit onto floor, or onto the floor reached through a slab gap. A
     top end opening into an air-only corridor is an unreachable stub.
   Check per run (merge contiguous vertical ladder tiles per column),
   not per tile, and apply the check to every level in the game, legacy
   or starter levels included.

## 4. Escape ladder

- `exit_ladder` is drawn when the last gold is collected: from row 0
  downwards in column `x`, as far as the first non-empty tile.
- Therefore the column must be **completely empty from row 0 down to the
  floor it should connect to**, and that bottom neighbour must be solid or
  a ladder so the ladder touches reachable ground. If row 0 at that column
  is not empty in the layout, the escape ladder will not be drawn at all.
- The bottom of the escape ladder must be reachable from the rest of the
  level before all gold is collected (usually the top floor or an upper
  floor).
- Touching any EXIT tile advances to the next level; the level ends after
  the last one in `screens`.

## 5. Enemies

*Principle: the enemy AI is the level's difficulty; design terrain around
what the pathfinder can actually do.* Current engine:

- Enemies walk the shortest path to the player's current tile (recomputed
  each time the player changes tile). In this engine they **can use
  ladders and ropes** — there is no enemy restriction on climbing. Never
  assume a ladder or rope is player-only refuge.
- An enemy cannot jump gaps or rise without a ladder, so gaps and high
  ground are real defensible terrain, until the enemy paths around.
- The player's only reliable advantage is speed: player `step_ms` must be
  **strictly lower** than every enemy's (current convention: player 20,
  enemies 24 and 28 — larger = slower, also useful for readability of who
  chases whom). Any area that relies on outrunning an enemy inherits this
  as a precondition.
- Give enemy spawns on the same floor as their intended hunting ground;
  an enemy that cannot path anywhere useful is scenery.
- Getting caught is game over (no lives), so keep long chases possible:
  loops, multiple floors and (per §3.2) multiple exits per floor.

## 6. Anti-patterns

*Principle: these are failure modes any level can slide into; each was
actually shipped once in level 2 and then fixed. Fix the pattern, not
just the instance.*

- **Single-exit hostile area.** An area where enemies spawn (or hunt) with
  only one exit turns baited entries into guaranteed captures. *Instance:
  the original level-2 bottom floor had one ladder back up; fixed by
  spreading three exits across the floor.*
- **Slab gap misaligned with the ladder.** A ladder column crossing a
  solid row whose gap sits in a neighbouring column produces a brick in
  the run, an orphan `=` tile and a disconnected segment. ASCII rows make
  off-by-one column errors invisible; always re-check gaps against the
  column above. *Instance: level 2's column-16 ladder crossing row 6 with
  the gap at column 17.*
- **Symmetric filler.** Mirror-symmetric or copy-pasted level halves add
  nothing to learn and make both enemies redundant (§3.7). *Instance: the
  first rewritten level 2 had identical slab rows and mirror-paired
  ladder columns.*
- **Blocking the escape-ladder column.** Any tile (gold, rope, even
  decorative ladder) in the escape column above its landing floor stops
  the ladder being drawn or reachable (§4).
- **Ladder ending in mid-air.** A run whose bottom rung hangs over a
  shaft (no support under it) or whose top opens into an air-only
  corridor is decoration and an eyesore, and its last tile is a lie
  about where you can enter or leave the climb (§3.11). Rope beneath
  the bottom rung does not ground it.
- **Unreachable rope.** A rope segment whose ends hang in the air can
  never be grabbed or left at rope level — the player cannot jump, so a
  rope is only usable from tiles that are *level with its ends* (§3.10).
  *Instance: level 2's row-9 rope started two cells clear of the nearest
  ladder (unreachable from either side); the first fix connected only the
  west end, leaving a one-way drop-off at the east end. Final fix: extend
  each rope until both ends touch a standable or climbable tile in the
  same row.*
- **Disconnected floor segment (one-way pocket).** A floor segment whose
  only entry points are one-way falls is invisible to the enemy pathgraph:
  miners stop moving entirely while the player stands there, and the spot
  is a safe camping place (§3.8). Check the *spawn floor* especially — the
  segment around the player start must be enemy-reachable from the very
  first tick. *Instance: level 2's floor-1 start segment exited only via
  one ladder into a floor-2 pocket bracketed by two one-way fall-holes;
  fixed by converting one hole into a ladder link from the floor below.*

## 7. Validation checklist for a new or edited level

Run these before committing — **for every level**, not just the one you
touched; a checker that reads `screens` costs nothing to keep global:

1. Row grid is complete and rectangular (row count and row length match
   the engine's expectations, current 16 x 26).
2. BFS (walk / fall / ledge-step / ladder-climb, gravity after every step)
   from the player start reaches: every gold tile, every ladder tile,
   every rope tile, the stand tile under the escape ladder, and both
   directions of every floor. Beware checkers that forget ledge-step-off
   falls (false "unreachable") or let climbers fall mid-ascent (false
   "reachable").
3. For each ladder column: top-to-bottom continuity, no bricks in the run,
   no orphan ladder tiles; ladder tops adjacent to walkable floor; no
   ladder tile protrudes one segment above a floor (a `'='` in a floor
   layer with a ladder below and none above is a redundant top — rule 3.5).
   For every run (merged per column): the bottom tile must have support
   directly beneath it and the tile above the top must be standable — no
   ladder ends in mid-air (rule 3.11). Rope under a bottom rung is not
   support.
4. Every closed area has >= 2 independent exits; player `step_ms` < every
   enemy `step_ms`; all spawns standable and mutually reachable.
5. **Directed enemy-reachability (rule 3.8):** using the engine's own
   pathgraph (or a checker mirroring its edge rules), for *every* tile the
   player can stand on, BFS the graph in reverse from that tile and assert
   both enemy spawns are in the set. Zero disconnected (tile, spawn) pairs
   required. Also check the enemy spawns are in `paths` while the player
   is still at their start tile — the miners must be moving from tick one,
   not only after the player has fallen somewhere.
6. Escape-ladder column is empty from row 0 to a reachable floor.
7. Every rope segment bridges >= 2 cells with no floor directly beneath
   them (rule 3.9): for each rope column, the tile under the rope must be
   non-standable in at least two columns of the run. Every segment must
   also be reachable *from both ends* without jumping (rule 3.10): for
   each rope end, the tile directly beyond it in the same row (one column
   past the end) must be standable or climbable, and reachable from the
   start — verified against the engine graph so one-way fall-stubs don't
   pass as an end connection.
8. No symmetry: no two slab rows identical, no feature columns in mirror
   pairs around the centre (rule 3.7).
9. Smoke test: `SDL_VIDEODRIVER=dummy timeout 3 python loderunner.py
   --level N` must not crash (exit code 124 = still running = good).
