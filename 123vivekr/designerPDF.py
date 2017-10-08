#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
l = len(word)
a = ord('a')
tallest = h[ord(word[0]) - a]
for x in word[1:]:
    t = h[ord(x) - a]
    if(t > tallest):
        tallest = t
print(len(word) * tallest)
