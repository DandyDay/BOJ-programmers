import sys

S = sys.stdin.readline().rsplit('\n')[0]

lst = [-1] * 26

for i, char in enumerate(S):
    if lst[ord(char)-ord('a')] == -1:
        lst[ord(char)-ord('a')] = i

print(*lst)