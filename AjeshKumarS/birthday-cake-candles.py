#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    n1=n2=0
    for i in range(n):
        if(ar[i]>n1):
            n1 = ar[i]
    for f in ar:
        if(f==n1):
            n2+=1
    return n2

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)