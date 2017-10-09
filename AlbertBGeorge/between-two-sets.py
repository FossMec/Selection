#!/bin/python3

import sys

def getTotalX(a, b):
    c = 0
    x = sorted(a)
    y = sorted(b)
    for i in range(x[len(a)-1], y[0]+1):
        for j in a:
            if(i%j != 0):
                break
        else:
            for j in b:
                if(j%i != 0):
                    break
            else:
                c+=1
    return c

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)