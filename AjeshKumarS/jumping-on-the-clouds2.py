#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i = 0
ct = 0
while i < n-1:
    if(i!=n-2):
        if(c[i+2] is 0):
            ct+=1
            i+=2
        else:
            ct+=1
            i+=1
    else:
        ct+=1
        i+=1
print(ct)