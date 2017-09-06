#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


while n>-1:
    if len(arr)==0:
        break
    print(len(arr))
    arr = [x for x in arr if x!= min(arr)]