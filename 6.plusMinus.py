#!/bin/python3

import sys
def fraction(a,n):
    p=n1=z=0
    for i in range(n):
        if a[i]>0:
            p=p+1
        elif a[i]==0:
            z=z+1
        else:
            n1=n1+1
    print(p/n)
    print(n1/n)
    print(z/n)
    return(0)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
fraction(arr,n)
