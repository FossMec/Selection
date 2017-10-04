#!/bin/python
from collections import Counter
n = int(raw_input().strip())
a = Counter(map(int, raw_input().strip().split(' ')))

print a.most_common()[0][0]
