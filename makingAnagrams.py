def number_needed(a, b):
    letter_dict = {}
    for l in a:
        if l in letter_dict:
            letter_dict[l] += 1
        else:
            letter_dict[l] = 1
    count = 0
    for l in b:
        if l in letter_dict:
            if letter_dict[l] <= 1:
                del letter_dict[l]
            else:
                letter_dict[l] -= 1
        else:
            count += 1
    for l in letter_dict:
        count += letter_dict[l]
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))