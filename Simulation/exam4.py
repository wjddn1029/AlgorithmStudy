n, m = map(int, input().split())
a, b, d = map(int, input().split())
loc = []
for i in range(n):
    loc.append(list(map(int, input().split())))

visit = [[0] * m for _ in range(n)]
visit[a][b] = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx = a + dx[d]
    nx = a + dx[d]



