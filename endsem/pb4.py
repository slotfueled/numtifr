
import numpy as np
from scipy import integrate
import math as ma



def f1(x):
    return ma.sqrt(1+x*x)
def f2(x):
    return ma.sqrt(1-x*x)



def gauIx(x):
    f4 = lambda y: ma.sqrt(1-x*x-y*y)
    f = np.vectorize(f1)
    di = integrate.fixed_quad(f,f2(x),f1(x),n=2)
    return di[0]

def gauIF():
    fu = np.vectorize(gauIx)
    di = integrate.fixed_quad(fu,-1,1,n=2)
    print("Value of integral for given limits: ",'%.5f'%di[0])


def gauISx(x):
    f4 = lambda y: ma.sqrt(1-x*x-y*y)
    f = np.vectorize(f1)
    di = integrate.fixed_quad(f,-1*f2(x),f2(x),n=2)
    return di[0]

def gauIFS():
    fu = np.vectorize(gauISx)
    di = integrate.fixed_quad(fu,-1,1,n=2)
    print("Value of integral for the usual sphere limits: ",'%.5f'%di[0])


gauIF()  #this function evaluates the integral with the given limits of question
gauIFS() #this function evaluates the volume of "sphere" using usual limits -sqrt(1-x^2) to sqrt(1-x^2)


