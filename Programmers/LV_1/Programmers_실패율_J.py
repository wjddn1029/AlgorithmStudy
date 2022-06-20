# N	stages	result
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3]

def solution(N, stages):
    result = {}
    length = len(stages)
    for i in range(1, N + 1):
        if length != 0:                 # 분모가 0인 케이스 예외처리
            count = stages.count(i)     # 파이썬 count 함수로
            result[i] = count / length
            length -= count     # 총 길이에서 count를 빼주고 다음꺼 재계산
        else:
            result[i] = 0       # 이 부분에서 result[i] = i로 했다가 계속 틀렸던 부분
    return sorted(result, key=lambda x: result[x], reverse=True)
