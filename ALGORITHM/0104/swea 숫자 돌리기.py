import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    base = list()
    final = [[0]*N for _ in range(N)]
    for _ in range(N):
        li = list(map(str, input().split()))
        base.append(li)
    #90도 일때
    for i in range(N):
        for j in range(N):
            a = base[i][j]
            final[N-j-1][i] = a
    print(final)

    #180도 일때

    #270도 일때


    # print('#{} {}'.format())