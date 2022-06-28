#https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))

# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3

# 투포인터 개념으로 풀이
# 가장큰 몸무게와 가장 작은몸무게 합을 이용하여