import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    a = int(input())
    base = [0] * 101
    li = list(map(int, input().split()))
    for i in range(1000):
        base[li[i]] += 1
    if base.count(max(base)) > 1:
        a = base.index(max(base))
        base[a] -= 1
    print('#{} {}'.format(tc,base.index(max(base))))