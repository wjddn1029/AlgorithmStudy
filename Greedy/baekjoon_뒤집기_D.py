data = input()

count_one = 0
count_zero = 0

if data[0] == '0':
    count_one += 1
else:
    count_zero += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            count_one += 1
        else:
            count_zero += 1

print(min(count_zero, count_one))
