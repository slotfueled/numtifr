def y(x):

    return (10-x*x)

def trapezoidal(a,b,n):
    
    h = (b-a)/n

    s = y(a) + y(b)

    i=1
    while i<n:
        s += 2 * y(a+i*h)
        i+=1

    return((h/2)*s)

x0 = -2
x1 = 2

n = 10

print("Value of integral is ", "%.4f"%trapezoidal(x0,x1,n))
