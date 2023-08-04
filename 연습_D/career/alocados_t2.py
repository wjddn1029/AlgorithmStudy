N = int(input())

def solution(n, start, end, mid):
    if n == 1:
        print("[ {} ]".format(str(mid - 1)), end=' ')
        print("{0} -> {1}".format(str(start - 1), str(end - 1)))
        return
    else:
        solution(n - 1, start, mid, end)
        print("[ {} ]".format(str(mid - 1)), end=' ')
        print("{0} -> {1}".format(str(start - 1), str(end - 1)))
        solution(n - 1, mid, end, start)

solution(N, 1, 3, 2)