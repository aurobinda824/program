import matplotlib.pyplot as plt
import numpy as np
from math import factorial
x= np.linspace(0,2*np.pi,40)
y = np.linspace(0,2*np.pi,6)

def sin(x):
    s=0
    for n in range(10):
        s = s+ (((-1)**n)*(x**(2*n+1)))/factorial(2*n+1)
    return s

plt.plot(x,sin(x))
plt.plot(y,sin(y))
for mn in zip(y,sin(y)):
    plt.annotate('(%.2f,%.2f)'%mn ,mn)
plt.show()