
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
A,B,C=[0.0,0.0,0.0]
for i in range(0,n):
  if(arr[i]>0):
    A+=1
  elif(arr[i]<0):
    B+=1
  else:
    C+=1
print(A/n)
print(B/n)
print(C/n)
    
