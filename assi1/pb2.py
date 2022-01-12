import numpy as np

N = 10

def larges(a, st):
    la = a[st]
    for i in range(st,N):
        if la < a[i]:
            la = a[i]
            st = i
    return st


arr = [1,200,33,4,-3,88,7,8,9,4]
t=0
n = int(input('Enter the number of sorted element: '))
for i in range(0,n):
    j = larges(arr,i)
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    print(' ', arr[i])
