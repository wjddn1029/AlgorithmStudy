import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

n = int(input())
data = list(map(int, input().split()))
ans = []

for i in range(1, n+1):
    if is_prime_number(i) and i != 1:
        ans.append(data[i-1])

print(sum(ans))

