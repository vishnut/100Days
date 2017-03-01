#!/bin/python3

import sys

def lonely_integer(a):
    num_set = set()
    for i in a:
        if i in num_set:
            num_set.remove(i)
        else:
            num_set.add(i)
    return tuple(num_set)[0]

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

