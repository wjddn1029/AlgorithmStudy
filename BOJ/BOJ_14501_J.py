N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i + li[i][0], N+1):
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]

print(dp[-1])


# input:
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# output:
# 45
