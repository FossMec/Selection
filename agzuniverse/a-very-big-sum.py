#!/bin/python3

def aVeryBigSum(n, r):
    s=0
    for i in range(0,n):
        s+=r[i]
    return s

n = int(input().strip())
r = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, r)
print(result)
