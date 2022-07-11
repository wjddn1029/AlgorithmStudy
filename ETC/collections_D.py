from collections import deque, Counter

#https://doragoon.tistory.com/3

data = deque([2,3,4])
data.appendleft(1)  # 첫번째 인덱스에 원소 넣기
print(data)
data.append(5)  # 마지막 인덱스에 원소 넣기

print(data)

deq = deque(['c', 'd'])
deq.extend('ef')
print(deq)


deq.extendleft('ab')
print(deq)


test1 = deque(['a', 'b', 'c', 'd', 'e'])
test1.rotate(2)
print(test1)

test2 = deque(['a', 'b', 'c', 'd', 'e'])
test2.rotate(-2)
print(test2)

############## counter  ##############
# 리스트 : 요소의 개수 파악
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(Counter(lst))

# 딕셔너리 : value 값이 큰 순서대로
dic = {'가': 3, '나': 2, '다': 4}
print(Counter(dic))

# 값 = 개수 형태
c = Counter(a=2, b=3, c=2)
print(Counter(c))
print(sorted(c.elements()))

# 문자열
container = Counter()
container.update("aabcdeffgg")
print(container)

# most_common() : 개수의 해당하는 값 추출
c2 = 'apple, orange, grape'
c2 = Counter(c2)
print(c2.most_common())
print(c2.most_common(3))
