n = input()

height = '12345678'
low = 'abcdefgh'
directions = [[-1, -2], [1, -2], [1, 2], [-1, 2], [-2, 1], [-2, -1], [2, -1], [2, 1]]
dx, dy = int(height[low.index(n[0])]), int(n[1])
print(dx, dy)
cnt = 0
#ans[0] < 1 or ans[1] < 1 or ans[0] > n or ans[1] > n
for i in directions:
    if dx + i[0] < 1 or dy + i[1] < 1 or dx + i[0] > 8 or dy + i[1] > 8:
        pass
    else:
        cnt += 1

print(cnt)


