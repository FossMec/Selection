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
apple_count,orange_count=0,0

for apples_d in apple:
    dist=a+(apples_d)
    if dist>=s and dist<=t:
        apple_count+=1

for orange_d in orange:
    dist=b+(orange_d)
    if dist>=s and dist<=t:
        orange_count+=1
        
print(apple_count)
print(orange_count)

