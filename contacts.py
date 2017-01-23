n = int(input().strip())
contacts = {}
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        name = ""
        for letter in contact:
            name = name + letter
            num = contacts.get(name, 0)
            contacts[name] = num + 1
    else:
        print(contacts.get(contact, 0))