import sys
sys.stdin = open('백준 카잉달력.txt')

tc = int(input())

for i in range(tc):
    a, b, c, d = map(int, input().split())
    if a > b:
        a ,b = b, a
        c, d = d, c
    d -= c
    cnt = 0
    while cnt < 40001:
        s = d - a*cnt
        if not (s % b):
            print(a*cnt+c)
            break
        cnt += 1
    else:
        print(-1)