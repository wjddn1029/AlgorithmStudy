def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right = n
        else:
            n = 11 if n == 0 else n
            absL = abs(n - left)
            absR = abs(n - right)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right = n
            elif sum(divmod(absR, 3)) > sum(divmod(absL, 3)):
                answer += 'L'
                left = n
            else:
                if hand == 'right':
                    answer += 'R'
                    right = n
                else:
                    answer += 'L'
                    left = n

    return answer
