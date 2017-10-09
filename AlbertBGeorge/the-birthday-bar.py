#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    i = 0
    ct = 0
    while((i+m)<=n):
        sum = 0
        for x in range(m):
            sum+=s[i+x]
        
        if(sum is d):
            ct+=1
        i+=1
    return ct
    

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
