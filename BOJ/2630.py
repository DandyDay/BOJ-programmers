output = [0, 0]


def chkclr(lst):
    chk = True
    tmp = lst[0][0]
    for i in lst:
        for j in i:
            if j != tmp:
                chk = False
    if chk is False:
        cutlist(lst)
    else:
        output[int(tmp)] += 1


def cutlist(lst):
    size = len(lst)
    tmp = [[], [], [], []]
    for i in range(size//2):
        tmp[0].append(lst[i][0:size//2])
    for i in range(size//2):
        tmp[1].append(lst[i][size//2:size])
    for i in range(size//2):
        tmp[2].append(lst[size//2+i][0:size//2])
    for i in range(size//2):
        tmp[3].append(lst[size//2+i][size//2:size])

    for i in range(4):
        chkclr(tmp[i])


num = int(input())
inputlist = []
for i in range(2*num-1):
    inputlist.append(input())

print(inputlist)
chkclr(inputlist)

print(output[0])
print(output[1])
