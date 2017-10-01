#!/bin/python3

def solve(year):
    if(year<1918):
        d=13
        if(year%4==0):
            d=12
    elif(year>1918):
        d=13
        if(year%400==0 or (year%4==0 and year%100!=0)):
            d=12
    elif(year==1918):
        d=26
    return(str(d)+'.09.'+str(year))
        

year = int(input().strip())
result = solve(year)
print(result)

