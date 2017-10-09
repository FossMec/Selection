#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    h = l = s[0]
    ch = cl = 0
    
    for i in range(len(s)):
        if s[i] > h :
            h = s[i]
            ch += 1
        elif s[i] < l :
            l = s[i]
            cl += 1
    return [ch, cl]
    

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
