import random
import matplotlib.pyplot as plt
f =[0] *100
for i in range(100):
    x = random.randint(0,99)
    f[x] = f[x]+1
    plt.scatter(i,x,color = 'black')
plt.show()