#!/bin/python3

import sys

def rotate(a,k,n):
    for _ in range(k):
        x = a.pop()
        a.insert(0,x)
    return a


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
y = rotate(a,k,n)
for a0 in range(q):
    m = int(input().strip())
    print(y[m])
