def solution(rows, columns, queries):
    answer = []
    matrix = []
    for r in range(rows):       # rows별 columns값을 가지고있는 matrix를 만들어 줍니다.
        matrix.append([a for a in range(r * columns + 1, (r + 1) * columns + 1)])

    for query in queries:
        query = [x - 1 for x in query]   # 인덱스는 0부터 시작하므로 -1
        temp = matrix[query[0]][query[1]]  # 좌측 제일 위 벨류 저장 (※중요: 제일 먼저 이동하는 벨류값은 matrix에서 사라지기 때문에 임시로 넣어두고 기존자리 +1 한 곳에 다시 넣어준다.)
        min_num = temp

        # 좌측 값 회전
        for i in range(query[0] + 1, query[2] + 1):
            matrix[i - 1][query[1]] = matrix[i][query[1]]
            min_num = min(min_num, matrix[i][query[1]])     # 최소값 저장

        # 하단 값 회전
        for i in range(query[1] + 1, query[3] + 1):
            matrix[query[2]][i - 1] = matrix[query[2]][i]
            min_num = min(min_num, matrix[query[2]][i])     # 최소값 저장

        # 우측 값 회전 (※중요: 우측과 상단 시계방향으로 벨류값 이동 시 더 큰 위치에서 작은 위치로 이동하기 때문에 for문에 역순으로 순회)
        for i in range(query[2] - 1, query[0] - 1, -1):
            matrix[i + 1][query[3]] = matrix[i][query[3]]
            min_num = min(min_num, matrix[i][query[3]])     # 최소값 저장

        # 상단 값 회전 (※중요: 우측과 상단 시계방향으로 벨류값 이동 시 더 큰 위치에서 작은 위치로 이동하기 때문에 for문에 역순으로 순회)
        for i in range(query[3] - 1, query[1] - 1, -1):
            matrix[query[0]][i + 1] = matrix[query[0]][i]
            min_num = min(min_num, matrix[query[0]][i])     # 최소값 저장

        matrix[query[0]][query[1] + 1] = temp

        answer.append(min_num)

    return answer

rows = 6
columns = 6
table = []
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)


# result: [8, 10, 25]