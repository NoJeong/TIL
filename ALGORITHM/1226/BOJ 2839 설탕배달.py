import sys
sys.stdin = open('BOJ 2839 설탕배달.txt')

num = int(input())
cnt = 0
while 1:
    if num % 5 == 0:
        cnt += (num // 5)
        print(cnt)
        break
    num -= 3
    cnt += 1
    if num < 0:
        print(-1)
        break
