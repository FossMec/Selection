def rev(num):
    b = ''
    m = str(num)
    for l in range(len(m)):
        b+=m[len(m)-l-1]
    return int(b)


i, j, k = [int(x) for x in input().split()]
c = 0
for x in range(i,j+1):
    if(abs(x-rev(x))%k is 0):
        c+=1
print(c)