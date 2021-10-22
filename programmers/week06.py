#승률 > 무거운 복서 승 수 > 자기 몸무게 무거움 > 작은 번호
def solution(weights, head2head):
    winrates = []
    for idx, fight in enumerate(head2head) :
        try:
            winrates.append([fight.count("W") / (fight.count("W")+fight.count("L"))])
        except ZeroDivisionError:
            winrates.append([0])
        winheavy = 0
        for index, onefight in enumerate(fight):
            if onefight=="W" and weights[idx] < weights[index]: winheavy += 1
        winrates[idx].append(winheavy)
        winrates[idx].append(weights[idx])
    answer = []
    winrates_tmp = list(winrates)
    print(winrates)
    while(len(winrates_tmp)):
        maxV = max(winrates_tmp)
        pos = 0
        if winrates.count(maxV) == 1:
            answer.append(winrates.index(maxV)+1)
            winrates_tmp.remove(max(winrates_tmp))
        else: 
            for i in range(winrates.count(maxV)):
                answer.append(winrates.index(maxV,pos)+1)
                try:
                    pos = winrates.index(maxV,pos+1)
                except ValueError:
                    pass
                winrates_tmp.remove(max(winrates_tmp))

        
    return answer

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))
print(solution([60,70,60],["NNN","NNN","NNN"]))
