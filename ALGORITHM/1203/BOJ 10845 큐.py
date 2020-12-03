import sys
from collections import deque
sys.stdin = open('BOJ 10845 큐.txt')
input=sys.stdin.readline


N = int(input())
base = deque()
for i in  range(N):
    a = input().split()
    if a[0] == 'push':
        base.append(a[1])
    elif a[0] == 'pop':
        if base:
            print(base.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(base))
    elif a[0] == 'empty':
        if base:
            print(0)
        else:
            print(1)
    elif a[0] == 'back':
        if base:
            print(base[-1])
        else:
            print(-1)

    elif a[0] == 'front':
        if base:
            print(base[0])
        else:
            print(-1)
