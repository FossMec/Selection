#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    A=0
    B=0
    if a0>b0:
        A=A+1
    elif b0>a0:
         B=B+1
    else:
        A=0
        B=0
    if a1>b1:
        A=A+1
    elif b1>a1:
         B=B+1
        
    if a2>b2:
        A=A+1
    elif b2>a2:
         B=B+1  
    return(A,B)
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


