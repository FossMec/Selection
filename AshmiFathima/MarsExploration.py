#!/bin/python

import sys

s = raw_input().strip()
l=len(s)
if(l%3==0 and l<=99):
    n=l/3
v="SOS"*n
c=0
for i in range(l):
    if(s[i]!=v[i]):
        c+=1
print c
