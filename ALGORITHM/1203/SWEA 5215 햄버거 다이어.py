import sys
sys.stdin = open('SWEA 5215 햄버거 다이어트.txt')

def findkal(idx,score,T):
    global max_score
    if L < T:
        return

    if max_score < score:
        max_score = score

    if idx == N:
        return

    a,b = base[idx]
    findkal(idx+1,score+a,T+b)
    findkal(idx+1,score,T)

for tc in range(1,int(input())+1):
    N,L = map(int,input().split())
    base = list()
    max_score = 0
    for n in range(N):
        base.append(list(map(int,input().split())))
    findkal(0,0,0)
    print('#{} {}'.format(tc, max_score))