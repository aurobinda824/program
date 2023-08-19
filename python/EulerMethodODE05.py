import matplotlib.pyplot as plt
import numpy as np

def method(m,step,mass):
    f ,f_= 1,0
    y = []
    for i,j in enumerate(m):
        y.append(f)
        g = (-2*f-f_)/mass
        f = f+step*f_ + step**2*g/2
        f_ = (f - y[i])/step
    return y

m = 1 #mass
h=0.1
x = np.arange(0,20,h)
x_ = np.arange(0,-20,(-1)*h)

plt.plot(x,method(x,h,m),color='#000000')
plt.show()
