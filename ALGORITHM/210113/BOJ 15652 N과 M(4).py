import sys
sys.stdin = open('BOJ 15649 N과M.txt')
input = sys.stdin.readline
n, m = map(int,input().split())
number_list = [i for i in range(1,n+1)]
array = []
# 이건 구글링해서 찾은 코드
def dfs(x):
    if x == m:
        print(*array)
        return
    for i in range(len(number_list)):
        if array and array[-1] > number_list[i]:
            continue
        array.append(number_list[i])
        dfs(x+1)
        array.pop()


# 이건 내가 했는데 시간초과가 떴다.
# 마지막 조건에서 for문을 한번 더써서 그런갑다.
def dfs(x):
    if x == m:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return
        print(*array)
        return
    for i in range(len(number_list)):
        array.append(number_list[i])
        dfs(x+1)
        array.pop()

dfs(0)