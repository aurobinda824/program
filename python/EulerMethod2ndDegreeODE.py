import matplotlib.pyplot as plt
import numpy as np
def sol(x,n,step):
    f,f_ = 1,1                          #f and f_ in this line are intial condition
    y = []
    for j,i in enumerate(x):            #f3f__+f2f_+f1f=f0,   f__ = f'',f_= f'
        y.append(f)
        f1 = 1
        f2 = -1
        f3 = 1
        f0 = 0
        f__ = (f0/f3) -(f1*f/f3) -(f2*f_/f3)
        f = f+step * f_ + (step**2)*f__/2
        f_ = (f - y[j])/step

    return y
n = 1
h = 0.1
x = np.arange(0,10,h)
y = np.arange(0,-10,-1*h)

plt.plot(x,sol(x,n,h),color='#000000')
plt.plot(y,sol(y,n,-1*h),color='#000000')
plt.show()
