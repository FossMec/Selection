n = int(input())
memo = []
lst = []
for i in range(n):
	x = int(input())
	memo.insert(i, x)
	i+=1
for x in memo:
	p = x%5
	if x < 38 :
		lst.append(x)
		continue

	if p > 2 :
		x -= p
		x += 5
	lst.append(x)
for u in lst:
	print(u)