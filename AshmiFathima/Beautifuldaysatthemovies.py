i,j,k = [int(x) for x in input().split()]
count = 0
for x in range(i,j+1):
    if (x - int(str(x)[::-1])) % k == 0:
        count += 1
print(count)
