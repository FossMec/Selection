#!/bin/python3

import heapq
arr=list(map(int,input().strip().split(' ')))
print(str(sum(heapq.nsmallest(4,arr)))+" "+str(sum(heapq.nlargest(4,arr))))
