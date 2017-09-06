

n = int(input())
way = input()
l = 0
v = 0
for i in range(n):
    if(way[i] == 'U'):
        l+=1
    else:
        l-=1
    if(l==0 and way[i]=='U'):
        v+=1
print(v)