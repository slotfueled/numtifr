import numpy as np
from scipy import integrate
import math as ma

xa=np.linspace(0,1,100)

def f(x):
    return ma.exp(x)

di=np.trapz(np.exp(xa),xa)
print("Value of integral by trapezoidal method: ","%.8f"%di)

di = integrate.simpson(np.exp(xa),xa)
print('Value of integral by simspon method: ','%.8f'%di)

di = integrate.romberg(f,0,1)
print('Value of integral by romberg method: ','%.8f'%di)

di = integrate.fixed_quad(np.exp,0,1,n=5)
print('Value of integral by quadrature method (5th order): ','%.8f'%di[0])
