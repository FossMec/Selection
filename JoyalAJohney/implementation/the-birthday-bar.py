#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    count=0
    for i in range(n-(m-1)):
        if d==sum(s[i:m+i]):
            count+=1
    return(count)
    
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

