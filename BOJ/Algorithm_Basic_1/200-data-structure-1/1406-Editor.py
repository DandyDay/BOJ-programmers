import sys

text_left = list(sys.stdin.readline().rstrip())
text_right = []
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    ipt = sys.stdin.readline().split()
    if ipt[0] == 'L':
        if text_left != []:
            text_right.append(text_left.pop())
    elif ipt[0] == 'D':
        if text_right != []:
            text_left.append(text_right.pop())
    elif ipt[0] == 'B':
        if text_left != []:
            text_left.pop()
    elif ipt[0] == 'P':
        text_left.append(ipt[1])

print("".join(text_left + list(reversed(text_right))))
