from snake_model.cube_state import CubeState
from snake_model.snake_description import SnakeDescription

import matplotlib.pyplot as plt
import time
import copy

show_all = False
#desc = SnakeDescription([3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2])
desc = SnakeDescription([3,1,1,2,1,2,1,1,2,2,1,1,1,2,2,2,2])

# time measurement
start_time = time.time()

# depth first search
# initialization
seed = CubeState(desc)
open_set = [seed]
solutions = []
# tree traversal
while open_set and (show_all  or (not solutions)):
    current_node = open_set.pop(0)
    for i in range(4):
        new_node = copy.deepcopy(current_node)
        new_node.extend(i)
        #new_node.plotState()

        # check for solution
        if new_node.isComplete():
            solutions.append(new_node)
            break # if there is just one segment left, only one solution is feasible
        # sort out invalid branches
        elif new_node.isValid():
            open_set.insert(0, new_node)
end_time = time.time()

# output
duration = (end_time - start_time)
print("Found {0:d} solutions in {1:.3f} s.".format(len(solutions), duration))
if show_all:
    print("I'll show you all solutions.")
    for s in solutions:
        s.plotState()
        plt.show()

else:
    print("I'll show you the first solution.")
    if solutions:
        solutions[0].plotState()
        plt.show()

# Todo:
# Plot
# CLI