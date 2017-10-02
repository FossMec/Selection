#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positive,negative,zero=0,0,0
for i in range(n):
    if(arr[i]>0):
        positive+=1
    elif(arr[i]<0):
        negative+=1
    else:
        zero+=1

print(float("{0:.6f}".format(positive/n)))
print(float("{0:.6f}".format(negative/n)))
print(float("{0:.6f}".format(zero/n)))
