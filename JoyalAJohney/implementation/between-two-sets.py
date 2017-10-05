#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function
    max_a,min_b,final_count=max(a),min(b),0
    
    for i in range(max_a,min_b+1):
        flag=1
        for a1 in a:
            if i%a1!=0:
                flag=0
                break
        
        if flag==1:
            for b1 in b:
                if b1%i!=0:
                    flag=0
                    break
        
        if flag==1:
            final_count+=1
                    
    return(final_count)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)

