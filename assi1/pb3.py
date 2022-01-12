import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2*(np.pi), 0.01)

x1 = np.cos(t)
y1 = np.sin(t)

x2 = np.cos(3*t)
y2 = np.sin(2*t)

x3 = abs(np.cos(4*t))*np.cos(t)
y3 = abs(np.cos(4*t))*np.sin(t)

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)

plt.legend(["a", "b", "c"], loc = "upper right")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Different parametric plots')
plt.show()

