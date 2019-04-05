from enum import Enum, unique

@unique
class Direction(Enum):
    Xp = 1
    Xn = 2
    Yp = 3
    Yn = 4
    Zp = 5
    Zn = 6


# two fields:
# 1. segment_lengths
# 2. cube_size
class SnakeDescription:

    def __init__(self, segments):
        self.segment_lengths = segments
        num_elements = sum(self.segment_lengths)
        size = num_elements**(1./3.)
        if round(size)**3 == num_elements:
            self.cube_size = round(size)
            print("Cube side length is {0}.".format(self.cube_size))
            print("Using the following snake description:")
            print(self.segment_lengths)
        else:
            raise Exception("The length of the given snake will not fit into a cube!")





    

