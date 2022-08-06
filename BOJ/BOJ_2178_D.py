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

#https://www.acmicpc.net/problem/2178