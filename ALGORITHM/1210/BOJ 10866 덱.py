import sys
from collections import deque
sys.stdin = open('BOJ 10866 덱.txt')

N = int(input())

queue = deque()
for i in range(N):
    a = list(map(str,sys.stdin.readline().split()))

    if a[0] == 'push_front':
        queue.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        queue.append(int(a[1]))
    elif a[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)