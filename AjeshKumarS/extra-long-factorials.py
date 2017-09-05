#!/bin/python3

import sys


n = int(input().strip())
p = 1
for i in range(1,n+1):
    p*=i
print(p)