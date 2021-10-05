import sys


n = int(sys.stdin.readline())
stack = []
for i in range(n):
    ipt = sys.stdin.readline()
    try:
        command, num = ipt.split()
        num = int(num)
    except ValueError:
        command = ipt.split()[0]
    if command == "push":
        stack.append(num)
    elif command == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    elif command == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])