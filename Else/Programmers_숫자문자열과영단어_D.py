#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_list = {
        'zero': '0'
        , 'one': '1'
        , 'two': '2'
        , 'three': '3'
        , 'four': '4'
        , 'five': '5'
        , 'six': '6'
        , 'seven': '7'
        , 'eight': '8'
        , 'nine': '9'}
    str_to_num = ''
    answer = ''
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            str_to_num += i
            if num_list.get(str_to_num):
                answer += num_list.get(str_to_num)
                str_to_num = ''

    return int(answer)