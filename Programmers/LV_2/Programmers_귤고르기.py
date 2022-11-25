from collections import Counter

def solution(k, tangerine):
    answer = 0
    temp = 0
    counter = {}
    for value in tangerine:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
    # counter = dict(Counter(targerine))
    a = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    for item in a:
        temp += a[item]
        if k > temp:
            answer += 1
        else:
            answer += 1
            break
    return answer

# k = 6
# targerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 4
targerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, targerine))

# # result = 3
# k = 4
# targernine = [1, 3, 2, 5, 4, 5, 2, 3]
# result = 2
