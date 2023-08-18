from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dxdt(x,t):
    return 10*t

t = np.linspace(0,2,10)
x = odeint(dxdt,0,t)
plt.plot(t,x)
plt.show()