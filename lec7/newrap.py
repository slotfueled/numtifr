def fun(x):
    return x*x-10

def dfun(x):
    return 2*x

def newton(x):
    h = fun(x)/dfun(x)
    count=0
    while(count < 100):
        h = fun(x)/dfun(x)
        x = x-h
        count=count+1

    print("Value of root is : ", "%.4f"% x)

x0 = int(input("Enter the starting point: "))
newton(x0)

