#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    count_f,count_b=0,0
    for i in range(1,n+1):
        if i==p:
            break
        elif (i!=p and i%2!=0) or (i!=p and i==1): 
            count_f+=1
    
    for j in range(n,0,-1):
        if j==p:
            break
        elif j!=p and j%2==0:
            count_b+=1
    
    count=[count_f,count_b]
    return(min(count))
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)

