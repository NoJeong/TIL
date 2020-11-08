import sys
sys.stdin = open('boj 소수찾기.txt')

N = int(input())
n_list = list(map(int, input().split()))
cnt = 0
for i in n_list:
    if i == 1:
        cnt += 1
    for j in range(2,i):
        if not i % j:
            cnt += 1
            break
print(N-cnt)