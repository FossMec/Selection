#!/bin/python3

import sys

def solve(grades):
    for i in range(len(grades)):
        if(grades[i]>37):
            for j in range(1,3):
                if((grades[i]+j) % 5 is 0):
                    grades[i]+=j
                    break
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))