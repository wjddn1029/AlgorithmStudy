#https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
from itertools import combinations
from collections import deque

def solution(people, limit):
    weights = list(combinations(people, 2))
    p = deque(people.sort())
    answer = 0
    for i in weights:
        if limit >= sum(i):
            if i[0] in p and i[1] in p:
                p.pop()
                p.pop()
                answer += 1

    answer += len(people)
    return answer


print(solution([70, 50, 80, 50], 100))

# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3