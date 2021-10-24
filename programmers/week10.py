def solution(line):
    xans = []
    yans = []

    for i, l in enumerate(line):
        for j, m in enumerate(line):
            if i < j and l[0]*m[1] - m[0]*l[1] != 0:
                x = (l[1]*m[2] - l[2]*m[1]) / (l[0]*m[1] - m[0]*l[1])
                y = (l[2]*m[0] - l[0]*m[2]) / (l[0]*m[1] - m[0]*l[1])
                if(x == int(x) and y == int(y)):
                    xans.append(int(x))
                    yans.append(int(y))
    answer = []
    for i in range(max(yans) - min(yans) + 1):
        answer.append("." * (max(xans) - min(xans) + 1))

    for i in range(len(xans)):
        answer[yans[i]-min(yans)] = answer[yans[i]-min(yans)][:xans[i]-min(xans)] + "*" + answer[yans[i]-min(yans)][xans[i]-min(xans)+1:]

    answer.reverse()
    return answer