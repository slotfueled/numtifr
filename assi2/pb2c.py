import numpy as np
import math as ma
import matplotlib.pyplot as plt

xa=np.linspace(1,100,100)
ya = np.linspace(1,100,100)

def func(x):
    return ma.exp(x)

def lefI(a, b, n):
    h = (b-a)/n
    s = 0
    e = 0
    for i in range (n):
        s = s + h*func(a+i*h)
        e = abs(e)-abs(s)
        ya[i]=e

    print("Value of integral by RH method: ",'%.8f'%s)
    plt.plot(xa,ya,label='left')

def rigI(a, b, n):
    h = (b-a)/n
    s = 0
    e = 0
    for i in range(1,n+1):
        s = s+h*func(a+i*h)
        e = abs(e)-abs(s)
        ya[i-1]=e
    plt.plot(xa,ya,label='right')
    print("value of integral by LH method: ","%.8f"%s)
def midI(a, b, n):
    h = (b-a)/n
    s=0
    e = 0
    for i in range (n):
        s = s+h*func((a+h/2)+i*h)
        e =abs(e)-abs(s)
        ya[i]=e
    print("Value of integral by RH method: ","%.8f"%s)
    plt.plot(xa,ya, label='midpoint')

def trapz(a, b, n):
    h = (b-a)/n
    s = 0
    e=0
    for i in range(n):
        s = s+h*(func(a+i*h)+func(a+(i+1)*h))/2
        e = abs(e)-abs(s)
        ya[i]=e
    plt.plot(xa,ya, label='trapezoidal')
    print("Value of integral by Trapezoidal method: ","%.8f"%s)

def simps(a, b, n):
    h = (b-a)/n
    s=(func(a)+func(b))*h/3
    e=0
    ya[0] = e
    for i in range(1,n):
        if i%2==0:
            s = s+2*func(a+i*h)*h/3
        else:
            s = s+4*func(a+i*h)*h/3
        e = abs(e)-abs(s)
        ya[i]=e
    #s = s*h/3
    plt.plot(xa,ya, label='simpson')
    print("Value of integral by Simpson method: ","%.8f"%s)


lefI(0,1,100)
rigI(0,1,100)
midI(0,1,100)
trapz(0,1,100)
simps(0,1,100)
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Error vs Iteration for different method of integration')
plt.legend()
plt.show()
