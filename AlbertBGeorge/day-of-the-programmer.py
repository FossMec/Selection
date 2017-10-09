#!/bin/python3

import sys

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif((year<=1917) & (year%4==0)) or ((year>1918) & (year%400==0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.{}'.format(year)
    else:
        return '13.09.{}'.format(year)
        

year = int(input().strip())
result = solve(year)
print(result)