import sys
sys.stdin = open('BOJ 2108 통계학.txt')
input = sys.stdin.readline

base = []
N = int(input())
for i in range(N):
    base.append(int(input()))
# print(base,base_dic)
base.sort()
#산술 평균
print(round(sum(base)/N))

#중앙값
base.sort()
print(base[N//2])

#최빈값
from collections import Counter

k = Counter(base).most_common()
# k = [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
if len(base) > 1: #만약에 입력값이 하나면, 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(base[0])

#범위
print(base[-1] - base[0])