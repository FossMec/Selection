#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()

max = 0
for x in word:
    if(h[ord(x)-97] > max):
        max = h[ord(x)-97]
print(len(word)*max)