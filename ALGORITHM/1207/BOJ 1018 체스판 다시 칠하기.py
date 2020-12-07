import sys
sys.stdin = open('BOJ 1018 체스판 다시 칠하기.txt')

N,M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
ans = []
# print(*chess, sep='\n')

for i in range(N-7):
    for j in range(M-7):
        idx1 = 0
        idx2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if chess[a][b] != 'W':
                        idx1 += 1
                    else:
                        idx2 += 1
                else:
                    if chess[a][b] != 'B':
                        idx1 += 1
                    else:
                        idx2 += 1

        ans.append(idx1)
        ans.append(idx2)
print(min(ans))