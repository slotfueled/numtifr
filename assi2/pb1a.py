import math as ma

def func(x):
    return ma.sin(ma.cos(ma.exp(x)))

def derf(x):
    f = -ma.cos(ma.cos(ma.exp(x)))*ma.sin(ma.exp(x))*ma.exp(x)
    return f

def bise(a,b):
    c = a
    d=func(c)
     
    while((b-a) >= 0.001):
        c = (a+b)/2
        d=func(c)
        if(d==0):
            break
        if(d*func(a)<0):
            b=c
        else:
            a=c
    print("Value of root is: ","%.4f"%c)

def newrap(s):
    h = func(s)/derf(s)
    for i in range (50):
        h = func(s)/derf(s)
        s = s-h
    print("Value of root by Newton method: ","%.7f"%s)


bise(-1,1)
newrap(-1)
