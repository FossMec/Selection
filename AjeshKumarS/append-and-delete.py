#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())
l = min(len(s),len(t))


for i in range(len(t)):
    if s[:i] != t[:i]:
        l = i-1
        break

diff = len(s)-l + len(t)-l
if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k:
    print('Yes')
else:
    print('No')