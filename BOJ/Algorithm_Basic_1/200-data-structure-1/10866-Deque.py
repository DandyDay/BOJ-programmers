import sys


class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def size(self):
        return len(self.deque)

    def pop_front(self):
        if self.size() != 0:
            return self.deque.pop(0)
        else:
            return -1

    def pop_back(self):
        if self.size() != 0:
            return self.deque.pop()
        else:
            return -1

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return self.deque[0] if self.size() != 0 else -1

    def back(self):
        return self.deque[self.size() - 1] if self.size() != 0 else -1


deque = Deque()
n = int(sys.stdin.readline())
for i in range(n):
    ipt = sys.stdin.readline().split()
    if ipt[0] == 'push_back':
        deque.push_back(ipt[1])
    elif ipt[0] == 'push_front':
        deque.push_front(ipt[1])
    elif ipt[0] == 'pop_front':
        print(deque.pop_front())
    elif ipt[0] == 'pop_back':
        print(deque.pop_back())
    elif ipt[0] == 'size':
        print(deque.size())
    elif ipt[0] == 'empty':
        print(deque.empty())
    elif ipt[0] == 'front':
        print(deque.front())
    elif ipt[0] == 'back':
        print(deque.back())
