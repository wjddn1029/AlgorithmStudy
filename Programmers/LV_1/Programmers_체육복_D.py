def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)


def solution2(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
        elif i - 1 in lost and i != 1:
            lost.remove(i-1)
        elif i + 1 in lost and i != 30:
            lost.remove(i + 1)

    answer = n - len(lost)

    return answer

print(solution(5, [2,4], [1,3,5]))



# n	lost	reserve	    return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	        4
# 3	[3]	    [1]	        2

