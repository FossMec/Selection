#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    count = 0
    # Complete this function
    m = max(ar)
    for i in ar :
    	if i == m :
    		count += 1
    return count


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)