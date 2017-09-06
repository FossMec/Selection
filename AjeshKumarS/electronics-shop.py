#!/bin/python3

import sys

def getMoneySpent(k, d, s):
    a = -1
    for i in k:
        for j in d:
            if(i+j <= s):
                a = max(a, i+j)
    return a

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)