
import sys


n = int(input().strip())
for i in range(1,n+1):
  for j in range(1,n+1):
    if(i+j>n):
      print('#',end='')
    else:
      print('\t',end='')
  print('\n')
