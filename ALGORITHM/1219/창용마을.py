import sys
sys.stdin = open('창용마을.txt')

def search(i):
    visited[i] = 1
    for k in range(len(base)):
        if base[i][k] and not visited[k]:
            search(k)



for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    base = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
    for i in range(M):
        s, e = map(int,input().split())
        base[s][e] = 1
        base[e][s] = 1

    for i in range(1,N+1):
        if not visited[i]:
            search(i)
            cnt += 1

    print(cnt)