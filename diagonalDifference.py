import sys

n = int(input().strip())
diag1 = 0
diag2 = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    diag1 += a_t[a_i]
    diag2 += a_t[n - a_i - 1]
    
print(abs(diag1 - diag2))