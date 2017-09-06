#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    s = 0
    for i in range(n):
        if(i!=k):
            s+=ar[i]
    if(s/2 == b):
        return 'Bon Appetit'
    else:
        return int(abs(b-s/2))

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)