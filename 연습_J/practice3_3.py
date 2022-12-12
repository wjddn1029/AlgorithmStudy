def solution(N):
    sum = 0
    temp = 0
    for i in str(N):
        sum += int(i)

    for i in range(N+1, 50001):
        for num in str(i):
            temp += int(num)
        if sum == temp:
            return i
        else:
            temp = 0

N = 28
print(solution(N))
