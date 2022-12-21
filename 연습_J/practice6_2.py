a, b = map(str, input().split())
year_a = int(a[:4])
year_b = int(b[:4])
month_a = int(a[4:6])
month_b = int(b[4:6])
day_a = int(a[6:])
day_b = int(b[6:])

day = 0
temp_day_a = 0
temp_day_b = 0


for i in range(year_a, year_b):
    if year_b - year_a > 0:
        if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
            day += 366
        else:
            day += 365

if ((year_a % 4 == 0) and (year_a % 100 != 0)) or (year_a % 400 == 0):
    arrList_a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    arrList_a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if ((year_b % 4 == 0) and (year_b % 100 != 0)) or (year_b % 400 == 0):
    arrList_b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    arrList_b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month_a-1):
    temp_day_a = temp_day_a + day_a + arrList_a[i]
if month_a-1 == 0:
    temp_day_a = day_a

for i in range(month_b-1):
    temp_day_b = temp_day_b + day_b + arrList_b[i]
if month_b-1 == 0:
    temp_day_b = day_b


day = day + (temp_day_b - temp_day_a)

print(day)a, b = map(str, input().split())
year_a = int(a[:4])
year_b = int(b[:4])
month_a = int(a[4:6])
month_b = int(b[4:6])
day_a = int(a[6:])
day_b = int(b[6:])

day = 0
temp_day_a = 0
temp_day_b = 0


for i in range(year_a, year_b):
    if year_b - year_a > 0:
        if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
            day += 366
        else:
            day += 365

if ((year_a % 4 == 0) and (year_a % 100 != 0)) or (year_a % 400 == 0):
    arrList_a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    arrList_a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if ((year_b % 4 == 0) and (year_b % 100 != 0)) or (year_b % 400 == 0):
    arrList_b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    arrList_b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month_a-1):
    temp_day_a = temp_day_a + day_a + arrList_a[i]
if month_a-1 == 0:
    temp_day_a = day_a

for i in range(month_b-1):
    temp_day_b = temp_day_b + day_b + arrList_b[i]
if month_b-1 == 0:
    temp_day_b = day_b


day = day + (temp_day_b - temp_day_a)

print(day)