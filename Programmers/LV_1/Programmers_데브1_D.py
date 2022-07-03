def solution(grade):
    if grade == sorted(grade):
        return 0
    answer = 0
    idx = grade.index(min(grade))
    min_value = min(grade)
    for i, v in enumerate(grade):
        if i < idx:
            answer += v - min_value
            grade[i] = min_value

    while grade != sorted(grade):
        for i in range(idx, len(grade)):
            prev = grade[i-1]
            if prev > grade[i]:
                answer += prev - grade[i]
                grade[i-1] = grade[i]
            if grade == sorted(grade):
                break
    return answer
# 3문제 시간 초과
