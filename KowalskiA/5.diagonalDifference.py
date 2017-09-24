#!/bin/python

import sys
def difference(ar,p):
    d1=d2=0
    for i in range(p):
        d1+=ar[i][i]
        d2+=ar[i][p-i-1]
    return(abs(d1-d2))
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
print difference(a,n)
