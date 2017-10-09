#!/bin/python3

import sys

def timeConversion(s):
    n = s
    if(s[8:] == "AM"):
        if(int(s[:2]) == 12):
             n = "00" + s[2:8]
    else:
        if(int(s[:2]) != 12):
            n = str(int(s[:2]) + 12) + s[2:8]        
    return n[:8]
        

s = input().strip()
result = timeConversion(s)
print(result)

