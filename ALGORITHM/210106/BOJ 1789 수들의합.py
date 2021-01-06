import sys
sys.stdin = open('BOJ 1789 수들의합.txt')

N= int(input())
count = 0
num = 1
sum_num= 0
while sum_num <= N:
    sum_num+=num
    num += 1
    count+=1
print(count - 1)

#########
#아이디어 구글링해서 발견했다 세상에 천재는많다
'''
200을 각각 다른 수로 해당 수를 구성하는 방법 중 최댓값은
1 + 2 + 3 + ... + 16 + 17 + 18 + 29
이다

즉 다시 말해 자연수 x의 정답은

sum(1: 18) <= x < sum(1: 19) (171~189)

-> 18개가 최대

sum(1: 19) <= x < sum(1: 20) (190~209)

-> 19개가 최대
'''