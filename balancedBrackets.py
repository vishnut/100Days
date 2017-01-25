def is_matched(expression):
    stack = []
    for i in expression:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif len(stack) == 0 or not matchingbrackets(stack.pop(), i):
            return False
    return len(stack) == 0

def matchingbrackets(a, b):
    return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

