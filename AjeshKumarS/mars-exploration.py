#!/bin/python3

import sys


S = input().strip()
l = len(S)
c=0
for i in range(0,l-1,3):
    s = S[i:i+4]
    if s[0] != 'S':
        c=c+1
    if s[1] != 'O':
        c=c+1
    if s[2] != 'S':
        c=c+1
print(c)