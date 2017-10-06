#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    c=0
    for i in range(n):
        if i!=k:
            c=c+ar[i]
    c=c/2
    if c==b:
        return("Bon Appetit")
    else:
        return(int(b-c))
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
