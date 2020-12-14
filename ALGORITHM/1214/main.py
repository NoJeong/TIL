import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = [list(map(int,input().split())) for _ in range(n)]
    visit = [1] * n
    min_num = 1000000000
    b = []
    for i in range(n):
        if num[0][i] < min_num:
            min_num = num[0][i]
            b.append(num[0][i])
        for x in range(n):
            for y in range(n):
                visit[x][i] = 1
                if visit[x][y] == 0 and num[x][y] < min_num :
                    min_num = num[x][y]
                    b.append(num[x][y])
                    continue

    print('#%d %d' %(tc, sum(b)))