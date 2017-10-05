#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(n):
         if grades[i]>=38:
            for p in range(1,3):
                if (grades[i]+p)%5==0:
                    grades[i]+=p
    return(grades)
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


