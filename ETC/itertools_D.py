from itertools import permutations, combinations, product, combinations_with_replacement

test = [1, 2, 3] # 테스트 데이터
result = list(permutations(test, 2)) # 2개를 뽑는 모든 순열 구하기
print(result)
result = list(combinations(test, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)
result = list(product(test, repeat=2)) # 2개를 뽑는 모든 중복순열 구하기
print(result)
result = list(combinations_with_replacement(test, 2)) # 2개를 뽑는 모든 중복조합 구하기
print(result)

#https://doragoon.tistory.com/2 내용정리

