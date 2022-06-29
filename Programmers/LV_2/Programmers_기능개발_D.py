from collections import deque

def solution(progresses, speeds):
    answer = []
    days, count = 0, 0
    
    q = deque(progresses)
    s = deque(speeds)

    while q:
        if q[0] + days * s[0] >= 100:
            q.popleft()
            s.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
    answer.append(count)
    return answer