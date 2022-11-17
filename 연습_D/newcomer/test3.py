# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.8.10
    ans = 0
    if S == contraction(S):
        return ans

    s_list = list(S)
    flag = True
    for i in C:
        cnt = s_list.count('$')
        if i < cnt:
            s_list.insert(i, '$')
        else:
            s_list.insert(i + cnt, '$')
        compare_str = ''.join(s_list)
        print(compare_str)
        split_list = compare_str.split('$')
        tmp_list = []
        for j in split_list:
            tmp_list.append(contraction(j))
        if tmp_list == split_list:
            flag = False
            ans = compare_str.count('$')
            return ans

    if flag:
        ans = -1
    return ans

def contraction(s):
    a = ''.join(dict.fromkeys(s))
    return a

print(solution('aabcddcb', [3,5,1,4,7]))


