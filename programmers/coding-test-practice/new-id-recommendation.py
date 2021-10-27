# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ""
    charlist = ['-','_','.']
    for i in range(10):
        charlist.append(str(i))
    for i in range(26):
        charlist.append(chr(97+i))
    new_id = new_id.lower()
    for char in new_id:
        if char in charlist:
            answer += char
    prevpoint = False
    replacedPoints = 0
    for i, char in enumerate(answer):
        if char == ".":
            if prevpoint is True:
                answer = answer[:i-replacedPoints] + answer[i-replacedPoints+1:]
                replacedPoints += 1
            prevpoint = True
        else:
            prevpoint = False
    if answer[0] == '.':
        answer = answer[1:]
    if answer != "" and answer[-1] == '.':
        answer = answer[:-1]
    if answer == "":
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) <= 2:
        while(len(answer) < 3):
            answer = answer + answer[-1]

    return answer

hi = ["...!@BaT#*..y.abcdefghijklm"	,"z-+.^."	,"=.="	,"123_.def"	,"abcdefghijklmn.p"	]
for i in hi:
    print(solution(i))