from itertools import combinations

def solution(nums):
    answer = list(combinations(nums, 3))
    a = []
    for i in answer:
        a.append(i[0] + i[1] + i[2])

    result = 0
    for i in a:
        if isPrimeNumber(i):
            result += 1

    return result


def isPrimeNumber(a):
    flag = True
    for i in range(2, a):
        if a % i == 0:
            return False
    return flag