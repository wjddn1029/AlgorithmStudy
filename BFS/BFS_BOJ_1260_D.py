from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] != 1:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#번호가 작은것 번저 방문하기 위한 정렬
for i in range(m):
    graph[i].sort()

visited = [0] * (n + 1)
bfs(graph, v, visited)

#단방향 그래프 기준




