def array_left_rotation(a, n, k):
    b = list()
    for i in range(n):
        b.append(a[(k - n + i) % n])
    return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')