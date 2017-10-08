#!/bin/python3

import sys

def sockMerchant(n, ar):
    count = 0
    for a in set(ar):
        count+=(ar.count(a))//2
    return (count)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
