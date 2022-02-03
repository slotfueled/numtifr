import math as ma
import numpy as np
import matplotlib.pyplot as plt

xa = np.linspace(1,100,100)

def func(x):
    return ma.sin(ma.cos(ma.exp(x)))

def derf(x):
    f = -ma.cos(ma.cos(ma.exp(x)))*ma.sin(ma.exp(x))*ma.exp(x)
    return f

def bise(a,b):
    c = a
    d=func(c)
    #xa=np.linspace(1,100,100)
    ya=np.linspace(1,100,100)
    e = c

    
    for i in range (100):
        c = (a+b)/2
        e =abs(e)-abs(c)
        ya[i]=e
        d=func(c)
        if(d==0):
            break
        if(d*func(a)<0):
            b=c
        else:
            a=c
    print("Value of root is: ","%.4f"%c)
    return ya
    #print(ya)
    #plt.plot(xa,ya)
    #plt.xlabel('iteration')
    #plt.ylabel('error')
    #plt.show()

def newrap(s):
    ya=np.linspace(1,100,100)
    e=s
    h = func(s)/derf(s)
    for i in range (100):
        h = func(s)/derf(s)
        s = s-h
        e=abs(e)-abs(s)
        ya[i]=e
    print("Value of root by Newton method: ","%.7f"%s)
    return ya


y1=bise(-1,1)
y2=newrap(-1)
plt.plot(xa,y1, color='r', label='bisection')
plt.plot(xa,y2, color='b', label='newton')

plt.xlabel("Iteration")
plt.ylabel('Error')
plt.title('Error vs Iteration for different root finding method')
plt.legend()
plt.show()
