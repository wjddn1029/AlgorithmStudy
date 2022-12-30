n = int(input())
data = list(map(str, input().split()))
t = input().split()
print(t)
ans = [1, 1]
direction = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

for i in data:
    ans[0] += direction[i][0]
    ans[1] += direction[i][1]
    if ans[0] < 1 or ans[1] < 1 or ans[0] > n or ans[1] > n:
        ans[0] -= direction[i][0]
        ans[1] -= direction[i][1]

print(ans)


