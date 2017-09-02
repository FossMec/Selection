#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
ar = sorted(arr)
s1 = 0
s2 = 0
for i in range(len(arr)-1):
    s1+=ar[i]
    s2+=ar[i+1]
print(s1, s2)