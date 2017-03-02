memo = {}
def ways_to_climb(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    if stairs not in memo:
        memo[stairs] = ways_to_climb(stairs - 1) + ways_to_climb(stairs - 2) + ways_to_climb(stairs - 3)
    return memo[stairs]

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(ways_to_climb(n))
