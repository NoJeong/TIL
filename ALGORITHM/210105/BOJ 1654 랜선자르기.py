import sys
sys.stdin = open('BOJ 1654 랜선자르기.txt')

input=sys.stdin.readline
K, N = map(int,input().split())

base = [ int(input()) for _ in range(K)]
h, l = max(base),1

while l <= h:
    mid = (h+l) // 2
    counts = 0
    for i in base:
        counts += (i//mid)
    if counts >= N:
        l = mid+1
    elif counts < N:
        h = mid-1
print(h)