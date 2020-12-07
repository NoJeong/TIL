import sys
sys.stdin = open('SWEA 추억의 2048게임.txt')

from collections import deque
#위로 미는 함수
def push():
    for i in range(N):
        stack = []
        for j in range(N-1,-1,-1):
            if tile[j][i]:
                stack.append(tile[j][i])
                tile[j][i] = 0
        idx = 0

        while stack:
            if len(stack)>1:
                A,B = stack.pop(),stack.pop()
                if A == B:
                    tile[idx][i] = A + B
                else:
                    tile[idx][i] = A
                    stack.append(B)
            else:
                tile[idx][i] = stack.pop()

#시계방향으로 90도 돌린ㄴ것
def rotation(arr):
    tmp = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp




for tc in range(1, int(input())+1):
    N, S = input().split()
    N = int(N)

    tile = [list(map(int,input().split())) for _ in range(N)]

    if S =='up':
        push()
    elif S =='left':
        tile = rotation(tile)
        push()
        tile = rotation(tile)
        tile = rotation(tile)
        tile = rotation(tile)
    elif S == ' down':
        tile = rotation(tile)
        tile = rotation(tile)
        push()
        tile = rotation(tile)
        tile = rotation(tile)
    else:
        tile = rotation(tile)
        tile = rotation(tile)
        tile = rotation(tile)
        push()
        tile = rotation(tile)


    print("#{}".format(tc))
    for i in range(N):
        # for j in range(N):
        #     print(tile[i][j],end=" ")
        # print()
        print(*tile[i])