#!/bin/python3

from fractions import gcd

def getTotalX(a, b):
    lcm=a[0]
    count=0
    check=1
    for i in a:
        lcm=lcm*i/gcd(lcm,i)
        o=lcm
    while(lcm<=min(b)):
        for j in b:
            if(j%lcm!=0):
                check=0
                break
        if(check):
            count+=1
        lcm+=o
        check=1
    return(count)
        

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)

