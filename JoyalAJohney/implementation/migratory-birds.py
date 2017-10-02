#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    count_1,count_2,count_3,count_4,count_5=0,0,0,0,0
    for i in ar:
        if i==1:
            count_1+=1
        elif i==2:
            count_2+=1
        elif i==3:
            count_3+=1
        elif i==4:
            count_4+=1
        else:
            count_5+=1
    count_list=[count_1,count_2,count_3,count_4,count_5]
    n_count=len(count_list)
    champ=0
    
    for j in range(n_count):
        if count_list[j]>champ:
            champ=count_list[j]
            temp=j+1
    
    return(temp)    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

