def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                temp = 0        # 바구니에 넣으려고 하는 인형을 저장하기 위해 temp변수를 만들어 줍니다.
                if result:
                    temp = result[-1]
                if temp == board[j][i-1]:   # 바구니에 넣으려고 하는 인형이 현재 바구니에 제일 마지막에 담겼던 인형과 종류가 같으면
                    result.pop()            # 없애주고 따로 result에 append 시켜주지 않고
                    answer += 2             # 결과값에 +2를 해줍니다
                else:
                    result.append(board[j][i-1])
                board[j][i - 1] = 0
                break       # 인형 하나 찾았으면 다음 moves로 이동하기 위해 break 시켜줍니다.

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


print(solution(board, moves))

#https://school.programmers.co.kr/learn/courses/30/lessons/64061
