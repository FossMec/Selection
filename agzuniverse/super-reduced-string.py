#!/bin/python3

def super_reduced_string(s):
    c=1
    while(c):
        c=0
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                s=s[:i]+s[i+2:]
                c=1
                break
    if(s==''):
        s='Empty String'
    return(s)

s = input().strip()
result = super_reduced_string(s)
print(result)
