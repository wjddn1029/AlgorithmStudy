#https://programmers.co.kr/learn/courses/30/lessons/12921

import math

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if isPrimeNumber(i):
            answer += 1

    return answer


def isPrimeNumber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True