import sys
sys.stdin = open('BOJ 15649 N과M.txt')

n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]  # 숫자 리스트
check_number = [False] * n  # 중복숫자 체크
array = []  # 출력할 수열


def DFS(x):
    if x == m:
        print(*array)
        return
    for i in range(len(number_list)):
        array.append(number_list[i])
        DFS(x+1)
        array.pop()

DFS(0)