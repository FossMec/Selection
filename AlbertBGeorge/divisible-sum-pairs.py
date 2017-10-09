#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    for i in range(n) :
    	p = 0
    	while p < i :
    		if (ar[p]+ar[i]) % k == 0 :
    			count += 1

    		p += 1
    return count


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
