import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    li_a = list(map(int, input().split()))
    li_b = list(map(int, input().split()))
    if len(li_b) < len(li_a):
        li_a, li_b = li_b, li_a
    max_sum = 0
    for i in range(abs(M-N)+1):
        total = 0
        for j in range(len(li_a)):
            total += li_a[j] * li_b[i+j]
        if max_sum < total:
            max_sum = total
    print('#{} {}'.format(tc,max_sum))