print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)

print('delhi' + 'mumbai')
S = 'mumbai'
print('navi' + S)
print(S*5)
print(S[:0])
print('Costal {0} and landlocked {1}.'.format('Mumbai', 'Delhi'))

L = [1,2,3] + [4,5,6]
print(L)
print(L[:])
print(L[:0])
print(L[-2])
print(L[-2:])
print(([1,2,3] + [4,5,6])[2:4])
print([L[2], L[3]])
print(L.reverse())
print(L)
L.sort();
print(L)
print(L.index(4))

D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
print(D['x'] + D['w'])
D[3] = 6
D[(1,2,3)] = 4
print(list(D.keys()))
print(list(D.values()))
print((1,2,3) in D)
