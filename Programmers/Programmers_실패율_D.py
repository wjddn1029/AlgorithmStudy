#https://programmers.co.kr/learn/courses/30/lessons/42889

# N	stages	result
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3]

def solution(N, stages):
    answer = []
    failRate = [0] * (N + 1)
    for i, v in enumerate(stages):  #단계별 실패율 총합
       failRate[v-1] += 1
    player = len(stages)
    dic = {}
    for i, v in enumerate(failRate):
        if player != 0:     #0인 경우 예외처리
            failRate[i] /= player
            player -= v
        else:
            failRate[i] = 0
        dic[i+1] = failRate[i]
    dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)    #value 기준 값 정렬
    for k, v in dic:
        if k <= N:
            answer.append(k)
    return answer

print(solution(4, [4,4,4,4,4]))


# 나는 for문 3개나 써서 만들었는데 -> for 1개로 풀이가능...