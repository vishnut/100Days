import sys
import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(a, a_t)
    if len(a) % 2 == 0:
        print((a[len(a) // 2] + a[len(a) // 2 - 1]) / 2.0)
    else:
        print(a[len(a) // 2] / 1.0)