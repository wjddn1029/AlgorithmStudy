def solution(n):
    # 1
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    # 2
    for i in range(n):
        for j in range(i, n):
            # 3
            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 4
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer

# 정답 풀이


#잘못된 방향성 -> 수학적으로 깔끔하게 풀이 할 수 있는 걸 생각해보자
#https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
def solve(n):
    answer = []
    #첫번째 항 푸쉬
    for i in range(n):
        answer.append([i+1])

    #마지막리슽 항 추가
    for i in range(1, n):
        answer[n-1].append(answer[n-1][0] + i)

    #끝열 추가
    end = answer[n-1][n-1]
    tmp = n
    for i in range(n-1, 0, -1):
        if len(answer[i]) == tmp:
            pass
        else:
            end += 1
            answer[i].append(end)
        tmp -= 1
    end_point = 0
    for i in range(n):
        end_point += i+1
    print(end_point)
    return answer

print(solution(4))

#잘못된 방향성