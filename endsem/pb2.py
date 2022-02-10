import numpy as np
import math as ma
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
def func(x,r):
    return ma.sqrt(r*r-x*x)

def midI(a, b, n):
    h = (b-a)/n
    s=0
    for i in range (n):
        s = s+h*func((a+h/2)+i*h,b)
    return s
    #print("Value of integral by midpoint method: ","%.8f"%s)

def yval():
    xa= np.linspace(5,50,10)
    ya = np.linspace(5,50,10)
    for i in range(0,10):
        e = midI(-xa[i],xa[i],30)
        ya[i]=e
    
    plt.plot(xa, ya, label='intgrat', marker = "*")
    cs = CubicSpline(xa,ya)
    d=cs(13)
    print('Value of f(13) by cubic spline is: ','%.4f'%d)
    plt.plot(xa,cs(xa),label='intpol', marker = "s")
    plt.xlabel('radius')
    plt.ylabel('area')
    plt.title('area vs radius (both plots are overlapping)')
    plt.legend()
    plt.show()

yval()
