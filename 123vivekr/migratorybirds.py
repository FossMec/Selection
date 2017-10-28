#!/bin/python3

import sys

def migratoryBirds(n, ar):
    return max(set(ar), key=ar.count)
    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

