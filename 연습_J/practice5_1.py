def solution(n):
    result = []
    answer = 0
    for i in range(1, 1000000):
        a, b = divmod(i, n)
        if a == b:
            result.append(i)
    for value in result:
        answer += value
    return answer

n = 2
# result = 12
print(solution(n))
