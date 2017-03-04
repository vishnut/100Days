from bisect import bisect_left

v = int(input().strip())
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
print(bisect_left(ar, v))