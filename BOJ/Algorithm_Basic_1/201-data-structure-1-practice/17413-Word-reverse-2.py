import sys


def reverse(text):
    tmp = ""
    for i in text:
        tmp = i + tmp
    return tmp


tag = 0
tmp = ""
lst = []
text = sys.stdin.readline().rsplit("\n")[0]
for i in text:
    if tag == 0 and i == '<':
        if tmp != "":
            lst.append(tmp)
        tag = 1
        tmp = "<"
    elif tag == 1:
        if i == '>':
            tmp += i
            tag = 0
            lst.append(tmp)
            tmp = ""
        elif i != '<':
            tmp += i
    elif tag == 0 and i != ' ':
        tmp += i
    elif tag == 0 and i == ' ':
        lst.append(tmp)
        tmp = ""
lst.append(tmp)

for i in range(len(lst)):
    try:
        if lst[i][0] == "<":
            print(lst[i], end="")
        elif lst[i+1][0] != '<':
            print(reverse(lst[i]), end=" ")
        else:
            print(reverse(lst[i]), end="")
    except IndexError:
        print(reverse(lst[i]), end="")