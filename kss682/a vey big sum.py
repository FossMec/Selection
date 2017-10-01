#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    S=0
    for i in range(0,n):
      S=S+ar[i]
    return S  

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
