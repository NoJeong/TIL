import sys
sys.stdin = open('N과 M.txt')

N, M = map(int,input().split())
base_list = list((i+1) for i in range(N))
check_list = [False] * (N+1)
# print(check_list)
result = []

def dfs(n):
    if n == M:
        print(*result)

    for i in base_list:
        if check_list[i]:
            continue
        result.append(i)
        check_list[i] = True
        dfs(n+1)
        result.pop()
        check_list[i] = False
dfs(0)