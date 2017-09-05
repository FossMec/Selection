#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    c = 0
    for x in a:
        if(x<=0):
            c+=1
    if(c<k):
        print("YES")
    else:
        print("NO")
