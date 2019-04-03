import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from snake_model.snake_description import SnakeDescription, Direction


class CubeState:
    datatype = np.dtype((np.int32, (3,))) # datatyp for 3D integer points

    def __init__(self):
        # create memory for points
        self.points = np.zeros(CubeState.snake_description.cube_size**3,dtype=self.datatype) # points that are occupied by the snake
        self.current_point = np.zeros(1, CubeState.datatype) # current position
        self.current_points_index = 0 # index of last written array place
        
        # insert the first segment
        self.current_seg = 0
        self.current_dir = Direction.Xp
        self.appendSegment(self.current_seg, self.current_dir)


    def plotState(self):
        #print(self.points)
        
        figure = plt.figure()
        ax = figure.gca(projection='3d')

        x = self.points[0:self.current_points_index+1, 0]
        y = self.points[0:self.current_points_index+1, 1]
        z = self.points[0:self.current_points_index+1, 2]
        
        limit = CubeState.snake_description.cube_size + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(-limit, limit)
        ax.set_facecolor('green' if self.isValid() else 'red')
        ax.plot(x,y,z, color='black', linewidth=3)
        plt.show()

    def isValid(self):
        valid_points = self.points[0:self.current_points_index+1]

        minima = np.amin(valid_points, axis=0)
        maxima = np.amax(valid_points, axis=0)

        delta = maxima-minima # size in x,y,z-direciton
        unique_points = np.unique(valid_points, axis=0) # unique points

        # cube state is valid if dimensions are not exceeded and points are unique
        if (max(delta) <= CubeState.snake_description.cube_size  
            and unique_points.shape[0] == valid_points.shape[0]):
            return True
        else:
            return False

    def appendSegment(self, seg_num, dir):
        # kind of a switch case
        dir_vec = {
            Direction.Xn : (-1,0,0),
            Direction.Xp : (+1,0,0),
            Direction.Yn : (0,-1,0),
            Direction.Yp : (0,+1,0),
            Direction.Zn : (0,0,-1),
            Direction.Zp : (0,0,+1)
        }[dir]
        
        seg_length = CubeState.snake_description.segment_lengths[seg_num]
        # special treatment for first segment
        if seg_num == 0:
            seg_length -= 1

        # add specified amount of cubes to list
        for _ in range(0,seg_length):
            self.current_point += dir_vec
            self.current_points_index += 1
            self.points[self.current_points_index,:] = self.current_point

    def extend(self, variant)
        if variant > 3:
            raise Exception("Only four variants are available!")
        variants = {
            Direction.Xp : [Direction.Yp, Direction.Zp, Direction.Yn, Direction.Zn],
            Direction.Xn : [Direction.Zn, Direction.Yn, Direction.Zp, Direction.Yp],
        }[self.current_dir][variant]


    @staticmethod
    def setDescription(description):
        CubeState.snake_description = description


