def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    same_count = 0
    rank_list = {'0': 6, '1': 6, '2': 5, '3': 4, '4': 3, '5': 2, '6': 1}
    for i in lottos:
        if i == 0:
            zero_count += 1
        for j in win_nums:
            if i == j:
                same_count += 1
    answer.append(rank_list[str(same_count + zero_count)])
    answer.append(rank_list[str(same_count)])
    return answer