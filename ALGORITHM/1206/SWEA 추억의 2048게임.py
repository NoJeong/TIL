import sys
sys.stdin = open('SWEA 추억의 2048게임.txt')
from collections import deque

def game():


    if S =='up':
        for i in range(N):
            queue = deque()
            for j in range(N):
                if base[j][i]:
                    queue.append(base[j][i])
                    base[j][i] = 0
                idx = 0
            while queue:
                if len(queue) > 1:
                    a,b = queue.popleft(), queue.popleft()
                    if a == b:
                       base[idx][i] = a + b

                    else:
                        base[idx][i] = a
                        queue.appendleft(b)
                    idx += 1

                else:
                    a = queue.popleft()
                    base[idx][i] = a



for tc in range(1, int(input())+1):
    N, S = input().split()
    N= int(N)
    base = list(list(map(int, input().split())) for _ in range(N))
    game()
    print(*base,sep='\n')