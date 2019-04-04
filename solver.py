from snake_model.cube_state import CubeState
from snake_model.snake_description import SnakeDescription

import matplotlib.pyplot as plt
import time
import copy

desc = SnakeDescription([3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2])
#desc = SnakeDescription([1])

seed = CubeState(desc)
seed.plotState()

open_set = [seed]
solution = None

while open_set and (solution == None):
    current_node = open_set.pop(0)
    for i in range(4):
        new_node = copy.deepcopy(current_node)
        new_node.extend(i)
        #new_node.plotState()

        # sort out invalid branches
        if new_node.isValid():
            open_set.insert(0, new_node)
        # check for solution
        if new_node.isComplete():
            solution = new_node
            break


if solution != None:
    solution.plotState()
    plt.show()

# Todo:
# Plot
# Runtime
# 4x4x4