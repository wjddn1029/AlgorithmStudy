#https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    L_list = [1, 4, 7]
    C_list = [2, 5, 8, 0]
    R_list = [3, 6, 9]
    L_thumb, R_thumb = 10, 12

    for i in numbers:
        if i in L_list:
            answer += 'L'
            L_thumb = i
        elif i in R_list:
            answer += 'R'
            R_thumb = i
        else:
            i = 11 if i == 0 else i
            L = abs(i - L_thumb)
            R = abs(i - R_thumb)

            if sum(divmod(L,3)) > sum(divmod(R,3)):   #다른로우에서 거리가 같은 경우
                answer += 'R'
                R_thumb = i
            elif sum(divmod(L,3)) < sum(divmod(R,3)):
                answer += 'L'
                L_thumb = i
            else:
                if hand == 'left':
                    answer += 'L'
                    L_thumb = i
                else:
                    answer += 'R'
                    R_thumb = i

    return answer
