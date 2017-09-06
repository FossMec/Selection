n = int(input())

c = 5
l = 0
for i in range(1, n+1):
    l+=c//2
    c=(c//2)*3
print(l)