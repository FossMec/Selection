#!/bin/python3

import sys

def getTotalX(a, b):
    maxi=max(a)
    mini=min(b)+1
    c=0
    for i in range(maxi,mini):
        for j in range(n):
            if i%a[j]!=0:
                break
            else:
                if a[j]==a[n-1]:
                    for k in range(m):
                        if b[k]%i!=0:
                            break
                        else:
                            if b[k]==b[m-1]:
                                c+=1
    return(c)                            
                            
    
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
