import matplotlib.pyplot as plt
import numpy as np

def method(m,step):
    f = 1
    y = []
    for i in m:
        y.append(f)
        g = 10
        f = step*g+f
    return y

h=0.01
x = np.arange(0,10,h)
x_ = np.arange(0,-10,(-1)*h)

plt.plot(x,method(x,h),color='#000000')
plt.plot(x_,method(x_,(-1)*h),color ='#000000')
plt.show()
