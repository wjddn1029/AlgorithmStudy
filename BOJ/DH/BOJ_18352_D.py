from collections import deque

def bfs(graph, start, visited):
    #시작 방문노드 큐 추가 및 방문처리
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] != 1:
                queue.append(i)
                visited[i] = 1


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)




