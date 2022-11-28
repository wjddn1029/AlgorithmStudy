def solution(fees, usage):
    answer = 0
    temp = 0
    price = usage
    for i, v in enumerate(fees):
        if price - (v[0] - temp) >= 0 and i != len(fees) - 1:
            answer += v[2] * (v[0] - temp)
            price -= v[0]
            temp = v[0]
        else:
            answer += (usage - temp) * v[2] + v[1]
            break
    return answer


fees = [[200, 910, 93],[400,1600,188],[655,7300,281],[0,15372,435]]
usage = 450
#208750
print(solution(fees, usage))
