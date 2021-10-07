import sys


def calc(tmpa, tmpb, cal):
    if cal == "*":
        return (tmpa * tmpb)
    elif cal == "+":
        return (tmpa + tmpb)
    elif cal == "/":
        return (tmpa / tmpb)
    elif cal == "-":
        return (tmpa - tmpb)


n = int(sys.stdin.readline().rsplit()[0])

expression = sys.stdin.readline()

numbers = []
for i in range(n):
    tmp = int(sys.stdin.readline().rsplit()[0])
    numbers.append(tmp)

stack = []

for i in expression[-2::-1]:
    if i.isalpha():
        stack.append(numbers[ord(i) - ord('A')])
    else:
        stack.append(i)
    if type(stack[-1]) == int and type(stack[-2]) == int:
        tmpa, tmpb = stack.pop(), stack.pop()
        cal = stack.pop()
        stack.append(calc(tmpa, tmpb, cal))
try:
    print(f"{calc(stack.pop(),stack.pop(),stack.pop()):.2f}")
except IndexError:
    print(f"{stack[0]:.2f}")