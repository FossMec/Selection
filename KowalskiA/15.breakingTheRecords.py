#!/bin/python3

import sys

def getRecord(s):
    high=low=s[0]
    c=p=0
    for i in range(n):
        if s[i]>high:
            c=c+1
            high=s[i]
        elif s[i]<low:
            p+=1
            low=s[i]
    return(c,p)
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
