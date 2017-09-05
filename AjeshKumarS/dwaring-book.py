#!/bin/python3

import sys

def solve(n, p):
    x = p//2
    y = n//2 - p//2
    if(x<y):
        return x
    else:
        return y

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)