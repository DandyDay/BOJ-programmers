import sys

text = sys.stdin.readline().rsplit()[0]

stack = []

priority = {'(': 1, '*': 3, '/': 3, '+': 2, '-': 2}

for i in text:
    if i.isalpha():
        print(i, end="")
    elif i != ')':
        try:
            if priority[stack[-1]] > priority[i]:
                print(i, end="")
            else:
                stack.append(i)
        except IndexError:
            stack.append(i)
    else:
        tmp = stack.pop()

for i in stack.reversed():
    print(i, end="")