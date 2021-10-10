import sys

S = sys.stdin.readline().rsplit('\n')[0]

lst = [0] * 26

for i in S:
    lst[ord(i)-ord('a')] += 1

print(*lst)