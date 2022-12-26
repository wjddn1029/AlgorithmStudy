N, M = map(int, input().split())
ind = []
answer = 'ABCDEF'[:N]
answer_arr = list(answer)
answer_set = set(answer)
for i in range(M):
    ind.append(input())



for i, v in enumerate(ind):
    if answer.find(v[0]) >= answer.find(v[-1]):
        answer_arr[answer.find(v[0])] = v[-1]
        answer_arr[answer.find(v[-1])] = v[0]
        answer = ''.join(answer_arr)
        if v[0] in answer_set:
            answer_set.remove(v[0])
        if v[1] in answer_set:
            answer_set.remove(v[1])

temp_arr = list(answer_set)


print(''.join(answer_arr))
