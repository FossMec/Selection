#!/bin/python3

import sys

def solve(year):
    ye=str(year)
    if year==1918:
        return('26.09.1918')
    if year<1918 and year %4==0 or year>1918 and (year%400==0 or (year%4==0 and year%100!=0)):
        return('12.09.'+ye)
    else:
        return('13.09.'+ ye)
year = int(input().strip())
result = solve(year)
print(result)
