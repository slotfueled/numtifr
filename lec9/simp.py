def fun(x):
    y = 10-3*x*x
    return y

def simps(ll,ul,n):

    h = (ul-ll)/n

    x = list()
    fx = list()

    for i in range (n+1):
        x.append(ll + i*h)
        fx.append(fun(x[i]))

    sum = 0
    i = 0
    for i in range(n+1):
        if i==0 or i==n:
            sum+=fx[i]
        elif i%2 !=0:
            sum+= 4*fx[i]
        else:
            sum+= 2*fx[i]
    sum = sum*(h/3)
    
    return sum

lower_limit = -1
upper_limit = 3

n = int(input("Enter the value of n (only even are allowed): "))
print("%.4f"% simps(lower_limit, upper_limit, n))

    
