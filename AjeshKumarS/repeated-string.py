#!/bin/python3

import sys

def cc(s ,l):
    ct = 0
    for i in range(l):
        if(s[i] is 'a'):
            ct+=1
    return ct

s = input().strip()
n = int(input().strip())
if(len(s)>=n):
    print(cc(s,n))
else:
    print(cc(s,len(s))*(n//len(s)) + cc(s,n%len(s)))