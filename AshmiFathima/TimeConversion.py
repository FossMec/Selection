#!/bin/python

    

s = raw_input()
time=s[-2: ]
if (time=="PM" and s[:2]!="12") :
    s=str(12+int(s[ :2]))+s[2: ]
if (time=="AM" and s[:2]=="12") :
    s="00"+s[2: ]
print s[ :-2]
