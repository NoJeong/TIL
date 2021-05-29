import sys
sys.stdin = open('프로그래머스 기능개발.txt')

progresses = list(map(int,input().split()))
speeds = list(map(int,input().split()))

answer = []
while progresses:
    cnt = 0
    for i in range(len(progresses)):
        progresses[i] += speeds[i]
        if progresses[i] >= 100 and i == cnt:
            cnt += 1
    if cnt:
        for i in range(cnt):
            progresses.pop(0)
    if cnt >= 1:
        answer.append(cnt)

print(answer)