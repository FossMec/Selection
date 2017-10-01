#!/bin/python3

def migratoryBirds(n, ar):
    f=0
    t=0
    for i in range(1,6):
        j=ar.count(i)
        if(f<j):
            f=j
            t=i
    return(t)
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

