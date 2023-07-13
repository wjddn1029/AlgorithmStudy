def solution(N):
    for i in range(26, 0, -1):
        if N % i == 0:
            print(N // i)
            break
    alphabets = 'abcdefghijklmnopqrstuvwxyz'[:i]
    result = alphabets * (N // i)
    return result
