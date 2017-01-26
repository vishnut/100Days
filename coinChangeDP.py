#!/bin/python3

import sys

memoizer = {}
def make_change(coins, n, m):
    ways = 0
    num = 0
    if n == 0:
        return 1
    if len(coins) == 1:
        return n % coins[0] == 0
    if (m, n) in memoizer:
        return memoizer[(m, n)]
    while coins[0] * num <= n:
        ways += make_change(coins[1:], n - (num * coins[0]), m + 1)
        num += 1
    memoizer[(m, n)] = ways
    return ways

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coins.sort()
print(make_change(coins, n, 0))