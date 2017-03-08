n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

total = 0
bottom = 0
for i in range(n):
    total += a[i]*b[i]
    bottom += b[i]
    
print("%.1f" % (total/bottom))