# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    stack4 = stack1 + stack2 + stack3
    stack4 = sorted(stack4, reverse=True)
    ans = ''
    for i in stack4:
        if i in stack1:
            ans += '1'
        elif i in stack2:
            ans += '2'
        elif i in stack3:
            ans += '3'

    return ans




print(solution([2,7],[4,5],[1]))