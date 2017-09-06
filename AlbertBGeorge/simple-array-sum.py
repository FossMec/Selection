#!/bin/python3

import sys

def simpleArraySum(n, ar):
	sum = 0
	for i in range(n):
		sum += int(ar[i])
	return sum
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
