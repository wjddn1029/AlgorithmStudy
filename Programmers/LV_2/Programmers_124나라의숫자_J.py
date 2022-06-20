# 문제 보자마자 3진법과 비슷하다고 생각.
# 3진법과 비슷하다면 10진법을 3진법으로 바꿀때와 마찬가지로 재귀함수를 써야한다는 생각을 함.

def solution(n):
    if n <= 3:
        answer = '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)                 # 처음에 n-1 이 아닌 n으로 (divmod(n,3)) 생각했다가 테스트케이스 몇개 해보고 변경
        answer = solution(q) + '124'[r]         # 위와 세트로 처음에는 '124'[r-1]로 생각했다가 divmod(n-1,3)으로 바꾸면서 해당부분도 수정

    return answer

print(solution(6))
