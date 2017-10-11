import sys

def simpleArraySum(n, ar):
    # Complete this function
    s=0
    for i in range(n): 
        s+=ar[i]
    return s

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
