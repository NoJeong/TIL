import sys
sys.stdin = open('BOJ 1978 소수 찾기.txt')

N = int(input())
base_list = list(map(int,input().split()))
cnt = 0

for i in base_list:
    cnt += 1
    if i == 1:
        cnt -= 1
        continue
    for j in range(2,i):
        if i % j == 0:
            cnt -= 1
            break


print(cnt)