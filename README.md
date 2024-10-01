# forest_fire_sim
Simple forest fire simulation similar to Conway's game fo life

# Rules:

## Burning Trees:
If a tree (1) has a burning neighbour (2) (not diagonal neighbours), it catches fire and becomes a burning tree (2) in the next step.
## Burned Trees:
A burning tree (2) will turn into an empty cell (0) in the next step (it burns down).
## Tree Growth:
Empty cells (0) randomly turn into trees (1) with a small probability at each step, simulating regrowth.
