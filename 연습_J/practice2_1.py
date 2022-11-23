def solution(s1, s2, s3):
    s4 = s1 + s2 + s3
    s4 = sorted(s4, reverse=True)
    ans = ''
    for i in s4:
        if i in s1:
            ans += '1'
        elif i in s2:
            ans += '2'
        elif i in s3:
            ans += '3'

    return ans

print(solution([2,7],[4,5],[1]))
