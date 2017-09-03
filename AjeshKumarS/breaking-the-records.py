#!/bin/python3

import sys

def getRecord(s):
    h=l=s[0]
    hc=lc=0
    for i in range(len(s)):
        if(s[i]>h):
            h = s[i]
            hc+=1
        elif(s[i]<l):
            l = s[i]
            lc+=1
    return [hc, lc]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))