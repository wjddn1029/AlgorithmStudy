def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        flag = True
        for j in range(len(board)):
            if flag and board[j][i-1] != 0:
                check_box = box[-1] if box else 0
                if check_box == board[j][i-1]:
                    answer += 2
                    box.pop()
                else:
                    box.append(board[j][i-1])
                board[j][i - 1] = 0
                flag = False


    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


#https://school.programmers.co.kr/learn/courses/30/lessons/64061


