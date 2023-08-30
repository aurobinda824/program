import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3+2*x+np.sin(x)+1
def roots():
    x_1 = 2
    x_2 = -2
    for i in range(10):
        if func(x_1)*func(x_2) == 0:
            return x_1 if func(x_1) == 0 else x_2
        if func(x_1)*func(x_2) > 0:
            return 'No Roots in the given range.'
        else:
            x_3 = (x_1+x_2)/2
            if func(x_3)*func(x_1) < 0:
                x_1 = x_1
                x_2 = x_3
            else:
                x_1 = x_3
                x_2 = x_2
    return x_1

x = np.arange(-3,3,0.1)
y = func(x)
print(f"roots are {roots()}")
plt.plot(x,y)
plt.show()