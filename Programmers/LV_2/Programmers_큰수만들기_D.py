#https://school.programmers.co.kr/learn/courses/30/lessons/42883
from itertools import permutations

from itertools import permutations, combinations


def solution(number, k):
    answer = list(combinations(number, len(number) - k))
    s = []
    for i in answer:
        s.append(int(''.join(i)))
    return str(max(s))

# 입출력 예
# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"