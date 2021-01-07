import sys
sys.stdin = open('BOJ 11651 좌표 정렬하기 2.txt')

input = sys.stdin.readline

N = int(input())
base = list()
for i in range(N):
    base.append(list(map(int,input().split())))
a = sorted(base, key = lambda x : (x[1],x[0]))
for c,b in a:
    print(c,b)