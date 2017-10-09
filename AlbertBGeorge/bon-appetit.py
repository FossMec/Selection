#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    bill = int(sum(ar)) - int(ar[k])
    pay = int(bill/2)
    if pay == b :
    	return "Bon Appetit"
    else :
    	return b-pay


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)