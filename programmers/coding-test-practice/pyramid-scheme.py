# https://programmers.co.kr/learn/courses/30/lessons/77486

def makelist(lst, enroll, referral, sell):
    if referral[enroll.index(sell)] != "-":
        lst.append(enroll.index(sell))
        makelist(lst, enroll, referral, referral[enroll.index(sell)])
    else:
        lst.append(enroll.index(sell))


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    tmp = []
    for sell in seller:
        lst = []
        makelist(lst, enroll, referral, sell)
        tmp.append(lst)
    for i, sale in enumerate(tmp):
        if amount[i] == 0: continue
        money = amount[i] * 100
        for idx in sale:
            moneyleft = money - money//10
            money = money//10
            answer[idx] += moneyleft
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])