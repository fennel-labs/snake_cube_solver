from snake_model.cube_state import CubeState

test = CubeState()
test.points[1] = (1,0,0)
test.points[2] = (2,0,0)
test.points[3] = (2,1,0)
test.points[4] = (2,2,0)
test.points[5] = (6,2,1)
test.points_index = 5
test.plotState()

print("Hello test world")
