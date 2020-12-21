import sys
sys.stdin = open('BOJ 2805 나무자르기.txt')


N,M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1,max(trees)

#이분탐색을 이용한다
#두개의 값이 같아지면 그것이 답!
while start <= end:
    #중앙값을 정해준다
    mid = (start + end) // 2
    #장작의합
    log = 0
    for i in trees:
        if i > mid:
            log += i - mid
    #장작의 합이 구하려던것보다 크거나 같으면 시작값을 키워준다
    #만약에 같을경우 while문 탈출의 시그널!
    if log >= M:
        start = mid + 1
    #장작의 합이 더 적으면 더 낮게 잘라야하기 때문에 끝값을 낮춰준다
    elif log < M:
        end = mid - 1
#탈출했다면 끝값을 프린트!
print(end)

