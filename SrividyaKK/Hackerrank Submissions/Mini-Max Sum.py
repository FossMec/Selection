import sys

arr = list(map(int, input().strip().split(' ')))
S=[]
for i in range(len(arr)): 
    s=0
    for j in range(len(arr)):
        s+=arr[j]
    s-=arr[i]
    S.append(s)
print(min(S), max(S))
