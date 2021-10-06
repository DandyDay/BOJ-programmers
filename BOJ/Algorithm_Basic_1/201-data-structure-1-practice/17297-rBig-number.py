import sys
n = int(sys.stdin.readline().rsplit()[0])
numbers = list(map(int, sys.stdin.readline().split()))

stack = []
answer = [-1] * n
stack.append(0)
for i in range(1, n):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
