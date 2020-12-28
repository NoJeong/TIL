import sys
sys.stdin = open('BOJ 1260 DFS와 BFS.txt')
from collections import deque
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1 , N+1):
        if G[v][w] == 1 and not visited[w] :
            dfs(w)

def bfs(v):

    used = [0] * (N + 1)
    Q = deque()
    Q.append(v)
    print_list = []
    while Q:
        v = Q.popleft()
        used[v] = 1
        if v not in print_list:
            print(v,end=' ')
            print_list.append(v)
        for w in range(N+1):
            if G[v][w] == 1 and not used[w]:
                Q.append(w)

N,M,V = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(M)]
G = [[0] * (N+1) for _ in range(N+1)]
for i in temp:
    G[i[1]][i[0]] = 1
    G[i[0]][i[1]] = 1
visited = [0] * (N+1)
dfs(V)
print()
bfs(V)