class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def intpl(f, xi, n):
    res = 0
    for i in range(n):
        val = f[i].y
        for j in range(n):
            if j!=i:
                val = val*(f[j].x-xi)/(f[j].x - f[i].x)

        res+=val
    return res

f = [Data(0,1), Data(1,2), Data(2,4)]
y = intpl(f,1.5,3)
print("Value of f(1.5) using interpolation is :", y)
x=2**1.5
print("error is : %.4f"%(y-x))
