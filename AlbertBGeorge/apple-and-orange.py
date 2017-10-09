#!/bin/python

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int, input().strip().split(' '))
orange = map(int,input().strip().split(' '))
ans0 = ans1 = 0
for i in apple:
    if a + i >= s and a + i <= t:
        ans0 += 1
for i in orange:
    if b + i >= s and b + i <= t:
        ans1 += 1
print(ans0)
print(ans1)