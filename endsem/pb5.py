import numpy as np
import math as ma



def func(x,y):
    return ma.sqrt(1-x*x-y*y)
def func1(x):
    return ma.sqrt(1-x*x)
def func2(x,y):
    return (x*x+y*y)

def midI(xa, xb, ya, yb, n):
    hx = (xb-xa)/n        #delta x
    hy = (yb-ya)/n        #delta y
    yl = 0                #for the variable limit of y as x moves inside the region of integration
    s=0
    j=0
    for i in range (n):
        yl = -1*func1(xa+hx/2+i*hx)
        j=0
        while func2(xa+hx/2+i*hx, yl+hy/2+j*hy)<1:       # for checking if y is inside the sphere for x
            s = s+ hx*hy*func((xa+hx/2)+i*hx,(yl+hy/2)+j*hy) 
            j=j+1
    print("Value of integral by midpoint method: ","%.8f"%s)
midI(-1,1,-1,1,30)

