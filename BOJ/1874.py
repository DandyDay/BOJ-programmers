import sys

# input = sys.stdin.readline().rstrip

class Stack:
    def __init__(self):
        self.topidx = -1
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        self.topidx += 1

    def pop(self):
        self.topidx -= 1
        return self.stack.pop()

    def top(self):
        if self.topidx == -1:
            return -1
        return self.stack[self.topidx]

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.topidx == -1:
            return 1
        else:
            return 0


stack = Stack()

n = int(input())
data = list(range(1, n+1))
idx = 0
tmp = []
result = []
for i in range(n):
    tmp.append(int(input()))
success = True
tmp_i = 0

while(True):
    if stack.top() != tmp[tmp_i]:
        try:
            stack.push(data[idx])
            idx += 1
            result.append("+")
        except IndexError:
            success = False
            print("NO")
            break
    else:
        tmp_i += 1
        result.append("-")
        stack.pop()
    if tmp_i == n:
        break

if success:
    for i in result:
        print(i)
