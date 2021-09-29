ipt = int(input())
find = False
i = 666
repeat = 0
while not find:
    stri = str(i)
    if "666" in stri:
        ipt -= 1
    if ipt == 0:
        print(i)
        find = True
    i += 1
