import sys
sys.stdin = open('BOJ 17219 비밀번호 찾기.txt')

input = sys.stdin.readline

N,M = map(int,input().split())
base = dict()
for i in range(N):
    a,b = input().split()
    if a not in base:
        base[a] = b
for i in range(M):
    c = input().split()
    print(base[c[0]])