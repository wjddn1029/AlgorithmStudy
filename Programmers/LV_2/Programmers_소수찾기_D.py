#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
import math


def solution(numbers):
    num = [n for n in numbers]
    print(num)
    # 만들수 있는 전체 숫자 경우의 수 추가
    answer = []
    for i in range(1, len(num) + 1):
        answer.append(list(permutations(num, i)))

    result = []
    for i in answer:
        print(i)

    return answer


def isPrimeNumber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(solution("011"))