import numpy as np
import matplotlib.pyplot as plt

def func1(x,y,z):
    return 10*np.sin(x) - 5*z - 6*y

def func2(x,y):
    return y

def func(x):
    return -6*np.exp(-3*x) + 7*np.exp(-2*x) + np.sin(x) - np.cos(x)

def rk_4(x):
    f = 0
    f_ = 5
    z = []
    for i in x:
        z.append(f_)
        q1 = h*func2(i,f)
        q2 = h*func2(i+h/2, f+q1/2)
        q3 = h*func2(i+h/2, f+q2/2)
        q4 = h*func2(i+h, f+q3)
        f = f+ (1/3)*(q1/2+q2+q3+q4/2)
        #these are for z
        k1 = h*func1(i,f,f_)
        k2 = h*func1(i+h/2,f, f_+k1/2)
        k3 = h*func1(i+h/2,f, f_+k2/2)
        k4 = h*func1(i+h,f, f_+k3)
        f_ = f_ +(1/3)*(k1/2+k2+k3+k4)
    return z

h = 0.1
x = np.arange(0,3+h,h)
y = rk_4(x)
y_ = func(x)
plt.plot(x,y,label='solution')
plt.plot(x,y,label='analytic')
plt.legend()
plt.show()