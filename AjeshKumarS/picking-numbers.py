#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

max = 0
x = 0
for i in a:
    x = a.count(i) + a.count(i-1)
    if(x>max):
        max = x
print(max)