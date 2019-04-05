from cube_state import CubeState
from snake_description import SnakeDescription

import matplotlib.pyplot as plt
import time
import copy
import argparse
import ast

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all',
                        dest='find_all',
                        action='store_true',
                        help="find all solutions")
    parser.add_argument('definition',
                        metavar='snake_definition',
                        nargs='?', # zero or one
                        default='',
                        action='store',
                        help="""snake description in python list format,
                             e.g. \"[2,1,1,1,1,1,1]\" for a 2x2x2 cube""")
    result = parser.parse_args()
    #print(result)
    return (result.definition, result.find_all)

def main(desc, show_all):
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
                if new_node.isValid():
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

if __name__ == "__main__":
    # parse arguments and decide what to do    
    definiton_string, show_all = parseArguments()
    if definiton_string == '':
        # default snake description
        #desc = SnakeDescription([3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2])
        desc = SnakeDescription([3,1,1,2,1,2,1,1,2,2,1,1,1,2,2,2,2])
    else:
        desc = SnakeDescription(ast.literal_eval(definiton_string))
    main(desc, show_all)


# Todo:
# Plot