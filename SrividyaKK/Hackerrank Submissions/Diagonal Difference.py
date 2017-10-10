n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sm=0
so=0
for i in range(n):
    for j in range(n):
        if i==j: 
            sm+=a[i][j]
        if (i+j==n-1):
            so+=a[i][j]
print(abs(sm-so))
