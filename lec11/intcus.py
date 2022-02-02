import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0,1,2])
y = np.array([0,2,4])
cs = CubicSpline(x,y)
d=cs(1.5)
t=2**1.5
print('Value of f(1.5) by cubic spline is: ','%.4f'%d)
print('Error is: ','%.4f'%(t-d))
