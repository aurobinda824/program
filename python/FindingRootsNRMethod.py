#Newton-Raphson Method

import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x**2 - 2*x + 1 - np.sin(x)

def derivative(x):
    return 2*x - 2 - np.cos(x)

def method(x_0):
    if derivative == 0:
        return 'Provide another point.'
    for i in range(100):
        if derivative(x_0) == 0:
            return x_0
        x_0 = x_0 - func(x_0)/derivative(x_0)
    return x_0
x = np.arange(-10,10,0.1)
y = func(x)
plt.plot(x,y)
plt.show()
print(f'one root is: {method(2)}')
