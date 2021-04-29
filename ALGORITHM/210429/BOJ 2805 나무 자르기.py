import sys
sys.stdin = open('BOJ 2805 나무 자르기.txt')

N,M = map(int, input().split())

trees = list(map(int,input().split()))

max_height = max(trees)
min_height = 1

while min_height <= max_height:
    mid = (max_height + min_height) // 2
    temp_cnt = 0
    for i in trees:
        if i > mid:
            temp_cnt += (i-mid)
    if temp_cnt >= M:
        min_height = mid + 1
    elif temp_cnt < M:
        max_height = mid - 1


print(max_height)