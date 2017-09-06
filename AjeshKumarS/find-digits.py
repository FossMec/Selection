#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = input().strip()
    c = 0
    for i in range(len(n)):
        if(int(n[i])!=0 and int(n)%int(n[i]) is 0):
            c+=1
    print(c)