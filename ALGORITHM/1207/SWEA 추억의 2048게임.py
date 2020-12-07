import sys
sys.stdin = open('SWEA 추억의 2048게임.txt')

from collections import deque

def push():
    if S == "up":
        #열 우선순회
        for i in range(N):
            queue = deque()
            for j in range(N):
                if tile[j][i]:
                    queue.append(tile[j][i])
                    tile[j][i] = 0
            #가장 위부터 채워 나가기
            idx = 0
            while queue:
                if len(queue) > 1:
                    A,B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[idx][i] = A + B
                    else:
                        tile[idx][i] = A
                        queue.appendleft(B)
                    idx += 1
                else:
                    tile[idx][i] = queue.popleft()


    elif S == 'down':
        #열 역 우선 순회
        for i in range(N):
            queue = deque()
            for j in range(N-1,-1,-1):
                if tile[j][i]:
                    queue.appendleft(tile[j][i])
                    tile[j][i] = 0
            idx = N-1

            while queue:
                if len(queue)>1:
                    A,B = queue.popleft(),queue.popleft()
                    if A == B:
                        tile[idx][i] = A + B
                    else:
                        tile[idx][i] = A
                        queue.appendleft(B)
                    idx -= 1
                else:
                    tile[idx][i] = queue.popleft()
    elif S =='left':
        #행우선
        for i in range(N):
            queue = deque()
            for j in range(N):
                if tile[i][j]:
                    queue.append(tile[i][j])
                    tile[i][j] = 0
            #가장 왼쪽부터 채워 나가기
            idx = 0
            while queue:
                if len(queue) > 1:
                    A,B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[i][idx] = A + B
                    else:
                        tile[i][idx] = A
                        queue.appendleft(B)
                    idx += 1
                else:
                    tile[i][idx] = queue.popleft()
    else:
        # 행우선
        for i in range(N):
            queue = deque()
            for j in range(N-1,-1,-1):
                if tile[i][j]:
                    queue.append(tile[i][j])
                    tile[i][j] = 0
            # 가장 왼쪽부터 채워 나가기
            idx = 0
            while queue:
                if len(queue) > 1:
                    A, B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[i][idx] = A + B
                    else:
                        tile[i][idx] = A
                        queue.appendleft(B)
                    idx -= 1
                else:
                    tile[i][idx] = queue.popleft()



for tc in range(1, int(input())+1):
    N, S = input().split()
    N = int(N)

    tile = [list(map(int,input().split())) for _ in range(N)]
    push()

    print("#{}".format(tc))
    for i in range(N):
        # for j in range(N):
        #     print(tile[i][j],end=" ")
        # print()
        print(*tile[i])