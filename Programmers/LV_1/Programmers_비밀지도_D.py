#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    ans = [format(arr1[i] | arr2[i], '#b')[2:].rjust(n, '0').replace('1','#').replace('0',' ') for i in range(n)]
    return ans


print(solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

# 문제 풀이 아이디어 비트연산
# 찾아본 아이디어 이진수 변환하기
