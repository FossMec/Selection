n = int(input())
a = [int(x) for x in input().split()]

v = 0
vf = 0
for x in set(a):
    if(a.count(x)>vf):
        vf = a.count(x)
        v = x
print(len(a)-vf)