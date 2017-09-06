import math
t = int(input())

for _ in range(t):
    a,b = [int(x) for x in input().split()]
    ar = math.ceil(math.sqrt(a))
    br = math.floor(math.sqrt(b))
    
    print(br - ar + 1)