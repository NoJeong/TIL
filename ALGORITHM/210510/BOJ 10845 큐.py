import sys
sys.stdin = open('BOJ 10845 큐.txt')

from collections import deque
input=sys.stdin.readline
N = int(input())
q = deque()
for i in range(N):
    a = input().split()
    if a[0] == 'push':
        q.append(int(a[1]))
    elif a[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if q:
            print(q[0])
        else :
            print(-1)
    else:
        if q:
            print(q[-1])
        else :
            print(-1)