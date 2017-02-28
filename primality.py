import math

p = int(input().strip())
p_string = ("Not prime", "Prime")
for a0 in range(p):
    n = int(input().strip())
    is_prime = True
    if n == 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i < n:
                is_prime = False
                break
    print(p_string[is_prime])