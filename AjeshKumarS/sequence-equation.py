def pp(i,p):
    return p.index(i)+1

n = int(input())
p = [int(x) for x in input().split()]

for i in range(1,n+1):
    print(pp(pp(i,p),p))