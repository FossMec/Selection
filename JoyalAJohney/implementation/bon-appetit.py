#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    ar[k]=0
    b_actual=sum(ar)//2
    if b==b_actual:
        return("Bon Appetit")
    else:
        return(b-b_actual)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)

