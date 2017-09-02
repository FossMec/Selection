#!/bin/python3

import sys

def simpleArraySum(n, ar):
    s = 0
    for x in range(n):
        s+=ar[x]
    return s

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)