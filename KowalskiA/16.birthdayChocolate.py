#!/bin/python3

import sys

def solve(n, s, d, m):
    w=sum=0
    for i in range(n-m+1):
        t=i
        for j in range(m):
            
            sum+=s[t]
            t=t+1
        if sum==d:
            w=w+1
            sum=0       
        else:
            sum=0
            continue
    return(w)       
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
