#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
