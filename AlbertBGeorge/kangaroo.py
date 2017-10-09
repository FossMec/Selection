#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    p1 = x1
    p2 = x2
    if((x1>x2 and v1>=v2) or (x2>x1 and v2>=v1)):
        return "NO"
    else:
        for i in range(10000):
            p1+=v1
            p2+=v2
            if(p1==p2):
                return "YES"
        return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)