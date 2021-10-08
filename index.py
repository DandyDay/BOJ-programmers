import sys

text = sys.stdin.readline().rsplit()[0]

stack = []

for i in text:
    if not i.isalpha() and i != ")":
        stack.append(i)
    else:
        print(i, end="")
    