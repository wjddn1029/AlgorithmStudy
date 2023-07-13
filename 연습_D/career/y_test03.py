def solution(A):
    hole = sorted(A)
    min_position = min(A)
    max_position = max(A)
    mid = (max_position + min_position) / 2
    left_boat = []
    right_boat = []
    print(mid)
    for i, v in enumerate(hole):
        if mid < v:
            right_boat.append(v)
        else:
            left_boat.append(v)

    left_boat_length = 1 if len(left_boat) == 1 or len(left_boat) == 0 else left_boat[-1] - left_boat[0]
    right_boat_length = 1 if len(right_boat) == 1 or len(right_boat) == 0 else right_boat[-1] - right_boat[0]
    ans = max(left_boat_length, right_boat_length)

    return ans


# Example usage
print(solution([0, 15, 30]))  # Output: 4
