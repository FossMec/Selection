#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    final_list=[]
    for i in grades:
        if i<38:
            final_list.append(i)
        else:
            rem=i%5
            if rem<3:
                final_list.append(i)
            elif rem==3:
                final_list.append(i+2)
            else:
                final_list.append(i+1)
    return(final_list)
            

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



