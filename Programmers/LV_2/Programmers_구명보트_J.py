# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    count = 0
    people.sort()

    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                count += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                count += 1
        else:
            if q[0] <= limit:
                q.pop()
                count += 1
    return count


people = [70, 80, 50]
limit = 100
print(solution(people, limit))
