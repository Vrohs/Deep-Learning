import math
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline

def f(x):
    return 3*x**2 - 4*x + 5

print(f'{f(3.0)}')

xs = np.arange(-10, 10, 0.225)
print(f'{f(xs)}')