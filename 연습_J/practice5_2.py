def solution(data):
    answer = []
    time = data[0][1] + data[0][2] if data else 0
    answer.append(data[0][0])
    data.pop(0)

    while data:
        time = printData(data, time, answer)

    return answer


def printData(data, time, answer):
    compare = list(filter(lambda x: x[1] <= time, data))
    if not compare:
        time += 1
        return time
    compare.sort(key=lambda x: x[2])
    if compare:
        for i in compare:
            time += i[2]
            answer.append(i[0])
            index = [data.index(n) for n in data if n == i]
            data.pop(index[0])
            break

    return time




data = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]
result = [1, 2, 4, 5, 3]

print(solution(data))

