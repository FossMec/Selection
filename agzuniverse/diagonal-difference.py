#!/bin/python3

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
m=0
o=0
for d in range(0,n):
    m+=a[d][d]
    o+=a[d][n-d-1]
print(abs(m-o))
