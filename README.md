# Phase 3

Finish the game with a terminaison condition.

You are allowed to update any existing code to check if the game has ended.
- The easy way is to count the total number of hits.
- The best way is to keep track of each boat individually, and detects when each of them sunk.

Run the main.py script and enjoy!

# Rules
## Elements
- Each player has a 10x10 grid (1 to 10 horizontally, A to J vertically)
- Each player has 5 ships:
    - Carrier (5 cells)
    - Battleship (4 cells)
    - Cruiser (3 cells)
    - Submarine (3 cells)
    - Destroyer (2 cells)
    
## Phase 1: "Preparation"
Each player places its boats on the grid.

- Boats cannot be placed on top of each other
- Boats cannot be placed diagonally
- Boats must be placed entirely on the grid

## Phase 2: "Duel"
The game is turn-by-turn.

On its turn, a player shouts the coordinate of cell (e.g., A1). If an opponent's ship is placed on that cell, he annouces "hit" and marks it. The opponent announces "miss" otherwise. If an entire ship is marked, he annouces "sunk".

The same player keeps attacking the same way so long as he's hitting. As soon as he misses, the turn is over and the other player starts attacking.

The game ends as soon as player's whole army sunk.