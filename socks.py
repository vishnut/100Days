#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

socks = set()
num = 0
for i in c:
    if i in socks:
        num += 1
        socks.remove(i)
    else:
        socks.add(i)
print(num)
