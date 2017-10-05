#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
min,max=sum(arr[:-1]),sum(arr[1:])
print(min,max)
