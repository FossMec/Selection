#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

if(max(height)-k > 0):
    print(max(height)-k)
else:
    print(0)