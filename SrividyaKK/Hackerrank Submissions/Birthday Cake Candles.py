import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    #ar denotes the height of the candles
    m=max(ar)
    c=0
    for i in range(n): 
       if ar[i]==m: c+=1
    return c

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
