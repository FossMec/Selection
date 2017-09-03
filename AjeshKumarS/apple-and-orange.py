#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

c1=c2=0
for i in range(m):
    if((a+apple[i]) >= s and (a+apple[i]) <= t):
        c1+=1
        
for j in range(n):
    if((b+orange[j]) >= s and (b+orange[j]) <= t):
        c2+=1

print("{}\n{}".format(c1,c2))