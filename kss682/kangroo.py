
import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
  if(v2>v1 or v1>v2): 
    if(((x2-x1)%(v1-v2)==0 and v1-v2>0 and x2>x1) or ((x1-x2)%(v2-v1)==0 and v2>v1 and x1>x2))  :
      return "YES"
    else:
      return "NO"
  else:
    return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
