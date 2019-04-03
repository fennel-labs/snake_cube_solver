import numpy as np

class CubeState:
    datatype = np.dtype((np.int32, (2,))) 

    points = np.array([],dtype=datatype) # points that are occupied by the snake
    decisions # decision for each segment, according to Direction enum, current direction is decisions.last
              # segment zero has a fixed decision

    def __init__(self):

    def show(self):

    def isValid(self):

