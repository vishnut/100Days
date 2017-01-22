import sys

n = int(input().strip())

spaces = n - 1
hashes = 1

for i in range(n):
    line = ""
    for j in range(spaces):
        line += " "
    for j in range(hashes):
        line += "#"
    spaces -= 1
    hashes += 1
    print(line)