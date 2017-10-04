#!/bin/python

import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
charged=b-(sum(ar)-ar[k])/2
if(charged==0):
    print "Bon Appetit"
else:
    print charged
