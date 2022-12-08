def solution(histogram):
    histogram = histogram[1:-1]
    result = 0

    histogram.append(0)
    height = [(0, histogram[0])]
    for i in range(1, len(histogram)):
        width = i
        while height and height[-1][1] > histogram[i]:
            width, temp = height.pop()
            result = max(result, temp * (i - width))
        height.append((width, histogram[i]))
    return result



histogram = [6, 5, 7, 3, 4, 2]
# histogram = [2, 1, 4, 5, 1, 3, 3]
# result = 4
print(solution(histogram))