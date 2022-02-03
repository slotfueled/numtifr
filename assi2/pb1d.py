import math as ma
from scipy import optimize

def func(x):
    return ma.sin(ma.cos(ma.exp(x)))

def derf(x):
    f = -ma.cos(ma.cos(ma.exp(x)))*ma.sin(ma.exp(x))*ma.exp(x)
    return f

def bis(a,b):
    root = optimize.bisect(func, a, b)
    print("Root by bisection method is: ","%.5f"%root)

def newr(s):
    root = optimize.newton(func, s, derf)
    print('Root by newton method is: ','%.5f'%root)

bis(-1,1)
newr(-1)
