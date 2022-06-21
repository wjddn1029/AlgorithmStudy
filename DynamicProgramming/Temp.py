def solution(n):
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