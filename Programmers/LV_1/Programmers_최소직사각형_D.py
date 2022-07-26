def solution(sizes):
    w_max, h_max = 0, 0
    for i, v in enumerate(sizes):
        if v[1] >= v[0]:
            sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]

    for i in sizes:
        w_max = i[0] if i[0] >= w_max else w_max
        h_max = i[1] if i[1] >= h_max else h_max

    return w_max * h_max
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	))
#https://school.programmers.co.kr/learn/courses/30/lessons/86491