import math as ma

def func(x):
    return ma.exp(x)

def lefI(a, b, n):
    h = (b-a)/n
    s = 0
    for i in range (n):
        s = s + h*func(a+i*h)

    print("Value of integral by RH method: ",'%.8f'%s)

def rigI(a, b, n):
    h = (b-a)/n
    s = 0
    for i in range(1,n+1):
        s = s+h*func(a+i*h)

    print("value of integral by LH method: ","%.8f"%s)
def midI(a, b, n):
    h = (b-a)/n
    s=0
    for i in range (n):
        s = s+h*func((a+h/2)+i*h)

    print("Value of integral by midpoint method: ","%.8f"%s)

def trapz(a, b, n):
    h = (b-a)/n
    s = 0
    for i in range(n):
        s = s+h*(func(a+i*h)+func(a+(i+1)*h))/2
    print("Value of integral by Trapezoidal method: ","%.8f"%s)
def simps(a, b, n):
    h = (b-a)/n
    s=(func(a)+func(b))
    for i in range(1,n):
        if i%2==0:
            s = s+2*func(a+i*h)
        else:
            s = s+4*func(a+i*h)
    s = s*h/3
    print("Value of integral by Simpson method: ","%.8f"%s)


lefI(0,1,100)
rigI(0,1,100)
midI(0,1,100)
trapz(0,1,100)
simps(0,1,100)
