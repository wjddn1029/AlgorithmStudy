# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    count = 0
    people.sort()
    q = deque(people)   # list 이용하여 remove를 쓴다면 시간복잡도가 O(n) 이어서 효율성에서 걸리기 때문에 deque 이용 (시간복잡도 O(1))

    while q:
        if len(q) >= 2:                     # 큐에 2개이상 남았을 때 비교하여 처리
            if q[0] + q[-1] <= limit:       # 큐 내에 가장 작은값과 가장 큰값을 더하여 limit과 비교
                q.pop()                     # limit보다 작거나 같으면 둘다 보트에 태우고(pop), count 1 증가
                q.popleft()
                count += 1
            elif q[0] + q[-1] > limit:
                q.pop()                     # limit보다 크면 무게가 큰 사람을 보트에 태움(greedy), count 1 증가
                count += 1
        else:                               # 큐에 혼자 남았을 경우 혼자 탈출
            if q[0] <= limit:
                q.pop()
                count += 1
    return count


people = [70, 80, 50]
limit = 100
print(solution(people, limit))
