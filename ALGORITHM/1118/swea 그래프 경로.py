import sys
sys.stdin = open('input.txt')

def dfs(v):
    #방문체크
    visited[v] = 1
    #v의 인접한 정점중에서 방문안한 정점을 재귀호출
    for w in range(1, V+1):
        if base[v][w] == 1 and visited[w] == 0:
            dfs(w)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    visited = [0] * (V+1)
    for e in range(E):
        a, b = map(int,input().split())
        base[a][b] = 1
        #base[b][a] = 1
    S, G = map(int, input().split())
    dfs(S)
    result = 1
    if visited[G] == 0:
        result = 0
    print('#{} {}'.format(tc, result))







    # dr = base[S].index(1)
    # dc = S
    # while dr < V+1:
    #     if dc > 0 and base[dc+1][dr] == 1:
    #         if dc-1 == G:
    #             print('1')
    #         dc += 1
    #     else:
    #         while base[dc+1][dr] == 0:
    #             dc += 1
    #             if dc == V+1:
    #                 break
    #1에서 6을 갈 수 있느냐
    # 1에서 갈수있는곳을 간다 그다음 단계를 탐색한다
    #6이 있는지 확인한다.
    # print(base)

