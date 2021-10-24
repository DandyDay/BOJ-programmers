def solution(lottos, win_nums):
    answer = []
    win = [6,6,5,4,3,2,1]
    tmp = 0
    for lotto in lottos:
        if lotto in win_nums:
            tmp += 1
    answer.append(win[tmp+lottos.count(0)])
    answer.append(win[tmp])
    return answer