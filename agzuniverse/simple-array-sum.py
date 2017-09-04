import sys

def simpleArraySum(n, ar):
    sum=0
    for i in ar:
        sum+=i
    return(sum)
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
