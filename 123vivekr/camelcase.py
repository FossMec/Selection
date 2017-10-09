#!/bin/python3

import sys
s = input().strip()
print(1 + sum(1 for c in s if c.isupper()))
