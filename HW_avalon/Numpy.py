import numpy as np
import math

def Task_001():
    Array = np.random.randint(0,10,10)
    x_average = np.average(Array)
    print(Array)
    print(x_average)
    sum = 0
    for x in Array:
        sum += (x - x_average) ** 2

    sigma = math.sqrt(sum/len(Array))
    print("стандартное отклонение сигма = ", sigma)

Task_001()


