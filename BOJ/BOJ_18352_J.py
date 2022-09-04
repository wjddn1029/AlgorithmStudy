from collections import deque
import heapq
import sys


def bfs(x):
    answer = []
    q = deque([x])
    visited[x] = True
    distance[x] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')


f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

bfs(x)


# 4 4 2 1             4
# 1 2
# 1 3
# 2 3
# 2 4
#
#
# 4 3 2 1            -1
# 1 2
# 1 3
# 1 4
#
#
# 4 4 1 1            2
# 1 2                3
# 1 3
# 2 3
# 2 4


# 2차풀이
f = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')