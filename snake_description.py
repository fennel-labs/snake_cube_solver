from enum import Enum

@unique
class Direction(Enum)
    Xp = 1
    Xn = 2
    Yp = 3
    Yn = 4
    Zp = 5
    Zn = 6


class SnakeDescription
    
    segment_lengths=[]
    cube_size = 0

    def __init__(self, segments):
        self.segment_lengths = segments
        size = sum(self.segment_lengths)**(1./3.)
        if round(size)**3 == size:
            self.cube_size = size
        else:
            raise Exception("The length of the given snake will not fit into a cube!")





    

