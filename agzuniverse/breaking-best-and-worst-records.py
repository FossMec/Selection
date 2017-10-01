#!/bin/python3

def getRecord(s):
    max_n=s[0]
    min_n=s[0]
    max_c=0
    min_c=0
    
    for i in s:
        if(i>max_n):
            max_n=i
            max_c+=1
        elif(i<min_n):
            min_n=i
            min_c+=1
    print(str(max_c)+" "+str(min_c))
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
getRecord(s)
