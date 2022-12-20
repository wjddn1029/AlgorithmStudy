from decimal import Decimal
H, U, D, F = map(int, input().split())    # 우물높이, 올라갈수 있는 거리, 미끄러져 내려오는 거리, 피로도

def well(H, U, D, F):
    count = 0
    height = 0
    tired = Decimal(U) * (Decimal(F) / 100)
    while height < H:
        count += 1
        height = height + U - tired * (count - 1)
        if height < 0:
            return print("Failure " + str(count))

        elif height <= H:
            height -= D

    return print("Success " + str(count))

well(H, U, D, F)


# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)