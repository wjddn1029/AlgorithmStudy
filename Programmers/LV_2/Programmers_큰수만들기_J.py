# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 1차풀이
from itertools import combinations

def solution(number, k):
    answer = list(combinations(number, len(number) - k))
    s = []
    for i in answer:
        s.append(int(''.join(i)))
    return str(max(s))

# 1차풀이 결과 타임아웃 => 저번 구명보트 문제처럼 스택 or 큐 사용 예정


# 2차풀이
def solution(number, k):
    answer = []

    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break
        answer.append(i)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


