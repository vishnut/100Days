#!/bin/python3

import sys

n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if grade >= 38 and (grade % 5) > 2:
        grade = ((grade // 5) + 1) * 5
    print(grade)
