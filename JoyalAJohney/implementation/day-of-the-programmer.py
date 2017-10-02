#!/bin/python3

import sys

def solve(year):
    # Complete this function
    if year==1918:
        return("26.09.1918")
    elif year>=1700 and year<=1917:
        if year%4==0:
            return("12.09.{}".format(year))
        else:
            return("13.09.{}".format(year))
    elif year>=1919 and year<=2700:
        if year%400==0:
            return("12.09.{}".format(year))
        elif year%4==0 and year%100!=0:
            return("12.09.{}".format(year))
        else:
            return("13.09.{}".format(year))

year = int(input().strip())
result = solve(year)
print(result)

