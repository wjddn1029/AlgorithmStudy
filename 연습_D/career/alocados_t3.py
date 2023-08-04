n, m = map(int, input().split())

def solution(n, m):
    ans = 1
    for i in range(5):
        ans *= (n - i) * (m - i)
    return ans % 1000000007

print(solution(n, m))