#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_no,n=max(ar),0
    for i in ar:
        if i==max_no:
            n+=1
    return n

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

