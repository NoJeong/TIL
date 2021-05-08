import sys
sys.stdin = open('BOJ 최대공약수와 최소공배수.txt')

N, M = map(int, input().split())
a, b = N,M
# 최대공약수
if N < M:
    N ,M = M, N

while (M!=0):
    N = N % M
    N, M = M, N
print(N)
#최소공배수
print(int((a*b)/N))
