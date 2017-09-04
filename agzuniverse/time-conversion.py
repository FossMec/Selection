#!/bin/python3

def timeConversion(s):
    m=""
    if(s[8:]=="PM" and s[0:2]!="12"):
        m=str((int(s[0:2])+12)%24)+s[2:8]
    elif(s[8:]=="AM" and s[0:2]=="12"):
        m="00"+s[2:8]
    else:
        m=s[:8]
    return m

s = input().strip()
result = timeConversion(s)
print(result)
