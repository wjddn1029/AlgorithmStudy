#https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

def solution(dartResult):
    temp = ''
    answer = []
    for i in dartResult:
        if i.isnumeric():
            temp += i
        if i == 'S':
            answer.append(int(temp))
            temp = ''
        elif i == 'D':
            answer.append(pow(int(temp), 2))
            temp = ''
        elif i == 'T':
            answer.append(pow(int(temp), 3))
            temp = ''
        elif i == '#':
            answer[-1] *= -1
        elif i == '*':
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
    ans = sum(answer)

    return ans
dart = '1D2S3T*'

print(solution(dart))


# 전에 같이 풀었는데 같은 부분에서 같은 실수 했었음