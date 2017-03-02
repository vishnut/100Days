memo = {0:0, 1:1, 2:1}
def fibonacci(n):
    # Write your code here.
    assert n >= 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
n = int(input())
print(fibonacci(n))
