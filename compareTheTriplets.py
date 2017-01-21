import sys

alice = 0
bob = 0

def addPoints(aScore, bScore):
    global alice
    global bob
    if aScore > bScore:
        alice += 1
    elif bScore > aScore:
        bob += 1
        
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

addPoints(a0, b0)
addPoints(a1, b1)
addPoints(a2, b2)

print(alice, bob)