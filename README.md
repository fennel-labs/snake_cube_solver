# snake_cube_solver
Python script, that solves arbitrary snake cubes (see https://en.wikipedia.org/wiki/Snake_cube) and visualizes the result.

This script was written for python3 and can be invoked using
```
python3 solver.py "[2,1,1,1,1,1,1]"
```
The cube layout list above is encoded as follows:
- The first item is the length of the first segment
- All other items represent the number of cubes after a bend and before the next bend occurs.

To get all possible solutions, add `-a` to the command. Note, that the solutions also include congruent solutions.

Cubes of size 3 are solvable within seconds (<10s on Core i7 ULV processor).
Cubes of size 4 have not been tested yet.
