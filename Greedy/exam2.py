n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
ans = []
for i in data:
    ans.append(min(i))

print(max(ans))