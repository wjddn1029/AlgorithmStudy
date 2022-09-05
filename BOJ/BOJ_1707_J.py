import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in que[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    que = [[] for i in range(v+1)]
    visited = [0]*(v+1)
    flg = 1
    for j in range(e):
        a, b = map(int, input().split())
        que[a].append(b)
        que[b].append(a)
    for k in range(1, v+1):
        if visited[k] == 0:
            if not bfs(k):
                flg = -1
                break
    print('YES' if flg == 1 else 'NO')
