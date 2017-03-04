#!/bin/python3

import sys

s = input().strip()
up = (v for v in s if v.isupper())
print(sum(1 for i in up) + 1)
