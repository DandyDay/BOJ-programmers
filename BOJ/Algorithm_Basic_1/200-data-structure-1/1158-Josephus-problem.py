import sys
n, m = map(int, sys.stdin.readline().split())
idx = 0
lst = list(range(1, n+1))
result = []
while(lst):
    idx = (idx + m - 1) % (len(lst))
    result.append(str(lst.pop(idx)))

print("<%s>" % ", ".join(result))