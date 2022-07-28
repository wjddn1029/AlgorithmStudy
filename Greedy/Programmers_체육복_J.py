def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

n = 5
lost = [2, 4]
reverse = [1, 3, 5]

print(solution(n, lost, reverse))

# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3