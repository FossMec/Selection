#!/bin/python3

import sys

def simpleArraySum(n, ar):
    if (n==0):
        return 0;
    else:
        return ar[n-1] + simpleArraySum(n-1,ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
