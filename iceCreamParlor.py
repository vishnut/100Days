t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    hash_a = {}
    for i, x in enumerate(a):
        if (m - x) in hash_a:
            print(hash_a[m-x] + 1, i + 1)
        hash_a[x] = i
