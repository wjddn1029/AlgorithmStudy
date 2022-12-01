def solution(A):
    answer = 0  # 길이
    for i, v in enumerate(A):
        if i == 0:  # i = 0 자기자신이랑 비교하는거
            pass
        else:
            compare = A[i-1]        # A[0] v =1
            compare = comparison(i, v, compare)     # comparison(1, jqw, eva)
            if compare != A[i-1]:
                if answer <= len(compare):
                    answer = len(compare)

    return answer


def comparison(i, v, compare):
    temp = compare
    flag = True
    result = []
    for value in v:
        if value not in result:
            result.append(value)
    if v != ''.join(result):
        return compare
    for j in v:
        if compare.find(j) != -1:
            flag = False
            break
    if flag == True:
        temp += v
    if compare == temp or i == len(A) - 1:
        return compare
    else:
        compare = temp
        return comparison(i+1, A[i+1], compare)


A = ["eva", "jqw", "tyn", "jan"]
print(solution(A))
