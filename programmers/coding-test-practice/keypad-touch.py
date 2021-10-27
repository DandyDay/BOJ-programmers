# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7]
    r = [3, 6, 9]
    c = [2, 5, 8, 0]
    r_loc, l_loc = 3, 3
    l_corr, r_corr = 0, 0
    for n in numbers:
        if n in r:
            answer += "R"
            r_loc = r.index(n)
            r_corr = 0
        elif n in l:
            answer += "L"
            l_loc = l.index(n)
            l_corr = 0
        else:
            ldis = abs(c.index(n) - l_loc) - l_corr
            rdis = abs(c.index(n) - r_loc) - r_corr
            if ldis > rdis:
                answer += "R"
                r_corr = 1
                r_loc = c.index(n)
            elif rdis > ldis:
                answer += "L"
                l_corr = 1
                l_loc = c.index(n)
            else:
                if hand == "right":
                    answer += "R"
                    r_loc = c.index(n)
                    r_corr = 1
                else:
                    answer += "L"
                    l_loc = c.index(n)
                    l_corr = 1
    return answer

ss = [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"], [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]]

for s in ss:
    print(solution(s[0],s[1]))