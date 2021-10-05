import sys

def flip(string):
    tmpstr = ""
    for i in string:
        tmpstr = i + tmpstr
    return tmpstr

n = int(sys.stdin.readline())

for i in range(n):
    tmp = sys.stdin.readline().split()
    for word in tmp:
        print(flip(word), end=" ")
    print()