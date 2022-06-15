#https://www.acmicpc.net/problem/1181

import sys
n = int(sys.stdin.readline())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())
set_word = list(set(word))      # 중복제거
set_word.sort()                 # 알파벳순 정렬
set_word.sort(key=len)          # 길이정렬

for i in set_word:
    print(i)


    


# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours
