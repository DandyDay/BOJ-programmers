def solution(table, languages, preference):
    tmpscore = 0
    maxlist = []
    maxscore = 0
    tmp = []
    
    for i in table:
        tmp.append(i.split())
    
    for i in tmp:
        tmpscore = 0
        for langidx in range(len(languages)):
            if i.count(languages[langidx]) != 0:
                tmpscore += preference[langidx] * (6-i.index(languages[langidx]))
        if tmpscore > maxscore:
            maxscore = tmpscore
            maxlist = [i[0]]
        elif tmpscore == maxscore:
            maxlist.append(i[0])
            
    maxlist.sort()
    answer = maxlist[0]
    return answer
