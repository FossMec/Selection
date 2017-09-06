#!/bin/python3

import sys

def sockMerchant(n, ar):
    ct = 0
    for x in set(ar):
        ct+=(ar.count(x))//2
    return ct

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)