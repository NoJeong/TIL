import sys
sys.stdin = open('boj 수찾기.txt')

N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))
n_list.sort()
for i in m_list:
    right = N - 1
    left = 0
    result = 0
    while left <= right:

        mid = (left + right) // 2

        if n_list[mid] == i:
            result = 1
            break
        elif n_list[mid] > i:
            right = mid - 1
        elif n_list[mid] < i:
            left = mid + 1

    print(result)