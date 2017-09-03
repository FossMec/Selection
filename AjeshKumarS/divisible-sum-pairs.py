#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    ct = 0
    for j in range(n):
        i = 0
        while(i<j):
            if((ar[i]+ar[j])%k is 0):
                ct+=1
            i+=1
    return ct

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)