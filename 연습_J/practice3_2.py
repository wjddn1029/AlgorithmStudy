from collections import deque

def solution(ball, order):
    answer = []
    temp = []
    queue = deque(ball)
    for i in order:
        if temp:
            for v in temp:
                if queue and queue[0] == v:
                    answer.append(queue.popleft())
                elif queue and queue[-1] == v:
                    answer.append(queue.pop())
        if not queue:
            break
        elif i == queue[0]:
            answer.append(queue.popleft())
            if temp:
                for v in temp:
                    if queue and queue[0] == v:
                        answer.append(queue.popleft())
                    elif queue and queue[-1] == v:
                        answer.append(queue.pop())
        elif i == queue[-1]:
            answer.append(queue.pop())
            if temp:
                for v in temp:
                    if queue and queue[0] == v:
                        answer.append(queue.popleft())
                    elif queue and queue[-1] == v:
                        answer.append(queue.pop())
        else:
            temp.append(i)
    return answer

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]
# result = [24, 13, 9, 2, 11]

print(solution(ball, order))
