import sys
sys.stdin = open('별 찍기-10.txt')

N = int(input())
base =[['*'*N] for _ in range(N)]
for i in range(N):
    print(base[i])
    for j in range(N):
        pass