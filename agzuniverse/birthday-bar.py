#!/bin/python3

def solve(n, s, d, m):
    c=0
    sum=0
    for i in range(n-m+1):
        for j in range(i,i+m):
            sum+=s[j]
        if(sum==d):
            c+=1
        sum=0
    return(c)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

