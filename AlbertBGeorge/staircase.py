#!/bin/python3

import sys


n = int(input().strip())
for x in range(n):
    print(" "*(n-x-1) + "#"*(x+1))