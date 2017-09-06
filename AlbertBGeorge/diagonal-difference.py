#!/bin/python3

import sys

def result(x, arr) :
	maindia = offdia = 0
	for i in range(x) :
		maindia += arr[i][i]
		offdia += arr[i][x-i-1]
		diff = maindia - offdia
	if diff >= 0:
		return diff
	else :
		return (-1*diff)
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
print(result(n, a))
