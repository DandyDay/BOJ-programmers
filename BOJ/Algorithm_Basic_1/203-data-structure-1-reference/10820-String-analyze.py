import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    output = [0, 0, 0, 0]

    if not line:
        break

    for char in line:
        if char.isspace():
            output[3] += 1
        elif char.isupper():
            output[1] += 1
        elif char.islower():
            output[0] += 1
        elif char.isdigit():
            output[2] += 1
    print(*output)
