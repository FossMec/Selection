#!/bin/python3

import sys

def result(x, ar):
    a=b=c=0
    for i in range(x):
        if(ar[i]<0):
            a+=1
        elif(ar[i]>0):
            b+=1
        else:
            c+=1
    print("{}\n{}\n{}".format(b/x,a/x,c/x))


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
result(n, arr)