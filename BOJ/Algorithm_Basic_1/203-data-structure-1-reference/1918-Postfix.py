import sys

text = sys.stdin.readline().rsplit()[0]

stack = []

priority = {'(': 1, '*': 3, '/': 3, '+': 2, '-': 2}

for i in text:
    if i.isalpha():
        print(i, end="")
    elif i == '(':
        stack.append(i)
    elif i != ')':
        if stack == []:
            stack.append(i)
        elif priority[stack[-1]] < priority[i]:
            stack.append(i)
        else:
            for j in stack:
                if priority[j] >= priority[i]:
                    print(i + stack.pop(), end="")
                else:
                    stack.append(i)
                    break
    else:
        tmpstack = reversed(stack)
        for j in stack:
            if j != '(':
                print(stack.pop(), end="")
            else:
                break

for i in stack:
    print(i, end="")