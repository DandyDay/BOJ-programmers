import sys
S = sys.stdin.readline().rstrip('\n')

for char in S:
    if char.isupper():
        if ord(char) < 65+13:
            print(chr(ord(char) + 13), end="")
        else:
            print(chr(ord(char) - 13), end="")
    elif char.islower():
        if ord(char) < 97+13:
            print(chr(ord(char) + 13), end="")
        else:
            print(chr(ord(char) - 13), end="")
    else:
        print(char, end="")
