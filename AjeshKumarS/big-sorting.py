#!/bin/python3

import sys

n = int(input().strip())
x = {}

for i in range(n):
    num = input().strip()
    l = len(num)
    
    if not l in x:
        x[l] = []
    
    x[l].append(num)

for y in sorted(x):
    for v in sorted(x[y]):
        print(v)