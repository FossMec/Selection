#!/bin/python3

import sys


s = input().strip()
n=0
for l in s:
    if l.isupper():
        n+=1
print (n+1)