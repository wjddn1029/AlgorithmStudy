# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    tmp = S.lower()
    # b 만 있는 경우
    if 'b' in tmp and 'a' not in tmp:
        return True

    # a 만 있는 경우
    if 'a' in tmp and 'b' not in tmp:
        return True

    ans = True
    # 둘다 있는 경우
    for i, v in enumerate(tmp):
        if v == 'b':
            if 'a' in tmp[i:]:
                ans = False

    return ans


print(solution('bb'))