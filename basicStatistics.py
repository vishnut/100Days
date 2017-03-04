n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

total = 0
for i in ar:
    total += i
print(total / n)

ar.sort()
ar_len = len(ar)
if ar_len % 2:
    print(ar[ar_len // 2])
else:
    print((ar[ar_len // 2] + ar[ar_len // 2 - 1]) / 2)
    
maxinst = 0
instnum = None
lastnum = None
count = 0
for i in ar:
    if i == lastnum:
        count += 1
    else:
        if count > maxinst:
            maxinst = count
            instnum = lastnum
        lastnum = i
        count = 1
print(instnum)