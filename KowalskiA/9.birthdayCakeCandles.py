#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    
    big=max(ar)
    p=0
    for i in range(n):
        if ar[i]==big:
            p=1+p
    return (p)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
