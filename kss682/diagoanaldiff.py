
import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
s,s1=0,0
for i in range(n):
    s=s+a[i][i]
for i in range(n):
    s1=s1+a[i][n-1-i]
print(abs(s-s1))    
