import sys
sys.stdin = open('프로그래머스 기능개발.txt')

progresses = list(map(int,input().split()))
speeds = list(map(int,input().split()))

answer = []
while progresses:
    answer = []
    times = 0
    while progresses:
        cnt = 0
        times += 1
        for i in range(len(progresses)):
            if progresses[i] + (speeds[i] * times) >= 100 and i == cnt:
                cnt += 1
        if cnt:
            answer.append(cnt)
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)

print(answer)