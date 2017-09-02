#!/bin/python3

import sys

def timeConversion(s):
    hh = int(s[0:2])
    p = s[8:]
    y = '00'
    if(p == 'PM'):
        if(hh == 12):
            return str(hh) + s[2:8]
        else:
            return str(hh+12) + s[2:8]
    elif(p == 'AM'):
        if(hh == 12):
            y == '00' 
        elif(hh<11):
            y = '0' + str(hh)
        else:
            y = str(hh)
        return y + s[2:8]

s = input().strip()
result = timeConversion(s)
print(result)