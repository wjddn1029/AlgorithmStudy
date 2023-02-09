from collections import deque

n, m = map(int, input().split())
# 0: 빈칸, 1: 벽, 2: 바이러스
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 2:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

print(graph)
