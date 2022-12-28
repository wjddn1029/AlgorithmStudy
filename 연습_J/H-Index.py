def solution(citations):
    answer = len(citations)
    citations.sort()
    i = 1
    for index in citations[::-1]:
        if index == i:
            answer = i
            break
        if index < i:
            answer=i-1
            break
        i+=1
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))

# citations	return
# [3, 0, 6, 1, 5]	3