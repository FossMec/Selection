#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sum_primary_diagonal,sum_secondary_diagonal,i=0,0,0
for item in a:
    sum_primary_diagonal+=item[i]
    sum_secondary_diagonal+=item[(n-1)-i]
    i+=1

print(abs(sum_primary_diagonal-sum_secondary_diagonal))
    
