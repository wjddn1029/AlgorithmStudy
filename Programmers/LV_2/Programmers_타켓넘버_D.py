def solution(numbers, target):
    answer = 0
    flag = True
    #while flag:
    temp = ''
    calc = ['+'] * len(numbers)
    for i, v in enumerate(numbers):
        temp += calc[i]
        temp += str(v)
    print(temp)
    print(eval(temp))

    return answer




