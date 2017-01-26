def ransom_note(magazine, ransom):
    worddict = {}
    for i in magazine:
        if i in worddict:
            worddict[i] += 1
        else:
            worddict[i] = 1
    for i in ransom:
        if i not in worddict:
            return False
        elif worddict[i] > 1:
            worddict[i] -= 1
        else:
            del worddict[i]
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if answer:
    print("Yes")
else:
    print("No")
