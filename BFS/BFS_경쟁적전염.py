n, k = map(int, input().split())
virus = []
for _ in range(n):
    virus.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

print(virus)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

parasite = [[False] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if virus[i][j] != 0:
#             parasite[i][j] = True


def bfs(x1, y1, k1):
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행
            if virus[nx][ny] == 0:
                virus[nx][ny] = k1


for time in range(1, s+1):
    for i in range(n):
        for j in range(n):
            if parasite[i][j] == False:
                parasite[i][j] = True
                bfs(i, j, time)



