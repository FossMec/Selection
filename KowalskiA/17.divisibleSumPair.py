#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    c=0
    d=1
    for i in range(n):
        for j in range(d,n):
            if (ar[i]+ar[j])%k==0:
                c+=1
        d+=1 
    return(c)
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
