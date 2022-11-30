def solution(A, B):
    mul = A*B
    answer = 0
    rest = []
    getBinaryNum(mul, rest)
    for i in rest:
        if i == 1:
            answer += 1
    return answer

def getBinaryNum(mul, rest):
    a, b = divmod(mul, 2)
    rest.append(b)
    if a == 0:
        return rest
    else:
        return getBinaryNum(a, rest)

A = 1
B = 31

print(solution(A, B))
