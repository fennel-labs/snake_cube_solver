from snake_model.cube_state import CubeState
from snake_model.snake_description import SnakeDescription

import matplotlib.pyplot as plt
import time

desc = SnakeDescription([3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2])

test = CubeState(desc)
test.plotState()
test.extend(0)
time.sleep(3)
test.plotState()
test.extend(1)
time.sleep(3)
test.plotState()
test.extend(2)
time.sleep(3)
test.plotState()
test.extend(3)
time.sleep(3)
test.plotState()
plt.show()


print("Hello test world")
