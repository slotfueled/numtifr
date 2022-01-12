import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(1000)
y = np.random.randn(10000)

fig, ax = plt.subplots(1,2)

ax[0].hist(x, 50, density=True, facecolor='g', alpha=0.75)
ax[0].grid(True)
ax[0].set(xlabel='Value of x', ylabel='Number of events')
ax[0].set_title("Histogram of random distribution")


ax[1].hist(y, 100, density=True, facecolor='r')
ax[1].set_xlim([-2,2])
ax[1].set(xlabel='Value of x', ylabel='Number of events')
ax[1].set_title('Histogram of normal distribution mean = 0')


plt.show()
