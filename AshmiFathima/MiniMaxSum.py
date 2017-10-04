#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
n=sum(arr)
print n-(max(arr)), n-(min(arr))
