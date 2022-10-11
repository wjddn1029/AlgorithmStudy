import sys


def dfs(v):
    visit_list[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visit_list[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4