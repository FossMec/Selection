#!/bin/python3

import sys

def migratoryBirds(n, ar):
    a=[0,0,0,0,0,0]
    for i in range(1,6):
       
        for i in ar:
            a[i]+=1
    return a.index(max(a))
            
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
