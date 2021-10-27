# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ""
    numlist = []
    tmp = ""
    charlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i in range(10):
        numlist.append(str(i))
    for char in s:
        if char in numlist:
            answer += char
        else:
            tmp += char
            if tmp in charlist:
                answer += str(charlist.index(tmp))
                tmp = ""
    return int(answer)

s= ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
for ss in s:
    print(solution(ss))