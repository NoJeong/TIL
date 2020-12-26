import sys
sys.stdin = open('BOJ 2292 벌집.txt')

num = int(input())
first = 1
plus = 6
cnt = 1
if num == 1:
    print(1)
else:
    while 1:
        first += plus
        cnt += 1
        if num <= first:
            print(cnt)
            break
        plus += 6
