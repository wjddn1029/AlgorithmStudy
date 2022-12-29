n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)
end1, end2 = data[-1], data[-2]
ans = 0
for i in range(1, m+1):
    if i % k != 0:
        ans += end1
    else:
        ans += end2

print(ans)


