import sys
sys.stdin = open('BOJ 15649 N과M.txt')

n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]  # 숫자 리스트
check_number = [False] * n  # 중복숫자 체크
array = []  # 출력할 수열


def DFS(x):
    if len(array) >= 2:
        if array[len(array)-1] < array[len(array)-2]:
            return
    if x == m:
        print(*array)
        return
    for i in range(len(number_list)):
        if check_number[i]:
            continue
        array.append(number_list[i])
        check_number[i] = True
        DFS(x+1)
        array.pop()
        check_number[i] = False

DFS(0)