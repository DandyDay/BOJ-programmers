def solution(price, money, count):
    answer = -1
    cost = 0
    for i in range(count):
        cost += price * (i+1)
    answer = cost-money
    if answer<0: answer=0

    return answer