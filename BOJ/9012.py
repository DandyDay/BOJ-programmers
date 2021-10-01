import sys


def VPS(string):
    tmp = 0
    for i in range(len(string)):
        if string[i] == "(":
            tmp += 1
        elif string[i] == ")":
            tmp -= 1
        if tmp < 0:
            return "NO"
    if tmp != 0:
        return "NO"
    else:
        return "YES"


n = int(sys.stdin.readline())

for i in range(n):
    tmp = sys.stdin.readline()
    print(VPS(tmp))
