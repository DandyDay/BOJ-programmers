def GPA(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    tmpscore=0
    for i in range(len(scores)):
        tmp = []
        for j in scores:
            tmp.append(j[i])
        if (max(tmp) == tmp[i] and tmp.count(tmp[i]) == 1) or (min(tmp) == tmp[i] and tmp.count(tmp[i]) == 1):
            tmp.remove(tmp[i])
            tmpscore = sum(tmp)/len(tmp)
        else:
            tmpscore = sum(tmp)/len(tmp)
        answer = answer + GPA(tmpscore)
    return answer

a = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(a))