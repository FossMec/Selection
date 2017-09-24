#!/bin/python3

import sys
def pattern(n):
    for i in range(n):
        for p in range(n):
            if p<n-1-i:
                print(" ",end="")
            else:
                print("#",end="")
                
        print()     
    return(0) 
n = int(input().strip())
pattern(n)
