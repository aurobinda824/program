from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dxdt(x,t):
    return 2*x+10

t = np.linspace(0,5,100)
x = odeint(dxdt,0,t)
plt.plot(t,x)
plt.show()