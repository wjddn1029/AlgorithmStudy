#https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    down = up.lower()
    ans = ''
    idx = 0
    for i in s:
        if i == ' ':
            ans += ' '
        elif i.isupper():
            idx = up.find(i) + n
            idx = idx - 26 if idx >= 26 else idx
            ans += up[idx]
        else:
            idx = down.find(i) + n
            idx = idx - 26 if idx >= 26 else idx
            ans += down[idx]

    return ans

print(solution("a B z",4))