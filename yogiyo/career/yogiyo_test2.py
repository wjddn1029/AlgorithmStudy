
s = [['photo.jpg', 'Warsaw', '2013-09-05', '14:08:15']
,['john.png', 'London', '2015-06-20', '15:13:22']
,['myFriends.png', 'Warsaw', '2013-09-05', '14:07:13']
,['Eiffel.jpg','Paris', '2015-07-23', '08:03:02']
,['pisatower.jpg','Paris', '2015-07-22', '23:59:59']
,['BOB.jpg', 'London', '2015-08-05', '00:02:03']
,['notredame.png','Paris', '2015-09-01', '12:00:00']
,['me.jpg', 'Warsaw', '2013-09-06', '15:40:22']
,['a.png', 'Warsaw', '2016-02-13', '13:33:50']
,['b.jpg', 'Warsaw', '2016-01-02', '15:12:22']
,['c.jpg', 'Warsaw', '2016-01-02', '14:34:30']
,['d.jpg', 'Warsaw', '2016-01-02', '15:15:01']
,['e.png', 'Warsaw', '2016-01-02', '09:49:09']
,['f.png', 'Warsaw', '2016-01-02', '10:55:32']
,['g.jpg', 'Warsaw', '2016-02-29', '22:13:11']]

tmp = set([i[1] for i in s])
temp = {}
for i in tmp:
    temp[i] = []
    for j in s:
        if i == j[1]:
            temp[i].append([j[2], j[3]])

for i, v in enumerate(s):
    a = v[1] + v[0][v[0].index('.'):]
    s[i].append(a)

for k, v in temp.items():
    temp[k] = sorted(v, key=lambda v: (v[0], v[1]))

for k1, v1 in temp.items():
    a = []
    if len(v1) >= 10:
        for k2, v2 in enumerate(v1):
            v2.append(str(k2 + 1).zfill(2))
    else:
        for k2, v2 in enumerate(v1):
            v2.append(str(k2 + 1))

for k1, v1 in temp.items():
    for k2, v2 in enumerate(temp[k1]):
        for k3, v3 in enumerate(s):
            if k1 == v3[1] and v2[0] == v3[2] and v2[1] == v3[3]:
                v3[4] = v3[4][:v3[4].find('.')] + v2[2] + v3[4][v3[4].find('.'):]

for i in s:
    print(i[4])

# 1. 도시별로 그룹화
# 2. 각 그룹 내 사진을 찍은 시간별로 정렬
# 3. 마지막으로 1부터 시작하여 사진에 연속적인 자연수 할당



# Warsaw02.jpg
# London1.png
# Warsaw01.png
# Paris2.jpg
# Paris1.jpg
# London2.jpg
# Paris3.png
# Warsaw03.jpg
# Warsaw09.png
# Warsaw07.jpg
# Warsaw06.jpg
# Warsaw08.jpg
# Warsaw04.png
# Warsaw05.png
# Warsaw10.jpg