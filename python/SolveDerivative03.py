from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dydx(y,x):
    return x

x = np.linspace(0,10,100)
y = odeint(dydx,0,x)
plt.plot(x,y)
plt.show()