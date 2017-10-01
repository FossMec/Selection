#!/bin/python3
def solve(grades):
    for i in grades:
        if(i<38):
            continue
        elif(i%5>=3):
            grades[grades.index(i)]+=5-(i%5)
    return(grades)
n = int(input().strip())
grades = []
for i in range(n):
   t = int(input().strip())
   grades.append(t)
result = solve(grades)
print ("\n".join(map(str, result)))
