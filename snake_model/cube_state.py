import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class CubeState:
    cube_size = 3 # cube side length
    cube_elements = cube_size**3 # total elements in cube
    datatype = np.dtype((np.int32, (3,))) # datatyp for 3D integer points

    # num_points
    # decisions # decision for each segment, according to Direction enum, current direction is decisions.last
    #           # segment zero has a fixed decision
    # num_decisions

    # snake_specification

    def __init__(self):
        # create memory for points
        self.points = np.zeros(CubeState.cube_elements,dtype=self.datatype) # points that are occupied by the snake
        self.points_index = 0 # counter for number of taken places

    def plotState(self):
        #print(self.points)
        
        figure = plt.figure()
        ax = figure.gca(projection='3d')

        x = self.points[0:self.points_index+1, 0]
        y = self.points[0:self.points_index+1, 1]
        z = self.points[0:self.points_index+1, 2]
        
        limit = CubeState.cube_size + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(-limit, limit)
        ax.set_facecolor('green' if self.isValid() else 'red')
        ax.plot(x,y,z, color='black', linewidth=3)
        plt.show()


    def isValid(self):
        valid_points = self.points[0:self.points_index+1]

        minima = np.amin(valid_points, axis=0)
        maxima = np.amax(valid_points, axis=0)

        delta = maxima-minima # size in x,y,z-direciton

        if max(delta) <= CubeState.cube_size:
            return True
        else:
            return False

