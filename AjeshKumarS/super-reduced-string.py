#!/bin/python3

import sys

def super_reduced_string(s):
    res = []
    for c in s:
        if res and res[len(res)-1] == c: # peek what's on top
            res.pop()
        else:
            res.append(c)   
    st = ''
    for x in res:
        st+=x
    if(st is ''):
        return 'Empty String'
    else:
        return st

s = input().strip()
result = super_reduced_string(s)
print(result)