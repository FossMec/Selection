#!/bin/python3

n=int(input().strip())
arr=list(map(int,input().strip().split(' ')))
arr=sorted(arr)
l=arr[n-1]
c=0
for i in reversed(arr):
    if(i==l):
        c+=1
    else:
        break
print(c)
