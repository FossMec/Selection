#!/bin/python


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    if(grades_t>=38 and grades_t%5>=3):
        while(grades_t%5!=0):
            grades_t=grades_t+1
    print grades_t
