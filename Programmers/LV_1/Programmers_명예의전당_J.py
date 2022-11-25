def solution(k, score):
    answer = []
    temp = []
    for i, v in enumerate(score):
        if k > len(temp):
            temp.append(v)
            temp.sort()
            answer.append(temp[0])
        else:
            if temp and temp[0] < v:
                temp.pop(0)
                temp.append(v)
                temp.sort()
                answer.append(temp[0])
            else:
                answer.append(temp[0])

    return answer

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k, score))
