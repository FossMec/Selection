#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
a=sorted(arr)
s1=s2=0
for i in range(1,len(a)):
    s1=s1+a[i-1]
    s2=s2+a[i]
print(s1,s2)
    
