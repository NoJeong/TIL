import sys
sys.stdin = open('boj 체스판 다시 칠하기.txt')

delta = [(1,0)]

N,M = map(int, input().split())
base = [list(input()) for _ in range(N)]
mini = []
for i in range(N - 7):
    for j in range(M - 7):
        idx1 = 0
        idx2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):

                if (a+b) % 2 == 0:
                    if base[a][b] != 'W':
                        idx1 += 1
                    if base[a][b] != 'B':
                        idx2 += 1
                else:
                    if base[a][b] != 'B':
                        idx1 += 1
                    if base[a][b] != 'W':
                        idx2 += 1

        mini.append(idx1)
        mini.append(idx2)
print(min(mini))