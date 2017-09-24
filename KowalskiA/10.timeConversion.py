#!/bin/python3

import sys

def timeConversion(s):
    hours=int(s[:2])
    t=s[8:]
    if t=='AM':
        if hours==12:
            return('00'+s[2:8])        
        else:
            return(s[:8])
    else:
        if hours!=12:
            return(str(12+hours)+s[2:8])        
        else:
            return(s[:8])
        
    

s =(input().strip())
result = timeConversion(s)
print(result)
