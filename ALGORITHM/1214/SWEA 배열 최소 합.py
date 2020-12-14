import sys
sys.stdin = open('input.txt')

def select(r, sums):
    global min_result
    if r >= N:
        if sums < min_result:
            min_result = sums
        return

    if sums > min_result:
        return
    for i in range(N):
        if check[i]:
            check[i] = False
            select(r+1, sums + base[r][i])
            check[i] = True



T = int(input())
for tc in range(T):
    N = int(input())
    base = [list(map(int, list(input().split()))) for n in range(N)]
    check = [True for _ in range(N)]
    min_result = 1901910910910910910910
    select(0, 0)
    print('#{} {}'.format(tc+1, min_result))