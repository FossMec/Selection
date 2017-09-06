#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
	alPoint = 0
	boPoint = 0
	if a0 > b0 :
		alPoint += 1
	elif a0 < b0 :
		boPoint += 1
	if a1 > b1 :
		alPoint += 1
	elif a1 < b1 :
		boPoint += 1
	if a2 > b2 :
		alPoint += 1
	elif a2 < b2 :
		boPoint += 1
	return alPoint, boPoint
    # Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
