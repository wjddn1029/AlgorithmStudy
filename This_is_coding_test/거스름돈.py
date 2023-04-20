money = 1260
change = [500, 100, 50, 10]
ans = 0
while money != 0:
    if money >= 500:
        money -= 500
        ans += 1
    elif money >= 100:
        money -= 100
        ans += 1
    elif money >= 50:
        money -= 50
        ans += 1
    elif money >= 10:
        money -= 10
        ans += 1

print(ans)

