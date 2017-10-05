#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    count=0
    for i in range(n):
        if i==n-1:
            break
        elif ar[i]!=0:
            for j in range(i+1,n):
                if ar[i]==ar[j]:
                    count+=1
                    ar[i],ar[j]=0,0
                    break
    return(count)    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

