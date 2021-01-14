import sys
sys.stdin = open('BOJ 1966 프린터 큐.txt')
from collections import deque

for tc in range(int(input())):
    N, M = map(int,input().split())
    array = deque()
    numbering = list(map(int, input().split()))
    for i in range(N):
        array.append((i,numbering[i]))
    count = 1
    def maxnum():
        global max_num
        max_num = 0
        for i in range(len(array)):
            if max_num < array[i][1]:
                max_num = array[i][1]
        return max_num
    a = maxnum()
    count = 0
    while 1:
        if array:
            if array[0][1] != a:
                array.append(array.popleft())
            if array[0][1] == a:
                b = array.popleft()
                count += 1
                a = maxnum()
                if b[0] == M:
                    print(count)
                    break
