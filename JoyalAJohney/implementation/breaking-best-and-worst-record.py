#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    max,max_count=s[0],0
    min,min_count=s[0],0
    for item in s:
        if item>max:
            max=item
            max_count+=1
        elif item<min:
            min=item
            min_count+=1
    return([max_count,min_count])

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

