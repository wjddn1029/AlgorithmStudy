def solution(dartResult):
    answer = []
    score = ''
    for i in dartResult:
        if i.isnumeric():   # i가 숫자면 score에 저장하여 다음 계산때 이용
            score += i      # 10처럼 연속적으로 숫자가 들어왔을경우 처리해주기 위해 += 이용
        elif i == 'S':
            answer.append(int(score))
            score = ''                  # score += i 이부분 때문에 다시 초기화
        elif i == 'D':
            score = pow(int(score), 2)
            answer.append(score)
            score = ''                  # score += i 이부분 때문에 다시 초기화
        elif i == 'T':
            score = pow(int(score), 3)
            answer.append(score)
            score = ''                  # score += i 이부분 때문에 다시 초기화
        elif i == '*':
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2
        elif i == '#':
            answer[-1] *= -1

    answer = sum(answer)

    return answer
