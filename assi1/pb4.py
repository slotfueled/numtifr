import time

def fib(n):
    if n <= 2 :
        return n
    return fib(n-1) + fib(n-2)

def fibd(n):
    a=0
    b=1
    c=0
    if n==1:
        return a
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    return b


n = int(input("Enter the term of fibbonaci to be printed: "))
start = time.time()
print("Value of fibonnaci term is: ", fib(n))
end = time.time()
print("time taken via recursion: ", (end-start))

start = time.time()
print("Value of fibonnaci term is: ", fibd(n+2))
end = time.time()
print("time taken via recursion: ", (end-start))
