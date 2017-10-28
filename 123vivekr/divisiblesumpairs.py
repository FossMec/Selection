#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                c += 1
    return c

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

