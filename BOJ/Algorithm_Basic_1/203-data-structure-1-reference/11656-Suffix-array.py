import sys
S = sys.stdin.readline().rstrip('\n')
suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()
print("\n".join(suffix))