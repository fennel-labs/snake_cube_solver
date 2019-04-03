from snake_model.cube_state import CubeState
from snake_model.snake_description import SnakeDescription

CubeState.setDescription(SnakeDescription([3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]))

test = CubeState()
test.points[1] = (1,0,0)
test.points[2] = (2,0,0)
test.points[3] = (2,1,0)
test.points[4] = (2,2,0)
test.points[5] = (1,0,0)
test.points_index = 5
test.plotState()

print("Hello test world")
