#!/bin/python3

n=int(input().strip())
for i in range(n,0,-1):
    print((" "*(i-1))+("#"*(n+1-i)))
