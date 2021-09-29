n, m = input().split()
n = int(n)
m = int(m)
ipt = []

for i in range(n):
    tmp = input()
    if len(tmp) == m: ipt.append(tmp)

minout = -1
data = ['B','W']

for i in range(n-7):
    for j in range(m-7):
        tmp = 0
        for k in range(8):
            for l in range(8):
                if ipt[i+k][j+l] == data[(k+l)%2]: tmp += 1
        if tmp>32: tmp=64-tmp
        if minout == -1: minout = tmp
        if minout >tmp: minout = tmp
print(minout)
