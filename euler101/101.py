import math
from numpy import *

def poly(n):
    return 1 - n + n*n - n ** 3 +n ** 4 - n ** 5 + n ** 6 - n ** 7 + n ** 8 - n ** 9 + n ** 10

def cube(n):
    return n*n*n

p = {}
for i in range(1, 11):
    p[i] = poly(i)

c = {}
for i in range(1, 11):
    c[i] = cube(i)

def matrix(n):  
    o = []
    for i in range(n):  
        t = [((x+1) ** i) for x in range(n)]
        o.append(t)
    a = array(o).transpose()
    return a

def solver(n, seq):  
    if n == 1:
        return seq[1]
    else:
        mtr = matrix(n)
        mtrI = linalg.inv(mtr)
        v = array([seq[x] for x in range(1, n+1)])
        d = dot(mtrI, v)
        p = n+1
        pS = [p ** e for e in range(n)]
        return sum(d*pS)

answer = 0
for i in range(1, 11):
    temp = solver(i,p)
    #print i, temp
    answer += temp

print answer
