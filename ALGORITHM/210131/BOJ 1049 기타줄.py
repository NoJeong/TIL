import sys
sys.stdin = open('BOJ 1049 기타줄.txt')

#N,M 받아오기
N,M = map(int,input().split())
# 빈리스트,초기가격 만들기
base = []
price = 0
price_array = []
#리스트에 조합 넣기
for i in range(M):
    base.append(list(map(int,input().split())))
package = 0
thing = N
#N이 6보다 크다면
if N >= 6:
#몇배수로 큰지 알아내고 그만큼 빼기
    package = (N // 6)
    thing = (N % 6)
#패키지+ 낱개
#리스트 첫번쨰껄로 정렬하고 그만큼 가격에 더하기
base_1 = sorted(base, key= lambda x : x[0])
price += (package * base_1[0][0])
#리스트 두번쨰껄로 정렬하고 남은수만큼 가격에 더하기
base_2 = sorted(base, key= lambda x : x[1])
price += (thing * base_2[0][1])
price_array.append(price)
#패키지만 , 낱개만
price = 0
price += ((package+1) * base_1[0][0])
price_array.append(price)
price = 0
price += (N * base_2[0][1])
price_array.append(price)

print(min(price_array))