import sys

ipt = sys.stdin.readline().rsplit()[0]
stick = 0
prev = ""
output = 0

for i in range(len(ipt)):
    if ipt[i] == "(":
        stick += 1
    elif ipt[i] == ")":
        if prev == "(":
            stick -= 1
            output += stick
        else:
            stick -= 1
            output += 1
    prev = ipt[i]

print(output)
