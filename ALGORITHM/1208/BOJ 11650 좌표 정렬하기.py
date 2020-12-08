import sys
sys.stdin = open('BOJ 11650 좌표 정렬하기.txt')

N = int(input())

base = list(list(map(int,input().split())) for _ in range(N))

a = sorted(base,key=lambda x : (x[0], x[1]))
for i in a:
    print(*i)