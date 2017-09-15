a = [int(x) for x in input().split()]
b = []
for i in a :
	b.append(sum(a) - i)
print(min(b), max(b)) 