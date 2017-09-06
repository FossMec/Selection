#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pv = nv = zr = 0
for i in range(n) :
	if arr[i] > 0 :
		pv += 1
	elif arr[i] < 0 :
		nv += 1
	else :
		zr += 1
print(pv/n)
print(nv/n)
print(zr/n)
