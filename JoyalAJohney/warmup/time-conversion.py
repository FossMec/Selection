#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    hour=int(s[:2])
    
    if(s[-2]=="A"or s[-2]=="a"):
        a=s[2:-2]
        if(hour==12):
            return("00"+a)
        else:
            return(s[:-2])
            
    else:
        b=s[2:-2]
        if(hour<12):
            hour+=12
            return(str(hour)+b)
        else:
            return(s[:-2])

s = input().strip()
result = timeConversion(s)
print(result)
