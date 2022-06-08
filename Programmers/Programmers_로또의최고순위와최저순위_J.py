# lottos	win_nums	result
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
a = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

def solution(lottos, win_nums):
    max = 0
    min = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for i in lottos:
        if i == 0:
            max += 1
        else:
            if i in win_nums:
                max += 1
                min += 1

    return [rank.get(max), rank.get(min)]
